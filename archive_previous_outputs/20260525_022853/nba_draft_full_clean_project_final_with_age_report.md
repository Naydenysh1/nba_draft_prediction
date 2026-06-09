# Final Project Dataset With Draft Age Report

## Summary

| metric                              |    value |
|:------------------------------------|---------:|
| base_rows                           | 2347     |
| final_rows                          | 2347     |
| row_count_equals_base               |    1     |
| base_columns                        |   49     |
| final_columns                       |   51     |
| duplicate_name_draft_year_pick_rows |    0     |
| birth_date_rows                     | 1792     |
| birth_date_coverage_pct             |   76.4   |
| draft_age_rows                      | 1792     |
| draft_age_coverage_pct              |   76.4   |
| min_draft_age                       |   17.67  |
| max_draft_age                       |   28.055 |
| ncaa_team_absent                    |    1     |
| ncaa_match_method_absent            |    1     |
| ncaa_source_absent                  |    1     |
| ncaa_player_raw_absent              |    1     |
| sportsref_url_absent                |    1     |
| sportsref_match_method_absent       |    1     |
| sportsref_match_score_absent        |    1     |
| sportsref_player_raw_absent         |    1     |
| birth_date_source_absent            |    1     |
| birth_date_confidence_absent        |    1     |
| age_validation_status_absent        |    1     |
| id_source_absent                    |    1     |
| draft_date_absent                   |    1     |

## Base Columns

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

## Final Columns

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
- birth_date
- draft_age

## Draft Age Coverage By draft_year

|   draft_year |   rows |   draft_age_rows |   missing_draft_age |   draft_age_coverage_pct |
|-------------:|-------:|-----------------:|--------------------:|-------------------------:|
|         2000 |     99 |               63 |                  36 |                     63.6 |
|         2001 |     96 |               63 |                  33 |                     65.6 |
|         2002 |    102 |               58 |                  44 |                     56.9 |
|         2003 |    106 |               64 |                  42 |                     60.4 |
|         2004 |    103 |               67 |                  36 |                     65   |
|         2005 |    107 |               77 |                  30 |                     72   |
|         2006 |    107 |               72 |                  35 |                     67.3 |
|         2007 |     98 |               59 |                  39 |                     60.2 |
|         2008 |    102 |               65 |                  37 |                     63.7 |
|         2009 |     66 |               53 |                  13 |                     80.3 |
|         2010 |     68 |               63 |                   5 |                     92.6 |
|         2011 |     71 |               57 |                  14 |                     80.3 |
|         2012 |     71 |               61 |                  10 |                     85.9 |
|         2013 |     78 |               61 |                  17 |                     78.2 |
|         2014 |     73 |               61 |                  12 |                     83.6 |
|         2015 |     80 |               60 |                  20 |                     75   |
|         2016 |     78 |               68 |                  10 |                     87.2 |
|         2017 |     82 |               72 |                  10 |                     87.8 |
|         2018 |     85 |               73 |                  12 |                     85.9 |
|         2019 |     88 |               83 |                   5 |                     94.3 |
|         2020 |     78 |               77 |                   1 |                     98.7 |
|         2021 |     87 |               87 |                   0 |                    100   |
|         2022 |     91 |               89 |                   2 |                     97.8 |
|         2023 |     83 |               82 |                   1 |                     98.8 |
|         2024 |     84 |               78 |                   6 |                     92.9 |
|         2025 |     86 |               71 |                  15 |                     82.6 |
|         2026 |     78 |                8 |                  70 |                     10.3 |

## Draft Age Coverage By draft_group_preview

| draft_group_preview     |   rows |   draft_age_rows |   missing_draft_age |   draft_age_coverage_pct |
|:------------------------|-------:|-----------------:|--------------------:|-------------------------:|
| picks_15_30             |    416 |              413 |                   3 |                     99.3 |
| picks_6_14              |    234 |              233 |                   1 |                     99.6 |
| prediction_2026_unknown |     78 |                8 |                  70 |                     10.3 |
| second_round            |    762 |              654 |                 108 |                     85.8 |
| top_5                   |    130 |              130 |                   0 |                    100   |
| undrafted_999           |    727 |              354 |                 373 |                     48.7 |

## Youngest 30 Players

| name                  |   draft_year |   overall_pick | birth_date   |   draft_age | position   | organization                        |
|:----------------------|-------------:|---------------:|:-------------|------------:|:-----------|:------------------------------------|
| andrew bynum          |         2005 |             10 | 1987-10-27   |      17.67  | nan        | Saint Joseph                        |
| darko milicic         |         2003 |              2 | 1985-06-20   |      18.015 | PF         | KK Vrsac (Serbia)                   |
| ersan ilyasova        |         2005 |             36 | 1987-05-15   |      18.122 | SF         | Ulkerspor (Turkey)                  |
| yaroslav korolev      |         2005 |             12 | 1987-05-07   |      18.144 | nan        | PBC CSKA Moscow (Russia)            |
| amir johnson          |         2005 |             56 | 1987-05-01   |      18.16  | nan        | Westchester                         |
| cenk akyol            |         2005 |             59 | 1987-04-16   |      18.201 | nan        | Anadolu Efes S.K. (Turkey)          |
| andris biedrins       |         2004 |             11 | 1986-04-02   |      18.229 | C          | BK Skonto (Latvia)                  |
| cj miles              |         2005 |             34 | 1987-03-18   |      18.281 | nan        | Skyline                             |
| maciej lampe          |         2003 |             30 | 1985-02-05   |      18.385 | nan        | Madrid (ESP)                        |
| pavel podkolzin       |         2003 |            999 | 1985-01-15   |      18.442 | C          | nan                                 |
| lebron james          |         2003 |              1 | 1984-12-30   |      18.486 | SF-SG      | Saint Vincent-Saint Mary            |
| sekou doumbouya       |         2019 |             15 | 2000-12-23   |      18.489 | nan        | Limoges CSP (France)                |
| ulrich chomche        |         2024 |             57 | 2005-12-30   |      18.489 | C          | APR BBC (Rwanda)                    |
| gg jackson            |         2023 |             45 | 2004-12-17   |      18.511 | PF         | South Carolina                      |
| cooper flagg          |         2025 |              1 | 2006-12-21   |      18.511 | SF-PF      | Duke                                |
| noa essengue          |         2025 |             12 | 2006-12-18   |      18.519 | PF         | Ratiopharm Ulm (Germany)            |
| dwight howard         |         2004 |              1 | 1985-12-08   |      18.543 | PF-C       | Southwest Atlanta Christian Academy |
| josh smith            |         2004 |             17 | 1985-12-05   |      18.552 | SG-SF      | Oak Hill Academy                    |
| robert swift          |         2004 |             12 | 1985-12-03   |      18.557 | nan        | Bakersfield                         |
| giannis antetokounmpo |         2013 |             15 | 1994-12-06   |      18.557 | nan        | Basket Zaragoza 2002 (Spain)        |
| eddy curry            |         2001 |              4 | 1982-12-05   |      18.56  | C          | Thornwood                           |
| dorell wright         |         2004 |             19 | 1985-12-02   |      18.56  | nan        | South Kent School                   |
| talen horton tucker   |         2019 |             46 | 2000-11-25   |      18.565 | SG         | Iowa State                          |
| martell webster       |         2005 |              6 | 1986-12-04   |      18.565 | SF         | Seattle Preparatory School          |
| leonard miller        |         2022 |            999 | 2003-11-26   |      18.574 | SF         | nan                                 |
| jalen duren           |         2022 |             13 | 2003-11-18   |      18.595 | C          | Memphis                             |
| joshua primo          |         2021 |             12 | 2002-12-24   |      18.595 | SG         | Alabama                             |
| dragan bender         |         2016 |              4 | 1997-11-17   |      18.598 | nan        | Maccabi Tel Aviv B.C. (Israel)      |
| jontay porter         |         2018 |            999 | 1999-11-15   |      18.598 | C-PF       | nan                                 |
| yannick nzosa         |         2022 |             54 | 2003-11-15   |      18.604 | nan        | Unicaja Baloncesto Malaga (Spain)   |

## Oldest 30 Players

| name                |   draft_year |   overall_pick | birth_date   |   draft_age | position   | organization           |
|:--------------------|-------------:|---------------:|:-------------|------------:|:-----------|:-----------------------|
| marcus thornton     |         2015 |             45 | 1987-06-05   |      28.055 | PG-SG      | William & Mary         |
| bernard james       |         2012 |             33 | 1985-02-07   |      27.387 | PF         | Florida State          |
| chris massie        |         2003 |            999 | 1976-09-10   |      26.79  | PF-C       | Memphis                |
| horace jenkins      |         2001 |            999 | 1974-10-14   |      26.702 | PG         | nan                    |
| predrag savovic     |         2002 |            999 | 1976-05-21   |      26.097 | SG         | Hawaii                 |
| michel morandais    |         2004 |            999 | 1979-01-10   |      25.454 | SG-SF      | Colorado               |
| souleymane wane     |         2001 |            999 | 1976-01-28   |      25.413 | C          | UConn                  |
| travis hansen       |         2003 |             37 | 1978-04-15   |      25.196 | SG         | Brigham Young          |
| mamadou n diaye     |         2000 |             26 | 1975-06-16   |      25.035 | nan        | Auburn                 |
| lester hudson       |         2009 |             58 | 1984-08-07   |      24.882 | nan        | Tennessee-Martin       |
| vernon macklin      |         2011 |             52 | 1986-09-25   |      24.742 | nan        | Florida                |
| tony bobbitt        |         2004 |            999 | 1979-10-22   |      24.674 | SG         | Cincinnati             |
| stephane lasme      |         2007 |             46 | 1982-12-17   |      24.528 | PF         | Massachusetts          |
| joey dorsey         |         2008 |             33 | 1983-12-16   |      24.528 | PF-C       | Memphis                |
| sam merrill         |         2020 |             60 | 1996-05-15   |      24.512 | nan        | Utah State             |
| sean kilpatrick     |         2014 |            999 | 1990-01-06   |      24.468 | SG         | nan                    |
| damien wilkins      |         2004 |            999 | 1980-01-11   |      24.452 | SG-SF      | Georgia                |
| chris boucher       |         2017 |            999 | 1993-01-11   |      24.444 | PF         | nan                    |
| jamel artis         |         2017 |            999 | 1993-01-12   |      24.441 | SG-SF      | nan                    |
| kadeem allen        |         2017 |             53 | 1993-01-15   |      24.433 | PG         | Arizona                |
| george king         |         2018 |             59 | 1994-01-15   |      24.43  | SF-SG      | Colorado               |
| mark madsen         |         2000 |             29 | 1976-01-28   |      24.416 | PF         | Stanford               |
| eric dixon          |         2025 |            999 | 2001-01-26   |      24.411 | PF         | nan                    |
| dan gadzuric        |         2002 |             33 | 1978-02-02   |      24.394 | nan        | California-Los Angeles |
| darius songaila     |         2002 |             49 | 1978-02-14   |      24.361 | PF         | Wake Forest            |
| marco killingsworth |         2006 |            999 | 1982-02-21   |      24.348 | PF         | Indiana                |
| magnum rolle        |         2010 |             51 | 1986-02-23   |      24.331 | nan        | Louisiana Tech         |
| antonio burks       |         2004 |             36 | 1980-02-25   |      24.329 | PG         | Memphis                |
| robert vaden        |         2009 |             54 | 1985-03-03   |      24.312 | nan        | Alabama-Birmingham     |
| jesse edwards       |         2024 |            999 | 2000-03-18   |      24.274 | C          | nan                    |

## 2026 Rows Still Missing Draft Age

| name               |   draft_year |   overall_pick | position   |   organization |   organization_type |
|:-------------------|-------------:|---------------:|:-----------|---------------:|--------------------:|
| aaron nkrumah      |         2026 |            nan | SG         |            nan |                 nan |
| aday mara          |         2026 |            nan | C          |            nan |                 nan |
| alex karaban       |         2026 |            nan | PF         |            nan |                 nan |
| allen graves       |         2026 |            nan | PF         |            nan |                 nan |
| amari allen        |         2026 |            nan | SF         |            nan |                 nan |
| andrej stojakovic  |         2026 |            nan | SF         |            nan |                 nan |
| anicet dybantsa    |         2026 |            nan | SF         |            nan |                 nan |
| baba miller        |         2026 |            nan | PF         |            nan |                 nan |
| bennett stirtz     |         2026 |            nan | PG         |            nan |                 nan |
| billy richmond     |         2026 |            nan | SF         |            nan |                 nan |
| braden smith       |         2026 |            nan | PG         |            nan |                 nan |
| brayden burries    |         2026 |            nan | SG         |            nan |                 nan |
| bruce thornton     |         2026 |            nan | PG         |            nan |                 nan |
| bryce hopkins      |         2026 |            nan | PF         |            nan |                 nan |
| caleb wilson       |         2026 |            nan | PF         |            nan |                 nan |
| cameron boozer     |         2026 |            nan | PF         |            nan |                 nan |
| cameron carr       |         2026 |            nan | SG         |            nan |                 nan |
| christian anderson |         2026 |            nan | PG         |            nan |                 nan |
| christopher brown  |         2026 |            nan | PG         |            nan |                 nan |
| christopher cenac  |         2026 |            nan | PF         |            nan |                 nan |
| dailyn swain       |         2026 |            nan | SF         |            nan |                 nan |
| darius acuff       |         2026 |            nan | PG         |            nan |                 nan |
| darryn peterson    |         2026 |            nan | SG         |            nan |                 nan |
| dillon mitchell    |         2026 |            nan | PF         |            nan |                 nan |
| ebuka okorie       |         2026 |            nan | PG         |            nan |                 nan |
| emanuel sharp      |         2026 |            nan | SG         |            nan |                 nan |
| felix okpara       |         2026 |            nan | C          |            nan |                 nan |
| flory bidunga      |         2026 |            nan | C          |            nan |                 nan |
| izaiyah nelson     |         2026 |            nan | C          |            nan |                 nan |
| jaden harris       |         2026 |            nan | SF         |            nan |                 nan |
| jeremy fears       |         2026 |            nan | PG         |            nan |                 nan |
| john blackwell     |         2026 |            nan | SG         |            nan |                 nan |
| joshua jefferson   |         2026 |            nan | PF         |            nan |                 nan |
| karim lopez        |         2026 |            nan | PF         |            nan |                 nan |
| keaton wagler      |         2026 |            nan | PG         |            nan |                 nan |
| keyshawn hall      |         2026 |            nan | SF         |            nan |                 nan |
| kingston flemings  |         2026 |            nan | PG         |            nan |                 nan |
| koa peat           |         2026 |            nan | PF         |            nan |                 nan |
| kylan boswell      |         2026 |            nan | PG         |            nan |                 nan |
| labaron philon     |         2026 |            nan | PG         |            nan |                 nan |
| luigi suigo        |         2026 |            nan | C          |            nan |                 nan |
| malachi moreno     |         2026 |            nan | C          |            nan |                 nan |
| maliq brown        |         2026 |            nan | C          |            nan |                 nan |
| matthew able       |         2026 |            nan | SG         |            nan |                 nan |
| meleek thomas      |         2026 |            nan | SG         |            nan |                 nan |
| milan momcilovic   |         2026 |            nan | PF         |            nan |                 nan |
| milos uzan         |         2026 |            nan | PG         |            nan |                 nan |
| morez johnson      |         2026 |            nan | PF         |            nan |                 nan |
| nathaniel ament    |         2026 |            nan | PF         |            nan |                 nan |
| nicholas boyd      |         2026 |            nan | PG         |            nan |                 nan |
| nick martinelli    |         2026 |            nan | PF         |            nan |                 nan |
| otega oweh         |         2026 |            nan | SG         |            nan |                 nan |
| peter suder        |         2026 |            nan | SG         |            nan |                 nan |
| rafael castro      |         2026 |            nan | C          |            nan |                 nan |
| richie saunders    |         2026 |            nan | SG         |            nan |                 nan |
| rueben chinyelu    |         2026 |            nan | C          |            nan |                 nan |
| ryan conwell       |         2026 |            nan | SG         |            nan |                 nan |
| sergio de larrea   |         2026 |            nan | PG         |            nan |                 nan |
| tarris reed        |         2026 |            nan | C          |            nan |                 nan |
| tobe awaka         |         2026 |            nan | C          |            nan |                 nan |
| tobi lawal         |         2026 |            nan | PF         |            nan |                 nan |
| tounde yessoufou   |         2026 |            nan | SG         |            nan |                 nan |
| trevon brazile     |         2026 |            nan | PF         |            nan |                 nan |
| trey kaufman renn  |         2026 |            nan | PF         |            nan |                 nan |
| tyler bilodeau     |         2026 |            nan | PF         |            nan |                 nan |
| tyler nickel       |         2026 |            nan | SF         |            nan |                 nan |
| tyler tanner       |         2026 |            nan | PG         |            nan |                 nan |
| ugonna onyenso     |         2026 |            nan | C          |            nan |                 nan |
| yaxel lendeborg    |         2026 |            nan | PF         |            nan |                 nan |
| zuby ejiofor       |         2026 |            nan | C          |            nan |                 nan |

## Technical Column Absence Checks

| column                 | absent   |
|:-----------------------|:---------|
| ncaa_team              | True     |
| ncaa_match_method      | True     |
| ncaa_source            | True     |
| ncaa_player_raw        | True     |
| sportsref_url          | True     |
| sportsref_match_method | True     |
| sportsref_match_score  | True     |
| sportsref_player_raw   | True     |
| birth_date_source      | True     |
| birth_date_confidence  | True     |
| age_validation_status  | True     |
| id_source              | True     |
| draft_date             | True     |