# Sports-Reference Early Undrafted NCAA Layer Report

This is an experimental standalone layer. No final NBA Draft dataset was modified.

## Summary

| metric                                          | value                           |
|:------------------------------------------------|:--------------------------------|
| target_undrafted_players                        | 349                             |
| matched_players                                 | 277                             |
| unmatched_players                               | 72                              |
| match_rate_pct                                  | 79.4                            |
| duplicate_name_draft_year_rows_after_resolution | 0                               |
| min_page_name_score                             | 92                              |
| season_rule                                     | exact pre-draft season required |

## Match Rate By draft_year

|   draft_year |   targets |   matched |   unmatched |   match_rate_pct |
|-------------:|----------:|----------:|------------:|-----------------:|
|         2000 |        41 |        33 |           8 |             80.5 |
|         2001 |        39 |        30 |           9 |             76.9 |
|         2002 |        45 |        36 |           9 |             80   |
|         2003 |        48 |        38 |          10 |             79.2 |
|         2004 |        44 |        28 |          16 |             63.6 |
|         2005 |        47 |        38 |           9 |             80.9 |
|         2006 |        47 |        41 |           6 |             87.2 |
|         2007 |        38 |        33 |           5 |             86.8 |

## Missing-Value Percentage For Matched Numeric Columns

| column                  |   missing_pct |
|:------------------------|--------------:|
| sportsref_three_pct     |          14.4 |
| sportsref_mpg           |           0.4 |
| sportsref_tpg           |           0.4 |
| sportsref_ft_pct        |           0.4 |
| sportsref_games         |           0   |
| sportsref_match_score   |           0   |
| sportsref_rpg           |           0   |
| sportsref_ppg           |           0   |
| sportsref_games_started |           0   |
| sportsref_apg           |           0   |
| sportsref_bpg           |           0   |
| sportsref_spg           |           0   |
| sportsref_two_pct       |           0   |
| sportsref_fg_pct        |           0   |

## First 50 Matched Rows

| name              |   draft_year | sportsref_player_raw   | sportsref_url                                                         | sportsref_match_method   |   sportsref_match_score | sportsref_school   | sportsref_conf   | sportsref_season   |   sportsref_games |   sportsref_games_started |   sportsref_mpg |   sportsref_ppg |   sportsref_rpg |   sportsref_apg |   sportsref_spg |   sportsref_bpg | sportsref_tpg   |   sportsref_fg_pct |   sportsref_two_pct | sportsref_three_pct   |   sportsref_ft_pct |
|:------------------|-------------:|:-----------------------|:----------------------------------------------------------------------|:-------------------------|------------------------:|:-------------------|:-----------------|:-------------------|------------------:|--------------------------:|----------------:|----------------:|----------------:|----------------:|----------------:|----------------:|:----------------|-------------------:|--------------------:|:----------------------|-------------------:|
| a j granger       |         2000 | a j granger            | https://www.sports-reference.com/cbb/players/aj-granger-1.html        | strict_slug_exact_season |                     100 | Michigan St.       | Big Ten          | 1999-00            |                39 |                        35 |            28.8 |             9.5 |             5.3 |             1.2 |             0.4 |             0.5 | 1.3             |              0.5   |               0.538 | 0.45                  |              0.893 |
| alex scales       |         2000 | alex scales            | https://www.sports-reference.com/cbb/players/alex-scales-1.html       | strict_slug_exact_season |                     100 | Oregon             | Pac-10           | 1999-00            |                30 |                        28 |            32   |            16.3 |             4.3 |             2.5 |             1.4 |             0.4 | 2.9             |              0.455 |               0.536 | 0.338                 |              0.78  |
| aubrey reese      |         2000 | aubrey reese           | https://www.sports-reference.com/cbb/players/aubrey-reese-1.html      | strict_slug_exact_season |                     100 | Murray St.         | OVC              | 1999-00            |                32 |                        32 |            37.6 |            20.4 |             5.3 |             4.8 |             1.9 |             0.2 | 3.8             |              0.461 |               0.52  | 0.353                 |              0.819 |
| bootsy thornton   |         2000 | bootsy thornton        | https://www.sports-reference.com/cbb/players/bootsy-thornton-1.html   | strict_slug_exact_season |                     100 | St. John's (NY)    | Big East         | 1999-00            |                33 |                        33 |            35.3 |            15.3 |             5.5 |             2.9 |             2.4 |             0.3 | 1.9             |              0.486 |               0.564 | 0.355                 |              0.573 |
| brandon kurtz     |         2000 | brandon kurtz          | https://www.sports-reference.com/cbb/players/brandon-kurtz-1.html     | strict_slug_exact_season |                     100 | Tulsa              | WAC              | 1999-00            |                37 |                        35 |            27   |            11.2 |             7   |             1.6 |             1.2 |             1.3 | 2.2             |              0.513 |               0.526 | 0.231                 |              0.669 |
| brian montonati   |         2000 | brian montonati        | https://www.sports-reference.com/cbb/players/brian-montonati-1.html   | strict_slug_exact_season |                     100 | Oklahoma St.       | Big 12           | 1999-00            |                34 |                        34 |            27.5 |            12.1 |             7.2 |             1.6 |             1.4 |             0.6 | 1.8             |              0.544 |               0.545 | 0.5                   |              0.69  |
| caswell cyrus     |         2000 | caswell cyrus          | https://www.sports-reference.com/cbb/players/caswell-cyrus-1.html     | strict_slug_exact_season |                     100 | St. Bonaventure    | A-10             | 1999-00            |                30 |                        28 |            32.9 |            12   |             6.6 |             0.6 |             0.5 |             1.7 | 2.1             |              0.498 |               0.498 | <NA>                  |              0.617 |
| ceedric goodwyn   |         2000 | ceedric goodwyn        | https://www.sports-reference.com/cbb/players/ceedric-goodwyn-1.html   | strict_slug_exact_season |                     100 | Colorado St.       | MWC              | 1999-00            |                30 |                        29 |            27.5 |            17.8 |             4.5 |             2.5 |             0.8 |             1.2 | 3.4             |              0.513 |               0.541 | 0.42                  |              0.699 |
| ed cota           |         2000 | ed cota                | https://www.sports-reference.com/cbb/players/ed-cota-1.html           | strict_slug_exact_season |                     100 | UNC                | ACC              | 1999-00            |                35 |                        34 |            36.7 |            10.1 |             4.4 |             8.1 |             1.1 |             0.1 | 3.3             |              0.443 |               0.476 | 0.367                 |              0.728 |
| eddie gill        |         2000 | eddie gill             | https://www.sports-reference.com/cbb/players/eddie-gill-1.html        | strict_slug_exact_season |                     100 | Weber St.          | Big Sky          | 1999-00            |                28 |                        28 |            36   |            16.3 |             6.4 |             6.9 |             3.2 |             0.3 | 3.9             |              0.394 |               0.415 | 0.366                 |              0.861 |
| eric coley        |         2000 | eric coley             | https://www.sports-reference.com/cbb/players/eric-coley-1.html        | strict_slug_exact_season |                     100 | Tulsa              | WAC              | 1999-00            |                37 |                        37 |            29.5 |            11.3 |             6.8 |             3.4 |             3.3 |             1.2 | 1.6             |              0.524 |               0.584 | 0.204                 |              0.568 |
| gabe muoneke      |         2000 | gabe muoneke           | https://www.sports-reference.com/cbb/players/gabe-muoneke-1.html      | strict_slug_exact_season |                     100 | Texas              | Big 12           | 1999-00            |                33 |                        25 |            28.7 |            13.7 |             6.3 |             1.9 |             0.9 |             0.6 | 2.9             |              0.527 |               0.57  | 0.211                 |              0.6   |
| harold arceneaux  |         2000 | harold arceneaux       | https://www.sports-reference.com/cbb/players/harold-arceneaux-1.html  | strict_slug_exact_season |                     100 | Weber St.          | Big Sky          | 1999-00            |                28 |                        27 |            32.8 |            23   |             7.4 |             1.7 |             1.4 |             0.9 | 2.6             |              0.512 |               0.559 | 0.369                 |              0.796 |
| jacob jaacks      |         2000 | jacob jaacks           | https://www.sports-reference.com/cbb/players/jacob-jaacks-1.html      | strict_slug_exact_season |                     100 | Iowa               | Big Ten          | 1999-00            |                30 |                        28 |            27.4 |            12.2 |             7.3 |             1   |             0.3 |             0.4 | 2.5             |              0.468 |               0.493 | 0.375                 |              0.602 |
| jameel watkins    |         2000 | jameel watkins         | https://www.sports-reference.com/cbb/players/jameel-watkins-1.html    | strict_slug_exact_season |                     100 | Georgetown         | Big East         | 1999-00            |                34 |                        23 |            12.3 |             4.1 |             3.3 |             0.2 |             0.4 |             1.1 | 1.3             |              0.417 |               0.417 | <NA>                  |              0.492 |
| jarrett stephens  |         2000 | jarrett stephens       | https://www.sports-reference.com/cbb/players/jarrett-stephens-1.html  | strict_slug_exact_season |                     100 | Penn St.           | Big Ten          | 1999-00            |                35 |                        35 |            34.9 |            18.8 |            10.5 |             1.4 |             1.8 |             0.6 | 2.4             |              0.566 |               0.577 | 0.294                 |              0.698 |
| johnny hemsley    |         2000 | johnny hemsley         | https://www.sports-reference.com/cbb/players/johnny-hemsley-1.html    | strict_slug_exact_season |                     100 | Miami (FL)         | Big East         | 1999-00            |                30 |                        29 |            35.8 |            18.1 |             3.6 |             1.7 |             1.3 |             0.3 | 2.3             |              0.398 |               0.451 | 0.32                  |              0.849 |
| justin love       |         2000 | justin love            | https://www.sports-reference.com/cbb/players/justin-love-1.html       | strict_slug_exact_season |                     100 | Saint Louis        | CUSA             | 1999-00            |                33 |                        32 |            31.2 |            18.2 |             4.9 |             2.5 |             1.5 |             0.2 | 2.9             |              0.438 |               0.446 | 0.425                 |              0.821 |
| karim shabazz     |         2000 | karim shabazz          | https://www.sports-reference.com/cbb/players/karim-shabazz-1.html     | strict_slug_exact_season |                     100 | Providence         | Big East         | 1999-00            |                21 |                        21 |            30.4 |            10.4 |             8.2 |             1.5 |             0.8 |             2.6 | <NA>            |              0.435 |               0.435 | <NA>                  |              0.56  |
| kenyon jones      |         2000 | kenyon jones           | https://www.sports-reference.com/cbb/players/kenyon-jones-1.html      | strict_slug_exact_season |                     100 | San Francisco      | WCC              | 1999-00            |                28 |                        28 |            26.1 |            16.5 |             9   |             0.9 |             0.9 |             1.4 | 2.5             |              0.583 |               0.583 | 0.571                 |              0.701 |
| lamont barnes     |         2000 | lamont barnes          | https://www.sports-reference.com/cbb/players/lamont-barnes-1.html     | strict_slug_exact_season |                     100 | Temple             | A-10             | 1999-00            |                33 |                        33 |            29.8 |             9   |             5   |             0.8 |             0.8 |             1.2 | 1.2             |              0.484 |               0.493 | 0.0                   |              0.64  |
| malik allen       |         2000 | malik allen            | https://www.sports-reference.com/cbb/players/malik-allen-1.html       | strict_slug_exact_season |                     100 | Villanova          | Big East         | 1999-00            |                33 |                        33 |            33.4 |            14.2 |             7.4 |             1   |             0.7 |             1.9 | 2.2             |              0.511 |               0.511 | <NA>                  |              0.692 |
| marcus goree      |         2000 | marcus goree           | https://www.sports-reference.com/cbb/players/marcus-goree-1.html      | strict_slug_exact_season |                     100 | West Virginia      | Big East         | 1999-00            |                28 |                        27 |            34.8 |            14.5 |             8.3 |             1.9 |             1.6 |             2.5 | 2.5             |              0.532 |               0.566 | 0.382                 |              0.71  |
| mario bland       |         2000 | mario bland            | https://www.sports-reference.com/cbb/players/mario-bland-1.html       | strict_slug_exact_season |                     100 | Miami (FL)         | Big East         | 1999-00            |                34 |                        34 |            27.9 |            12.6 |             7   |             1.2 |             0.8 |             0.3 | 1.9             |              0.473 |               0.497 | 0.167                 |              0.73  |
| matt santangelo   |         2000 | matt santangelo        | https://www.sports-reference.com/cbb/players/matt-santangelo-1.html   | strict_slug_exact_season |                     100 | Gonzaga            | WCC              | 1999-00            |                35 |                        35 |            35.7 |            13.2 |             3.9 |             6.4 |             0.8 |             0.2 | 2.6             |              0.373 |               0.406 | 0.335                 |              0.654 |
| nate johnson      |         2000 | nate johnson           | https://www.sports-reference.com/cbb/players/nate-johnson-3.html      | strict_slug_exact_season |                     100 | Louisville         | CUSA             | 1999-00            |                31 |                        31 |            30.8 |            13.9 |             5.4 |             3.1 |             1.9 |             0.7 | 2.6             |              0.477 |               0.481 | 0.451                 |              0.692 |
| nick sheppard     |         2000 | nick sheppard          | https://www.sports-reference.com/cbb/players/nick-sheppard-1.html     | strict_slug_exact_season |                     100 | Pepperdine         | WCC              | 1999-00            |                34 |                        34 |            22.4 |             9.1 |             6.7 |             0.7 |             0.8 |             0.4 | 1.9             |              0.579 |               0.579 | <NA>                  |              0.596 |
| pepe sanchez      |         2000 | pepe sanchez           | https://www.sports-reference.com/cbb/players/pepe-sanchez-1.html      | strict_slug_exact_season |                     100 | Temple             | A-10             | 1999-00            |                25 |                        25 |            33.6 |             5.6 |             5.5 |             8   |             3.4 |             0.1 | 2.1             |              0.324 |               0.306 | 0.338                 |              0.786 |
| reed rawlings     |         2000 | reed rawlings          | https://www.sports-reference.com/cbb/players/reed-rawlings-1.html     | strict_slug_exact_season |                     100 | Samford            | TAAC             | 1999-00            |                32 |                        32 |            31.3 |            14.6 |             4.6 |             1.6 |             1.9 |             0.4 | 1.9             |              0.492 |               0.621 | 0.385                 |              0.77  |
| ron hale          |         2000 | ron hale               | https://www.sports-reference.com/cbb/players/ron-hale-1.html          | strict_slug_exact_season |                     100 | Florida St.        | ACC              | 1999-00            |                28 |                        25 |            30.9 |            15.6 |             4.8 |             1.2 |             0.8 |             0.9 | 2.4             |              0.399 |               0.423 | 0.355                 |              0.755 |
| schea cotton      |         2000 | schea cotton           | https://www.sports-reference.com/cbb/players/schea-cotton-1.html      | strict_slug_exact_season |                     100 | Alabama            | SEC              | 1999-00            |                27 |                        20 |            27.7 |            15.5 |             4.5 |             1.6 |             0.9 |             0.2 | 3.4             |              0.429 |               0.466 | 0.255                 |              0.717 |
| shaheen holloway  |         2000 | shaheen holloway       | https://www.sports-reference.com/cbb/players/shaheen-holloway-1.html  | strict_slug_exact_season |                     100 | Seton Hall         | Big East         | 1999-00            |                31 |                        31 |            31.5 |            13.2 |             5.1 |             5.6 |             1.7 |             0   | 3.2             |              0.447 |               0.474 | 0.403                 |              0.78  |
| terrance roberson |         2000 | terrance roberson      | https://www.sports-reference.com/cbb/players/terrance-roberson-1.html | strict_slug_exact_season |                     100 | Fresno St.         | WAC              | 1999-00            |                33 |                        33 |            34.3 |            16.3 |             4.9 |             4.1 |             1.2 |             0.4 | 3.1             |              0.425 |               0.503 | 0.365                 |              0.846 |
| adam allenspach   |         2001 | adam allenspach        | https://www.sports-reference.com/cbb/players/adam-allenspach-1.html   | strict_slug_exact_season |                     100 | Clemson            | ACC              | 2000-01            |                22 |                        15 |            19.2 |             7.7 |             5.5 |             0.5 |             0.3 |             0.5 | 1.3             |              0.453 |               0.453 | <NA>                  |              0.676 |
| anthony evans     |         2001 | anthony evans          | https://www.sports-reference.com/cbb/players/anthony-evans-1.html     | strict_slug_exact_season |                     100 | Georgia            | SEC              | 2000-01            |                31 |                        31 |            28.2 |            11.5 |             7.5 |             1.1 |             0.5 |             1   | 1.2             |              0.536 |               0.541 | 0.0                   |              0.752 |
| brent wright      |         2001 | brent wright           | https://www.sports-reference.com/cbb/players/brent-wright-1.html      | strict_slug_exact_season |                     100 | Florida            | SEC              | 2000-01            |                20 |                        14 |            24.4 |            12.7 |             6.2 |             1.7 |             1.3 |             0.5 | 2.0             |              0.579 |               0.579 | 0.577                 |              0.809 |
| calvin bowman     |         2001 | calvin bowman          | https://www.sports-reference.com/cbb/players/calvin-bowman-1.html     | strict_slug_exact_season |                     100 | West Virginia      | Big East         | 2000-01            |                29 |                        28 |            32.7 |            17.6 |             9.7 |             1.1 |             1.2 |             1.1 | 2.9             |              0.541 |               0.544 | 0.0                   |              0.691 |
| charles hathaway  |         2001 | charles hathaway       | https://www.sports-reference.com/cbb/players/charles-hathaway-1.html  | strict_slug_exact_season |                     100 | Tennessee          | SEC              | 2000-01            |                31 |                        27 |            19.8 |             5.1 |             4.8 |             0.5 |             0.4 |             1.4 | 1.4             |              0.649 |               0.649 | <NA>                  |              0.603 |
| charlie bell      |         2001 | charlie bell           | https://www.sports-reference.com/cbb/players/charlie-bell-1.html      | strict_slug_exact_season |                     100 | Michigan St.       | Big Ten          | 2000-01            |                33 |                        33 |            31.3 |            13.5 |             4.7 |             5.1 |             1   |             0.2 | 2.8             |              0.402 |               0.443 | 0.342                 |              0.77  |
| cookie belcher    |         2001 | cookie belcher         | https://www.sports-reference.com/cbb/players/cookie-belcher-1.html    | strict_slug_exact_season |                     100 | Nebraska           | Big 12           | 2000-01            |                30 |                        30 |            34.1 |            16.4 |             5.1 |             4.4 |             2.7 |             0.7 | 3.2             |              0.449 |               0.514 | 0.336                 |              0.744 |
| darrell johns     |         2001 | darrell johns          | https://www.sports-reference.com/cbb/players/darrell-johns-1.html     | strict_slug_exact_season |                     100 | Chicago St.        | Mid-Cont         | 2000-01            |                25 |                        15 |            23.6 |            11.6 |             5.8 |             0.7 |             0.5 |             1.2 | 2.0             |              0.506 |               0.506 | <NA>                  |              0.595 |
| darren kelly      |         2001 | darren kelly           | https://www.sports-reference.com/cbb/players/darren-kelly-1.html      | strict_slug_exact_season |                     100 | Texas              | Big 12           | 2000-01            |                26 |                        26 |            34.6 |            15.3 |             4.6 |             2.9 |             1.2 |             0.5 | 3.2             |              0.36  |               0.405 | 0.276                 |              0.76  |
| demarcus minor    |         2001 | demarcus minor         | https://www.sports-reference.com/cbb/players/demarcus-minor-1.html    | strict_slug_exact_season |                     100 | Baylor             | Big 12           | 2000-01            |                31 |                        31 |            37.5 |            15.2 |             5.9 |             4.5 |             1.4 |             0.1 | 3.5             |              0.4   |               0.415 | 0.328                 |              0.842 |
| demetrius porter  |         2001 | demetrius porter       | https://www.sports-reference.com/cbb/players/demetrius-porter-1.html  | strict_slug_exact_season |                     100 | Fresno St.         | WAC              | 2000-01            |                33 |                        33 |            31.2 |            15.2 |             2.3 |             2.9 |             1.7 |             0.2 | 1.7             |              0.441 |               0.524 | 0.387                 |              0.771 |
| greg stevenson    |         2001 | greg stevenson         | https://www.sports-reference.com/cbb/players/greg-stevenson-1.html    | strict_slug_exact_season |                     100 | Richmond           | CAA              | 2000-01            |                29 |                        27 |            35.2 |            19.7 |             7.7 |             1.7 |             1.4 |             0.9 | 1.9             |              0.536 |               0.553 | 0.485                 |              0.767 |
| gyasi cline heard |         2001 | gyasi cline heard      | https://www.sports-reference.com/cbb/players/gyasi-cline-heard-1.html | strict_slug_exact_season |                     100 | Penn St.           | Big Ten          | 2000-01            |                33 |                        33 |            33.4 |            16   |             8.2 |             1.8 |             1.3 |             1.5 | 1.7             |              0.501 |               0.503 | 0.333                 |              0.735 |
| jason gardner     |         2001 | jason gardner          | https://www.sports-reference.com/cbb/players/jason-gardner-1.html     | strict_slug_exact_season |                     100 | Arizona            | Pac-10           | 2000-01            |                36 |                        36 |            32.4 |            10.9 |             3   |             4.1 |             1.6 |             0.1 | 1.8             |              0.381 |               0.413 | 0.367                 |              0.809 |
| jerry green       |         2001 | jerry green            | https://www.sports-reference.com/cbb/players/jerry-green-1.html       | strict_slug_exact_season |                     100 | UC Irvine          | Big West         | 2000-01            |                30 |                        30 |            32.1 |            19   |             4.8 |             3   |             1.4 |             0.3 | 3.0             |              0.453 |               0.459 | 0.426                 |              0.834 |
| kenny gregory     |         2001 | kenny gregory          | https://www.sports-reference.com/cbb/players/kenny-gregory-1.html     | strict_slug_exact_season |                     100 | Kansas             | Big 12           | 2000-01            |                30 |                        30 |            31.7 |            15.6 |             7.3 |             2.4 |             1   |             0.2 | 1.7             |              0.567 |               0.601 | 0.386                 |              0.424 |
| kimani ffriend    |         2001 | kimani ffriend         | https://www.sports-reference.com/cbb/players/kimani-ffriend-1.html    | strict_slug_exact_season |                     100 | Nebraska           | Big 12           | 2000-01            |                28 |                        25 |            29.5 |            13.8 |             8.2 |             0.9 |             0.6 |             2.6 | 3.0             |              0.623 |               0.623 | <NA>                  |              0.455 |

## First 80 Unmatched Rows

| name                 |   draft_year |   overall_pick | position   | reason                     |   attempted_urls_count |
|:---------------------|-------------:|---------------:|:-----------|:---------------------------|-----------------------:|
| antonis fotsis       |         2000 |            999 | SF         | not_found_or_not_confident |                     14 |
| damon reed           |         2000 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| jimmie hunter        |         2000 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| julius doc robinson  |         2000 |            999 | PG         | not_found_or_not_confident |                     28 |
| matthew nielsen      |         2000 |            999 | PF         | not_found_or_not_confident |                     14 |
| michael hermon       |         2000 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| ndongo n diaye       |         2000 |            999 | C          | not_found_or_not_confident |                     28 |
| vassil evtimov       |         2000 |            999 | PF         | not_found_or_not_confident |                     14 |
| benjamin eze         |         2001 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| damone thornton      |         2001 |            999 | PF         | not_found_or_not_confident |                     14 |
| horace jenkins       |         2001 |            999 | PG         | not_found_or_not_confident |                     14 |
| jamario moon         |         2001 |            999 | SF         | not_found_or_not_confident |                     14 |
| lazaros papadopoulos |         2001 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| michael hicks        |         2001 |            999 | SG         | not_found_or_not_confident |                     14 |
| norman richardson    |         2001 |            999 | SG         | not_found_or_not_confident |                     14 |
| robb dryden          |         2001 |            999 | C          | not_found_or_not_confident |                     14 |
| tate decker          |         2001 |            999 | SF         | not_found_or_not_confident |                     14 |
| israel sheinfeld     |         2002 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| julian sensley       |         2002 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| kei madison          |         2002 |            999 | SF         | not_found_or_not_confident |                     14 |
| lee benson           |         2002 |            999 | SF-PF      | not_found_or_not_confident |                     14 |
| lenny cooke          |         2002 |            999 | SG-SF      | not_found_or_not_confident |                     14 |
| muhammed lasege      |         2002 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| sylvere bryan        |         2002 |            999 | PF         | not_found_or_not_confident |                     14 |
| teddy dupay          |         2002 |            999 | PG         | not_found_or_not_confident |                     14 |
| uche okafor          |         2002 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| aleksander djuric    |         2003 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| donald little        |         2003 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| marlon parmer        |         2003 |            999 | PG         | not_found_or_not_confident |                     14 |
| michael ignerski     |         2003 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| pavel podkolzin      |         2003 |            999 | C          | not_found_or_not_confident |                     14 |
| sani ibrahim         |         2003 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| sasha vujacic        |         2003 |            999 | PG-SG      | not_found_or_not_confident |                     14 |
| souleymane camara    |         2003 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| ugonna okyekwe       |         2003 |            999 | SF         | not_found_or_not_confident |                     14 |
| wayne wallace        |         2003 |            999 | PF         | not_found_or_not_confident |                     14 |
| aleksandar capin     |         2004 |            999 | PG         | not_found_or_not_confident |                     14 |
| ales chan            |         2004 |            999 | C          | not_found_or_not_confident |                     14 |
| blagota sekulic      |         2004 |            999 | SF-PF      | not_found_or_not_confident |                     14 |
| chris garnett        |         2004 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| drago pasalic        |         2004 |            999 | PF         | not_found_or_not_confident |                     14 |
| ivan koljevic        |         2004 |            999 | PG         | not_found_or_not_confident |                     14 |
| jackie butler        |         2004 |            999 | C          | not_found_or_not_confident |                     14 |
| kelvin pena          |         2004 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| marko tomas          |         2004 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| misan nikagbatse     |         2004 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| omar quintero        |         2004 |            999 | PG         | not_found_or_not_confident |                     14 |
| randall orr          |         2004 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| rich melzer          |         2004 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| tiago splitter       |         2004 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| tim bowers           |         2004 |            999 | PG-SG      | not_found_or_not_confident |                     14 |
| tom timmerrmans      |         2004 |            999 | PF-C       | not_found_or_not_confident |                     14 |
| brandon rush         |         2005 |            999 | SG-SF      | not_found_or_not_confident |                     14 |
| charles hayes        |         2005 |            999 | SF-PF      | not_found_or_not_confident |                     14 |
| d or fischer         |         2005 |            999 | C-PF       | not_found_or_not_confident |                     28 |
| daryl dorsey         |         2005 |            999 | PG         | not_found_or_not_confident |                     14 |
| deji akindele        |         2005 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| drago pasalic        |         2005 |            999 | SF-PF      | not_found_or_not_confident |                     14 |
| larry o bannon       |         2005 |            999 | SG         | not_found_or_not_confident |                     28 |
| nemanja aleksandrov  |         2005 |            999 | PF-SF      | not_found_or_not_confident |                     14 |
| rudy fernandez       |         2005 |            999 | SG         | not_found_or_not_confident |                     14 |
| danilo pinnock       |         2006 |            999 | PG-SG      | not_found_or_not_confident |                     14 |
| frans steyn          |         2006 |            999 | C          | not_found_or_not_confident |                     14 |
| lou amundson         |         2006 |            999 | PF         | not_found_or_not_confident |                     14 |
| michael southhall    |         2006 |            999 | C          | not_found_or_not_confident |                     14 |
| tedric hill          |         2006 |            999 | SF-PF      | not_found_or_not_confident |                     14 |
| viktor keyru         |         2006 |            999 | SG-PG      | not_found_or_not_confident |                     14 |
| ali traore           |         2007 |            999 | C-PF       | not_found_or_not_confident |                     14 |
| avis wyatt           |         2007 |            999 | PF         | not_found_or_not_confident |                     14 |
| major wingate        |         2007 |            999 | C          | not_found_or_not_confident |                     14 |
| marko lekic          |         2007 |            999 | C          | not_found_or_not_confident |                     14 |
| reynolds             |         2007 |            999 | PG         | not_found_or_not_confident |                     14 |

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
