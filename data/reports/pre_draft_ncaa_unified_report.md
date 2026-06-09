# Unified NCAA Dataset Report

## Summary

| metric                                          | value   |
|:------------------------------------------------|:--------|
| start_year                                      | 2000    |
| end_year                                        | 2026    |
| sportsref_input_rows                            | 322     |
| torvik_input_rows                               | 90022   |
| rows_before_duplicate_resolution                | 90344   |
| rows_after_duplicate_resolution                 | 90344   |
| columns                                         | 33      |
| final_columns_exact                             | True    |
| duplicate_name_draft_year_rows_after_resolution | 0       |
| overlap_name_draft_year_rows_before_resolution  | 0       |
| missing_years                                   | None    |
| extra_years                                     | None    |

## Rows By draft_year

|   draft_year |   rows |
|-------------:|-------:|
|         2000 |     44 |
|         2001 |     44 |
|         2002 |     40 |
|         2003 |     32 |
|         2004 |     34 |
|         2005 |     37 |
|         2006 |     44 |
|         2007 |     47 |
|         2008 |   4533 |
|         2009 |   4544 |
|         2010 |   4648 |
|         2011 |   4511 |
|         2012 |   4553 |
|         2013 |   4577 |
|         2014 |   4679 |
|         2015 |   4681 |
|         2016 |   4655 |
|         2017 |   4702 |
|         2018 |   4669 |
|         2019 |   4712 |
|         2020 |   4693 |
|         2021 |   4933 |
|         2022 |   4977 |
|         2023 |   5012 |
|         2024 |   4963 |
|         2025 |   5031 |
|         2026 |   4949 |

## Rows By Source

| ncaa_source      |   rows |
|:-----------------|-------:|
| sports_reference |    322 |
| torvik           |  90022 |

## Rows By draft_year And Source

|   draft_year | ncaa_source      |   rows |
|-------------:|:-----------------|-------:|
|         2000 | sports_reference |     44 |
|         2001 | sports_reference |     44 |
|         2002 | sports_reference |     40 |
|         2003 | sports_reference |     32 |
|         2004 | sports_reference |     34 |
|         2005 | sports_reference |     37 |
|         2006 | sports_reference |     44 |
|         2007 | sports_reference |     47 |
|         2008 | torvik           |   4533 |
|         2009 | torvik           |   4544 |
|         2010 | torvik           |   4648 |
|         2011 | torvik           |   4511 |
|         2012 | torvik           |   4553 |
|         2013 | torvik           |   4577 |
|         2014 | torvik           |   4679 |
|         2015 | torvik           |   4681 |
|         2016 | torvik           |   4655 |
|         2017 | torvik           |   4702 |
|         2018 | torvik           |   4669 |
|         2019 | torvik           |   4712 |
|         2020 | torvik           |   4693 |
|         2021 | torvik           |   4933 |
|         2022 | torvik           |   4977 |
|         2023 | torvik           |   5012 |
|         2024 | torvik           |   4963 |
|         2025 | torvik           |   5031 |
|         2026 | torvik           |   4949 |

## Numeric Column Checks

| column         | numeric_ok   | dtype   |
|:---------------|:-------------|:--------|
| draft_year     | True         | Int64   |
| ncaa_games     | True         | float64 |
| ncaa_mpg       | True         | float64 |
| ncaa_ppg       | True         | float64 |
| ncaa_fg_pct    | True         | float64 |
| ncaa_two_pct   | True         | float64 |
| ncaa_three_pct | True         | float64 |
| ncaa_ft_pct    | True         | float64 |
| ncaa_oreb      | True         | float64 |
| ncaa_dreb      | True         | float64 |
| ncaa_rpg       | True         | float64 |
| ncaa_apg       | True         | float64 |
| ncaa_ast_to    | True         | float64 |
| ncaa_spg       | True         | float64 |
| ncaa_bpg       | True         | float64 |
| ncaa_tpg       | True         | float64 |
| ncaa_ortg      | True         | float64 |
| ncaa_adj_oe    | True         | float64 |
| ncaa_drtg      | True         | float64 |
| ncaa_porpag    | True         | float64 |
| ncaa_dporpag   | True         | float64 |
| ncaa_bpm       | True         | float64 |
| ncaa_obpm      | True         | float64 |
| ncaa_dbpm      | True         | float64 |
| ncaa_usage     | True         | float64 |

## Missing-Value Percentage For Numeric Columns

| column         |   missing_pct |
|:---------------|--------------:|
| ncaa_tpg       |          27.7 |
| ncaa_fg_pct    |          19.5 |
| ncaa_mpg       |          16.6 |
| ncaa_ast_to    |           6.7 |
| ncaa_oreb      |           0.4 |
| ncaa_dreb      |           0.4 |
| ncaa_ortg      |           0.4 |
| ncaa_porpag    |           0.4 |
| ncaa_dporpag   |           0.4 |
| ncaa_bpm       |           0.4 |
| ncaa_obpm      |           0.4 |
| ncaa_dbpm      |           0.4 |
| ncaa_usage     |           0.4 |
| ncaa_drtg      |           0.4 |
| ncaa_adj_oe    |           0.4 |
| ncaa_games     |           0   |
| draft_year     |           0   |
| ncaa_ft_pct    |           0   |
| ncaa_three_pct |           0   |
| ncaa_two_pct   |           0   |
| ncaa_ppg       |           0   |
| ncaa_spg       |           0   |
| ncaa_bpg       |           0   |
| ncaa_rpg       |           0   |
| ncaa_apg       |           0   |

## Columns

- name
- draft_year
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

## First 30 Rows

| name               |   draft_year | ncaa_source      | ncaa_player_raw    | ncaa_team       | ncaa_conf   | ncaa_pos   | ncaa_exp   | ncaa_height   |   ncaa_games |   ncaa_mpg |   ncaa_ppg |   ncaa_fg_pct |   ncaa_two_pct |   ncaa_three_pct |   ncaa_ft_pct |   ncaa_oreb |   ncaa_dreb |   ncaa_rpg |   ncaa_apg |   ncaa_ast_to |   ncaa_spg |   ncaa_bpg |   ncaa_tpg |   ncaa_ortg |   ncaa_adj_oe |   ncaa_drtg |   ncaa_porpag |   ncaa_dporpag |   ncaa_bpm |   ncaa_obpm |   ncaa_dbpm |   ncaa_usage |
|:-------------------|-------------:|:-----------------|:-------------------|:----------------|:------------|:-----------|:-----------|:--------------|-------------:|-----------:|-----------:|--------------:|---------------:|-----------------:|--------------:|------------:|------------:|-----------:|-----------:|--------------:|-----------:|-----------:|-----------:|------------:|--------------:|------------:|--------------:|---------------:|-----------:|------------:|------------:|-------------:|
| a j guyton         |         2000 | sports_reference | a j guyton         | Indiana         | Big Ten     | <NA>       | <NA>       | <NA>          |           29 |       34.3 |       19.7 |         0.459 |          0.485 |            0.419 |         0.789 |         nan |         nan |        3.1 |        2.3 |           nan |        1   |        0.4 |        2.4 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| brian cardinal     |         2000 | sports_reference | brian cardinal     | Purdue          | Big Ten     | <NA>       | <NA>       | <NA>          |           32 |       29.5 |       13.9 |         0.411 |          0.455 |            0.339 |         0.769 |         nan |         nan |        6.3 |        2.2 |           nan |        2   |        0.3 |        2.3 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| chris carrawell    |         2000 | sports_reference | chris carrawell    | Duke            | ACC         | <NA>       | <NA>       | <NA>          |           34 |       35.6 |       16.9 |         0.486 |          0.51  |            0.377 |         0.778 |         nan |         nan |        6.1 |        3.2 |           nan |        1   |        1.1 |        2   |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| chris mihm         |         2000 | sports_reference | chris mihm         | Texas           | Big 12      | <NA>       | <NA>       | <NA>          |           33 |       30.7 |       17.7 |         0.523 |          0.525 |            0.467 |         0.707 |         nan |         nan |       10.5 |        0.7 |           nan |        0.3 |        2.7 |        2.5 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| chris porter       |         2000 | sports_reference | chris porter       | Auburn          | SEC         | <NA>       | <NA>       | <NA>          |           26 |       29   |       14.6 |         0.464 |          0.477 |            0.235 |         0.676 |         nan |         nan |        7.3 |        1.2 |           nan |        2   |        0.3 |        2.1 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| courtney alexander |         2000 | sports_reference | courtney alexander | Fresno St.      | WAC         | <NA>       | <NA>       | <NA>          |           27 |       36.1 |       24.8 |         0.447 |          0.499 |            0.331 |         0.781 |         nan |         nan |        4.7 |        3.5 |           nan |        1.4 |        0.1 |        2.5 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| dan langhi         |         2000 | sports_reference | dan langhi         | Vanderbilt      | SEC         | <NA>       | <NA>       | <NA>          |           30 |       34.4 |       22.1 |         0.477 |          0.511 |            0.403 |         0.871 |         nan |         nan |        6   |        0.8 |           nan |        0.4 |        0.3 |        1.8 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| dan mcclintock     |         2000 | sports_reference | dan mcclintock     | Northern Ariz.  | Big Sky     | <NA>       | <NA>       | <NA>          |           31 |       24.3 |       15.6 |         0.597 |          0.597 |          nan     |         0.682 |         nan |         nan |        6.5 |        1.2 |           nan |        0.4 |        2.3 |        1.8 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| dermarr johnson    |         2000 | sports_reference | dermarr johnson    | Cincinnati      | CUSA        | <NA>       | <NA>       | <NA>          |           32 |       27.5 |       12.6 |         0.478 |          0.575 |            0.371 |         0.737 |         nan |         nan |        3.8 |        1.4 |           nan |        1   |        0.9 |        1.4 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| desmond mason      |         2000 | sports_reference | desmond mason      | Oklahoma St.    | Big 12      | <NA>       | <NA>       | <NA>          |           34 |       35.4 |       18   |         0.499 |          0.536 |            0.43  |         0.767 |         nan |         nan |        6.6 |        1.5 |           nan |        1.2 |        1   |        1.8 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| donnell harvey     |         2000 | sports_reference | donnell harvey     | Florida         | SEC         | <NA>       | <NA>       | <NA>          |           37 |       20.2 |       10.1 |         0.507 |          0.509 |            0     |         0.61  |         nan |         nan |        7   |        1   |           nan |        0.7 |        0.8 |        1.6 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| eddie house        |         2000 | sports_reference | eddie house        | Arizona St.     | Pac-10      | <NA>       | <NA>       | <NA>          |           32 |       37.2 |       23   |         0.422 |          0.449 |            0.365 |         0.835 |         nan |         nan |        5.5 |        3.5 |           nan |        2.3 |        0.1 |        2.3 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| eduardo najera     |         2000 | sports_reference | eduardo najera     | Oklahoma        | Big 12      | <NA>       | <NA>       | <NA>          |           34 |       34.2 |       18.4 |         0.455 |          0.5   |            0.22  |         0.688 |         nan |         nan |        9.2 |        2.1 |           nan |        1.7 |        0.7 |        2.4 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| erick barkley      |         2000 | sports_reference | erick barkley      | St. John's (NY) | Big East    | <NA>       | <NA>       | <NA>          |           28 |       36.9 |       16   |         0.398 |          0.454 |            0.313 |         0.664 |         nan |         nan |        3   |        4.5 |           nan |        3   |        0.3 |        2.4 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| etan thomas        |         2000 | sports_reference | etan thomas        | Syracuse        | Big East    | <NA>       | <NA>       | <NA>          |           29 |       32.4 |       13.6 |         0.602 |          0.602 |          nan     |         0.678 |         nan |         nan |        9.3 |        0.6 |           nan |        0.8 |        3.7 |        2   |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| hanno mottola      |         2000 | sports_reference | hanno mottola      | Utah            | MWC         | <NA>       | <NA>       | <NA>          |           21 |       27.6 |       17   |         0.498 |          0.549 |            0.35  |         0.827 |         nan |         nan |        4.8 |        1.7 |           nan |        0.2 |        0.6 |        3   |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jabari smith       |         2000 | sports_reference | jabari smith       | LSU             | SEC         | <NA>       | <NA>       | <NA>          |           34 |       28.5 |       12.5 |         0.553 |          0.579 |            0.371 |         0.595 |         nan |         nan |        7   |        2.2 |           nan |        0.7 |        1   |        2.6 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jake voskuhl       |         2000 | sports_reference | jake voskuhl       | UConn           | Big East    | <NA>       | <NA>       | <NA>          |           34 |       22.9 |        8.5 |         0.571 |          0.571 |          nan     |         0.683 |         nan |         nan |        6.4 |        1.1 |           nan |        0.5 |        1.4 |        1.8 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jamaal magloire    |         2000 | sports_reference | jamaal magloire    | Kentucky        | SEC         | <NA>       | <NA>       | <NA>          |           33 |       29.6 |       13.2 |         0.5   |          0.5   |          nan     |         0.685 |         nan |         nan |        9.1 |        0.5 |           nan |        0.5 |        1.7 |        2.9 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jamal crawford     |         2000 | sports_reference | jamal crawford     | Michigan        | Big Ten     | <NA>       | <NA>       | <NA>          |           17 |       33.9 |       16.6 |         0.412 |          0.468 |            0.327 |         0.784 |         nan |         nan |        2.8 |        4.5 |           nan |        1.1 |        0.9 |        3.1 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jaquay walls       |         2000 | sports_reference | jaquay walls       | Colorado        | Big 12      | <NA>       | <NA>       | <NA>          |           32 |       30.8 |       17   |         0.441 |          0.474 |            0.388 |         0.754 |         nan |         nan |        3.2 |        4.5 |           nan |        1.5 |        0.2 |        2.6 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jason collier      |         2000 | sports_reference | jason collier      | Ga Tech         | ACC         | <NA>       | <NA>       | <NA>          |           30 |       32.5 |       17   |         0.473 |          0.503 |            0.369 |         0.735 |         nan |         nan |        9.2 |        1.6 |           nan |        0.8 |        1.1 |        3.2 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jason hart         |         2000 | sports_reference | jason hart         | Syracuse        | Big East    | <NA>       | <NA>       | <NA>          |           32 |       33.8 |       11.9 |         0.411 |          0.46  |            0.33  |         0.734 |         nan |         nan |        3   |        6.5 |           nan |        1.8 |        0.1 |        3.5 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| jerome moiso       |         2000 | sports_reference | jerome moiso       | UCLA            | Pac-10      | <NA>       | <NA>       | <NA>          |           33 |       29.5 |       13   |         0.501 |          0.508 |            0.167 |         0.613 |         nan |         nan |        7.6 |        1.2 |           nan |        1.1 |        1.7 |        2.7 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| joel przybilla     |         2000 | sports_reference | joel przybilla     | Minnesota       | Big Ten     | <NA>       | <NA>       | <NA>          |           21 |       30.4 |       14.2 |         0.613 |          0.613 |          nan     |         0.495 |         nan |         nan |        8.4 |        2.4 |           nan |        0.8 |        3.9 |        3.7 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| kaniel dickens     |         2000 | sports_reference | kaniel dickens     | Idaho           | Big West    | <NA>       | <NA>       | <NA>          |           29 |       27.4 |       12.1 |         0.486 |          0.502 |            0.382 |         0.638 |         nan |         nan |        6.6 |        0.9 |           nan |        0.9 |        0.9 |        2.2 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| kenyon martin      |         2000 | sports_reference | kenyon martin      | Cincinnati      | CUSA        | <NA>       | <NA>       | <NA>          |           31 |       29.3 |       18.9 |         0.568 |          0.573 |            0.286 |         0.684 |         nan |         nan |        9.7 |        1.4 |           nan |        1.4 |        3.5 |        1.8 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| keyon dooling      |         2000 | sports_reference | keyon dooling      | Missouri        | Big 12      | <NA>       | <NA>       | <NA>          |           31 |       31.7 |       15.3 |         0.389 |          0.424 |            0.347 |         0.743 |         nan |         nan |        2.7 |        3.6 |           nan |        1.4 |        0.5 |        2.5 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| khalid el amin     |         2000 | sports_reference | khalid el amin     | UConn           | Big East    | <NA>       | <NA>       | <NA>          |           35 |       31.9 |       16   |         0.411 |          0.443 |            0.356 |         0.892 |         nan |         nan |        3.1 |        5.2 |           nan |        1.7 |        0.1 |        2.7 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
| lavor postell      |         2000 | sports_reference | lavor postell      | St. John's (NY) | Big East    | <NA>       | <NA>       | <NA>          |           33 |       35   |       14.3 |         0.428 |          0.463 |            0.294 |         0.809 |         nan |         nan |        6.9 |        1.8 |           nan |        0.9 |        0.6 |        1.5 |         nan |           nan |         nan |           nan |            nan |        nan |         nan |         nan |          nan |
