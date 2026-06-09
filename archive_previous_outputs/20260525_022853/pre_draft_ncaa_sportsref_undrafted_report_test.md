# Sports-Reference Early Undrafted NCAA Layer Report

This is an experimental standalone layer. No final NBA Draft dataset was modified.

## Summary

| metric                                          | value                           |
|:------------------------------------------------|:--------------------------------|
| target_undrafted_players                        | 25                              |
| matched_players                                 | 21                              |
| unmatched_players                               | 4                               |
| match_rate_pct                                  | 84.0                            |
| duplicate_name_draft_year_rows_after_resolution | 0                               |
| min_page_name_score                             | 92                              |
| season_rule                                     | exact pre-draft season required |

## Match Rate By draft_year

|   draft_year |   targets |   matched |   unmatched |   match_rate_pct |
|-------------:|----------:|----------:|------------:|-----------------:|
|         2000 |        25 |        21 |           4 |               84 |

## Missing-Value Percentage For Matched Numeric Columns

| column                  |   missing_pct |
|:------------------------|--------------:|
| sportsref_three_pct     |          14.3 |
| sportsref_tpg           |           4.8 |
| sportsref_games_started |           0   |
| sportsref_mpg           |           0   |
| sportsref_match_score   |           0   |
| sportsref_games         |           0   |
| sportsref_rpg           |           0   |
| sportsref_ppg           |           0   |
| sportsref_spg           |           0   |
| sportsref_apg           |           0   |
| sportsref_bpg           |           0   |
| sportsref_fg_pct        |           0   |
| sportsref_two_pct       |           0   |
| sportsref_ft_pct        |           0   |

## First 50 Matched Rows

| name             |   draft_year | sportsref_player_raw   | sportsref_url                                                        | sportsref_match_method   |   sportsref_match_score | sportsref_school   | sportsref_conf   | sportsref_season   |   sportsref_games |   sportsref_games_started |   sportsref_mpg |   sportsref_ppg |   sportsref_rpg |   sportsref_apg |   sportsref_spg |   sportsref_bpg | sportsref_tpg   |   sportsref_fg_pct |   sportsref_two_pct | sportsref_three_pct   |   sportsref_ft_pct |
|:-----------------|-------------:|:-----------------------|:---------------------------------------------------------------------|:-------------------------|------------------------:|:-------------------|:-----------------|:-------------------|------------------:|--------------------------:|----------------:|----------------:|----------------:|----------------:|----------------:|----------------:|:----------------|-------------------:|--------------------:|:----------------------|-------------------:|
| a j granger      |         2000 | a j granger            | https://www.sports-reference.com/cbb/players/aj-granger-1.html       | strict_slug_exact_season |                     100 | Michigan St.       | Big Ten          | 1999-00            |                39 |                        35 |            28.8 |             9.5 |             5.3 |             1.2 |             0.4 |             0.5 | 1.3             |              0.5   |               0.538 | 0.45                  |              0.893 |
| alex scales      |         2000 | alex scales            | https://www.sports-reference.com/cbb/players/alex-scales-1.html      | strict_slug_exact_season |                     100 | Oregon             | Pac-10           | 1999-00            |                30 |                        28 |            32   |            16.3 |             4.3 |             2.5 |             1.4 |             0.4 | 2.9             |              0.455 |               0.536 | 0.338                 |              0.78  |
| aubrey reese     |         2000 | aubrey reese           | https://www.sports-reference.com/cbb/players/aubrey-reese-1.html     | strict_slug_exact_season |                     100 | Murray St.         | OVC              | 1999-00            |                32 |                        32 |            37.6 |            20.4 |             5.3 |             4.8 |             1.9 |             0.2 | 3.8             |              0.461 |               0.52  | 0.353                 |              0.819 |
| bootsy thornton  |         2000 | bootsy thornton        | https://www.sports-reference.com/cbb/players/bootsy-thornton-1.html  | strict_slug_exact_season |                     100 | St. John's (NY)    | Big East         | 1999-00            |                33 |                        33 |            35.3 |            15.3 |             5.5 |             2.9 |             2.4 |             0.3 | 1.9             |              0.486 |               0.564 | 0.355                 |              0.573 |
| brandon kurtz    |         2000 | brandon kurtz          | https://www.sports-reference.com/cbb/players/brandon-kurtz-1.html    | strict_slug_exact_season |                     100 | Tulsa              | WAC              | 1999-00            |                37 |                        35 |            27   |            11.2 |             7   |             1.6 |             1.2 |             1.3 | 2.2             |              0.513 |               0.526 | 0.231                 |              0.669 |
| brian montonati  |         2000 | brian montonati        | https://www.sports-reference.com/cbb/players/brian-montonati-1.html  | strict_slug_exact_season |                     100 | Oklahoma St.       | Big 12           | 1999-00            |                34 |                        34 |            27.5 |            12.1 |             7.2 |             1.6 |             1.4 |             0.6 | 1.8             |              0.544 |               0.545 | 0.5                   |              0.69  |
| caswell cyrus    |         2000 | caswell cyrus          | https://www.sports-reference.com/cbb/players/caswell-cyrus-1.html    | strict_slug_exact_season |                     100 | St. Bonaventure    | A-10             | 1999-00            |                30 |                        28 |            32.9 |            12   |             6.6 |             0.6 |             0.5 |             1.7 | 2.1             |              0.498 |               0.498 | <NA>                  |              0.617 |
| ceedric goodwyn  |         2000 | ceedric goodwyn        | https://www.sports-reference.com/cbb/players/ceedric-goodwyn-1.html  | strict_slug_exact_season |                     100 | Colorado St.       | MWC              | 1999-00            |                30 |                        29 |            27.5 |            17.8 |             4.5 |             2.5 |             0.8 |             1.2 | 3.4             |              0.513 |               0.541 | 0.42                  |              0.699 |
| ed cota          |         2000 | ed cota                | https://www.sports-reference.com/cbb/players/ed-cota-1.html          | strict_slug_exact_season |                     100 | UNC                | ACC              | 1999-00            |                35 |                        34 |            36.7 |            10.1 |             4.4 |             8.1 |             1.1 |             0.1 | 3.3             |              0.443 |               0.476 | 0.367                 |              0.728 |
| eddie gill       |         2000 | eddie gill             | https://www.sports-reference.com/cbb/players/eddie-gill-1.html       | strict_slug_exact_season |                     100 | Weber St.          | Big Sky          | 1999-00            |                28 |                        28 |            36   |            16.3 |             6.4 |             6.9 |             3.2 |             0.3 | 3.9             |              0.394 |               0.415 | 0.366                 |              0.861 |
| eric coley       |         2000 | eric coley             | https://www.sports-reference.com/cbb/players/eric-coley-1.html       | strict_slug_exact_season |                     100 | Tulsa              | WAC              | 1999-00            |                37 |                        37 |            29.5 |            11.3 |             6.8 |             3.4 |             3.3 |             1.2 | 1.6             |              0.524 |               0.584 | 0.204                 |              0.568 |
| gabe muoneke     |         2000 | gabe muoneke           | https://www.sports-reference.com/cbb/players/gabe-muoneke-1.html     | strict_slug_exact_season |                     100 | Texas              | Big 12           | 1999-00            |                33 |                        25 |            28.7 |            13.7 |             6.3 |             1.9 |             0.9 |             0.6 | 2.9             |              0.527 |               0.57  | 0.211                 |              0.6   |
| harold arceneaux |         2000 | harold arceneaux       | https://www.sports-reference.com/cbb/players/harold-arceneaux-1.html | strict_slug_exact_season |                     100 | Weber St.          | Big Sky          | 1999-00            |                28 |                        27 |            32.8 |            23   |             7.4 |             1.7 |             1.4 |             0.9 | 2.6             |              0.512 |               0.559 | 0.369                 |              0.796 |
| jacob jaacks     |         2000 | jacob jaacks           | https://www.sports-reference.com/cbb/players/jacob-jaacks-1.html     | strict_slug_exact_season |                     100 | Iowa               | Big Ten          | 1999-00            |                30 |                        28 |            27.4 |            12.2 |             7.3 |             1   |             0.3 |             0.4 | 2.5             |              0.468 |               0.493 | 0.375                 |              0.602 |
| jameel watkins   |         2000 | jameel watkins         | https://www.sports-reference.com/cbb/players/jameel-watkins-1.html   | strict_slug_exact_season |                     100 | Georgetown         | Big East         | 1999-00            |                34 |                        23 |            12.3 |             4.1 |             3.3 |             0.2 |             0.4 |             1.1 | 1.3             |              0.417 |               0.417 | <NA>                  |              0.492 |
| jarrett stephens |         2000 | jarrett stephens       | https://www.sports-reference.com/cbb/players/jarrett-stephens-1.html | strict_slug_exact_season |                     100 | Penn St.           | Big Ten          | 1999-00            |                35 |                        35 |            34.9 |            18.8 |            10.5 |             1.4 |             1.8 |             0.6 | 2.4             |              0.566 |               0.577 | 0.294                 |              0.698 |
| johnny hemsley   |         2000 | johnny hemsley         | https://www.sports-reference.com/cbb/players/johnny-hemsley-1.html   | strict_slug_exact_season |                     100 | Miami (FL)         | Big East         | 1999-00            |                30 |                        29 |            35.8 |            18.1 |             3.6 |             1.7 |             1.3 |             0.3 | 2.3             |              0.398 |               0.451 | 0.32                  |              0.849 |
| justin love      |         2000 | justin love            | https://www.sports-reference.com/cbb/players/justin-love-1.html      | strict_slug_exact_season |                     100 | Saint Louis        | CUSA             | 1999-00            |                33 |                        32 |            31.2 |            18.2 |             4.9 |             2.5 |             1.5 |             0.2 | 2.9             |              0.438 |               0.446 | 0.425                 |              0.821 |
| karim shabazz    |         2000 | karim shabazz          | https://www.sports-reference.com/cbb/players/karim-shabazz-1.html    | strict_slug_exact_season |                     100 | Providence         | Big East         | 1999-00            |                21 |                        21 |            30.4 |            10.4 |             8.2 |             1.5 |             0.8 |             2.6 | <NA>            |              0.435 |               0.435 | <NA>                  |              0.56  |
| kenyon jones     |         2000 | kenyon jones           | https://www.sports-reference.com/cbb/players/kenyon-jones-1.html     | strict_slug_exact_season |                     100 | San Francisco      | WCC              | 1999-00            |                28 |                        28 |            26.1 |            16.5 |             9   |             0.9 |             0.9 |             1.4 | 2.5             |              0.583 |               0.583 | 0.571                 |              0.701 |
| lamont barnes    |         2000 | lamont barnes          | https://www.sports-reference.com/cbb/players/lamont-barnes-1.html    | strict_slug_exact_season |                     100 | Temple             | A-10             | 1999-00            |                33 |                        33 |            29.8 |             9   |             5   |             0.8 |             0.8 |             1.2 | 1.2             |              0.484 |               0.493 | 0.0                   |              0.64  |

## First 80 Unmatched Rows

| name                |   draft_year |   overall_pick | position   | reason                     |   attempted_urls_count |
|:--------------------|-------------:|---------------:|:-----------|:---------------------------|-----------------------:|
| antonis fotsis      |         2000 |            999 | SF         | not_found_or_not_confident |                     14 |
| damon reed          |         2000 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| jimmie hunter       |         2000 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| julius doc robinson |         2000 |            999 | PG         | not_found_or_not_confident |                     28 |

## Output Columns

- name
- draft_year
- sportsref_player_raw
- sportsref_url
- sportsref_match_method
- sportsref_match_score
- sportsref_school
- sportsref_conf
- sportsref_season
- sportsref_games
- sportsref_games_started
- sportsref_mpg
- sportsref_ppg
- sportsref_rpg
- sportsref_apg
- sportsref_spg
- sportsref_bpg
- sportsref_tpg
- sportsref_fg_pct
- sportsref_two_pct
- sportsref_three_pct
- sportsref_ft_pct
