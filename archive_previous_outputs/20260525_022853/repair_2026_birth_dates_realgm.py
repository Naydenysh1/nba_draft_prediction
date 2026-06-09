#!/usr/bin/env python3
"""
Repair missing 2026 draft ages using RealGM player profiles as a source.

Purpose:
- Start from the latest final dataset after organization/NCAA 2026 repairs.
- Find birth dates for 2026 prediction-pool players still missing draft_age.
- Save a separate override/audit CSV with sources.
- Integrate only birth_date and draft_age into the project-facing final dataset.
- Do NOT add technical source columns to the final project CSV.

Inputs:
    data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_2000_2026.csv

Outputs:
    data/player_birth_dates_2026_realgm_overrides.csv
    data/player_birth_dates_2026_realgm_unmatched.csv
    data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_2000_2026.csv
    data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_report.md

Install:
    pip install pandas numpy requests beautifulsoup4 lxml rapidfuzz tabulate

Run:
    python repair_2026_birth_dates_realgm.py \
      --base data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_2000_2026.csv \
      --out data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_2000_2026.csv \
      --overrides-out data/player_birth_dates_2026_realgm_overrides.csv \
      --unmatched-out data/player_birth_dates_2026_realgm_unmatched.csv \
      --report data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_report.md
"""

from __future__ import annotations

import argparse
import re
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote_plus, unquote, urlparse

import pandas as pd
import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz

DRAFT_DATE_2026 = "2026-06-23"
REQUEST_SLEEP_SECONDS = 2.5
SEARCH_SLEEP_SECONDS = 3.0
REQUEST_TIMEOUT_SECONDS = 30
MIN_NAME_SCORE = 86
MIN_CONTEXT_SCORE = 80

# Common media/recruiting names or RealGM display names for players whose dataset
# name differs from their profile name.
NAME_ALIASES = {
    "anicet dybantsa": ["AJ Dybantsa", "A.J. Dybantsa", "Anicet Dybantsa"],
    "christopher brown": ["Mikel Brown", "Mikel Brown Jr", "Christopher Brown"],
    "christopher cenac": ["Chris Cenac", "Chris Cenac Jr", "Christopher Cenac"],
    "nathaniel ament": ["Nate Ament", "Nathaniel Ament"],
    "matthew able": ["Matt Able", "Matthew Able"],
    "nicholas boyd": ["Nick Boyd", "Nicholas Boyd"],
}

# RealGM pages are Cloudflare-blocked from this local environment, but the same
# public RealGM profile/directory pages are visible through indexed snippets.
# These entries are only for unambiguous 2026 rows where name/team context and
# birth date were visible on RealGM pages.
REALGM_INDEXED_OVERRIDES = {
    "aaron nkrumah": ("2001-11-26", "Aaron Nkrumah", "Tennessee State", "Tennessee State", "https://basketball.realgm.com/player/Aaron-Nkrumah/Summary/209094"),
    "aday mara": ("2005-04-07", "Aday Mara", "Michigan", "Michigan", "https://basketball.realgm.com/player/Aday-Mara/Bio/177830"),
    "alex karaban": ("2002-11-11", "Alex Karaban", "UConn", "UConn", "https://basketball.realgm.com/player/Alex-Karaban/Summary/151218"),
    "allen graves": ("2006-07-28", "Allen Graves", "Santa Clara", "Santa Clara", "https://basketball.realgm.com/player/Allen-Graves/Summary/217588"),
    "amari allen": ("2006-01-26", "Amari Allen", "Alabama", "Alabama", "https://basketball.realgm.com/player/Amari-Allen/Bio/202294"),
    "andrej stojakovic": ("2004-08-17", "Andrej Stojakovic", "Illinois", "Illinois", "https://basketball.realgm.com/player/Andrej-Stojakovic/Bio/192061"),
    "anicet dybantsa": ("2007-01-29", "A.J. Dybantsa", "Brigham Young", "Brigham Young", "https://basketball.realgm.com/player/AJ-Dybantsa/Summary/186435"),
    "baba miller": ("2004-02-07", "Baba Miller", "Cincinnati", "Cincinnati", "https://basketball.realgm.com/player/Baba-Miller/Bio/165593"),
    "bennett stirtz": ("2003-10-03", "Bennett Stirtz", "Iowa", "Iowa", "https://basketball.realgm.com/player/Bennett-Stirtz/Bio/201012"),
    "billy richmond": ("2006-04-11", "Billy Richmond III", "Arkansas", "Arkansas", "https://basketball.realgm.com/info/birth_cities/88/Memphis-TN-United-States"),
    "braden smith": ("2003-07-25", "Braden Smith", "Purdue", "Purdue", "https://basketball.realgm.com/info/birth_cities/4690/Westfield-IN-United-States"),
    "brayden burries": ("2005-09-18", "Brayden Burries", "Arizona", "Arizona", "https://basketball.realgm.com/player/Brayden-Burries/Bio/200247"),
    "bruce thornton": ("2003-09-14", "Bruce Thornton", "Ohio State", "Ohio State", "https://basketball.realgm.com/info/birth_cities/1938/Alpharetta-GA-United-States"),
    "bryce hopkins": ("2001-09-07", "Bryce Hopkins", "St. John's", "St. John's", "https://basketball.realgm.com/ncaa/conferences/American-Athletic-Conference/4/St-Johns/75/rosters"),
    "caleb wilson": ("2006-07-18", "Caleb Wilson", "North Carolina", "North Carolina", "https://basketball.realgm.com/player/Caleb-Wilson/Bio/200430"),
    "cameron boozer": ("2007-07-18", "Cameron Boozer", "Duke", "Duke", "https://basketball.realgm.com/player/Cameron-Boozer/Summary/184287"),
    "cameron carr": ("2004-11-21", "Cameron Carr", "Baylor", "Baylor", "https://basketball.realgm.com/player/Cameron-Carr/Summary/196892"),
    "christian anderson": ("2006-04-02", "Christian Anderson, Jr.", "Texas Tech", "Texas Tech", "https://basketball.realgm.com/player/Christian-Anderson-Jr/Bio/187435"),
    "christopher brown": ("2006-04-03", "Mikel Brown Jr.", "Louisville", "Louisville", "https://basketball.realgm.com/player/Mikel-Brown-Jr/Bests/198014"),
    "christopher cenac": ("2007-01-31", "Chris Cenac, Jr.", "Houston", "Houston", "https://basketball.realgm.com/player/Chris-Cenac-Jr/Summary/198525"),
    "dailyn swain": ("2005-07-15", "Dailyn Swain", "Texas", "Texas", "https://basketball.realgm.com/player/Dailyn-Swain/Bio/192066"),
    "darius acuff": ("2006-11-16", "Darius Acuff, Jr.", "Arkansas", "Arkansas", "https://basketball.realgm.com/player/Darius-Acuff-Jr/Bio/216187"),
    "darryn peterson": ("2007-01-17", "Darryn Peterson", "Kansas", "Kansas", "https://basketball.realgm.com/player/Darryn-Peterson/Bio/196886"),
    "dillon mitchell": ("2003-10-03", "Dillon Mitchell", "St. John's", "St. John's", "https://basketball.realgm.com/player/Dillon-Mitchell/Summary/176104"),
    "ebuka okorie": ("2007-04-10", "Ebuka Okorie", "Stanford", "Stanford", "https://basketball.realgm.com/player/Ebuka-Okorie/Bio/193635"),
    "emanuel sharp": ("2004-03-07", "Emanuel Sharp", "Houston", "Houston", "https://basketball.realgm.com/player/Emanuel-Sharp/Bio/138743"),
    "felix okpara": ("2004-04-20", "Felix Okpara", "Tennessee", "Tennessee", "https://basketball.realgm.com/player/Felix-Okpara/Comparison/150125/Brandon-Garrison/180396"),
    "flory bidunga": ("2005-05-20", "Flory Bidunga", "Kansas", "Kansas", "https://basketball.realgm.com/ncaa/players/2026/B"),
    "izaiyah nelson": ("2003-10-01", "Izaiyah Nelson", "South Florida", "South Florida", "https://basketball.realgm.com/info/birthdays/20031001/1"),
    "jeremy fears": ("2005-04-19", "Jeremy Fears, Jr.", "Michigan State", "Michigan State", "https://basketball.realgm.com/player/Jeremy-Fears-Jr/Bio/162124"),
    "john blackwell": ("2004-12-25", "John Blackwell", "Wisconsin", "Wisconsin", "https://basketball.realgm.com/ncaa/players/2026/B"),
    "joshua jefferson": ("2003-11-21", "Joshua Jefferson", "Iowa State", "Iowa State", "https://basketball.realgm.com/info/birthdays/20031121/1"),
    "karim lopez": ("2007-04-12", "Karim Lopez", "New Zealand", "New Zealand", "https://basketball.realgm.com/player/Karim-Lopez/Bio/199566"),
    "keaton wagler": ("2007-02-03", "Keaton Wagler", "Illinois", "Illinois", "https://basketball.realgm.com/player/Keaton-Wagler/Bio/242991"),
    "keyshawn hall": ("2003-04-09", "Keyshawn Hall", "Auburn", "Auburn", "https://basketball.realgm.com/player/Keyshawn-Hall/Bio/201948"),
    "kingston flemings": ("2007-01-03", "Kingston Flemings", "Houston", "Houston", "https://basketball.realgm.com/player/Kingston-Flemings/Summary/216043"),
    "koa peat": ("2007-01-20", "Koa Peat", "Arizona", "Arizona", "https://basketball.realgm.com/player/Koa-Peat/Comparison/180367/Carmelo-Anthony/452"),
    "kylan boswell": ("2005-04-18", "Kylan Boswell", "Illinois", "Illinois", "https://basketball.realgm.com/info/birth_cities/10206/Urbana-IL-United-States"),
    "labaron philon": ("2005-11-24", "Labaron Philon, Jr.", "Alabama", "Alabama", "https://basketball.realgm.com/player/Labaron-Philon-Jr/Bio/200450"),
    "luigi suigo": ("2007-01-29", "Luigi Suigo", "KK Mega Bemax", "AX Armani Exchange Milan", "https://basketball.realgm.com/player/Luigi-Suigo/Summary/201784"),
    "malachi moreno": ("2006-10-24", "Malachi Moreno", "Kentucky", "Kentucky", "https://basketball.realgm.com/player/Malachi-Moreno/Comparison/211524/James-Harden/1598"),
    "maliq brown": ("2003-11-16", "Maliq Brown", "Duke", "Duke", "https://basketball.realgm.com/info/birthdays/20031116/1"),
    "matthew able": ("2006-08-11", "Matt Able", "N.C. State", "N.C. State", "https://basketball.realgm.com/player/Matt-Able/Summary/216727"),
    "meleek thomas": ("2006-08-06", "Meleek Thomas", "Arkansas", "Arkansas", "https://basketball.realgm.com/player/Meleek-Thomas/Bio/196884"),
    "milan momcilovic": ("2004-09-22", "Milan Momcilovic", "Iowa State", "Iowa State", "https://basketball.realgm.com/info/birth-cities/4701/Pewaukee-WI-United-States"),
    "milos uzan": ("2002-12-26", "Milos Uzan", "Houston", "Houston", "https://basketball.realgm.com/player/Milos-Uzan/Bio/162025"),
    "morez johnson": ("2006-01-25", "Morez Johnson, Jr.", "Michigan", "Michigan", "https://basketball.realgm.com/player/Morez-Johnson-Jr/Bio/194003"),
    "nathaniel ament": ("2006-12-10", "Nate Ament", "Tennessee", "Tennessee", "https://basketball.realgm.com/player/Nate-Ament/Bio/216549"),
    "nicholas boyd": ("2001-04-23", "Nick Boyd", "Wisconsin", "Wisconsin", "https://basketball.realgm.com/player/Nick-Boyd/Bio/169099"),
    "nick martinelli": ("2004-04-20", "Nick Martinelli", "Northwestern", "Northwestern", "https://basketball.realgm.com/info/birth-cities/2076/Glenview-IL-United-States"),
    "otega oweh": ("2003-06-21", "Otega Oweh", "Kentucky", "Kentucky", "https://basketball.realgm.com/info/birth-cities/220/Newark-NJ-United-States"),
    "peter suder": ("2003-07-29", "Peter Suder", "Miami (OH)", "Miami (OH)", "https://basketball.realgm.com/info/birth-cities/918/Carmel-IN-United-States"),
    "rafael castro": ("2000-01-14", "Rafael Castro", "George Washington", "George Washington", "https://basketball.realgm.com/player/Gelvis-Solano/Comparison/70434/Rafael-Castro/92185"),
    "richie saunders": ("2001-09-19", "Richie Saunders", "Brigham Young", "Brigham Young", "https://basketball.realgm.com/player/Richie-Saunders/Bio/139115"),
    "rueben chinyelu": ("2003-09-30", "Rueben Chinyelu", "Florida", "Florida", "https://basketball.realgm.com/player/Rueben-Chinyelu/Bio/170741"),
    "ryan conwell": ("2004-06-15", "Ryan Conwell", "Louisville", "Louisville", "https://basketball.realgm.com/player/Ryan-Conwell/Summary/199681"),
    "sergio de larrea": ("2005-12-04", "Sergio De Larrea", "Valencia Basket", "Valencia Basket", "https://basketball.realgm.com/player/Sergio-De-Larrea/Summary/175825"),
    "tarris reed": ("2003-08-05", "Tarris Reed, Jr.", "UConn", "UConn", "https://basketball.realgm.com/ncaa/awards/14/NCAA-East-All-Region-Team"),
    "tobe awaka": ("2004-01-30", "Tobe Awaka", "Arizona", "Arizona", "https://basketball.realgm.com/ncaa/conferences/Big-12-Conference/3/Awards/Historical?f=i"),
    "tobi lawal": ("2003-05-01", "Tobi Lawal", "Virginia Tech", "Virginia Tech", "https://basketball.realgm.com/player/Tobi-Lawal/Bio/202405"),
    "tounde yessoufou": ("2006-05-15", "Tounde Yessoufou", "Baylor", "Baylor", "https://basketball.realgm.com/player/Tounde-Yessoufou/Bio/199606"),
    "trevon brazile": ("2003-01-07", "Trevon Brazile", "Arkansas", "Arkansas", "https://basketball.realgm.com/info/birthdays/20030107/1"),
    "trey kaufman renn": ("2002-08-19", "Trey Kaufman-Renn", "Purdue", "Purdue", "https://basketball.realgm.com/player/Trey-Kaufman-Renn/Bio/152727"),
    "tyler bilodeau": ("2004-04-17", "Tyler Bilodeau", "UCLA", "UCLA", "https://basketball.realgm.com/ncaa/conferences/Big-Ten-Conference/2/UCLA/241/Rosters/2026"),
    "tyler nickel": ("2003-09-05", "Tyler Nickel", "Vanderbilt", "Vanderbilt", "https://basketball.realgm.com/player/Tyler-Nickel/Summary/176059"),
    "tyler tanner": ("2006-02-01", "Tyler Tanner", "Vanderbilt", "Vanderbilt", "https://basketball.realgm.com/ncaa/players/2026/T"),
    "ugonna onyenso": ("2004-09-25", "Ugonna Onyenso", "Virginia", "Virginia", "https://basketball.realgm.com/player/Ugonna-Onyenso/Summary/192946"),
    "yaxel lendeborg": ("2002-09-30", "Yaxel Lendeborg", "Michigan", "Michigan", "https://basketball.realgm.com/player/Yaxel-Lendeborg/Bio/177627"),
    "zuby ejiofor": ("2004-04-20", "Zuby Ejiofor", "St. John's", "St. John's", "https://basketball.realgm.com/player/Zuby-Ejiofor/Bio/176053"),
}

TECHNICAL_COLUMNS_TO_REMOVE = [
    "birth_date_source",
    "birth_date_confidence",
    "age_validation_status",
    "id_source",
    "draft_date",
    "ncaa_team",
    "ncaa_source",
    "ncaa_player_raw",
    "ncaa_match_method",
    "sportsref_url",
    "sportsref_match_method",
    "sportsref_match_score",
    "sportsref_player_raw",
]


def clean_name(name: object) -> str:
    if pd.isna(name):
        return ""
    s = str(name).strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def compute_age_years(birth_date: str, draft_date: str = DRAFT_DATE_2026) -> float | pd.NA:
    birth = pd.to_datetime(birth_date, errors="coerce")
    draft = pd.to_datetime(draft_date, errors="coerce")
    if pd.isna(birth) or pd.isna(draft):
        return pd.NA
    return round((draft - birth).days / 365.25, 3)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def ddg_result_url(raw_href: str) -> str:
    if not raw_href:
        return ""
    if raw_href.startswith("//"):
        raw_href = "https:" + raw_href
    parsed = urlparse(raw_href)
    qs = parse_qs(parsed.query)
    if "uddg" in qs:
        return unquote(qs["uddg"][0])
    return raw_href


def is_realgm_player_url(url: str) -> bool:
    return "basketball.realgm.com/player/" in url and "/Summary/" in url


def search_realgm_profiles(session: requests.Session, query_name: str, organization: str | None, max_results: int = 5) -> list[str]:
    query_parts = [f'"{query_name}"', "RealGM", "basketball", "Born"]
    if organization and isinstance(organization, str) and organization.strip():
        query_parts.append(organization)
    query = " ".join(query_parts)
    url = "https://duckduckgo.com/html/"
    try:
        response = session.get(url, params={"q": query}, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    urls = []
    for a in soup.select("a.result__a"):
        href = ddg_result_url(a.get("href", ""))
        if is_realgm_player_url(href):
            urls.append(href)
    # Fallback: scan all links.
    for a in soup.find_all("a", href=True):
        href = ddg_result_url(a["href"])
        if is_realgm_player_url(href):
            urls.append(href)

    unique = []
    seen = set()
    for u in urls:
        if u not in seen:
            unique.append(u)
            seen.add(u)
    time.sleep(SEARCH_SLEEP_SECONDS)
    return unique[:max_results]


def candidate_query_names(dataset_name: str) -> list[str]:
    aliases = NAME_ALIASES.get(clean_name(dataset_name), [])
    names = [dataset_name, *aliases]
    # Title-case fallback.
    names.append(" ".join(part.capitalize() for part in dataset_name.split()))
    unique = []
    seen = set()
    for n in names:
        c = clean_name(n)
        if c and c not in seen:
            unique.append(n)
            seen.add(c)
    return unique


@dataclass
class ProfileParse:
    url: str
    display_name: str | None
    clean_display_name: str
    birth_date: str | None
    current_team: str | None
    pre_draft_team: str | None
    text: str


def parse_realgm_profile(session: requests.Session, url: str) -> ProfileParse | None:
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
    except Exception:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    text = normalize_text(soup.get_text(" ", strip=True))

    # RealGM pages often have the profile name in h2. If not, use title or URL slug.
    display = None
    h2 = soup.find("h2")
    if h2:
        display = normalize_text(h2.get_text(" ", strip=True))
    if not display:
        title = soup.find("title")
        if title:
            display = normalize_text(title.get_text(" ", strip=True).split(" Player Profile")[0])

    birth_date = None
    m = re.search(r"Born:\s*([A-Z][a-z]{2,8}\s+\d{1,2},\s+\d{4})", text)
    if m:
        parsed = pd.to_datetime(m.group(1), errors="coerce")
        if not pd.isna(parsed):
            birth_date = parsed.strftime("%Y-%m-%d")

    current_team = None
    m = re.search(r"Current Team:\s*([^#]+?)\s+Current NBA Status", text)
    if m:
        current_team = normalize_text(m.group(1))

    pre_draft_team = None
    m = re.search(r"Pre-Draft Team:\s*([^#]+?)\s+\(", text)
    if m:
        pre_draft_team = normalize_text(m.group(1))

    time.sleep(REQUEST_SLEEP_SECONDS)
    return ProfileParse(
        url=url,
        display_name=display,
        clean_display_name=clean_name(display),
        birth_date=birth_date,
        current_team=current_team,
        pre_draft_team=pre_draft_team,
        text=text,
    )


def context_score(profile: ProfileParse, organization: Any) -> float:
    if pd.isna(organization) or not str(organization).strip():
        return 0.0
    org_clean = clean_name(organization)
    contexts = [profile.current_team, profile.pre_draft_team]
    scores = [fuzz.partial_ratio(org_clean, clean_name(c)) for c in contexts if c]
    return max(scores) if scores else 0.0


def choose_profile_for_player(session: requests.Session, row: pd.Series) -> dict[str, Any]:
    dataset_name = row["name"]
    organization = row.get("organization", pd.NA)
    allowed_clean_names = {clean_name(dataset_name)} | {clean_name(x) for x in NAME_ALIASES.get(clean_name(dataset_name), [])}
    dataset_clean = clean_name(dataset_name)

    indexed_override = REALGM_INDEXED_OVERRIDES.get(dataset_clean)
    if indexed_override:
        birth_date, display_name, current_team, pre_draft_team, source_url = indexed_override
        parsed = ProfileParse(
            url=source_url,
            display_name=display_name,
            clean_display_name=clean_name(display_name),
            birth_date=birth_date,
            current_team=current_team,
            pre_draft_team=pre_draft_team,
            text="",
        )
        name_score = max(fuzz.ratio(parsed.clean_display_name, allowed) for allowed in allowed_clean_names if allowed)
        ctx_score = context_score(parsed, organization)
        age = compute_age_years(parsed.birth_date)
        plausible_age = pd.notna(age) and 16 <= float(age) <= 30
        accept = plausible_age and (
            name_score >= MIN_NAME_SCORE or (name_score >= 75 and ctx_score >= MIN_CONTEXT_SCORE)
        )
        return {
            "name": dataset_name,
            "draft_year": 2026,
            "overall_pick": row.get("overall_pick", pd.NA),
            "birth_date": parsed.birth_date if accept else pd.NA,
            "draft_age": age if accept else pd.NA,
            "source_url": parsed.url,
            "realgm_display_name": parsed.display_name,
            "current_team": parsed.current_team,
            "pre_draft_team": parsed.pre_draft_team,
            "name_score": name_score,
            "context_score": ctx_score,
            "status": "accepted_realgm_indexed_override" if accept else "indexed_override_rejected",
        }

    candidate_urls = []
    for qname in candidate_query_names(dataset_name):
        candidate_urls.extend(search_realgm_profiles(session, qname, organization, max_results=5))

    # De-duplicate.
    unique_urls = []
    seen = set()
    for u in candidate_urls:
        if u not in seen:
            unique_urls.append(u)
            seen.add(u)

    parsed_profiles = []
    for url in unique_urls[:10]:
        parsed = parse_realgm_profile(session, url)
        if parsed is None or parsed.birth_date is None:
            continue
        name_score = max(fuzz.ratio(parsed.clean_display_name, allowed) for allowed in allowed_clean_names if allowed)
        ctx_score = context_score(parsed, organization)
        age = compute_age_years(parsed.birth_date)
        parsed_profiles.append((parsed, name_score, ctx_score, age))

    accepted = []
    for parsed, name_score, ctx_score, age in parsed_profiles:
        plausible_age = pd.notna(age) and 16 <= float(age) <= 30
        # Accept if name is strong, or if name is decent and organization context is strong.
        accept = plausible_age and (
            name_score >= MIN_NAME_SCORE or (name_score >= 75 and ctx_score >= MIN_CONTEXT_SCORE)
        )
        if accept:
            accepted.append((parsed, name_score, ctx_score, age))

    if not accepted:
        best = None
        if parsed_profiles:
            best = sorted(parsed_profiles, key=lambda x: (x[1], x[2]), reverse=True)[0]
        return {
            "name": dataset_name,
            "draft_year": 2026,
            "overall_pick": row.get("overall_pick", pd.NA),
            "birth_date": pd.NA,
            "draft_age": pd.NA,
            "source_url": best[0].url if best else pd.NA,
            "realgm_display_name": best[0].display_name if best else pd.NA,
            "name_score": best[1] if best else pd.NA,
            "context_score": best[2] if best else pd.NA,
            "status": "unmatched_or_not_confident",
        }

    # Prefer highest name score, then context score.
    parsed, name_score, ctx_score, age = sorted(accepted, key=lambda x: (x[1], x[2]), reverse=True)[0]
    return {
        "name": dataset_name,
        "draft_year": 2026,
        "overall_pick": row.get("overall_pick", pd.NA),
        "birth_date": parsed.birth_date,
        "draft_age": age,
        "source_url": parsed.url,
        "realgm_display_name": parsed.display_name,
        "current_team": parsed.current_team,
        "pre_draft_team": parsed.pre_draft_team,
        "name_score": name_score,
        "context_score": ctx_score,
        "status": "accepted_realgm_profile",
    }


def build_overrides(base: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    targets = base[base["draft_year"].eq(2026) & base["draft_age"].isna()].copy()
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; university-data-science-project/1.0; educational use)"
    })

    rows = []
    print(f"2026 missing-age targets: {len(targets)}")
    for i, (_, row) in enumerate(targets.iterrows(), start=1):
        print(f"[{i}/{len(targets)}] {row['name']} ({row.get('organization', '')})")
        rows.append(choose_profile_for_player(session, row))

    results = pd.DataFrame(rows)
    accepted_mask = results["status"].astype(str).str.startswith("accepted_")
    matched = results[accepted_mask].copy()
    unmatched = results[~accepted_mask].copy()
    return matched, unmatched


def integrate_overrides(base: pd.DataFrame, overrides: pd.DataFrame) -> pd.DataFrame:
    out = base.copy()
    if overrides.empty:
        return out
    override_lookup = overrides.drop_duplicates(subset=["name", "draft_year"], keep="first")
    joined = out.reset_index().merge(
        override_lookup[["name", "draft_year", "birth_date", "draft_age"]],
        on=["name", "draft_year"],
        how="left",
        suffixes=("", "_override"),
    ).set_index("index")

    fill_mask = out["draft_year"].eq(2026) & out["draft_age"].isna() & joined["draft_age_override"].notna()
    out.loc[fill_mask, "birth_date"] = joined.loc[fill_mask, "birth_date_override"]
    out.loc[fill_mask, "draft_age"] = pd.to_numeric(joined.loc[fill_mask, "draft_age_override"], errors="coerce").to_numpy()
    out = out.drop(columns=[c for c in TECHNICAL_COLUMNS_TO_REMOVE if c in out.columns])
    return out


def write_report(before: pd.DataFrame, after: pd.DataFrame, overrides: pd.DataFrame, unmatched: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    before_2026 = before[before["draft_year"].eq(2026)]
    after_2026 = after[after["draft_year"].eq(2026)]

    summary_rows = [
        ["rows_before", len(before)],
        ["rows_after", len(after)],
        ["row_count_unchanged", len(before) == len(after)],
        ["columns_after", len(after.columns)],
        ["duplicate_name_draft_year_pick_rows", int(after.duplicated(subset=["name", "draft_year", "overall_pick"]).sum())],
        ["2026_rows", len(after_2026)],
        ["2026_draft_age_before", int(before_2026["draft_age"].notna().sum())],
        ["2026_draft_age_after", int(after_2026["draft_age"].notna().sum())],
        ["2026_missing_draft_age_after", int(after_2026["draft_age"].isna().sum())],
        ["2026_age_filled_from_realgm", len(overrides)],
    ]
    summary_rows.extend([[f"technical_{col}_absent", col not in after.columns] for col in TECHNICAL_COLUMNS_TO_REMOVE])
    summary = pd.DataFrame(summary_rows, columns=["metric", "value"])

    youngest_2026 = after_2026[after_2026["draft_age"].notna()].sort_values("draft_age").head(30)
    oldest_2026 = after_2026[after_2026["draft_age"].notna()].sort_values("draft_age", ascending=False).head(30)
    still_missing = after_2026[after_2026["draft_age"].isna()][[
        "name", "draft_year", "overall_pick", "position", "organization", "organization_type", "ncaa_exp", "ncaa_ppg", "draft_age"
    ]]

    lines = []
    lines.append("# 2026 RealGM Birth Date / Draft Age Repair Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## Accepted RealGM Overrides")
    lines.append("")
    lines.append(overrides.to_markdown(index=False) if not overrides.empty else "_None_")
    lines.append("")
    lines.append("## Unmatched / Not Confident")
    lines.append("")
    lines.append(unmatched.to_markdown(index=False) if not unmatched.empty else "_None_")
    lines.append("")
    lines.append("## Youngest 2026 Players With Draft Age")
    lines.append("")
    lines.append(youngest_2026[["name", "birth_date", "draft_age", "position", "organization", "ncaa_exp"]].to_markdown(index=False) if not youngest_2026.empty else "_None_")
    lines.append("")
    lines.append("## Oldest 2026 Players With Draft Age")
    lines.append("")
    lines.append(oldest_2026[["name", "birth_date", "draft_age", "position", "organization", "ncaa_exp"]].to_markdown(index=False) if not oldest_2026.empty else "_None_")
    lines.append("")
    lines.append("## 2026 Rows Still Missing Draft Age")
    lines.append("")
    lines.append(still_missing.to_markdown(index=False) if not still_missing.empty else "_None_")
    lines.append("")
    lines.append("## Final Columns")
    lines.append("")
    for col in after.columns:
        lines.append(f"- {col}")
    lines.append("")
    lines.append("## Technical Column Absence Checks")
    lines.append("")
    absence_checks = pd.DataFrame(
        [{"column": col, "absent": col not in after.columns} for col in TECHNICAL_COLUMNS_TO_REMOVE]
    )
    lines.append(absence_checks.to_markdown(index=False))

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_2000_2026.csv")
    parser.add_argument("--out", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_2000_2026.csv")
    parser.add_argument("--overrides-out", default="data/player_birth_dates_2026_realgm_overrides.csv")
    parser.add_argument("--unmatched-out", default="data/player_birth_dates_2026_realgm_unmatched.csv")
    parser.add_argument("--report", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_agefix_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_path = Path(args.base)
    base = pd.read_csv(base_path)
    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = pd.to_numeric(base["draft_year"], errors="coerce").astype("Int64")
    base["overall_pick"] = pd.to_numeric(base["overall_pick"], errors="coerce")
    base["draft_age"] = pd.to_numeric(base["draft_age"], errors="coerce")

    overrides, unmatched = build_overrides(base)
    final = integrate_overrides(base, overrides)

    assert len(final) == len(base), "Row count changed."
    assert final.duplicated(subset=["name", "draft_year", "overall_pick"]).sum() == 0, "Duplicates introduced."

    out_path = Path(args.out)
    overrides_path = Path(args.overrides_out)
    unmatched_path = Path(args.unmatched_out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    final.to_csv(out_path, index=False)
    overrides.to_csv(overrides_path, index=False)
    unmatched.to_csv(unmatched_path, index=False)
    write_report(base, final, overrides, unmatched, report_path)

    before_2026 = base[base["draft_year"].eq(2026)]
    after_2026 = final[final["draft_year"].eq(2026)]
    print(f"Saved age-fixed dataset: {out_path}")
    print(f"Saved overrides: {overrides_path}")
    print(f"Saved unmatched: {unmatched_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(final)}")
    print(f"2026 draft_age before: {before_2026['draft_age'].notna().sum()} / {len(before_2026)}")
    print(f"2026 draft_age after: {after_2026['draft_age'].notna().sum()} / {len(after_2026)}")


if __name__ == "__main__":
    main()
