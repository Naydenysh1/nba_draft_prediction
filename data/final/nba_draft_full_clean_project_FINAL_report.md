# Final NBA Draft Project Dataset Report

## Validation Summary

| metric                              | value   |
|:------------------------------------|:--------|
| final_rows                          | 2347    |
| final_columns                       | 51      |
| duplicate_name_draft_year_pick_rows | 0       |
| 2026_rows                           | 78      |
| 2026_missing_organization           | 0       |
| 2026_draft_age_rows                 | 78      |
| 2026_missing_draft_age              | 0       |
| technical_columns_present           | []      |
| overall_draft_age_coverage_pct      | 79.34   |
| top_5_draft_age_coverage_pct        | 100.0   |
| 2026_draft_age_coverage_pct         | 100.0   |
| ncaa_conf_non_missing               | 1849    |
| ncaa_exp_non_missing                | 1250    |
| columns_exact                       | True    |

## Final Column List

| column                         |
|:-------------------------------|
| name                           |
| draft_year                     |
| overall_pick                   |
| position                       |
| organization                   |
| organization_type              |
| draft_team_abbreviation        |
| height_wo_shoes_in             |
| height_w_shoes_in              |
| weight_lbs                     |
| wingspan_in                    |
| standing_reach_in              |
| body_fat_pct                   |
| hand_length_in                 |
| hand_width_in                  |
| standing_vertical_leap_in      |
| max_vertical_leap_in           |
| lane_agility_time_sec          |
| modified_lane_agility_time_sec |
| three_quarter_sprint_sec       |
| bench_press_reps               |
| ncaa_conf                      |
| ncaa_pos                       |
| ncaa_exp                       |
| ncaa_height                    |
| ncaa_games                     |
| ncaa_mpg                       |
| ncaa_ppg                       |
| ncaa_fg_pct                    |
| ncaa_two_pct                   |
| ncaa_three_pct                 |
| ncaa_ft_pct                    |
| ncaa_oreb                      |
| ncaa_dreb                      |
| ncaa_rpg                       |
| ncaa_apg                       |
| ncaa_ast_to                    |
| ncaa_spg                       |
| ncaa_bpg                       |
| ncaa_tpg                       |
| ncaa_ortg                      |
| ncaa_adj_oe                    |
| ncaa_drtg                      |
| ncaa_porpag                    |
| ncaa_dporpag                   |
| ncaa_bpm                       |
| ncaa_obpm                      |
| ncaa_dbpm                      |
| ncaa_usage                     |
| birth_date                     |
| draft_age                      |

## Organization Missingness

| column            |   missing_pct |   non_missing |
|:------------------|--------------:|--------------:|
| organization      |          5.16 |          2226 |
| organization_type |          5.16 |          2226 |

## Combine Missingness

| column                         |   missing_pct |   non_missing |
|:-------------------------------|--------------:|--------------:|
| height_wo_shoes_in             |         22.8  |          1812 |
| height_w_shoes_in              |         48.66 |          1205 |
| weight_lbs                     |         22.88 |          1810 |
| wingspan_in                    |         22.8  |          1812 |
| standing_reach_in              |         22.84 |          1811 |
| body_fat_pct                   |         45.63 |          1276 |
| hand_length_in                 |         54.15 |          1076 |
| hand_width_in                  |         54.15 |          1076 |
| standing_vertical_leap_in      |         31.1  |          1617 |
| max_vertical_leap_in           |         31.1  |          1617 |
| lane_agility_time_sec          |         31.36 |          1611 |
| modified_lane_agility_time_sec |         68.94 |           729 |
| three_quarter_sprint_sec       |         31.36 |          1611 |
| bench_press_reps               |         53.34 |          1095 |

## NCAA Missingness

| column         |   missing_pct |   non_missing |
|:---------------|--------------:|--------------:|
| ncaa_games     |         21.22 |          1849 |
| ncaa_mpg       |         30.12 |          1640 |
| ncaa_ppg       |         21.26 |          1848 |
| ncaa_fg_pct    |         30.08 |          1641 |
| ncaa_two_pct   |         21.22 |          1849 |
| ncaa_three_pct |         24.2  |          1779 |
| ncaa_ft_pct    |         21.26 |          1848 |
| ncaa_oreb      |         46.78 |          1249 |
| ncaa_dreb      |         46.78 |          1249 |
| ncaa_rpg       |         21.26 |          1848 |
| ncaa_apg       |         21.26 |          1848 |
| ncaa_ast_to    |         46.78 |          1249 |
| ncaa_spg       |         21.26 |          1848 |
| ncaa_bpg       |         21.26 |          1848 |
| ncaa_tpg       |         30.12 |          1640 |
| ncaa_ortg      |         46.74 |          1250 |
| ncaa_adj_oe    |         46.74 |          1250 |
| ncaa_drtg      |         46.74 |          1250 |
| ncaa_porpag    |         46.74 |          1250 |
| ncaa_dporpag   |         46.74 |          1250 |
| ncaa_bpm       |         46.74 |          1250 |
| ncaa_obpm      |         46.74 |          1250 |
| ncaa_dbpm      |         46.74 |          1250 |
| ncaa_usage     |         46.74 |          1250 |

## NCAA Text Column Missingness

| column      |   missing_pct |   non_missing |
|:------------|--------------:|--------------:|
| ncaa_conf   |         21.22 |          1849 |
| ncaa_pos    |         52.58 |          1113 |
| ncaa_exp    |         46.74 |          1250 |
| ncaa_height |         46.74 |          1250 |

## Birth Date / Draft Age Missingness

| column     |   missing_pct |   non_missing |
|:-----------|--------------:|--------------:|
| birth_date |         20.66 |          1862 |
| draft_age  |         20.66 |          1862 |

## Coverage By Draft Year

|   draft_year |   rows |   draft_age_rows |   draft_age_coverage_pct |
|-------------:|-------:|-----------------:|-------------------------:|
|         2000 |     99 |               63 |                    63.64 |
|         2001 |     96 |               63 |                    65.62 |
|         2002 |    102 |               58 |                    56.86 |
|         2003 |    106 |               64 |                    60.38 |
|         2004 |    103 |               67 |                    65.05 |
|         2005 |    107 |               77 |                    71.96 |
|         2006 |    107 |               72 |                    67.29 |
|         2007 |     98 |               59 |                    60.2  |
|         2008 |    102 |               65 |                    63.73 |
|         2009 |     66 |               53 |                    80.3  |
|         2010 |     68 |               63 |                    92.65 |
|         2011 |     71 |               57 |                    80.28 |
|         2012 |     71 |               61 |                    85.92 |
|         2013 |     78 |               61 |                    78.21 |
|         2014 |     73 |               61 |                    83.56 |
|         2015 |     80 |               60 |                    75    |
|         2016 |     78 |               68 |                    87.18 |
|         2017 |     82 |               72 |                    87.8  |
|         2018 |     85 |               73 |                    85.88 |
|         2019 |     88 |               83 |                    94.32 |
|         2020 |     78 |               77 |                    98.72 |
|         2021 |     87 |               87 |                   100    |
|         2022 |     91 |               89 |                    97.8  |
|         2023 |     83 |               82 |                    98.8  |
|         2024 |     84 |               78 |                    92.86 |
|         2025 |     86 |               71 |                    82.56 |
|         2026 |     78 |               78 |                   100    |

## Coverage By Draft Outcome Preview

| draft_group_preview     |   rows |   draft_age_rows |   draft_age_coverage_pct |
|:------------------------|-------:|-----------------:|-------------------------:|
| picks_15_30             |    416 |              413 |                    99.28 |
| picks_6_14              |    234 |              233 |                    99.57 |
| prediction_2026_unknown |     78 |               78 |                   100    |
| second_round            |    762 |              654 |                    85.83 |
| top_5                   |    130 |              130 |                   100    |
| undrafted_999           |    727 |              354 |                    48.69 |

## Youngest 30 Players

| name                  |   draft_year |   overall_pick | organization                        | birth_date   |   draft_age |
|:----------------------|-------------:|---------------:|:------------------------------------|:-------------|------------:|
| andrew bynum          |         2005 |             10 | Saint Joseph                        | 1987-10-27   |      17.67  |
| darko milicic         |         2003 |              2 | KK Vrsac (Serbia)                   | 1985-06-20   |      18.015 |
| ersan ilyasova        |         2005 |             36 | Ulkerspor (Turkey)                  | 1987-05-15   |      18.122 |
| yaroslav korolev      |         2005 |             12 | PBC CSKA Moscow (Russia)            | 1987-05-07   |      18.144 |
| amir johnson          |         2005 |             56 | Westchester                         | 1987-05-01   |      18.16  |
| cenk akyol            |         2005 |             59 | Anadolu Efes S.K. (Turkey)          | 1987-04-16   |      18.201 |
| andris biedrins       |         2004 |             11 | BK Skonto (Latvia)                  | 1986-04-02   |      18.229 |
| cj miles              |         2005 |             34 | Skyline                             | 1987-03-18   |      18.281 |
| maciej lampe          |         2003 |             30 | Madrid (ESP)                        | 1985-02-05   |      18.385 |
| pavel podkolzin       |         2003 |            999 | nan                                 | 1985-01-15   |      18.442 |
| lebron james          |         2003 |              1 | Saint Vincent-Saint Mary            | 1984-12-30   |      18.486 |
| ulrich chomche        |         2024 |             57 | APR BBC (Rwanda)                    | 2005-12-30   |      18.489 |
| sekou doumbouya       |         2019 |             15 | Limoges CSP (France)                | 2000-12-23   |      18.489 |
| cooper flagg          |         2025 |              1 | Duke                                | 2006-12-21   |      18.511 |
| gg jackson            |         2023 |             45 | South Carolina                      | 2004-12-17   |      18.511 |
| noa essengue          |         2025 |             12 | Ratiopharm Ulm (Germany)            | 2006-12-18   |      18.519 |
| dwight howard         |         2004 |              1 | Southwest Atlanta Christian Academy | 1985-12-08   |      18.543 |
| josh smith            |         2004 |             17 | Oak Hill Academy                    | 1985-12-05   |      18.552 |
| robert swift          |         2004 |             12 | Bakersfield                         | 1985-12-03   |      18.557 |
| giannis antetokounmpo |         2013 |             15 | Basket Zaragoza 2002 (Spain)        | 1994-12-06   |      18.557 |
| eddy curry            |         2001 |              4 | Thornwood                           | 1982-12-05   |      18.56  |
| dorell wright         |         2004 |             19 | South Kent School                   | 1985-12-02   |      18.56  |
| martell webster       |         2005 |              6 | Seattle Preparatory School          | 1986-12-04   |      18.565 |
| talen horton tucker   |         2019 |             46 | Iowa State                          | 2000-11-25   |      18.565 |
| leonard miller        |         2022 |            999 | nan                                 | 2003-11-26   |      18.574 |
| joshua primo          |         2021 |             12 | Alabama                             | 2002-12-24   |      18.595 |
| jalen duren           |         2022 |             13 | Memphis                             | 2003-11-18   |      18.595 |
| dragan bender         |         2016 |              4 | Maccabi Tel Aviv B.C. (Israel)      | 1997-11-17   |      18.598 |
| jontay porter         |         2018 |            999 | Missouri                            | 1999-11-15   |      18.598 |
| yannick nzosa         |         2022 |             54 | Unicaja Baloncesto Malaga (Spain)   | 2003-11-15   |      18.604 |

## Oldest 30 Players

| name             |   draft_year |   overall_pick | organization           | birth_date   |   draft_age |
|:-----------------|-------------:|---------------:|:-----------------------|:-------------|------------:|
| marcus thornton  |         2015 |             45 | William & Mary         | 1987-06-05   |      28.055 |
| bernard james    |         2012 |             33 | Florida State          | 1985-02-07   |      27.387 |
| chris massie     |         2003 |            999 | Memphis                | 1976-09-10   |      26.79  |
| horace jenkins   |         2001 |            999 | nan                    | 1974-10-14   |      26.702 |
| rafael castro    |         2026 |            nan | George Washington      | 2000-01-14   |      26.439 |
| predrag savovic  |         2002 |            999 | Hawaii                 | 1976-05-21   |      26.097 |
| michel morandais |         2004 |            999 | Colorado               | 1979-01-10   |      25.454 |
| souleymane wane  |         2001 |            999 | UConn                  | 1976-01-28   |      25.413 |
| travis hansen    |         2003 |             37 | Brigham Young          | 1978-04-15   |      25.196 |
| nicholas boyd    |         2026 |            nan | Wisconsin              | 2001-04-23   |      25.166 |
| mamadou n diaye  |         2000 |             26 | Auburn                 | 1975-06-16   |      25.035 |
| lester hudson    |         2009 |             58 | Tennessee-Martin       | 1984-08-07   |      24.882 |
| bryce hopkins    |         2026 |            nan | St. John's             | 2001-09-07   |      24.791 |
| richie saunders  |         2026 |            nan | BYU                    | 2001-09-19   |      24.758 |
| vernon macklin   |         2011 |             52 | Florida                | 1986-09-25   |      24.742 |
| tony bobbitt     |         2004 |            999 | Cincinnati             | 1979-10-22   |      24.674 |
| aaron nkrumah    |         2026 |            nan | Tennessee St.          | 2001-11-26   |      24.572 |
| joey dorsey      |         2008 |             33 | Memphis                | 1983-12-16   |      24.528 |
| stephane lasme   |         2007 |             46 | Massachusetts          | 1982-12-17   |      24.528 |
| sam merrill      |         2020 |             60 | Utah State             | 1996-05-15   |      24.512 |
| sean kilpatrick  |         2014 |            999 | Cincinnati             | 1990-01-06   |      24.468 |
| damien wilkins   |         2004 |            999 | Georgia                | 1980-01-11   |      24.452 |
| chris boucher    |         2017 |            999 | Oregon                 | 1993-01-11   |      24.444 |
| jamel artis      |         2017 |            999 | Pittsburgh             | 1993-01-12   |      24.441 |
| kadeem allen     |         2017 |             53 | Arizona                | 1993-01-15   |      24.433 |
| george king      |         2018 |             59 | Colorado               | 1994-01-15   |      24.43  |
| mark madsen      |         2000 |             29 | Stanford               | 1976-01-28   |      24.416 |
| eric dixon       |         2025 |            999 | Villanova              | 2001-01-26   |      24.411 |
| dan gadzuric     |         2002 |             33 | California-Los Angeles | 1978-02-02   |      24.394 |
| darius songaila  |         2002 |             49 | Wake Forest            | 1978-02-14   |      24.361 |

## 2026 Summary

| name               |   overall_pick | organization         | organization_type   | birth_date   |   draft_age |   ncaa_ppg |
|:-------------------|---------------:|:---------------------|:--------------------|:-------------|------------:|-----------:|
| aaron nkrumah      |            nan | Tennessee St.        | College/University  | 2001-11-26   |      24.572 |    17.697  |
| aday mara          |            nan | Michigan             | College/University  | 2005-04-07   |      21.21  |    12.1    |
| alex karaban       |            nan | Connecticut          | College/University  | 2002-11-11   |      23.614 |    13.175  |
| allen graves       |            nan | Santa Clara          | College/University  | 2006-07-28   |      19.904 |    11.7714 |
| amari allen        |            nan | Alabama              | College/University  | 2006-01-26   |      20.405 |    11.4062 |
| andrej stojakovic  |            nan | Illinois             | College/University  | 2004-08-17   |      21.848 |    13.5    |
| anicet dybantsa    |            nan | BYU                  | College/University  | 2007-01-29   |      19.398 |    25.5429 |
| baba miller        |            nan | Cincinnati           | College/University  | 2004-02-07   |      22.374 |    13.0323 |
| bennett stirtz     |            nan | Iowa                 | College/University  | 2003-10-03   |      22.721 |    19.8378 |
| billy richmond     |            nan | Arkansas             | College/University  | 2006-04-11   |      20.2   |    11.1622 |
| braden smith       |            nan | Purdue               | College/University  | 2003-07-25   |      22.913 |    14.2821 |
| brayden burries    |            nan | Arizona              | College/University  | 2005-09-18   |      20.761 |    16.0513 |
| bruce thornton     |            nan | Ohio St.             | College/University  | 2003-09-14   |      22.773 |    19.9118 |
| bryce hopkins      |            nan | St. John's           | College/University  | 2001-09-07   |      24.791 |    13.6216 |
| caleb wilson       |            nan | North Carolina       | College/University  | 2006-07-18   |      19.932 |    19.8333 |
| cameron boozer     |            nan | Duke                 | College/University  | 2007-07-18   |      18.932 |    22.5    |
| cameron carr       |            nan | Baylor               | College/University  | 2004-11-21   |      21.585 |    18.8824 |
| christian anderson |            nan | Texas Tech           | College/University  | 2006-04-02   |      20.225 |    18.5152 |
| christopher brown  |            nan | Louisville           | College/University  | 2006-04-03   |      20.222 |    18.1905 |
| christopher cenac  |            nan | Houston              | College/University  | 2007-01-31   |      19.392 |     9.5135 |
| dailyn swain       |            nan | Texas                | College/University  | 2005-07-15   |      20.939 |    17.3056 |
| darius acuff       |            nan | Arkansas             | College/University  | 2006-11-16   |      19.6   |    23.4722 |
| darryn peterson    |            nan | Kansas               | College/University  | 2007-01-17   |      19.431 |    20.1667 |
| dillon mitchell    |            nan | St. John's           | College/University  | 2003-10-03   |      22.721 |     8.3243 |
| ebuka okorie       |            nan | Stanford             | College/University  | 2007-04-10   |      19.203 |    23.1935 |
| emanuel sharp      |            nan | Houston              | College/University  | 2004-03-07   |      22.294 |    15.4595 |
| felix okpara       |            nan | Tennessee            | College/University  | 2004-04-20   |      22.174 |     7.9714 |
| flory bidunga      |            nan | Kansas               | College/University  | 2005-05-20   |      21.092 |    13.2571 |
| hannes steinbach   |            nan | Washington           | College/University  | 2006-05-01   |      20.145 |    18.5333 |
| henri veesaar      |            nan | North Carolina       | College/University  | 2004-03-28   |      22.237 |    17.0323 |
| isaiah evans       |            nan | Duke                 | College/University  | 2005-12-06   |      20.545 |    15.0263 |
| izaiyah nelson     |            nan | South Florida        | College/University  | 2003-10-01   |      22.727 |    15.8824 |
| ja kobi gillespie  |            nan | Tennessee            | College/University  | 2004-03-10   |      22.286 |    18.4054 |
| jack kayil         |            nan | Alba Berlin          | Other Team/Club     | 2006-01-27   |      20.402 |   nan      |
| jacob cofie        |            nan | USC                  | College/University  | 2006-02-07   |      20.372 |     9.9375 |
| jaden bradley      |            nan | Arizona              | College/University  | 2003-09-14   |      22.773 |    13.2821 |
| jaden harris       |            nan | Kennesaw St.         | College/University  | 2005-07-22   |      20.92  |     7.6    |
| jayden quaintance  |            nan | Kentucky             | College/University  | 2007-07-11   |      18.951 |     5      |
| jeremy fears       |            nan | Michigan St.         | College/University  | 2005-04-19   |      21.177 |    15.2286 |
| john blackwell     |            nan | Wisconsin            | College/University  | 2004-12-25   |      21.492 |    19.1176 |
| joshua jefferson   |            nan | Iowa St.             | College/University  | 2003-11-21   |      22.587 |    16.4286 |
| karim lopez        |            nan | New Zealand Breakers | Other Team/Club     | 2007-04-12   |      19.198 |   nan      |
| keaton wagler      |            nan | Illinois             | College/University  | 2007-02-03   |      19.384 |    17.9189 |
| keyshawn hall      |            nan | Auburn               | College/University  | 2003-04-09   |      23.206 |    19.2778 |
| kingston flemings  |            nan | Houston              | College/University  | 2007-01-03   |      19.469 |    16.0541 |
| koa peat           |            nan | Arizona              | College/University  | 2007-01-20   |      19.422 |    14.1111 |
| kylan boswell      |            nan | Illinois             | College/University  | 2005-04-18   |      21.18  |    12.2667 |
| labaron philon     |            nan | Alabama              | College/University  | 2005-11-24   |      20.578 |    21.9697 |
| luigi suigo        |            nan | Mega Basket (Serbia) | Other Team/Club     | 2007-01-29   |      19.398 |   nan      |
| malachi moreno     |            nan | Kentucky             | College/University  | 2006-10-24   |      19.663 |     7.7778 |
| maliq brown        |            nan | Duke                 | College/University  | 2003-11-16   |      22.601 |     4.9474 |
| matthew able       |            nan | N.C. State           | College/University  | 2006-08-11   |      19.866 |     8.8235 |
| meleek thomas      |            nan | Arkansas             | College/University  | 2006-08-06   |      19.88  |    15.6486 |
| milan momcilovic   |            nan | Iowa St.             | College/University  | 2004-09-22   |      21.749 |    16.8649 |
| milos uzan         |            nan | Houston              | College/University  | 2002-12-26   |      23.491 |    11.1081 |
| morez johnson      |            nan | Michigan             | College/University  | 2006-01-25   |      20.408 |    13.1    |
| nathaniel ament    |            nan | Tennessee            | College/University  | 2006-12-10   |      19.535 |    16.6857 |
| nicholas boyd      |            nan | Wisconsin            | College/University  | 2001-04-23   |      25.166 |    20.7429 |
| nick martinelli    |            nan | Northwestern         | College/University  | 2004-04-20   |      22.174 |    23      |
| otega oweh         |            nan | Kentucky             | College/University  | 2003-06-21   |      23.006 |    18.6389 |
| peter suder        |            nan | Miami OH             | College/University  | 2003-07-29   |      22.902 |    14.7576 |
| rafael castro      |            nan | George Washington    | College/University  | 2000-01-14   |      26.439 |    15.2759 |
| richie saunders    |            nan | BYU                  | College/University  | 2001-09-19   |      24.758 |    18.04   |
| rueben chinyelu    |            nan | Florida              | College/University  | 2003-09-30   |      22.73  |    10.9143 |
| ryan conwell       |            nan | Louisville           | College/University  | 2004-06-15   |      22.021 |    18.7647 |
| sergio de larrea   |            nan | Valencia Basket      | Other Team/Club     | 2005-12-04   |      20.55  |   nan      |
| tarris reed        |            nan | Connecticut          | College/University  | 2003-08-05   |      22.883 |    14.7143 |
| tobe awaka         |            nan | Arizona              | College/University  | 2004-01-30   |      22.396 |     9.2821 |
| tobi lawal         |            nan | Virginia Tech        | College/University  | 2003-05-01   |      23.146 |    12.2609 |
| tounde yessoufou   |            nan | Baylor               | College/University  | 2006-05-15   |      20.107 |    17.7941 |
| trevon brazile     |            nan | Arkansas             | College/University  | 2003-01-07   |      23.458 |    13.0278 |
| trey kaufman renn  |            nan | Purdue               | College/University  | 2002-08-19   |      23.844 |    14.1622 |
| tyler bilodeau     |            nan | UCLA                 | College/University  | 2004-04-17   |      22.182 |    17.6452 |
| tyler nickel       |            nan | Vanderbilt           | College/University  | 2003-09-05   |      22.798 |    13.5    |
| tyler tanner       |            nan | Vanderbilt           | College/University  | 2006-02-01   |      20.389 |    19.5    |
| ugonna onyenso     |            nan | Virginia             | College/University  | 2004-09-25   |      21.741 |     6.5    |
| yaxel lendeborg    |            nan | Michigan             | College/University  | 2002-09-30   |      23.729 |    15.075  |
| zuby ejiofor       |            nan | St. John's           | College/University  | 2004-04-20   |      22.174 |    16.3243 |

## Technical Column Absence Checks

| column                 | absent   |
|:-----------------------|:---------|
| ncaa_team              | True     |
| ncaa_source            | True     |
| ncaa_player_raw        | True     |
| ncaa_match_method      | True     |
| sportsref_url          | True     |
| sportsref_match_method | True     |
| sportsref_match_score  | True     |
| sportsref_player_raw   | True     |
| birth_date_source      | True     |
| birth_date_confidence  | True     |
| age_validation_status  | True     |
| id_source              | True     |
| draft_date             | True     |
