#!/usr/bin/env Rscript

# Build a standalone NCAA player-season statistics dataset from Bart Torvik/toRvik.
# This script intentionally does not merge NCAA data with NBA Draft/Combine data.

required_packages <- c(
  "toRvik", "dplyr", "purrr", "readr", "stringr", "stringi",
  "tibble", "tidyr", "knitr", "jsonlite", "curl"
)

install_missing_packages <- function(packages) {
  missing <- setdiff(packages, "toRvik")
  missing <- missing[!vapply(missing, requireNamespace, logical(1), quietly = TRUE)]
  if (length(missing) > 0) {
    install.packages(missing, repos = "https://cloud.r-project.org")
  }
  if (!requireNamespace("toRvik", quietly = TRUE)) {
    if (!requireNamespace("remotes", quietly = TRUE)) {
      install.packages("remotes", repos = "https://cloud.r-project.org")
    }
    remotes::install_github("andreweatherman/toRvik", upgrade = "never")
  }
}

install_missing_packages(required_packages)

suppressPackageStartupMessages({
  library(toRvik)
  library(dplyr)
  library(purrr)
  library(readr)
  library(stringr)
  library(stringi)
  library(tibble)
  library(tidyr)
  library(knitr)
  library(jsonlite)
  library(curl)
})

FINAL_COLUMNS <- c(
  "name",
  "draft_year",
  "ncaa_player_raw",
  "ncaa_team",
  "ncaa_conf",
  "ncaa_pos",
  "ncaa_exp",
  "ncaa_height",
  "ncaa_games",
  "ncaa_mpg",
  "ncaa_ppg",
  "ncaa_fg_pct",
  "ncaa_two_pct",
  "ncaa_three_pct",
  "ncaa_ft_pct",
  "ncaa_oreb",
  "ncaa_dreb",
  "ncaa_rpg",
  "ncaa_apg",
  "ncaa_ast_to",
  "ncaa_spg",
  "ncaa_bpg",
  "ncaa_tpg",
  "ncaa_ortg",
  "ncaa_adj_oe",
  "ncaa_drtg",
  "ncaa_porpag",
  "ncaa_dporpag",
  "ncaa_bpm",
  "ncaa_obpm",
  "ncaa_dbpm",
  "ncaa_usage"
)

TEXT_NCAA_COLUMNS <- c(
  "ncaa_player_raw", "ncaa_team", "ncaa_conf", "ncaa_pos",
  "ncaa_exp", "ncaa_height"
)

clean_name <- function(x) {
  x |>
    as.character() |>
    stringi::stri_trans_general("Latin-ASCII") |>
    stringr::str_to_lower() |>
    stringr::str_replace_all("\\b(jr|sr|ii|iii|iv|v)\\b\\.?", "") |>
    stringr::str_replace_all("[^a-z0-9 ]+", " ") |>
    stringr::str_squish()
}

safe_numeric <- function(x) {
  suppressWarnings(readr::parse_number(as.character(x)))
}

percent_to_rate <- function(x) {
  y <- safe_numeric(x)
  dplyr::if_else(!is.na(y) & y > 1, y / 100, y)
}

ensure_columns <- function(df, columns) {
  for (col in columns) {
    if (!col %in% names(df)) {
      df[[col]] <- NA
    }
  }
  df
}

fetch_torvik_year <- function(year, stat) {
  message("Fetching Torvik ", stat, " player-season stats for ", year, "...")
  tryCatch(
    {
      raw <- suppressWarnings(toRvik::bart_player_season(year = year, stat = stat))
      raw <- tibble::as_tibble(raw)
      raw$draft_year <- year
      if (nrow(raw) == 0) {
        message("Returned zero ", stat, " rows for ", year)
        return(list(data = raw, failed = TRUE, error = "returned zero rows"))
      }
      list(data = raw, failed = FALSE, error = NA_character_)
    },
    error = function(e) {
      message("Failed ", stat, " stats for ", year, ": ", conditionMessage(e))
      list(data = tibble::tibble(draft_year = integer()), failed = TRUE, error = conditionMessage(e))
    }
  )
}

row_value <- function(row, zero_based_index) {
  idx <- zero_based_index + 1
  if (length(row) < idx || is.null(row[[idx]])) {
    return(NA)
  }
  row[[idx]]
}

fetch_public_playerstat_year <- function(year) {
  message("Fetching Bart Torvik public fallback player stats for ", year, "...")
  start_date <- paste0(year - 1, "1101")
  end_date <- paste0(year, "0501")
  page_url <- paste0("https://barttorvik.com/playerstat.php?year=", year)
  api_url <- paste0(
    "https://barttorvik.com/getadvstats.php?",
    "year=", year,
    "&specialSource=0&conyes=0",
    "&start=", start_date,
    "&end=", end_date,
    "&top=364&xvalue=All&page=playerstat&team="
  )

  tryCatch(
    {
      handle <- curl::new_handle()
      curl::handle_setopt(
        handle,
        useragent = "Mozilla/5.0",
        cookiefile = "",
        cookiejar = "",
        post = TRUE,
        postfields = "js_test_submitted=1"
      )
      curl::curl_fetch_memory(page_url, handle = handle)
      curl::handle_setopt(handle, post = FALSE, httpget = TRUE)
      response <- curl::curl_fetch_memory(api_url, handle = handle)
      text <- rawToChar(response$content)
      parsed <- jsonlite::fromJSON(text, simplifyVector = FALSE)
      if (!is.list(parsed) || length(parsed) == 0) {
        stop("public endpoint returned no rows")
      }

      rows <- purrr::map_dfr(parsed, function(row) {
        player <- row_value(row, 0)
        tibble::tibble(
          name = clean_name(player),
          draft_year = as.integer(year),
          ncaa_player_raw = as.character(player),
          ncaa_team = as.character(row_value(row, 1)),
          ncaa_conf = as.character(row_value(row, 2)),
          ncaa_pos = as.character(row_value(row, 64)),
          ncaa_exp = as.character(row_value(row, 25)),
          ncaa_height = as.character(row_value(row, 26)),
          ncaa_games = safe_numeric(row_value(row, 3)),
          ncaa_mpg = NA_real_,
          ncaa_ppg = safe_numeric(row_value(row, 63)),
          ncaa_fg_pct = NA_real_,
          ncaa_two_pct = percent_to_rate(row_value(row, 18)),
          ncaa_three_pct = percent_to_rate(row_value(row, 21)),
          ncaa_ft_pct = percent_to_rate(row_value(row, 15)),
          ncaa_oreb = safe_numeric(row_value(row, 57)),
          ncaa_dreb = safe_numeric(row_value(row, 58)),
          ncaa_rpg = safe_numeric(row_value(row, 59)),
          ncaa_apg = safe_numeric(row_value(row, 60)),
          ncaa_ast_to = safe_numeric(row_value(row, 35)),
          ncaa_spg = safe_numeric(row_value(row, 61)),
          ncaa_bpg = safe_numeric(row_value(row, 62)),
          ncaa_tpg = NA_real_,
          ncaa_ortg = safe_numeric(row_value(row, 5)),
          ncaa_adj_oe = safe_numeric(row_value(row, 30)),
          ncaa_drtg = safe_numeric(row_value(row, 49)),
          ncaa_porpag = safe_numeric(row_value(row, 29)),
          ncaa_dporpag = safe_numeric(row_value(row, 48)),
          ncaa_bpm = safe_numeric(row_value(row, 50)),
          ncaa_obpm = safe_numeric(row_value(row, 51)),
          ncaa_dbpm = safe_numeric(row_value(row, 52)),
          ncaa_usage = safe_numeric(row_value(row, 6))
        )
      })

      rows <- rows |> dplyr::filter(!is.na(name), name != "")
      if (nrow(rows) == 0) {
        stop("public endpoint rows did not contain player names")
      }
      list(data = rows, failed = FALSE, error = NA_character_)
    },
    error = function(e) {
      warning("Failed public fallback stats for ", year, ": ", conditionMessage(e))
      list(data = tibble::tibble(), failed = TRUE, error = conditionMessage(e))
    }
  )
}

standardize_box <- function(df) {
  if (nrow(df) == 0) {
    return(tibble::tibble())
  }

  expected <- c(
    "player", "draft_year", "team", "conf", "pos", "exp", "hgt",
    "g", "games", "mpg", "ppg", "fg_pct", "oreb", "dreb", "rpg",
    "apg", "ast_to", "spg", "bpg", "tpg", "tov", "id"
  )
  df <- ensure_columns(df, expected)
  games_col <- if ("games" %in% names(df) && any(!is.na(df$games))) "games" else "g"
  turnover_col <- if ("tpg" %in% names(df) && any(!is.na(df$tpg))) "tpg" else "tov"

  tibble::tibble(
    name = clean_name(df$player),
    draft_year = as.integer(df$draft_year),
    ncaa_player_raw = as.character(df$player),
    ncaa_team = as.character(df$team),
    ncaa_conf = as.character(df$conf),
    ncaa_pos = as.character(df$pos),
    ncaa_exp = as.character(df$exp),
    ncaa_height = as.character(df$hgt),
    ncaa_games = safe_numeric(df[[games_col]]),
    ncaa_mpg = safe_numeric(df$mpg),
    ncaa_ppg = safe_numeric(df$ppg),
    ncaa_fg_pct = percent_to_rate(df$fg_pct),
    ncaa_oreb = safe_numeric(df$oreb),
    ncaa_dreb = safe_numeric(df$dreb),
    ncaa_rpg = safe_numeric(df$rpg),
    ncaa_apg = safe_numeric(df$apg),
    ncaa_ast_to = safe_numeric(df$ast_to),
    ncaa_spg = safe_numeric(df$spg),
    ncaa_bpg = safe_numeric(df$bpg),
    ncaa_tpg = safe_numeric(df[[turnover_col]]),
    ncaa_torvik_id = as.character(df$id)
  )
}

standardize_shooting <- function(df) {
  if (nrow(df) == 0) {
    return(tibble::tibble())
  }

  expected <- c(
    "player", "draft_year", "team", "conf", "two_pct", "tp_pct",
    "three_pct", "ft_pct", "usg", "id"
  )
  df <- ensure_columns(df, expected)
  three_col <- if ("three_pct" %in% names(df) && any(!is.na(df$three_pct))) "three_pct" else "tp_pct"

  tibble::tibble(
    name = clean_name(df$player),
    draft_year = as.integer(df$draft_year),
    ncaa_two_pct = percent_to_rate(df$two_pct),
    ncaa_three_pct = percent_to_rate(df[[three_col]]),
    ncaa_ft_pct = percent_to_rate(df$ft_pct),
    ncaa_usage = safe_numeric(df$usg),
    ncaa_torvik_id = as.character(df$id)
  )
}

standardize_advanced <- function(df) {
  if (nrow(df) == 0) {
    return(tibble::tibble())
  }

  expected <- c(
    "player", "draft_year", "team", "conf", "ortg", "adj_oe", "drtg",
    "porpag", "dporpag", "bpm", "obpm", "dbpm", "usg", "id", "pick"
  )
  df <- ensure_columns(df, expected)

  # Intentionally do not keep any column named "pick".
  tibble::tibble(
    name = clean_name(df$player),
    draft_year = as.integer(df$draft_year),
    ncaa_team = as.character(df$team),
    ncaa_conf = as.character(df$conf),
    ncaa_ortg = safe_numeric(df$ortg),
    ncaa_adj_oe = safe_numeric(df$adj_oe),
    ncaa_drtg = safe_numeric(df$drtg),
    ncaa_porpag = safe_numeric(df$porpag),
    ncaa_dporpag = safe_numeric(df$dporpag),
    ncaa_bpm = safe_numeric(df$bpm),
    ncaa_obpm = safe_numeric(df$obpm),
    ncaa_dbpm = safe_numeric(df$dbpm),
    ncaa_usage = safe_numeric(df$usg),
    ncaa_torvik_id = as.character(df$id)
  )
}

dedupe_stat <- function(df) {
  if (nrow(df) == 0) {
    return(df)
  }
  df |>
    dplyr::arrange(name, draft_year) |>
    dplyr::group_by(name, draft_year) |>
    dplyr::slice(1) |>
    dplyr::ungroup()
}

resolve_duplicates <- function(df) {
  df |>
    dplyr::arrange(
      name,
      draft_year,
      dplyr::desc(dplyr::coalesce(ncaa_mpg, -Inf)),
      dplyr::desc(dplyr::coalesce(ncaa_games, -Inf))
    ) |>
    dplyr::group_by(name, draft_year) |>
    dplyr::slice(1) |>
    dplyr::ungroup()
}

coalesce_joined <- function(df, base_col, suffix_col) {
  if (suffix_col %in% names(df)) {
    df[[base_col]] <- dplyr::coalesce(df[[base_col]], df[[suffix_col]])
    df[[suffix_col]] <- NULL
  }
  df
}

build_ncaa_dataset <- function(start_year, end_year) {
  years <- seq.int(start_year, end_year)

  box_results <- purrr::map(years, fetch_torvik_year, stat = "box")
  shooting_results <- purrr::map(years, fetch_torvik_year, stat = "shooting")
  advanced_results <- purrr::map(years, fetch_torvik_year, stat = "advanced")

  torvik_box_failed <- years[vapply(box_results, function(x) isTRUE(x$failed), logical(1))]
  torvik_shooting_failed <- years[vapply(shooting_results, function(x) isTRUE(x$failed), logical(1))]
  torvik_advanced_failed <- years[vapply(advanced_results, function(x) isTRUE(x$failed), logical(1))]

  fallback_needed <- sort(unique(c(torvik_box_failed, torvik_shooting_failed, torvik_advanced_failed)))
  fallback_results <- purrr::map(fallback_needed, fetch_public_playerstat_year)
  names(fallback_results) <- as.character(fallback_needed)
  fallback_success_years <- fallback_needed[
    vapply(fallback_results, function(x) !isTRUE(x$failed) && nrow(x$data) > 0, logical(1))
  ]

  fallback_data <- fallback_results |>
    purrr::map("data") |>
    dplyr::bind_rows()

  box <- box_results |>
    purrr::map("data") |>
    purrr::map(standardize_box) |>
    dplyr::bind_rows()

  shooting <- shooting_results |>
    purrr::map("data") |>
    purrr::map(standardize_shooting) |>
    dplyr::bind_rows() |>
    dedupe_stat()

  advanced <- advanced_results |>
    purrr::map("data") |>
    purrr::map(standardize_advanced) |>
    dplyr::bind_rows() |>
    dedupe_stat()

  if (nrow(fallback_data) > 0) {
    box <- dplyr::bind_rows(
      box,
      fallback_data |>
        dplyr::filter(draft_year %in% torvik_box_failed) |>
        dplyr::mutate(ncaa_torvik_id = NA_character_)
    )
  }

  if (nrow(box) == 0) {
    stop("No NCAA data were fetched.")
  }

  joined <- box |>
    dplyr::left_join(
      shooting |> dplyr::select(-dplyr::any_of("ncaa_torvik_id")),
      by = c("name", "draft_year"),
      suffix = c("", "_shooting")
    ) |>
    dplyr::left_join(
      advanced |> dplyr::select(-dplyr::any_of(c("ncaa_team", "ncaa_conf", "ncaa_torvik_id"))),
      by = c("name", "draft_year"),
      suffix = c("", "_advanced")
    )

  for (col in c("ncaa_two_pct", "ncaa_three_pct", "ncaa_ft_pct", "ncaa_usage")) {
    joined <- coalesce_joined(joined, col, paste0(col, "_shooting"))
  }

  for (col in c(
    "ncaa_two_pct", "ncaa_three_pct", "ncaa_ft_pct", "ncaa_usage",
    "ncaa_ortg", "ncaa_adj_oe", "ncaa_drtg", "ncaa_porpag", "ncaa_dporpag",
    "ncaa_bpm", "ncaa_obpm", "ncaa_dbpm"
  )) {
    joined <- coalesce_joined(joined, col, paste0(col, "_advanced"))
  }

  before_dedup_rows <- nrow(joined)

  final <- joined |>
    resolve_duplicates() |>
    ensure_columns(FINAL_COLUMNS)

  final <- final[, FINAL_COLUMNS]
  if ("pick" %in% names(final)) {
    stop("Unexpected column named pick found in final NCAA CSV.")
  }

  box_success_years <- setdiff(years, setdiff(torvik_box_failed, fallback_success_years))
  shooting_success_years <- setdiff(years, setdiff(torvik_shooting_failed, fallback_success_years))
  advanced_success_years <- setdiff(years, setdiff(torvik_advanced_failed, fallback_success_years))

  list(
    data = final,
    before_dedup_rows = before_dedup_rows,
    box_success_years = box_success_years,
    box_failed_years = setdiff(years, box_success_years),
    shooting_success_years = shooting_success_years,
    shooting_failed_years = setdiff(years, shooting_success_years),
    advanced_success_years = advanced_success_years,
    advanced_failed_years = setdiff(years, advanced_success_years),
    fallback_success_years = fallback_success_years,
    fallback_failed_years = setdiff(fallback_needed, fallback_success_years)
  )
}

format_years <- function(years) {
  if (length(years) == 0) {
    "None"
  } else {
    paste(years, collapse = ", ")
  }
}

write_report <- function(result, report_path, start_year, end_year) {
  df <- result$data
  numeric_cols <- setdiff(names(df)[stringr::str_detect(names(df), "^ncaa_")], TEXT_NCAA_COLUMNS)

  missing <- df |>
    dplyr::summarise(dplyr::across(dplyr::all_of(numeric_cols), ~ round(mean(is.na(.x)) * 100, 1))) |>
    tidyr::pivot_longer(dplyr::everything(), names_to = "column", values_to = "missing_pct") |>
    dplyr::arrange(dplyr::desc(missing_pct))

  key_missing <- missing |>
    dplyr::filter(column %in% c("ncaa_three_pct", "ncaa_ft_pct", "ncaa_usage"))

  duplicate_count <- df |>
    dplyr::count(name, draft_year) |>
    dplyr::filter(n > 1) |>
    nrow()

  rows_by_year <- df |> dplyr::count(draft_year, name = "rows")

  summary <- tibble::tibble(
    metric = c(
      "start_year",
      "end_year",
      "rows_before_duplicate_resolution",
      "rows_after_duplicate_resolution",
      "columns",
      "duplicate_name_draft_year_rows_after_resolution"
    ),
    value = c(
      start_year,
      end_year,
      result$before_dedup_rows,
      nrow(df),
      ncol(df),
      duplicate_count
    )
  )

  lines <- c(
    "# NCAA Torvik Standalone Dataset Report v2",
    "",
    "## Summary",
    "",
    paste(capture.output(print(knitr::kable(summary, format = "pipe"))), collapse = "\n"),
    "",
    "## Rows By draft_year",
    "",
    paste(capture.output(print(knitr::kable(rows_by_year, format = "pipe"))), collapse = "\n"),
    "",
    "## Successful Box Stats Years",
    "",
    format_years(result$box_success_years),
    "",
    "## Failed Box Stats Years",
    "",
    format_years(result$box_failed_years),
    "",
    "## Successful Shooting Stats Years",
    "",
    format_years(result$shooting_success_years),
    "",
    "## Failed Shooting Stats Years",
    "",
    format_years(result$shooting_failed_years),
    "",
    "## Successful Advanced Stats Years",
    "",
    format_years(result$advanced_success_years),
    "",
    "## Failed Advanced Stats Years",
    "",
    format_years(result$advanced_failed_years),
    "",
    "## Public Fallback Successful Years",
    "",
    format_years(result$fallback_success_years),
    "",
    "## Public Fallback Failed Years",
    "",
    format_years(result$fallback_failed_years),
    "",
    "## Duplicate name + draft_year Rows After Resolution",
    "",
    as.character(duplicate_count),
    "",
    "## Key Missingness Checks",
    "",
    paste(capture.output(print(knitr::kable(key_missing, format = "pipe"))), collapse = "\n"),
    "",
    "## Missing-Value Percentage For Numeric NCAA Columns",
    "",
    paste(capture.output(print(knitr::kable(missing, format = "pipe"))), collapse = "\n"),
    "",
    "## Columns",
    "",
    paste0("- ", names(df), collapse = "\n"),
    "",
    "## First 30 Rows",
    "",
    paste(capture.output(print(knitr::kable(head(df, 30), format = "pipe"))), collapse = "\n"),
    ""
  )

  dir.create(dirname(report_path), showWarnings = FALSE, recursive = TRUE)
  writeLines(lines, report_path)
}

parse_args <- function() {
  args <- commandArgs(trailingOnly = TRUE)

  get_arg <- function(flag, default) {
    idx <- which(args == flag)
    if (length(idx) == 0 || idx == length(args)) {
      return(default)
    }
    args[[idx + 1]]
  }

  list(
    start_year = as.integer(get_arg("--start-year", "2008")),
    end_year = as.integer(get_arg("--end-year", "2026")),
    out = get_arg("--out", "data/pre_draft_ncaa_torvik_2008_2026_v2.csv"),
    report = get_arg("--report", "data/pre_draft_ncaa_torvik_report_v2.md")
  )
}

main <- function() {
  args <- parse_args()
  dir.create(dirname(args$out), showWarnings = FALSE, recursive = TRUE)
  dir.create(dirname(args$report), showWarnings = FALSE, recursive = TRUE)

  result <- build_ncaa_dataset(args$start_year, args$end_year)
  readr::write_csv(result$data, args$out, na = "")
  write_report(result, args$report, args$start_year, args$end_year)

  message("Saved NCAA CSV: ", args$out)
  message("Saved NCAA report: ", args$report)
  message("Rows: ", nrow(result$data))
  message("Columns: ", ncol(result$data))
  message("Box failed years: ", format_years(result$box_failed_years))
  message("Shooting failed years: ", format_years(result$shooting_failed_years))
  message("Advanced failed years: ", format_years(result$advanced_failed_years))
}

main()
