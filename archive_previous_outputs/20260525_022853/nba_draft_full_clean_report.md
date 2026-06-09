# NBA Draft Full Clean Dataset Report

## Summary

| metric                                      |   value |
|:--------------------------------------------|--------:|
| base_rows                                   |  2347   |
| final_rows                                  |  2347   |
| final_columns                               |    53   |
| row_count_equals_base                       |     1   |
| duplicate_name_draft_year_overall_pick_rows |     0   |
| ncaa_matched_rows                           |  1566   |
| ncaa_match_rate_pct                         |    66.7 |
| exact_name_matches                          |  1545   |
| compact_initials_matches                    |    12   |
| spaced_initials_matches                     |     0   |
| manual_alias_matches                        |     9   |

## NCAA Match Rate By organization_type

| organization_type   |   rows |   matched |   unmatched |   match_rate_pct |
|:--------------------|-------:|----------:|------------:|-----------------:|
| College/University  |   1193 |      1167 |          26 |             97.8 |
| High School         |     35 |         0 |          35 |              0   |
| Other Team/Club     |    312 |         0 |         312 |              0   |
| nan                 |    807 |       399 |         408 |             49.4 |

## NCAA Match Rate By draft_year

|   draft_year |   rows |   matched |   unmatched |   match_rate_pct |
|-------------:|-------:|----------:|------------:|-----------------:|
|         2000 |     99 |        44 |          55 |             44.4 |
|         2001 |     96 |        44 |          52 |             45.8 |
|         2002 |    102 |        40 |          62 |             39.2 |
|         2003 |    106 |        32 |          74 |             30.2 |
|         2004 |    103 |        34 |          69 |             33   |
|         2005 |    107 |        37 |          70 |             34.6 |
|         2006 |    107 |        44 |          63 |             41.1 |
|         2007 |     98 |        47 |          51 |             48   |
|         2008 |    102 |        85 |          17 |             83.3 |
|         2009 |     66 |        52 |          14 |             78.8 |
|         2010 |     68 |        60 |           8 |             88.2 |
|         2011 |     71 |        53 |          18 |             74.6 |
|         2012 |     71 |        62 |           9 |             87.3 |
|         2013 |     78 |        61 |          17 |             78.2 |
|         2014 |     73 |        57 |          16 |             78.1 |
|         2015 |     80 |        65 |          15 |             81.2 |
|         2016 |     78 |        60 |          18 |             76.9 |
|         2017 |     82 |        69 |          13 |             84.1 |
|         2018 |     85 |        72 |          13 |             84.7 |
|         2019 |     88 |        73 |          15 |             83   |
|         2020 |     78 |        63 |          15 |             80.8 |
|         2021 |     87 |        71 |          16 |             81.6 |
|         2022 |     91 |        70 |          21 |             76.9 |
|         2023 |     83 |        69 |          14 |             83.1 |
|         2024 |     84 |        66 |          18 |             78.6 |
|         2025 |     86 |        68 |          18 |             79.1 |
|         2026 |     78 |        68 |          10 |             87.2 |

## NCAA Match Counts By ncaa_match_method

| ncaa_match_method   |   rows |
|:--------------------|-------:|
| compact_initials    |     12 |
| exact_name          |   1545 |
| manual_alias        |      9 |
| unmatched           |    781 |

## Missing-Value Percentage For Combine Columns

| column                         |   missing_pct |
|:-------------------------------|--------------:|
| modified_lane_agility_time_sec |          68.9 |
| hand_length_in                 |          54.2 |
| hand_width_in                  |          54.2 |
| bench_press_reps               |          53.3 |
| height_w_shoes_in              |          48.7 |
| body_fat_pct                   |          45.6 |
| lane_agility_time_sec          |          31.4 |
| three_quarter_sprint_sec       |          31.4 |
| max_vertical_leap_in           |          31.1 |
| standing_vertical_leap_in      |          31.1 |
| weight_lbs                     |          22.9 |
| standing_reach_in              |          22.8 |
| height_wo_shoes_in             |          22.8 |
| wingspan_in                    |          22.8 |

## Missing-Value Percentage For NCAA Columns

| column            |   missing_pct |
|:------------------|--------------:|
| ncaa_pos          |          52.8 |
| ncaa_exp          |          47   |
| ncaa_height       |          47   |
| ncaa_oreb         |          47   |
| ncaa_bpm          |          47   |
| ncaa_usage        |          47   |
| ncaa_obpm         |          47   |
| ncaa_dbpm         |          47   |
| ncaa_adj_oe       |          47   |
| ncaa_drtg         |          47   |
| ncaa_porpag       |          47   |
| ncaa_dporpag      |          47   |
| ncaa_ast_to       |          47   |
| ncaa_ortg         |          47   |
| ncaa_dreb         |          47   |
| ncaa_mpg          |          41.9 |
| ncaa_fg_pct       |          41.9 |
| ncaa_tpg          |          41.9 |
| ncaa_three_pct    |          34.6 |
| ncaa_source       |          33.3 |
| ncaa_player_raw   |          33.3 |
| ncaa_team         |          33.3 |
| ncaa_conf         |          33.3 |
| ncaa_ppg          |          33.3 |
| ncaa_spg          |          33.3 |
| ncaa_ft_pct       |          33.3 |
| ncaa_games        |          33.3 |
| ncaa_two_pct      |          33.3 |
| ncaa_rpg          |          33.3 |
| ncaa_bpg          |          33.3 |
| ncaa_apg          |          33.3 |
| ncaa_match_method |           0   |

## First 30 Rows

| name               |   draft_year |   overall_pick | position   | organization                            | organization_type   | draft_team_abbreviation   |   height_wo_shoes_in |   height_w_shoes_in |   weight_lbs |   wingspan_in |   standing_reach_in |   body_fat_pct |   hand_length_in |   hand_width_in |   standing_vertical_leap_in |   max_vertical_leap_in |   lane_agility_time_sec |   modified_lane_agility_time_sec |   three_quarter_sprint_sec |   bench_press_reps | ncaa_match_method   | ncaa_source      | ncaa_player_raw    | ncaa_team       | ncaa_conf   | ncaa_pos   | ncaa_exp   | ncaa_height   | ncaa_games   | ncaa_mpg   | ncaa_ppg   | ncaa_fg_pct   | ncaa_two_pct   | ncaa_three_pct   | ncaa_ft_pct   | ncaa_oreb   | ncaa_dreb   | ncaa_rpg   | ncaa_apg   | ncaa_ast_to   | ncaa_spg   | ncaa_bpg   | ncaa_tpg   | ncaa_ortg   | ncaa_adj_oe   | ncaa_drtg   | ncaa_porpag   | ncaa_dporpag   | ncaa_bpm   | ncaa_obpm   | ncaa_dbpm   | ncaa_usage   |
|:-------------------|-------------:|---------------:|:-----------|:----------------------------------------|:--------------------|:--------------------------|---------------------:|--------------------:|-------------:|--------------:|--------------------:|---------------:|-----------------:|----------------:|----------------------------:|-----------------------:|------------------------:|---------------------------------:|---------------------------:|-------------------:|:--------------------|:-----------------|:-------------------|:----------------|:------------|:-----------|:-----------|:--------------|:-------------|:-----------|:-----------|:--------------|:---------------|:-----------------|:--------------|:------------|:------------|:-----------|:-----------|:--------------|:-----------|:-----------|:-----------|:------------|:--------------|:------------|:--------------|:---------------|:-----------|:------------|:------------|:-------------|
| kenyon martin      |         2000 |              1 | nan        | Cincinnati                              | College/University  | NJN                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | kenyon martin      | Cincinnati      | CUSA        | nan        | nan        | nan           | 31.0         | 29.3       | 18.9       | 0.568         | 0.573          | 0.286            | 0.684         | nan         | nan         | 9.7        | 1.4        | nan           | 1.4        | 3.5        | 1.8        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| stromile swift     |         2000 |              2 | nan        | Louisiana State                         | College/University  | VAN                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | stromile swift     | LSU             | SEC         | nan        | nan        | nan           | 34.0         | 29.8       | 16.2       | 0.608         | 0.634          | 0.28             | 0.617         | nan         | nan         | 8.2        | 0.9        | nan           | 1.5        | 2.8        | 2.4        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| darius miles       |         2000 |              3 | nan        | East St. Louis                          | High School         | LAC                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| marcus fizer       |         2000 |              4 | nan        | Iowa State                              | College/University  | CHI                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | marcus fizer       | Iowa St.        | Big 12      | nan        | nan        | nan           | 37.0         | 33.6       | 22.8       | 0.582         | 0.6            | 0.357            | 0.732         | nan         | nan         | 7.7        | 1.1        | nan           | 0.8        | 1.1        | 2.1        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| mike miller        |         2000 |              5 | nan        | Florida                                 | College/University  | ORL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | mike miller        | Florida         | SEC         | nan        | nan        | nan           | 37.0         | 28.6       | 14.1       | 0.476         | 0.559          | 0.338            | 0.729         | nan         | nan         | 6.6        | 2.5        | nan           | 1.2        | 0.4        | 1.9        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| dermarr johnson    |         2000 |              6 | nan        | Cincinnati                              | College/University  | ATL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | dermarr johnson    | Cincinnati      | CUSA        | nan        | nan        | nan           | 32.0         | 27.5       | 12.6       | 0.478         | 0.575          | 0.371            | 0.737         | nan         | nan         | 3.8        | 1.4        | nan           | 1.0        | 0.9        | 1.4        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| chris mihm         |         2000 |              7 | nan        | Texas                                   | College/University  | CHI                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | chris mihm         | Texas           | Big 12      | nan        | nan        | nan           | 33.0         | 30.7       | 17.7       | 0.523         | 0.525          | 0.467            | 0.707         | nan         | nan         | 10.5       | 0.7        | nan           | 0.3        | 2.7        | 2.5        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| jamal crawford     |         2000 |              8 | PG-SG      | Michigan                                | College/University  | CLE                       |                76.5  |                 nan |        175   |          82   |               102.5 |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                  0 | exact_name          | sports_reference | jamal crawford     | Michigan        | Big Ten     | nan        | nan        | nan           | 17.0         | 33.9       | 16.6       | 0.412         | 0.468          | 0.327            | 0.784         | nan         | nan         | 2.8        | 4.5        | nan           | 1.1        | 0.9        | 3.1        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| joel przybilla     |         2000 |              9 | nan        | Minnesota                               | College/University  | HOU                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | joel przybilla     | Minnesota       | Big Ten     | nan        | nan        | nan           | 21.0         | 30.4       | 14.2       | 0.613         | 0.613          | nan              | 0.495         | nan         | nan         | 8.4        | 2.4        | nan           | 0.8        | 3.9        | 3.7        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| keyon dooling      |         2000 |             10 | nan        | Missouri                                | College/University  | ORL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | keyon dooling      | Missouri        | Big 12      | nan        | nan        | nan           | 31.0         | 31.7       | 15.3       | 0.389         | 0.424          | 0.347            | 0.743         | nan         | nan         | 2.7        | 3.6        | nan           | 1.4        | 0.5        | 2.5        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| jerome moiso       |         2000 |             11 | nan        | California-Los Angeles                  | College/University  | BOS                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | jerome moiso       | UCLA            | Pac-10      | nan        | nan        | nan           | 33.0         | 29.5       | 13.0       | 0.501         | 0.508          | 0.167            | 0.613         | nan         | nan         | 7.6        | 1.2        | nan           | 1.1        | 1.7        | 2.7        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| etan thomas        |         2000 |             12 | nan        | Syracuse                                | College/University  | DAL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | etan thomas        | Syracuse        | Big East    | nan        | nan        | nan           | 29.0         | 32.4       | 13.6       | 0.602         | 0.602          | nan              | 0.678         | nan         | nan         | 9.3        | 0.6        | nan           | 0.8        | 3.7        | 2.0        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| courtney alexander |         2000 |             13 | nan        | Fresno State                            | College/University  | ORL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | courtney alexander | Fresno St.      | WAC         | nan        | nan        | nan           | 27.0         | 36.1       | 24.8       | 0.447         | 0.499          | 0.331            | 0.781         | nan         | nan         | 4.7        | 3.5        | nan           | 1.4        | 0.1        | 2.5        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| mateen cleaves     |         2000 |             14 | nan        | Michigan State                          | College/University  | DET                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | mateen cleaves     | Michigan St.    | Big Ten     | nan        | nan        | nan           | 26.0         | 31.5       | 12.1       | 0.421         | 0.443          | 0.376            | 0.756         | nan         | nan         | 1.8        | 6.9        | nan           | 1.4        | 0.2        | 3.7        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| jason collier      |         2000 |             15 | nan        | Georgia Tech                            | College/University  | MIL                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | jason collier      | Ga Tech         | ACC         | nan        | nan        | nan           | 30.0         | 32.5       | 17.0       | 0.473         | 0.503          | 0.369            | 0.735         | nan         | nan         | 9.2        | 1.6        | nan           | 0.8        | 1.1        | 3.2        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| hedo turkoglu      |         2000 |             16 | nan        | Anadolu Efes S.K. (Turkey)              | Other Team/Club     | SAC                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| desmond mason      |         2000 |             17 | nan        | Oklahoma State                          | College/University  | SEA                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | desmond mason      | Oklahoma St.    | Big 12      | nan        | nan        | nan           | 34.0         | 35.4       | 18.0       | 0.499         | 0.536          | 0.43             | 0.767         | nan         | nan         | 6.6        | 1.5        | nan           | 1.2        | 1.0        | 1.8        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| quentin richardson |         2000 |             18 | nan        | DePaul                                  | College/University  | LAC                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | quentin richardson | DePaul          | CUSA        | nan        | nan        | nan           | 33.0         | 34.8       | 17.0       | 0.432         | 0.464          | 0.384            | 0.706         | nan         | nan         | 9.8        | 2.2        | nan           | 1.1        | 0.3        | 2.3        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| jamaal magloire    |         2000 |             19 | nan        | Kentucky                                | College/University  | CHH                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | jamaal magloire    | Kentucky        | SEC         | nan        | nan        | nan           | 33.0         | 29.6       | 13.2       | 0.5           | 0.5            | nan              | 0.685         | nan         | nan         | 9.1        | 0.5        | nan           | 0.5        | 1.7        | 2.9        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| speedy claxton     |         2000 |             20 | PG         | Hofstra                                 | College/University  | PHI                       |                70.5  |                 nan |        166   |          72   |                94.5 |            nan |              nan |             nan |                        36   |                   42.5 |                   10.48 |                              nan |                       3.06 |                  6 | exact_name          | sports_reference | speedy claxton     | Hofstra         | AmEast      | nan        | nan        | nan           | 31.0         | 35.1       | 22.8       | 0.47          | 0.5            | 0.381            | 0.764         | nan         | nan         | 5.4        | 6.0        | nan           | 3.3        | 0.2        | 3.3        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| morris peterson    |         2000 |             21 | nan        | Michigan State                          | College/University  | TOR                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | morris peterson    | Michigan St.    | Big Ten     | nan        | nan        | nan           | 39.0         | 29.1       | 16.8       | 0.465         | 0.494          | 0.425            | 0.773         | nan         | nan         | 6.0        | 1.3        | nan           | 1.2        | 0.3        | 2.2        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| donnell harvey     |         2000 |             22 | PF         | Florida                                 | College/University  | NYK                       |                79.25 |                 nan |        220   |          84.5 |               105.5 |            nan |              nan |             nan |                        33   |                   32.5 |                   11.23 |                              nan |                     nan    |                 15 | exact_name          | sports_reference | donnell harvey     | Florida         | SEC         | nan        | nan        | nan           | 37.0         | 20.2       | 10.1       | 0.507         | 0.509          | 0.0              | 0.61          | nan         | nan         | 7.0        | 1.0        | nan           | 0.7        | 0.8        | 1.6        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| deshawn stevenson  |         2000 |             23 | nan        | Washington Union                        | High School         | UTA                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| dalibor bagaric    |         2000 |             24 | nan        | KK Dubrava (Croatia)                    | Other Team/Club     | CHI                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| jake tsakalidis    |         2000 |             25 | nan        | A.E.K. Athens B.C. (Greece)             | Other Team/Club     | PHX                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| mamadou n diaye    |         2000 |             26 | nan        | Auburn                                  | College/University  | DEN                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | mamadou n diaye    | Auburn          | SEC         | nan        | nan        | nan           | 34.0         | 26.6       | 8.9        | 0.535         | 0.535          | nan              | 0.665         | nan         | nan         | 7.9        | 0.5        | nan           | 0.8        | 1.9        | 2.1        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| primoz brezec      |         2000 |             27 | C          | KK Olimpija (Slovenia)                  | Other Team/Club     | IND                       |                84.75 |                 nan |        243   |          86   |               110   |            nan |              nan |             nan |                        26   |                   29.5 |                   11.53 |                              nan |                       3.55 |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |
| erick barkley      |         2000 |             28 | nan        | St. John's (NY)                         | College/University  | POR                       |               nan    |                 nan |        nan   |         nan   |               nan   |            nan |              nan |             nan |                       nan   |                  nan   |                  nan    |                              nan |                     nan    |                nan | exact_name          | sports_reference | erick barkley      | St. John's (NY) | Big East    | nan        | nan        | nan           | 28.0         | 36.9       | 16.0       | 0.398         | 0.454          | 0.313            | 0.664         | nan         | nan         | 3.0        | 4.5        | nan           | 3.0        | 0.3        | 2.4        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| mark madsen        |         2000 |             29 | PF         | Stanford                                | College/University  | LAL                       |                80    |                 nan |        236.5 |          84.5 |               104.5 |            nan |              nan |             nan |                        30.5 |                   33.5 |                   12.12 |                              nan |                       3.46 |                 13 | exact_name          | sports_reference | mark madsen        | Stanford        | Pac-10      | nan        | nan        | nan           | 23.0         | 27.3       | 12.2       | 0.587         | 0.587          | nan              | 0.575         | nan         | nan         | 9.3        | 1.1        | nan           | 0.6        | 0.9        | 1.5        | nan         | nan           | nan         | nan           | nan            | nan        | nan         | nan         | nan          |
| marko jaric        |         2000 |             30 | SG-SF      | Fortitudo Pallacanestro Bologna (Italy) | Other Team/Club     | LAC                       |                78.5  |                 nan |        210   |          81   |               104   |            nan |              nan |             nan |                        27.5 |                   33   |                   11.32 |                              nan |                       3.28 |                nan | unmatched           | <NA>             | <NA>               | <NA>            | <NA>        | <NA>       | <NA>       | <NA>          | <NA>         | <NA>       | <NA>       | <NA>          | <NA>           | <NA>             | <NA>          | <NA>        | <NA>        | <NA>       | <NA>       | <NA>          | <NA>       | <NA>       | <NA>       | <NA>        | <NA>          | <NA>        | <NA>          | <NA>           | <NA>       | <NA>        | <NA>        | <NA>         |

## Final Column List

- name
- draft_year
- overall_pick
- position
- organization
- organization_type
- draft_team_abbreviation
- height_wo_shoes_in
- height_w_shoes_in
- weight_lbs
- wingspan_in
- standing_reach_in
- body_fat_pct
- hand_length_in
- hand_width_in
- standing_vertical_leap_in
- max_vertical_leap_in
- lane_agility_time_sec
- modified_lane_agility_time_sec
- three_quarter_sprint_sec
- bench_press_reps
- ncaa_match_method
- ncaa_source
- ncaa_player_raw
- ncaa_team
- ncaa_conf
- ncaa_pos
- ncaa_exp
- ncaa_height
- ncaa_games
- ncaa_mpg
- ncaa_ppg
- ncaa_fg_pct
- ncaa_two_pct
- ncaa_three_pct
- ncaa_ft_pct
- ncaa_oreb
- ncaa_dreb
- ncaa_rpg
- ncaa_apg
- ncaa_ast_to
- ncaa_spg
- ncaa_bpg
- ncaa_tpg
- ncaa_ortg
- ncaa_adj_oe
- ncaa_drtg
- ncaa_porpag
- ncaa_dporpag
- ncaa_bpm
- ncaa_obpm
- ncaa_dbpm
- ncaa_usage
