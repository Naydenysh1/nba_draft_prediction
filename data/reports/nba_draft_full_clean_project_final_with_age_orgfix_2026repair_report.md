# 2026 NCAA Alias / Organization Repair Report

## Summary

| metric                                  | value                                     |
|:----------------------------------------|:------------------------------------------|
| rows_before                             | 2347                                      |
| rows_after                              | 2347                                      |
| row_count_unchanged                     | True                                      |
| columns_after                           | 51                                        |
| duplicate_name_draft_year_pick_rows     | 0                                         |
| ncaa_source_file                        | data\pre_draft_ncaa_unified_2000_2026.csv |
| 2026_rows                               | 78                                        |
| 2026_missing_organization_before        | 9                                         |
| 2026_missing_organization_after         | 0                                         |
| 2026_missing_ncaa_ppg_before            | 10                                        |
| 2026_missing_ncaa_ppg_after             | 4                                         |
| 2026_has_ncaa_ppg_after                 | 74                                        |
| technical_ncaa_team_absent              | True                                      |
| technical_ncaa_source_absent            | True                                      |
| technical_ncaa_player_raw_absent        | True                                      |
| technical_ncaa_match_method_absent      | True                                      |
| technical_sportsref_url_absent          | True                                      |
| technical_sportsref_match_method_absent | True                                      |
| technical_sportsref_match_score_absent  | True                                      |
| technical_sportsref_player_raw_absent   | True                                      |
| technical_birth_date_source_absent      | True                                      |
| technical_birth_date_confidence_absent  | True                                      |
| technical_age_validation_status_absent  | True                                      |
| technical_id_source_absent              | True                                      |
| technical_draft_date_absent             | True                                      |

## NCAA Alias Repair Audit

| name              |   draft_year | alias_name   | status                 | ncaa_team   |   ncaa_ppg |   ncaa_bpm |   changed_cols_count |
|:------------------|-------------:|:-------------|:-----------------------|:------------|-----------:|-----------:|---------------------:|
| anicet dybantsa   |         2026 | aj dybantsa  | filled_from_ncaa_alias | BYU         |    25.5429 |    6.22968 |                   27 |
| christopher brown |         2026 | mikel brown  | filled_from_ncaa_alias | Louisville  |    18.1905 |    4.95751 |                   27 |
| christopher cenac |         2026 | chris cenac  | filled_from_ncaa_alias | Houston     |     9.5135 |    6.28734 |                   27 |
| nathaniel ament   |         2026 | nate ament   | filled_from_ncaa_alias | Tennessee   |    16.6857 |    6.11075 |                   27 |
| matthew able      |         2026 | matt able    | filled_from_ncaa_alias | N.C. State  |     8.8235 |    3.70858 |                   27 |
| nicholas boyd     |         2026 | nick boyd    | filled_from_ncaa_alias | Wisconsin   |    20.7429 |    7.78862 |                   27 |

## Non-NCAA Organization Repair Audit

| name             |   draft_year | organization         | organization_type   | status                            |
|:-----------------|-------------:|:---------------------|:--------------------|:----------------------------------|
| jack kayil       |         2026 | Alba Berlin          | Other Team/Club     | filled_non_ncaa_organization_only |
| karim lopez      |         2026 | New Zealand Breakers | Other Team/Club     | filled_non_ncaa_organization_only |
| luigi suigo      |         2026 | Mega Basket (Serbia) | Other Team/Club     | filled_non_ncaa_organization_only |
| sergio de larrea |         2026 | Valencia Basket      | Other Team/Club     | filled_non_ncaa_organization_only |

## Repaired / Reviewed 2026 Rows

| name              |   draft_year |   overall_pick | position   | organization         | organization_type   | ncaa_conf   | ncaa_pos   | ncaa_exp   |   ncaa_games |   ncaa_ppg |   ncaa_rpg |   ncaa_apg |   ncaa_bpm |   draft_age |
|:------------------|-------------:|---------------:|:-----------|:---------------------|:--------------------|:------------|:-----------|:-----------|-------------:|-----------:|-----------:|-----------:|-----------:|------------:|
| anicet dybantsa   |         2026 |            nan | SF         | BYU                  | College/University  | B12         | Wing F     | Fr         |           35 |    25.5429 |     6.8286 |     3.7143 |    6.22968 |     nan     |
| christopher brown |         2026 |            nan | PG         | Louisville           | College/University  | ACC         | Scoring PG | Fr         |           21 |    18.1905 |     3.3333 |     4.7143 |    4.95751 |     nan     |
| christopher cenac |         2026 |            nan | PF         | Houston              | College/University  | B12         | PF/C       | Fr         |           37 |     9.5135 |     7.8649 |     0.7297 |    6.28734 |     nan     |
| jack kayil        |         2026 |            nan | PG         | Alba Berlin          | Other Team/Club     | nan         | nan        | nan        |          nan |   nan      |   nan      |   nan      |  nan       |      20.402 |
| karim lopez       |         2026 |            nan | PF         | New Zealand Breakers | Other Team/Club     | nan         | nan        | nan        |          nan |   nan      |   nan      |   nan      |  nan       |     nan     |
| luigi suigo       |         2026 |            nan | C          | Mega Basket (Serbia) | Other Team/Club     | nan         | nan        | nan        |          nan |   nan      |   nan      |   nan      |  nan       |     nan     |
| matthew able      |         2026 |            nan | SG         | N.C. State           | College/University  | ACC         | Wing G     | Fr         |           34 |     8.8235 |     3.4412 |     0.9412 |    3.70858 |     nan     |
| nathaniel ament   |         2026 |            nan | PF         | Tennessee            | College/University  | SEC         | Wing F     | Fr         |           35 |    16.6857 |     6.3429 |     2.3429 |    6.11075 |     nan     |
| nicholas boyd     |         2026 |            nan | PG         | Wisconsin            | College/University  | B10         | Scoring PG | Sr         |           35 |    20.7429 |     3.8    |     4.2571 |    7.78862 |     nan     |
| sergio de larrea  |         2026 |            nan | PG         | Valencia Basket      | Other Team/Club     | nan         | nan        | nan        |          nan |   nan      |   nan      |   nan      |  nan       |     nan     |

## 2026 Rows Still Missing NCAA PPG

| name             |   draft_year |   overall_pick | position   | organization         | organization_type   |   ncaa_conf |   ncaa_ppg |   ncaa_bpm |   draft_age |
|:-----------------|-------------:|---------------:|:-----------|:---------------------|:--------------------|------------:|-----------:|-----------:|------------:|
| jack kayil       |         2026 |            nan | PG         | Alba Berlin          | Other Team/Club     |         nan |        nan |        nan |      20.402 |
| karim lopez      |         2026 |            nan | PF         | New Zealand Breakers | Other Team/Club     |         nan |        nan |        nan |     nan     |
| luigi suigo      |         2026 |            nan | C          | Mega Basket (Serbia) | Other Team/Club     |         nan |        nan |        nan |     nan     |
| sergio de larrea |         2026 |            nan | PG         | Valencia Basket      | Other Team/Club     |         nan |        nan |        nan |     nan     |

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