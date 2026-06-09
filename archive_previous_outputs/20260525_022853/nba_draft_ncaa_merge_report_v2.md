# NBA Draft/Combine to Unified NCAA Merge Diagnostic Report

This is a diagnostic report only. No merged CSV was saved.

## Summary

| metric                                    |   value |
|:------------------------------------------|--------:|
| base_rows                                 |  2347   |
| base_columns                              |    25   |
| ncaa_rows                                 | 90344   |
| ncaa_columns                              |    36   |
| merged_rows_for_report                    |  2347   |
| merged_row_count_equals_base              |     1   |
| base_duplicate_name_draft_year_pick_rows  |     0   |
| ncaa_duplicate_name_draft_year_rows       |     0   |
| old_exact_name_match_count                |  1545   |
| improved_match_count_after_alternate_keys |  1557   |
| additional_matches_from_alternate_keys    |    12   |
| additional_matches_from_compact_initials  |    12   |
| additional_matches_from_spaced_initials   |     0   |
| matched_rows                              |  1557   |
| unmatched_rows                            |   790   |
| match_rate_pct                            |    66.3 |
| college_university_rows                   |  1193   |
| college_university_matched                |  1158   |
| college_university_match_rate_pct         |    97.1 |
| prediction_2026_rows                      |    78   |
| prediction_2026_matched                   |    68   |
| prediction_2026_match_rate_pct            |    87.2 |

## Match Rate By draft_year

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
|         2010 |     68 |        59 |           9 |             86.8 |
|         2011 |     71 |        53 |          18 |             74.6 |
|         2012 |     71 |        61 |          10 |             85.9 |
|         2013 |     78 |        61 |          17 |             78.2 |
|         2014 |     73 |        56 |          17 |             76.7 |
|         2015 |     80 |        65 |          15 |             81.2 |
|         2016 |     78 |        60 |          18 |             76.9 |
|         2017 |     82 |        67 |          15 |             81.7 |
|         2018 |     85 |        70 |          15 |             82.4 |
|         2019 |     88 |        72 |          16 |             81.8 |
|         2020 |     78 |        63 |          15 |             80.8 |
|         2021 |     87 |        71 |          16 |             81.6 |
|         2022 |     91 |        70 |          21 |             76.9 |
|         2023 |     83 |        69 |          14 |             83.1 |
|         2024 |     84 |        66 |          18 |             78.6 |
|         2025 |     86 |        67 |          19 |             77.9 |
|         2026 |     78 |        68 |          10 |             87.2 |

## Match Rate By organization_type

| organization_type   |   rows |   matched |   unmatched |   match_rate_pct |
|:--------------------|-------:|----------:|------------:|-----------------:|
| College/University  |   1193 |      1158 |          35 |             97.1 |
| High School         |     35 |         0 |          35 |              0   |
| Other Team/Club     |    312 |         0 |         312 |              0   |
| nan                 |    807 |       399 |         408 |             49.4 |

## Match Rate By draft_group_preview

| draft_group_preview     |   rows |   matched |   unmatched |   match_rate_pct |
|:------------------------|-------:|----------:|------------:|-----------------:|
| picks_15_30             |    416 |       320 |          96 |             76.9 |
| picks_6_14              |    234 |       194 |          40 |             82.9 |
| prediction_2026_unknown |     78 |        68 |          10 |             87.2 |
| second_round            |    762 |       545 |         217 |             71.5 |
| top_5                   |    130 |        99 |          31 |             76.2 |
| undrafted_999           |    727 |       331 |         396 |             45.5 |

## Match Counts By ncaa_match_method

| ncaa_match_method   |   rows |
|:--------------------|-------:|
| compact_initials    |     12 |
| exact_name          |   1545 |
| unmatched           |    790 |

## Match Rate By draft_year And organization_type

|   draft_year | organization_type   |   rows |   matched |   unmatched |   match_rate_pct |
|-------------:|:--------------------|-------:|----------:|------------:|-----------------:|
|         2000 | College/University  |     46 |        44 |           2 |             95.7 |
|         2000 | High School         |      2 |         0 |           2 |              0   |
|         2000 | Other Team/Club     |     10 |         0 |          10 |              0   |
|         2000 | nan                 |     41 |         0 |          41 |              0   |
|         2001 | College/University  |     45 |        44 |           1 |             97.8 |
|         2001 | High School         |      5 |         0 |           5 |              0   |
|         2001 | Other Team/Club     |      7 |         0 |           7 |              0   |
|         2001 | nan                 |     39 |         0 |          39 |              0   |
|         2002 | College/University  |     42 |        40 |           2 |             95.2 |
|         2002 | High School         |      1 |         0 |           1 |              0   |
|         2002 | Other Team/Club     |     14 |         0 |          14 |              0   |
|         2002 | nan                 |     45 |         0 |          45 |              0   |
|         2003 | College/University  |     34 |        32 |           2 |             94.1 |
|         2003 | High School         |      5 |         0 |           5 |              0   |
|         2003 | Other Team/Club     |     19 |         0 |          19 |              0   |
|         2003 | nan                 |     48 |         0 |          48 |              0   |
|         2004 | College/University  |     38 |        34 |           4 |             89.5 |
|         2004 | High School         |      8 |         0 |           8 |              0   |
|         2004 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2004 | nan                 |     44 |         0 |          44 |              0   |
|         2005 | College/University  |     37 |        37 |           0 |            100   |
|         2005 | High School         |      9 |         0 |           9 |              0   |
|         2005 | Other Team/Club     |     14 |         0 |          14 |              0   |
|         2005 | nan                 |     47 |         0 |          47 |              0   |
|         2006 | College/University  |     44 |        44 |           0 |            100   |
|         2006 | Other Team/Club     |     16 |         0 |          16 |              0   |
|         2006 | nan                 |     47 |         0 |          47 |              0   |
|         2007 | College/University  |     47 |        47 |           0 |            100   |
|         2007 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2007 | nan                 |     38 |         0 |          38 |              0   |
|         2008 | College/University  |     48 |        48 |           0 |            100   |
|         2008 | Other Team/Club     |     12 |         0 |          12 |              0   |
|         2008 | nan                 |     42 |        37 |           5 |             88.1 |
|         2009 | College/University  |     47 |        47 |           0 |            100   |
|         2009 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2009 | nan                 |      6 |         5 |           1 |             83.3 |
|         2010 | College/University  |     53 |        52 |           1 |             98.1 |
|         2010 | Other Team/Club     |      7 |         0 |           7 |              0   |
|         2010 | nan                 |      8 |         7 |           1 |             87.5 |
|         2011 | College/University  |     47 |        45 |           2 |             95.7 |
|         2011 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2011 | nan                 |     11 |         8 |           3 |             72.7 |
|         2012 | College/University  |     52 |        50 |           2 |             96.2 |
|         2012 | Other Team/Club     |      8 |         0 |           8 |              0   |
|         2012 | nan                 |     11 |        11 |           0 |            100   |
|         2013 | College/University  |     47 |        45 |           2 |             95.7 |
|         2013 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2013 | nan                 |     18 |        16 |           2 |             88.9 |
|         2014 | College/University  |     45 |        44 |           1 |             97.8 |
|         2014 | Other Team/Club     |     15 |         0 |          15 |              0   |
|         2014 | nan                 |     13 |        12 |           1 |             92.3 |
|         2015 | College/University  |     46 |        45 |           1 |             97.8 |
|         2015 | High School         |      1 |         0 |           1 |              0   |
|         2015 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2015 | nan                 |     20 |        20 |           0 |            100   |
|         2016 | College/University  |     43 |        43 |           0 |            100   |
|         2016 | High School         |      1 |         0 |           1 |              0   |
|         2016 | Other Team/Club     |     15 |         0 |          15 |              0   |
|         2016 | nan                 |     19 |        17 |           2 |             89.5 |
|         2017 | College/University  |     50 |        48 |           2 |             96   |
|         2017 | Other Team/Club     |     10 |         0 |          10 |              0   |
|         2017 | nan                 |     22 |        19 |           3 |             86.4 |
|         2018 | College/University  |     51 |        48 |           3 |             94.1 |
|         2018 | High School         |      1 |         0 |           1 |              0   |
|         2018 | Other Team/Club     |      7 |         0 |           7 |              0   |
|         2018 | nan                 |     26 |        22 |           4 |             84.6 |
|         2019 | College/University  |     52 |        50 |           2 |             96.2 |
|         2019 | High School         |      1 |         0 |           1 |              0   |
|         2019 | Other Team/Club     |      7 |         0 |           7 |              0   |
|         2019 | nan                 |     28 |        22 |           6 |             78.6 |
|         2020 | College/University  |     49 |        48 |           1 |             98   |
|         2020 | High School         |      1 |         0 |           1 |              0   |
|         2020 | Other Team/Club     |     10 |         0 |          10 |              0   |
|         2020 | nan                 |     18 |        15 |           3 |             83.3 |
|         2021 | College/University  |     51 |        48 |           3 |             94.1 |
|         2021 | Other Team/Club     |      9 |         0 |           9 |              0   |
|         2021 | nan                 |     27 |        23 |           4 |             85.2 |
|         2022 | College/University  |     44 |        43 |           1 |             97.7 |
|         2022 | Other Team/Club     |     14 |         0 |          14 |              0   |
|         2022 | nan                 |     33 |        27 |           6 |             81.8 |
|         2023 | College/University  |     46 |        45 |           1 |             97.8 |
|         2023 | Other Team/Club     |     12 |         0 |          12 |              0   |
|         2023 | nan                 |     25 |        24 |           1 |             96   |
|         2024 | College/University  |     43 |        42 |           1 |             97.7 |
|         2024 | Other Team/Club     |     15 |         0 |          15 |              0   |
|         2024 | nan                 |     26 |        24 |           2 |             92.3 |
|         2025 | College/University  |     46 |        45 |           1 |             97.8 |
|         2025 | Other Team/Club     |     13 |         0 |          13 |              0   |
|         2025 | nan                 |     27 |        22 |           5 |             81.5 |
|         2026 | nan                 |     78 |        68 |          10 |             87.2 |

## Missing-Value Percentage For NCAA Columns After Left Join

| column          |   missing_pct |
|:----------------|--------------:|
| ncaa_pos        |          53.2 |
| ncaa_exp        |          47.4 |
| ncaa_height     |          47.4 |
| ncaa_oreb       |          47.4 |
| ncaa_usage      |          47.4 |
| ncaa_obpm       |          47.4 |
| ncaa_dbpm       |          47.4 |
| ncaa_adj_oe     |          47.4 |
| ncaa_drtg       |          47.4 |
| ncaa_porpag     |          47.4 |
| ncaa_dporpag    |          47.4 |
| ncaa_bpm        |          47.4 |
| ncaa_ortg       |          47.4 |
| ncaa_ast_to     |          47.4 |
| ncaa_dreb       |          47.4 |
| ncaa_mpg        |          42.2 |
| ncaa_fg_pct     |          42.2 |
| ncaa_tpg        |          42.2 |
| ncaa_three_pct  |          34.9 |
| ncaa_team       |          33.7 |
| ncaa_player_raw |          33.7 |
| ncaa_source     |          33.7 |
| ncaa_conf       |          33.7 |
| ncaa_ft_pct     |          33.7 |
| ncaa_two_pct    |          33.7 |
| ncaa_games      |          33.7 |
| ncaa_ppg        |          33.7 |
| ncaa_spg        |          33.7 |
| ncaa_bpg        |          33.7 |
| ncaa_rpg        |          33.7 |
| ncaa_apg        |          33.7 |

## Matched First-Round Examples

| name               |   draft_year |   overall_pick | organization             | ncaa_source      | ncaa_player_raw    | ncaa_match_method   | ncaa_team       | ncaa_conf   |   ncaa_games |   ncaa_ppg |   ncaa_rpg |   ncaa_apg |   ncaa_bpm |   ncaa_usage |
|:-------------------|-------------:|---------------:|:-------------------------|:-----------------|:-------------------|:--------------------|:----------------|:------------|-------------:|-----------:|-----------:|-----------:|-----------:|-------------:|
| kenyon martin      |         2000 |              1 | Cincinnati               | sports_reference | kenyon martin      | exact_name          | Cincinnati      | CUSA        |           31 |       18.9 |        9.7 |        1.4 |        nan |          nan |
| stromile swift     |         2000 |              2 | Louisiana State          | sports_reference | stromile swift     | exact_name          | LSU             | SEC         |           34 |       16.2 |        8.2 |        0.9 |        nan |          nan |
| marcus fizer       |         2000 |              4 | Iowa State               | sports_reference | marcus fizer       | exact_name          | Iowa St.        | Big 12      |           37 |       22.8 |        7.7 |        1.1 |        nan |          nan |
| mike miller        |         2000 |              5 | Florida                  | sports_reference | mike miller        | exact_name          | Florida         | SEC         |           37 |       14.1 |        6.6 |        2.5 |        nan |          nan |
| dermarr johnson    |         2000 |              6 | Cincinnati               | sports_reference | dermarr johnson    | exact_name          | Cincinnati      | CUSA        |           32 |       12.6 |        3.8 |        1.4 |        nan |          nan |
| chris mihm         |         2000 |              7 | Texas                    | sports_reference | chris mihm         | exact_name          | Texas           | Big 12      |           33 |       17.7 |       10.5 |        0.7 |        nan |          nan |
| jamal crawford     |         2000 |              8 | Michigan                 | sports_reference | jamal crawford     | exact_name          | Michigan        | Big Ten     |           17 |       16.6 |        2.8 |        4.5 |        nan |          nan |
| joel przybilla     |         2000 |              9 | Minnesota                | sports_reference | joel przybilla     | exact_name          | Minnesota       | Big Ten     |           21 |       14.2 |        8.4 |        2.4 |        nan |          nan |
| keyon dooling      |         2000 |             10 | Missouri                 | sports_reference | keyon dooling      | exact_name          | Missouri        | Big 12      |           31 |       15.3 |        2.7 |        3.6 |        nan |          nan |
| jerome moiso       |         2000 |             11 | California-Los Angeles   | sports_reference | jerome moiso       | exact_name          | UCLA            | Pac-10      |           33 |       13   |        7.6 |        1.2 |        nan |          nan |
| etan thomas        |         2000 |             12 | Syracuse                 | sports_reference | etan thomas        | exact_name          | Syracuse        | Big East    |           29 |       13.6 |        9.3 |        0.6 |        nan |          nan |
| courtney alexander |         2000 |             13 | Fresno State             | sports_reference | courtney alexander | exact_name          | Fresno St.      | WAC         |           27 |       24.8 |        4.7 |        3.5 |        nan |          nan |
| mateen cleaves     |         2000 |             14 | Michigan State           | sports_reference | mateen cleaves     | exact_name          | Michigan St.    | Big Ten     |           26 |       12.1 |        1.8 |        6.9 |        nan |          nan |
| jason collier      |         2000 |             15 | Georgia Tech             | sports_reference | jason collier      | exact_name          | Ga Tech         | ACC         |           30 |       17   |        9.2 |        1.6 |        nan |          nan |
| desmond mason      |         2000 |             17 | Oklahoma State           | sports_reference | desmond mason      | exact_name          | Oklahoma St.    | Big 12      |           34 |       18   |        6.6 |        1.5 |        nan |          nan |
| quentin richardson |         2000 |             18 | DePaul                   | sports_reference | quentin richardson | exact_name          | DePaul          | CUSA        |           33 |       17   |        9.8 |        2.2 |        nan |          nan |
| jamaal magloire    |         2000 |             19 | Kentucky                 | sports_reference | jamaal magloire    | exact_name          | Kentucky        | SEC         |           33 |       13.2 |        9.1 |        0.5 |        nan |          nan |
| speedy claxton     |         2000 |             20 | Hofstra                  | sports_reference | speedy claxton     | exact_name          | Hofstra         | AmEast      |           31 |       22.8 |        5.4 |        6   |        nan |          nan |
| morris peterson    |         2000 |             21 | Michigan State           | sports_reference | morris peterson    | exact_name          | Michigan St.    | Big Ten     |           39 |       16.8 |        6   |        1.3 |        nan |          nan |
| donnell harvey     |         2000 |             22 | Florida                  | sports_reference | donnell harvey     | exact_name          | Florida         | SEC         |           37 |       10.1 |        7   |        1   |        nan |          nan |
| mamadou n diaye    |         2000 |             26 | Auburn                   | sports_reference | mamadou n diaye    | exact_name          | Auburn          | SEC         |           34 |        8.9 |        7.9 |        0.5 |        nan |          nan |
| erick barkley      |         2000 |             28 | St. John's (NY)          | sports_reference | erick barkley      | exact_name          | St. John's (NY) | Big East    |           28 |       16   |        3   |        4.5 |        nan |          nan |
| mark madsen        |         2000 |             29 | Stanford                 | sports_reference | mark madsen        | exact_name          | Stanford        | Pac-10      |           23 |       12.2 |        9.3 |        1.1 |        nan |          nan |
| jason richardson   |         2001 |              5 | Michigan State           | sports_reference | jason richardson   | exact_name          | Michigan St.    | Big Ten     |           33 |       14.7 |        5.9 |        2.2 |        nan |          nan |
| shane battier      |         2001 |              6 | Duke                     | sports_reference | shane battier      | exact_name          | Duke            | ACC         |           39 |       19.9 |        7.3 |        1.8 |        nan |          nan |
| eddie griffin      |         2001 |              7 | Seton Hall               | sports_reference | eddie griffin      | exact_name          | Seton Hall      | Big East    |           30 |       17.8 |       10.8 |        1.6 |        nan |          nan |
| rodney white       |         2001 |              9 | North Carolina-Charlotte | sports_reference | rodney white       | exact_name          | Charlotte       | CUSA        |           28 |       18.7 |        6.5 |        1.5 |        nan |          nan |
| joe johnson        |         2001 |             10 | Arkansas                 | sports_reference | joe johnson        | exact_name          | Arkansas        | SEC         |           30 |       14.2 |        6.4 |        2.6 |        nan |          nan |
| richard jefferson  |         2001 |             13 | Arizona                  | sports_reference | richard jefferson  | exact_name          | Arizona         | Pac-10      |           35 |       11.3 |        5.4 |        2.7 |        nan |          nan |
| troy murphy        |         2001 |             14 | Notre Dame               | sports_reference | troy murphy        | exact_name          | Notre Dame      | Big East    |           30 |       21.8 |        9.2 |        2.1 |        nan |          nan |
| steven hunter      |         2001 |             15 | DePaul                   | sports_reference | steven hunter      | exact_name          | DePaul          | CUSA        |           30 |       11.4 |        5.6 |        0.5 |        nan |          nan |
| kirk haston        |         2001 |             16 | Indiana                  | sports_reference | kirk haston        | exact_name          | Indiana         | Big Ten     |           33 |       19   |        8.7 |        1.2 |        nan |          nan |
| michael bradley    |         2001 |             17 | Villanova                | sports_reference | michael bradley    | exact_name          | Villanova       | Big East    |           31 |       20.8 |        9.8 |        2.6 |        nan |          nan |
| jason collins      |         2001 |             18 | Stanford                 | sports_reference | jason collins      | exact_name          | Stanford        | Pac-10      |           34 |       14.5 |        7.8 |        1.5 |        nan |          nan |
| zach randolph      |         2001 |             19 | Michigan State           | sports_reference | zach randolph      | exact_name          | Michigan St.    | Big Ten     |           33 |       10.8 |        6.7 |        1   |        nan |          nan |
| brendan haywood    |         2001 |             20 | North Carolina           | sports_reference | brendan haywood    | exact_name          | UNC             | ACC         |           33 |       12.3 |        7.3 |        1.3 |        nan |          nan |
| joseph forte       |         2001 |             21 | North Carolina           | sports_reference | joseph forte       | exact_name          | UNC             | ACC         |           33 |       20.9 |        6.1 |        3.5 |        nan |          nan |
| jeryl sasser       |         2001 |             22 | Southern Methodist       | sports_reference | jeryl sasser       | exact_name          | SMU             | WAC         |           29 |       17   |        8.3 |        4.2 |        nan |          nan |
| brandon armstrong  |         2001 |             23 | Pepperdine               | sports_reference | brandon armstrong  | exact_name          | Pepperdine      | WCC         |           31 |       22.1 |        3.3 |        1.5 |        nan |          nan |
| gerald wallace     |         2001 |             25 | Alabama                  | sports_reference | gerald wallace     | exact_name          | Alabama         | SEC         |           36 |        9.8 |        6   |        1.5 |        nan |          nan |
| samuel dalembert   |         2001 |             26 | Seton Hall               | sports_reference | samuel dalembert   | exact_name          | Seton Hall      | Big East    |           29 |        8.3 |        5.7 |        0.3 |        nan |          nan |
| jamaal tinsley     |         2001 |             27 | Iowa State               | sports_reference | jamaal tinsley     | exact_name          | Iowa St.        | Big 12      |           31 |       14.3 |        3.8 |        6   |        nan |          nan |
| trenton hassell    |         2001 |             29 | Austin Peay              | sports_reference | trenton hassell    | exact_name          | Austin Peay     | OVC         |           32 |       21.7 |        7.8 |        4.5 |        nan |          nan |
| gilbert arenas     |         2001 |             30 | Arizona                  | sports_reference | gilbert arenas     | exact_name          | Arizona         | Pac-10      |           36 |       16.2 |        3.6 |        2.3 |        nan |          nan |
| jay williams       |         2002 |              2 | Duke                     | sports_reference | jay williams       | exact_name          | Duke            | ACC         |           35 |       21.3 |        3.5 |        5.3 |        nan |          nan |
| mike dunleavy      |         2002 |              3 | Duke                     | sports_reference | mike dunleavy      | exact_name          | Duke            | ACC         |           35 |       17.3 |        7.2 |        2.1 |        nan |          nan |
| drew gooden        |         2002 |              4 | Kansas                   | sports_reference | drew gooden        | exact_name          | Kansas          | Big 12      |           37 |       19.8 |       11.4 |        2   |        nan |          nan |
| dajuan wagner      |         2002 |              6 | Memphis                  | sports_reference | dajuan wagner      | exact_name          | Memphis         | CUSA        |           36 |       21.2 |        2.5 |        3.6 |        nan |          nan |
| chris wilcox       |         2002 |              8 | Maryland                 | sports_reference | chris wilcox       | exact_name          | Maryland        | ACC         |           36 |       12   |        7.1 |        1.5 |        nan |          nan |
| caron butler       |         2002 |             10 | Connecticut              | sports_reference | caron butler       | exact_name          | UConn           | Big East    |           34 |       20.3 |        7.5 |        3   |        nan |          nan |
| jared jeffries     |         2002 |             11 | Indiana                  | sports_reference | jared jeffries     | exact_name          | Indiana         | Big Ten     |           36 |       15   |        7.6 |        2.1 |        nan |          nan |
| melvin ely         |         2002 |             12 | Fresno State             | sports_reference | melvin ely         | exact_name          | Fresno St.      | WAC         |           28 |       23.3 |        9.1 |        1.8 |        nan |          nan |
| marcus haislip     |         2002 |             13 | Tennessee                | sports_reference | marcus haislip     | exact_name          | Tennessee       | SEC         |           25 |       16.7 |        6.7 |        1   |        nan |          nan |
| fred jones         |         2002 |             14 | Oregon                   | sports_reference | fred jones         | exact_name          | Oregon          | Pac-10      |           35 |       18.6 |        5.4 |        3.2 |        nan |          nan |
| juan dixon         |         2002 |             17 | Maryland                 | sports_reference | juan dixon         | exact_name          | Maryland        | ACC         |           36 |       20.4 |        4.6 |        2.9 |        nan |          nan |
| curtis borchardt   |         2002 |             18 | Stanford                 | sports_reference | curtis borchardt   | exact_name          | Stanford        | Pac-10      |           29 |       16.9 |       11.4 |        2   |        nan |          nan |
| ryan humphrey      |         2002 |             19 | Notre Dame               | sports_reference | ryan humphrey      | exact_name          | Notre Dame      | Big East    |           31 |       18.9 |       10.9 |        2.6 |        nan |          nan |
| kareem rush        |         2002 |             20 | Missouri                 | sports_reference | kareem rush        | exact_name          | Missouri        | Big 12      |           36 |       19.8 |        5.2 |        2.5 |        nan |          nan |
| casey jacobsen     |         2002 |             22 | Stanford                 | sports_reference | casey jacobsen     | exact_name          | Stanford        | Pac-10      |           30 |       21.9 |        4.5 |        3.5 |        nan |          nan |
| tayshaun prince    |         2002 |             23 | Kentucky                 | sports_reference | tayshaun prince    | exact_name          | Kentucky        | SEC         |           32 |       17.5 |        6.3 |        1.6 |        nan |          nan |
| frank williams     |         2002 |             25 | Illinois                 | sports_reference | frank williams     | exact_name          | Illinois        | Big Ten     |           35 |       16.2 |        4.7 |        4.4 |        nan |          nan |
| john salmons       |         2002 |             26 | Miami (FL)               | sports_reference | john salmons       | exact_name          | Miami (FL)      | Big East    |           32 |       13.1 |        6   |        6.1 |        nan |          nan |
| chris jefferies    |         2002 |             27 | Fresno State             | sports_reference | chris jefferies    | exact_name          | Fresno St.      | WAC         |           21 |       17.3 |        6.3 |        3   |        nan |          nan |
| dan dickau         |         2002 |             28 | Gonzaga                  | sports_reference | dan dickau         | exact_name          | Gonzaga         | WCC         |           32 |       21   |        3   |        4.7 |        nan |          nan |
| steve logan        |         2002 |             29 | Cincinnati               | sports_reference | steve logan        | exact_name          | Cincinnati      | CUSA        |           35 |       22   |        3.1 |        5.3 |        nan |          nan |
| roger mason        |         2002 |             30 | Virginia                 | sports_reference | roger mason        | exact_name          | Virginia        | ACC         |           29 |       18.6 |        3.2 |        4.1 |        nan |          nan |
| carmelo anthony    |         2003 |              3 | Syracuse                 | sports_reference | carmelo anthony    | exact_name          | Syracuse        | Big East    |           35 |       22.2 |       10   |        2.2 |        nan |          nan |
| chris bosh         |         2003 |              4 | Georgia Tech             | sports_reference | chris bosh         | exact_name          | Ga Tech         | ACC         |           31 |       15.6 |        9   |        1.2 |        nan |          nan |
| dwyane wade        |         2003 |              5 | Marquette                | sports_reference | dwyane wade        | exact_name          | Marquette       | CUSA        |           33 |       21.5 |        6.3 |        4.4 |        nan |          nan |
| chris kaman        |         2003 |              6 | Central Michigan         | sports_reference | chris kaman        | exact_name          | Central Mich.   | MAC         |           31 |       22.4 |       12   |        1.2 |        nan |          nan |
| kirk hinrich       |         2003 |              7 | Kansas                   | sports_reference | kirk hinrich       | exact_name          | Kansas          | Big 12      |           37 |       17.3 |        3.8 |        3.5 |        nan |          nan |
| t j ford           |         2003 |              8 | Texas                    | sports_reference | t j ford           | exact_name          | Texas           | Big 12      |           33 |       15   |        3.9 |        7.7 |        nan |          nan |
| michael sweetney   |         2003 |              9 | Georgetown               | sports_reference | mike sweetney      | exact_name          | Georgetown      | Big East    |           34 |       22.8 |       10.4 |        1.9 |        nan |          nan |
| jarvis hayes       |         2003 |             10 | Georgia                  | sports_reference | jarvis hayes       | exact_name          | Georgia         | SEC         |           27 |       18.3 |        4.4 |        2   |        nan |          nan |
| nick collison      |         2003 |             12 | Kansas                   | sports_reference | nick collison      | exact_name          | Kansas          | Big 12      |           38 |       18.5 |       10   |        2.2 |        nan |          nan |
| marcus banks       |         2003 |             13 | Nevada-Las Vegas         | sports_reference | marcus banks       | exact_name          | UNLV            | MWC         |           32 |       20.3 |        3.3 |        5.5 |        nan |          nan |
| luke ridnour       |         2003 |             14 | Oregon                   | sports_reference | luke ridnour       | exact_name          | Oregon          | Pac-10      |           33 |       19.7 |        3.4 |        6.6 |        nan |          nan |
| reece gaines       |         2003 |             15 | Louisville               | sports_reference | reece gaines       | exact_name          | Louisville      | CUSA        |           32 |       17.9 |        2.9 |        5   |        nan |          nan |
| troy bell          |         2003 |             16 | Boston College           | sports_reference | troy bell          | exact_name          | Boston College  | Big East    |           31 |       25.2 |        4.6 |        3.7 |        nan |          nan |
| david west         |         2003 |             18 | Xavier                   | sports_reference | david west         | exact_name          | Xavier          | A-10        |           32 |       20.1 |       11.8 |        3.2 |        nan |          nan |

## Unmatched First-Round Examples

| name                 |   draft_year |   overall_pick | draft_group_preview   | organization                              | organization_type   | position   |
|:---------------------|-------------:|---------------:|:----------------------|:------------------------------------------|:--------------------|:-----------|
| darius miles         |         2000 |              3 | top_5                 | East St. Louis                            | High School         | nan        |
| hedo turkoglu        |         2000 |             16 | picks_15_30           | Anadolu Efes S.K. (Turkey)                | Other Team/Club     | nan        |
| deshawn stevenson    |         2000 |             23 | picks_15_30           | Washington Union                          | High School         | nan        |
| dalibor bagaric      |         2000 |             24 | picks_15_30           | KK Dubrava (Croatia)                      | Other Team/Club     | nan        |
| jake tsakalidis      |         2000 |             25 | picks_15_30           | A.E.K. Athens B.C. (Greece)               | Other Team/Club     | nan        |
| primoz brezec        |         2000 |             27 | picks_15_30           | KK Olimpija (Slovenia)                    | Other Team/Club     | C          |
| marko jaric          |         2000 |             30 | picks_15_30           | Fortitudo Pallacanestro Bologna (Italy)   | Other Team/Club     | SG-SF      |
| kwame brown          |         2001 |              1 | top_5                 | Glynn Academy                             | High School         | PF-C       |
| tyson chandler       |         2001 |              2 | top_5                 | Dominguez                                 | High School         | SF-PF      |
| pau gasol            |         2001 |              3 | top_5                 | FC Barcelona Basquet (Spain)              | Other Team/Club     | nan        |
| eddy curry           |         2001 |              4 | top_5                 | Thornwood                                 | High School         | C          |
| desagana diop        |         2001 |              8 | picks_6_14            | Oak Hill Academy                          | High School         | C          |
| kedrick brown        |         2001 |             11 | picks_6_14            | Northwest Florida State                   | College/University  | nan        |
| vladimir radmanovic  |         2001 |             12 | picks_6_14            | KK FMP (Serbia)                           | Other Team/Club     | nan        |
| raul lopez           |         2001 |             24 | picks_15_30           | Real Madrid Baloncesto (Spain)            | Other Team/Club     | nan        |
| tony parker          |         2001 |             28 | picks_15_30           | Paris Basket Racing (France)              | Other Team/Club     | nan        |
| yao ming             |         2002 |              1 | top_5                 | Shanghai Sharks (China)                   | Other Team/Club     | nan        |
| nikoloz tskitishvili |         2002 |              5 | top_5                 | Universo Treviso Basket (Italy)           | Other Team/Club     | nan        |
| nene                 |         2002 |              7 | picks_6_14            | CR Vasco da Gama (Brazil)                 | Other Team/Club     | PF         |
| amar e stoudemire    |         2002 |              9 | picks_6_14            | Cypress Creek                             | High School         | PF         |
| bostjan nachbar      |         2002 |             15 | picks_15_30           | Universo Treviso Basket (Italy)           | Other Team/Club     | nan        |
| jiri welsch          |         2002 |             16 | picks_15_30           | KK Olimpija (Slovenia)                    | Other Team/Club     | nan        |
| qyntel woods         |         2002 |             21 | picks_15_30           | Northeast Mississippi Community College   | College/University  | SF-SG      |
| nenad krstic         |         2002 |             24 | picks_15_30           | KK Partizan (Serbia)                      | Other Team/Club     | nan        |
| lebron james         |         2003 |              1 | top_5                 | Saint Vincent-Saint Mary                  | High School         | SF-SG      |
| darko milicic        |         2003 |              2 | top_5                 | KK Vrsac (Serbia)                         | Other Team/Club     | PF         |
| mickael pietrus      |         2003 |             11 | picks_6_14            | Elan Bearnais Pau-Orthez (France)         | Other Team/Club     | nan        |
| zarko cabarkapa      |         2003 |             17 | picks_15_30           | KK Buducnost Podgorica (Montenegro)       | Other Team/Club     | nan        |
| sasha pavlovic       |         2003 |             19 | picks_15_30           | KK Buducnost Podgorica (Montenegro)       | Other Team/Club     | nan        |
| boris diaw           |         2003 |             21 | picks_15_30           | Elan Bearnais Pau-Orthez (France)         | Other Team/Club     | nan        |
| zoran planinic       |         2003 |             22 | picks_15_30           | KK Cibona (Croatia)                       | Other Team/Club     | nan        |
| travis outlaw        |         2003 |             23 | picks_15_30           | Starkville                                | High School         | nan        |
| carlos delfino       |         2003 |             25 | picks_15_30           | Fortitudo Pallacanestro Bologna (Italy)   | Other Team/Club     | nan        |
| ndudi ebi            |         2003 |             26 | picks_15_30           | Westbury Christian School                 | High School         | nan        |
| kendrick perkins     |         2003 |             27 | picks_15_30           | Clifton J. Ozen                           | High School         | nan        |
| leandro barbosa      |         2003 |             28 | picks_15_30           | Associacao Bauru Basketball Team (Brazil) | Other Team/Club     | nan        |
| maciej lampe         |         2003 |             30 | picks_15_30           | Madrid (ESP)                              | College/University  | nan        |
| dwight howard        |         2004 |              1 | top_5                 | Southwest Atlanta Christian Academy       | High School         | PF-C       |
| shaun livingston     |         2004 |              4 | top_5                 | Peoria                                    | High School         | PG-SG      |
| andris biedrins      |         2004 |             11 | picks_6_14            | BK Skonto (Latvia)                        | Other Team/Club     | C          |
| robert swift         |         2004 |             12 | picks_6_14            | Bakersfield                               | High School         | nan        |
| sebastian telfair    |         2004 |             13 | picks_6_14            | Abraham Lincoln                           | High School         | nan        |
| al jefferson         |         2004 |             15 | picks_15_30           | Prentiss                                  | High School         | PF-SF      |
| josh smith           |         2004 |             17 | picks_15_30           | Oak Hill Academy                          | High School         | SG-SF      |
| smith                |         2004 |             18 | picks_15_30           | Saint Benedict's Preparatory School       | High School         | SG-SF      |
| dorell wright        |         2004 |             19 | picks_15_30           | South Kent School                         | High School         | nan        |
| pavel podkolzin      |         2004 |             21 | picks_15_30           | Pallacanestro Varese (Italy)              | Other Team/Club     | nan        |
| viktor khryapa       |         2004 |             22 | picks_15_30           | PBC CSKA Moscow (Russia)                  | Other Team/Club     | nan        |
| sergei monia         |         2004 |             23 | picks_15_30           | PBC CSKA Moscow (Russia)                  | Other Team/Club     | nan        |
| sasha vujacic        |         2004 |             27 | picks_15_30           | Pallalcesto Amatori Udine (Italy)         | Other Team/Club     | nan        |
| beno udrih           |         2004 |             28 | picks_15_30           | Olimpia Milano (Italy)                    | Other Team/Club     | PG         |
| anderson varejao     |         2004 |             30 | picks_15_30           | FC Barcelona Basquet (Spain)              | Other Team/Club     | nan        |
| martell webster      |         2005 |              6 | picks_6_14            | Seattle Preparatory School                | High School         | SF         |
| andrew bynum         |         2005 |             10 | picks_6_14            | Saint Joseph                              | High School         | nan        |
| fran vazquez         |         2005 |             11 | picks_6_14            | Baloncesto Malaga (Spain)                 | Other Team/Club     | nan        |
| yaroslav korolev     |         2005 |             12 | picks_6_14            | PBC CSKA Moscow (Russia)                  | Other Team/Club     | nan        |
| gerald green         |         2005 |             18 | picks_15_30           | Gulf Shores Academy                       | High School         | SF         |
| johan petro          |         2005 |             25 | picks_15_30           | Elan Bearnais Pau-Orthez (France)         | Other Team/Club     | nan        |
| ian mahinmi          |         2005 |             28 | picks_15_30           | STB Le Havre (France)                     | Other Team/Club     | nan        |
| andrea bargnani      |         2006 |              1 | top_5                 | Universo Treviso Basket (Italy)           | Other Team/Club     | nan        |
| mouhamed sene        |         2006 |             10 | picks_6_14            | VOO Wolves Verviers-Pepinster (Belgium)   | Other Team/Club     | C          |
| thabo sefolosha      |         2006 |             13 | picks_6_14            | Pallacanestro Biella (Italy)              | Other Team/Club     | nan        |
| oleksiy pecherov     |         2006 |             18 | picks_15_30           | Paris Basket Racing (France)              | Other Team/Club     | nan        |
| sergio rodriguez     |         2006 |             27 | picks_15_30           | CB Estudiantes (Spain)                    | Other Team/Club     | nan        |
| joel freeland        |         2006 |             30 | picks_15_30           | CB Gran Canaria (Spain)                   | Other Team/Club     | nan        |
| yi jianlian          |         2007 |              6 | picks_6_14            | Guangdong Southern Tigers (China)         | Other Team/Club     | nan        |
| marco belinelli      |         2007 |             18 | picks_15_30           | Fortitudo Pallacanestro Bologna (Italy)   | Other Team/Club     | nan        |
| rudy fernandez       |         2007 |             24 | picks_15_30           | Joventut Badalona (Spain)                 | Other Team/Club     | nan        |
| tiago splitter       |         2007 |             28 | picks_15_30           | Saski Baskonia (Spain)                    | Other Team/Club     | nan        |
| petteri koponen      |         2007 |             30 | picks_15_30           | Espoon Honka (Finland)                    | Other Team/Club     | nan        |
| danilo gallinari     |         2008 |              6 | picks_6_14            | Olimpia Milano (Italy)                    | Other Team/Club     | nan        |
| alexis ajinca        |         2008 |             20 | picks_15_30           | Hyeres-Toulon Var Basket (France)         | Other Team/Club     | nan        |
| serge ibaka          |         2008 |             24 | picks_15_30           | CB L'Hospitalet (Spain)                   | Other Team/Club     | nan        |
| nicolas batum        |         2008 |             25 | picks_15_30           | Le Mans Sarthe Basket (France)            | Other Team/Club     | nan        |
| ricky rubio          |         2009 |              5 | top_5                 | Joventut Badalona (Spain)                 | Other Team/Club     | nan        |
| brandon jennings     |         2009 |             10 | picks_6_14            | Pallacanestro Virtus Roma (Italy)         | Other Team/Club     | nan        |
| victor claver        |         2009 |             22 | picks_15_30           | Valencia BC (Spain)                       | Other Team/Club     | nan        |
| omri casspi          |         2009 |             23 | picks_15_30           | Maccabi Tel Aviv B.C. (Israel)            | Other Team/Club     | SF         |
| rodrigue beaubois    |         2009 |             25 | picks_15_30           | Cholet Basket (France)                    | Other Team/Club     | PG         |
| christian eyenga     |         2009 |             30 | picks_15_30           | CB Prat (Spain)                           | Other Team/Club     | nan        |

## Unmatched College/University Examples

| name              |   draft_year |   overall_pick | draft_group_preview   | organization                            | organization_type   | position   |
|:------------------|-------------:|---------------:|:----------------------|:----------------------------------------|:--------------------|:-----------|
| ernest brown      |         2000 |             52 | second_round          | Indian Hills Community College          | College/University  | C          |
| cory hightower    |         2000 |             54 | second_round          | Indian Hills Community College          | College/University  | SG-SF      |
| kedrick brown     |         2001 |             11 | picks_6_14            | Northwest Florida State                 | College/University  | nan        |
| qyntel woods      |         2002 |             21 | picks_15_30           | Northeast Mississippi Community College | College/University  | SF-SG      |
| flip murray       |         2002 |             41 | second_round          | Shaw                                    | College/University  | SG         |
| maciej lampe      |         2003 |             30 | picks_15_30           | Madrid (ESP)                            | College/University  | nan        |
| jerome beasley    |         2003 |             33 | second_round          | North Dakota                            | College/University  | SF-PF      |
| donta smith       |         2004 |             34 | second_round          | Southeastern Illinois                   | College/University  | nan        |
| david young       |         2004 |             41 | second_round          | North Carolina Central                  | College/University  | nan        |
| ha ha             |         2004 |             46 | second_round          | Yonsei (KOR)                            | College/University  | nan        |
| sergei lishouk    |         2004 |             49 | second_round          | Miami (FL)                              | College/University  | PF-SF      |
| wesley johnson    |         2010 |              4 | top_5                 | Syracuse                                | College/University  | SF         |
| enes freedom      |         2011 |              3 | top_5                 | Kentucky                                | College/University  | PF-C       |
| trey thompkins    |         2011 |             37 | second_round          | Georgia                                 | College/University  | PF         |
| maurice harkless  |         2012 |             15 | picks_15_30           | St. John's (NY)                         | College/University  | SF         |
| tornike shengelia |         2012 |             54 | second_round          | Georgia                                 | College/University  | nan        |
| glen rice         |         2013 |             35 | second_round          | Michigan                                | College/University  | SF-SG      |
| ricky ledo        |         2013 |             43 | second_round          | Providence                              | College/University  | SG         |
| devyn marble      |         2014 |             56 | second_round          | Iowa                                    | College/University  | SG         |
| joe young         |         2015 |             43 | second_round          | Oregon                                  | College/University  | nan        |
| bam adebayo       |         2017 |             14 | picks_6_14            | Kentucky                                | College/University  | PF-C       |
| wes iwundu        |         2017 |             33 | second_round          | Kansas State                            | College/University  | SG-SF      |
| mo bamba          |         2018 |              6 | picks_6_14            | Texas                                   | College/University  | C          |
| de anthony melton |         2018 |             46 | second_round          | Southern California                     | College/University  | SG-PG      |
| svi mykhailiuk    |         2018 |             47 | second_round          | Kansas                                  | College/University  | SG-SF      |
| nic claxton       |         2019 |             31 | second_round          | Georgia                                 | College/University  | C          |
| dewan hernandez   |         2019 |             59 | second_round          | Miami (FL)                              | College/University  | C          |
| jay scrubb        |         2020 |             55 | second_round          | John A. Logan                           | College/University  | SG-SF      |
| usman garuba      |         2021 |             23 | picks_15_30           | Madrid (ESP)                            | College/University  | nan        |
| bones hyland      |         2021 |             26 | picks_15_30           | Virginia Commonwealth                   | College/University  | SG         |
| cam thomas        |         2021 |             27 | picks_15_30           | Louisiana State                         | College/University  | SG         |
| shaedon sharpe    |         2022 |              7 | picks_6_14            | Kentucky                                | College/University  | SG         |
| gg jackson        |         2023 |             45 | second_round          | South Carolina                          | College/University  | PF         |
| bub carrington    |         2024 |             14 | picks_6_14            | Pittsburgh                              | College/University  | PG         |
| vj edgecombe      |         2025 |              3 | top_5                 | Baylor                                  | College/University  | PG-SG      |

## Fuzzy Name Candidates For Unmatched College/University Examples

| name              |   draft_year | organization                            |   overall_pick | best_ncaa_name_candidate   |   candidate_score | candidate_team      |
|:------------------|-------------:|:----------------------------------------|---------------:|:---------------------------|------------------:|:--------------------|
| ernest brown      |         2000 | Indian Hills Community College          |             52 | quentin richardson         |           46.6667 | DePaul              |
| cory hightower    |         2000 | Indian Hills Community College          |             54 | chris porter               |           46.1538 | Auburn              |
| kedrick brown     |         2001 | Northwest Florida State                 |             11 | damone brown               |           56      | Syracuse            |
| qyntel woods      |         2002 | Northeast Mississippi Community College |             21 | drew gooden                |           43.4783 | Kansas              |
| flip murray       |         2002 | Shaw                                    |             41 | marcus haislip             |           45.6    | Tennessee           |
| maciej lampe      |         2003 | Madrid (ESP)                            |             30 | chris kaman                |           43.4783 | Central Mich.       |
| jerome beasley    |         2003 | North Dakota                            |             33 | troy bell                  |           52.1739 | Boston College      |
| donta smith       |         2004 | Southeastern Illinois                   |             34 | delonte west               |           60.8696 | Saint Joseph's      |
| david young       |         2004 | North Carolina Central                  |             41 | david harrison             |           64      | Colorado            |
| ha ha             |         2004 | Yonsei (KOR)                            |             46 | david harrison             |           85.5    | Colorado            |
| sergei lishouk    |         2004 | Miami (FL)                              |             49 | kirk snyder                |           45.6    | Nevada              |
| wesley johnson    |         2010 | Syracuse                                |              4 | wes johnson                |           88      | Syracuse            |
| enes freedom      |         2011 | Kentucky                                |              3 | kenneth faried             |           61.5385 | Morehead St.        |
| trey thompkins    |         2011 | Georgia                                 |             37 | trey blue                  |           85.5    | Illinois St.        |
| maurice harkless  |         2012 | St. John's (NY)                         |             15 | moe harkless               |           78.5714 | St. John's          |
| tornike shengelia |         2012 | Georgia                                 |             54 | levan shengelia            |           71.25   | Rhode Island        |
| glen rice         |         2013 | Michigan                                |             35 | greg rice                  |           77.7778 | IUPUI               |
| ricky ledo        |         2013 | Providence                              |             43 | ledrick eackles            |           70.4118 | McNeese St.         |
| devyn marble      |         2014 | Iowa                                    |             56 | roy devyn marble           |           95      | Iowa                |
| joe young         |         2015 | Oregon                                  |             43 | joseph young               |           85.7143 | Oregon              |
| bam adebayo       |         2017 | Kentucky                                |             14 | edrice adebayo             |           73.8889 | Kentucky            |
| wes iwundu        |         2017 | Kansas State                            |             33 | wesley iwundu              |           86.9565 | Kansas St.          |
| mo bamba          |         2018 | Texas                                   |              6 | amidou bamba               |           85.5    | Coastal Carolina    |
| de anthony melton |         2018 | Southern California                     |             46 | anthony gaston             |           70.9677 | Grambling St.       |
| svi mykhailiuk    |         2018 | Kansas                                  |             47 | sviatoslav mykhailiuk      |           85.5    | Kansas              |
| nic claxton       |         2019 | Georgia                                 |             31 | nicolas claxton            |           84.6154 | Georgia             |
| dewan hernandez   |         2019 | Miami (FL)                              |             59 | nino hernandez             |           75.8621 | Bryant              |
| jay scrubb        |         2020 | John A. Logan                           |             55 | jay jay chandler           |           85.5    | Texas A&M           |
| usman garuba      |         2021 | Madrid (ESP)                            |             23 | roman garcia               |           66.6667 | Tarleton St.        |
| bones hyland      |         2021 | Virginia Commonwealth                   |             26 | rylan jones                |           74.3478 | Utah                |
| cam thomas        |         2021 | Louisiana State                         |             27 | cam ron fletcher           |           85.5    | Kentucky            |
| shaedon sharpe    |         2022 | Kentucky                                |              7 | ty harper                  |           67.5    | Louisiana Lafayette |
| gg jackson        |         2023 | South Carolina                          |             45 | chandler jackson           |           85.5    | Florida St.         |
| bub carrington    |         2024 | Pittsburgh                              |             14 | braeden carrington         |           79.1667 | Minnesota           |
| vj edgecombe      |         2025 | Baylor                                  |              3 | j edgecombe                |           95.6522 | Baylor              |

## Matched 2026 Prediction-Pool Examples

| name               |   draft_year |   overall_pick | position   | ncaa_source   | ncaa_player_raw    | ncaa_match_method   | ncaa_team         | ncaa_conf   |   ncaa_ppg |   ncaa_rpg |   ncaa_apg |   ncaa_bpm |   ncaa_usage |
|:-------------------|-------------:|---------------:|:-----------|:--------------|:-------------------|:--------------------|:------------------|:------------|-----------:|-----------:|-----------:|-----------:|-------------:|
| aaron nkrumah      |         2026 |            nan | SG         | torvik        | Aaron Nkrumah      | exact_name          | Tennessee St.     | OVC         |    17.697  |     5.4848 |     3.0303 |    3.19841 |         27.2 |
| aday mara          |         2026 |            nan | C          | torvik        | Aday Mara          | exact_name          | Michigan          | B10         |    12.1    |     6.75   |     2.425  |   14.6193  |         23.8 |
| alex karaban       |         2026 |            nan | PF         | torvik        | Alex Karaban       | exact_name          | Connecticut       | BE          |    13.175  |     5.275  |     2.35   |    8.8434  |         17.6 |
| allen graves       |         2026 |            nan | PF         | torvik        | Allen Graves       | exact_name          | Santa Clara       | WCC         |    11.7714 |     6.5143 |     1.8    |   14.2222  |         22.4 |
| amari allen        |         2026 |            nan | SF         | torvik        | Amari Allen        | exact_name          | Alabama           | SEC         |    11.4062 |     6.9375 |     3.125  |    8.85086 |         19.3 |
| andrej stojakovic  |         2026 |            nan | SF         | torvik        | Andrej Stojakovic  | exact_name          | Illinois          | B10         |    13.5    |     4.5294 |     1      |    4.21116 |         23.8 |
| baba miller        |         2026 |            nan | PF         | torvik        | Baba Miller        | exact_name          | Cincinnati        | B12         |    13.0323 |    10.3226 |     3.7097 |    9.64885 |         22.3 |
| bennett stirtz     |         2026 |            nan | PG         | torvik        | Bennett Stirtz     | exact_name          | Iowa              | B10         |    19.8378 |     2.6486 |     4.4054 |    7.35854 |         26.1 |
| billy richmond     |         2026 |            nan | SF         | torvik        | Billy Richmond III | exact_name          | Arkansas          | SEC         |    11.1622 |     4.2973 |     2      |    6.67888 |         17.9 |
| braden smith       |         2026 |            nan | PG         | torvik        | Braden Smith       | exact_name          | Purdue            | B10         |    14.2821 |     3.5385 |     8.8462 |    8.51445 |         26.5 |
| brayden burries    |         2026 |            nan | SG         | torvik        | Brayden Burries    | exact_name          | Arizona           | B12         |    16.0513 |     4.8974 |     2.4359 |   10.2047  |         21.6 |
| bruce thornton     |         2026 |            nan | PG         | torvik        | Bruce Thornton     | exact_name          | Ohio St.          | B10         |    19.9118 |     5.0882 |     3.9118 |   10.9109  |         23.2 |
| bryce hopkins      |         2026 |            nan | PF         | torvik        | Bryce Hopkins      | exact_name          | St. John's        | BE          |    13.6216 |     6.2162 |     1.9459 |    6.58104 |         22   |
| caleb wilson       |         2026 |            nan | PF         | torvik        | Caleb Wilson       | exact_name          | North Carolina    | ACC         |    19.8333 |     9.4167 |     2.6667 |   12.2009  |         28.8 |
| cameron boozer     |         2026 |            nan | PF         | torvik        | Cameron Boozer     | exact_name          | Duke              | ACC         |    22.5    |    10.2368 |     4.1316 |   16.0077  |         30.6 |
| cameron carr       |         2026 |            nan | SG         | torvik        | Cameron Carr       | exact_name          | Baylor            | B12         |    18.8824 |     5.7941 |     2.6471 |    6.0069  |         24.3 |
| christian anderson |         2026 |            nan | PG         | torvik        | Christian Anderson | exact_name          | Texas Tech        | B12         |    18.5152 |     3.5758 |     7.3939 |    8.1787  |         25.2 |
| dailyn swain       |         2026 |            nan | SF         | torvik        | Dailyn Swain       | exact_name          | Texas             | SEC         |    17.3056 |     7.5278 |     3.5833 |    9.43828 |         25.5 |
| darius acuff       |         2026 |            nan | PG         | torvik        | Darius Acuff Jr.   | exact_name          | Arkansas          | SEC         |    23.4722 |     3.0833 |     6.4444 |    6.6812  |         29.5 |
| darryn peterson    |         2026 |            nan | SG         | torvik        | Darryn Peterson    | exact_name          | Kansas            | B12         |    20.1667 |     4.2083 |     1.5833 |    7.78055 |         30.9 |
| dillon mitchell    |         2026 |            nan | PF         | torvik        | Dillon Mitchell    | exact_name          | St. John's        | BE          |     8.3243 |     7      |     3      |    9.87044 |         15.9 |
| ebuka okorie       |         2026 |            nan | PG         | torvik        | Ebuka Okorie       | exact_name          | Stanford          | ACC         |    23.1935 |     3.6452 |     3.5806 |    6.86813 |         30.1 |
| emanuel sharp      |         2026 |            nan | SG         | torvik        | Emanuel Sharp      | exact_name          | Houston           | B12         |    15.4595 |     2.973  |     1.7297 |    8.66806 |         23.2 |
| felix okpara       |         2026 |            nan | C          | torvik        | Felix Okpara       | exact_name          | Tennessee         | SEC         |     7.9714 |     6.3429 |     0.4857 |    7.38782 |         13.5 |
| flory bidunga      |         2026 |            nan | C          | torvik        | Flory Bidunga      | exact_name          | Kansas            | B12         |    13.2571 |     8.9714 |     1.4857 |   11.6163  |         19.6 |
| hannes steinbach   |         2026 |            nan | C          | torvik        | Hannes Steinbach   | exact_name          | Washington        | B10         |    18.5333 |    11.7667 |     1.5667 |    8.65431 |         24.4 |
| henri veesaar      |         2026 |            nan | C          | torvik        | Henri Veesaar      | exact_name          | North Carolina    | ACC         |    17.0323 |     8.7097 |     2.0645 |    9.6505  |         22.7 |
| isaiah evans       |         2026 |            nan | SG         | torvik        | Isaiah Evans       | exact_name          | Duke              | ACC         |    15.0263 |     3.2105 |     1.2632 |    6.54394 |         21.8 |
| izaiyah nelson     |         2026 |            nan | C          | torvik        | Izaiyah Nelson     | exact_name          | South Florida     | Amer        |    15.8824 |     9.5882 |     1.2059 |    9.20818 |         23.7 |
| ja kobi gillespie  |         2026 |            nan | PG         | torvik        | Ja'Kobi Gillespie  | exact_name          | Tennessee         | SEC         |    18.4054 |     2.8378 |     5.4324 |    8.60623 |         25.7 |
| jacob cofie        |         2026 |            nan | PF         | torvik        | Jacob Cofie        | exact_name          | USC               | B10         |     9.9375 |     6.8438 |     1.9375 |    6.32134 |         16.9 |
| jaden bradley      |         2026 |            nan | PG         | torvik        | Jaden Bradley      | exact_name          | Arizona           | B12         |    13.2821 |     3.4103 |     4.359  |    7.5798  |         21.1 |
| jaden harris       |         2026 |            nan | SF         | torvik        | Jaden Harris       | exact_name          | Kennesaw St.      | CUSA        |     7.6    |     1.8    |     0.95   |   -1.45516 |         14.7 |
| jayden quaintance  |         2026 |            nan | C          | torvik        | Jayden Quaintance  | exact_name          | Kentucky          | SEC         |     5      |     5      |     0.5    |   -1.10083 |         20.9 |
| jeremy fears       |         2026 |            nan | PG         | torvik        | Jeremy Fears Jr.   | exact_name          | Michigan St.      | B10         |    15.2286 |     2.4    |     9.3714 |    8.1909  |         27.1 |
| john blackwell     |         2026 |            nan | SG         | torvik        | John Blackwell     | exact_name          | Wisconsin         | B10         |    19.1176 |     5.0588 |     2.3235 |    6.51967 |         25.6 |
| joshua jefferson   |         2026 |            nan | PF         | torvik        | Joshua Jefferson   | exact_name          | Iowa St.          | B12         |    16.4286 |     7.4286 |     4.7714 |   11.2303  |         28.6 |
| keaton wagler      |         2026 |            nan | PG         | torvik        | Keaton Wagler      | exact_name          | Illinois          | B10         |    17.9189 |     5.0811 |     4.2432 |   11.1599  |         25.7 |
| keyshawn hall      |         2026 |            nan | SF         | torvik        | Keyshawn Hall      | exact_name          | Auburn            | SEC         |    19.2778 |     7.0556 |     2.6111 |    5.03594 |         26.5 |
| kingston flemings  |         2026 |            nan | PG         | torvik        | Kingston Flemings  | exact_name          | Houston           | B12         |    16.0541 |     4.0541 |     5.1892 |   10.3482  |         26.5 |
| koa peat           |         2026 |            nan | PF         | torvik        | Koa Peat           | exact_name          | Arizona           | B12         |    14.1111 |     5.6389 |     2.5833 |    7.99692 |         24.4 |
| kylan boswell      |         2026 |            nan | PG         | torvik        | Kylan Boswell      | exact_name          | Illinois          | B10         |    12.2667 |     4      |     3      |    7.32276 |         20.6 |
| labaron philon     |         2026 |            nan | PG         | torvik        | Labaron Philon     | exact_name          | Alabama           | SEC         |    21.9697 |     3.5455 |     5      |    8.53411 |         29.9 |
| malachi moreno     |         2026 |            nan | C          | torvik        | Malachi Moreno     | exact_name          | Kentucky          | SEC         |     7.7778 |     6.3333 |     1.7778 |    8.58588 |         18.2 |
| maliq brown        |         2026 |            nan | C          | torvik        | Maliq Brown        | exact_name          | Duke              | ACC         |     4.9474 |     5.1842 |     1.6316 |   13.8643  |         14.5 |
| meleek thomas      |         2026 |            nan | SG         | torvik        | Meleek Thomas      | exact_name          | Arkansas          | SEC         |    15.6486 |     3.8378 |     2.4865 |    5.85943 |         22.1 |
| milan momcilovic   |         2026 |            nan | PF         | torvik        | Milan Momcilovic   | exact_name          | Iowa St.          | B12         |    16.8649 |     3.1081 |     1.027  |    7.63581 |         18.1 |
| milos uzan         |         2026 |            nan | PG         | torvik        | Milos Uzan         | exact_name          | Houston           | B12         |    11.1081 |     2.6757 |     4      |    5.3955  |         19.3 |
| morez johnson      |         2026 |            nan | PF         | torvik        | Morez Johnson Jr.  | exact_name          | Michigan          | B10         |    13.1    |     7.325  |     1.2    |   11.4082  |         21.1 |
| nick martinelli    |         2026 |            nan | PF         | torvik        | Nick Martinelli    | exact_name          | Northwestern      | B10         |    23      |     6.1818 |     2      |    5.86337 |         29.4 |
| otega oweh         |         2026 |            nan | SG         | torvik        | Otega Oweh         | exact_name          | Kentucky          | SEC         |    18.6389 |     4.8056 |     2.6667 |    4.83162 |         27.1 |
| peter suder        |         2026 |            nan | SG         | torvik        | Peter Suder        | exact_name          | Miami OH          | MAC         |    14.7576 |     4.6364 |     4.0303 |    4.69792 |         23   |
| rafael castro      |         2026 |            nan | C          | torvik        | Rafael Castro      | exact_name          | George Washington | A10         |    15.2759 |     9.069  |     1.6897 |    9.46067 |         24.7 |
| richie saunders    |         2026 |            nan | SG         | torvik        | Richie Saunders    | exact_name          | BYU               | B12         |    18.04   |     5.76   |     2.08   |    8.89803 |         23.8 |
| rueben chinyelu    |         2026 |            nan | C          | torvik        | Rueben Chinyelu    | exact_name          | Florida           | SEC         |    10.9143 |    11.2286 |     0.6571 |    7.29902 |         20.1 |
| ryan conwell       |         2026 |            nan | SG         | torvik        | Ryan Conwell       | exact_name          | Louisville        | ACC         |    18.7647 |     4.7647 |     2.6765 |    5.23004 |         27.5 |
| tarris reed        |         2026 |            nan | C          | torvik        | Tarris Reed Jr.    | exact_name          | Connecticut       | BE          |    14.7143 |     8.9714 |     2.2857 |   12.9328  |         26.5 |
| tobe awaka         |         2026 |            nan | C          | torvik        | Tobe Awaka         | exact_name          | Arizona           | B12         |     9.2821 |     9.0513 |     0.7949 |    8.64578 |         21   |
| tobi lawal         |         2026 |            nan | PF         | torvik        | Tobi Lawal         | exact_name          | Virginia Tech     | ACC         |    12.2609 |     8.4783 |     0.6087 |    2.38953 |         20.2 |
| tounde yessoufou   |         2026 |            nan | SG         | torvik        | Tounde Yessoufou   | exact_name          | Baylor            | B12         |    17.7941 |     5.8529 |     1.5882 |    5.2792  |         25.4 |
| trevon brazile     |         2026 |            nan | PF         | torvik        | Trevon Brazile     | exact_name          | Arkansas          | SEC         |    13.0278 |     7.3333 |     1.5556 |    9.28023 |         17.2 |
| trey kaufman renn  |         2026 |            nan | PF         | torvik        | Trey Kaufman-Renn  | exact_name          | Purdue            | B10         |    14.1622 |     8.3243 |     2.5405 |    8.03974 |         24.9 |
| tyler bilodeau     |         2026 |            nan | PF         | torvik        | Tyler Bilodeau     | exact_name          | UCLA              | B10         |    17.6452 |     5.6129 |     1.0645 |    5.64986 |         23.7 |
| tyler nickel       |         2026 |            nan | SF         | torvik        | Tyler Nickel       | exact_name          | Vanderbilt        | SEC         |    13.5    |     3.25   |     1.1944 |    6.34431 |         16.9 |
| tyler tanner       |         2026 |            nan | PG         | torvik        | Tyler Tanner       | exact_name          | Vanderbilt        | SEC         |    19.5    |     3.6389 |     5.1111 |   10.2242  |         26.3 |
| ugonna onyenso     |         2026 |            nan | C          | torvik        | Ugonna Onyenso     | exact_name          | Virginia          | ACC         |     6.5    |     4.8889 |     0.5833 |   13.8674  |         15.1 |
| yaxel lendeborg    |         2026 |            nan | PF         | torvik        | Yaxel Lendeborg    | exact_name          | Michigan          | B10         |    15.075  |     6.775  |     3.225  |   15.4997  |         20.5 |
| zuby ejiofor       |         2026 |            nan | C          | torvik        | Zuby Ejiofor       | exact_name          | St. John's        | BE          |    16.3243 |     7.3243 |     3.5405 |   14.2722  |         26.4 |

## Unmatched 2026 Prediction-Pool Examples

| name              |   draft_year |   overall_pick | position   |   organization |   organization_type |
|:------------------|-------------:|---------------:|:-----------|---------------:|--------------------:|
| anicet dybantsa   |         2026 |            nan | SF         |            nan |                 nan |
| christopher brown |         2026 |            nan | PG         |            nan |                 nan |
| christopher cenac |         2026 |            nan | PF         |            nan |                 nan |
| jack kayil        |         2026 |            nan | PG         |            nan |                 nan |
| karim lopez       |         2026 |            nan | PF         |            nan |                 nan |
| luigi suigo       |         2026 |            nan | C          |            nan |                 nan |
| matthew able      |         2026 |            nan | SG         |            nan |                 nan |
| nathaniel ament   |         2026 |            nan | PF         |            nan |                 nan |
| nicholas boyd     |         2026 |            nan | PG         |            nan |                 nan |
| sergio de larrea  |         2026 |            nan | PG         |            nan |                 nan |
