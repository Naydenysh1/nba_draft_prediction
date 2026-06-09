# Birth Date / Draft Age Layer v2 Report

This is a standalone layer. The final project dataset was not modified.

## Summary

| metric                   |   value |
|:-------------------------|--------:|
| base_rows                |  2347   |
| candidate_person_id_rows |  2347   |
| unique_person_ids        |  2264   |
| birth_date_rows          |  1792   |
| birth_date_coverage_pct  |    76.4 |
| draft_age_rows           |  1792   |
| draft_age_coverage_pct   |    76.4 |
| suspicious_ages_rejected |     1   |
| rejected_rows_total      |    10   |

## Draft Date Audit

|   draft_year | draft_date   | draft_date_source   |
|-------------:|:-------------|:--------------------|
|         2000 | 2000-06-28   | verified_hardcoded  |
|         2001 | 2001-06-27   | verified_hardcoded  |
|         2002 | 2002-06-26   | verified_hardcoded  |
|         2003 | 2003-06-26   | verified_hardcoded  |
|         2004 | 2004-06-24   | verified_hardcoded  |
|         2005 | 2005-06-28   | verified_hardcoded  |
|         2006 | 2006-06-28   | verified_hardcoded  |
|         2007 | 2007-06-28   | verified_hardcoded  |
|         2008 | 2008-06-26   | verified_hardcoded  |
|         2009 | 2009-06-25   | verified_hardcoded  |
|         2010 | 2010-06-24   | verified_hardcoded  |
|         2011 | 2011-06-23   | verified_hardcoded  |
|         2012 | 2012-06-28   | verified_hardcoded  |
|         2013 | 2013-06-27   | verified_hardcoded  |
|         2014 | 2014-06-26   | verified_hardcoded  |
|         2015 | 2015-06-25   | verified_hardcoded  |
|         2016 | 2016-06-23   | verified_hardcoded  |
|         2017 | 2017-06-22   | verified_hardcoded  |
|         2018 | 2018-06-21   | verified_hardcoded  |
|         2019 | 2019-06-20   | verified_hardcoded  |
|         2020 | 2020-11-18   | verified_hardcoded  |
|         2021 | 2021-07-29   | verified_hardcoded  |
|         2022 | 2022-06-23   | verified_hardcoded  |
|         2023 | 2023-06-22   | verified_hardcoded  |
|         2024 | 2024-06-26   | verified_hardcoded  |
|         2025 | 2025-06-25   | verified_hardcoded  |
|         2026 | 2026-06-23   | verified_hardcoded  |

## Coverage By draft_year

|   draft_year |   rows |   birth_dates |   missing_birth_dates |   birth_date_coverage_pct |
|-------------:|-------:|--------------:|----------------------:|--------------------------:|
|         2000 |     99 |            63 |                    36 |                      63.6 |
|         2001 |     96 |            63 |                    33 |                      65.6 |
|         2002 |    102 |            58 |                    44 |                      56.9 |
|         2003 |    106 |            64 |                    42 |                      60.4 |
|         2004 |    103 |            67 |                    36 |                      65   |
|         2005 |    107 |            77 |                    30 |                      72   |
|         2006 |    107 |            72 |                    35 |                      67.3 |
|         2007 |     98 |            59 |                    39 |                      60.2 |
|         2008 |    102 |            65 |                    37 |                      63.7 |
|         2009 |     66 |            53 |                    13 |                      80.3 |
|         2010 |     68 |            63 |                     5 |                      92.6 |
|         2011 |     71 |            57 |                    14 |                      80.3 |
|         2012 |     71 |            61 |                    10 |                      85.9 |
|         2013 |     78 |            61 |                    17 |                      78.2 |
|         2014 |     73 |            61 |                    12 |                      83.6 |
|         2015 |     80 |            60 |                    20 |                      75   |
|         2016 |     78 |            68 |                    10 |                      87.2 |
|         2017 |     82 |            72 |                    10 |                      87.8 |
|         2018 |     85 |            73 |                    12 |                      85.9 |
|         2019 |     88 |            83 |                     5 |                      94.3 |
|         2020 |     78 |            77 |                     1 |                      98.7 |
|         2021 |     87 |            87 |                     0 |                     100   |
|         2022 |     91 |            89 |                     2 |                      97.8 |
|         2023 |     83 |            82 |                     1 |                      98.8 |
|         2024 |     84 |            78 |                     6 |                      92.9 |
|         2025 |     86 |            71 |                    15 |                      82.6 |
|         2026 |     78 |             8 |                    70 |                      10.3 |

## 2026 Coverage

|   draft_year |   rows |   birth_dates |   missing_birth_dates |   birth_date_coverage_pct |
|-------------:|-------:|--------------:|----------------------:|--------------------------:|
|         2026 |     78 |             8 |                    70 |                      10.3 |

## Coverage By overall_pick Group

| draft_group             |   rows |   birth_dates |   birth_date_coverage_pct |
|:------------------------|-------:|--------------:|--------------------------:|
| picks_15_30             |    416 |           413 |                      99.3 |
| picks_6_14              |    234 |           233 |                      99.6 |
| prediction_2026_unknown |     78 |             8 |                      10.3 |
| second_round            |    762 |           654 |                      85.8 |
| top_5                   |    130 |           130 |                     100   |
| undrafted_999           |    727 |           354 |                      48.7 |

## Suspicious / Rejected Examples

| name            |   draft_year |   overall_pick |        person_id | birth_date   | draft_date   |   draft_age | birth_date_source        | display_first_last   | draft_year_api   | draft_number_api   | age_validation_status   |
|:----------------|-------------:|---------------:|-----------------:|:-------------|:-------------|------------:|:-------------------------|:---------------------|:-----------------|:-------------------|:------------------------|
| charles hayes   |         2005 |            999 | 101236           | 1983-06-11   | 2005-06-28   |      22.048 | nba_api_commonplayerinfo | Chuck Hayes          | <NA>             | <NA>               | rejected_name_mismatch  |
| reggie williams |         2008 |            999 |    199           | 1964-03-05   | 2008-06-26   |      44.309 | nba_api_commonplayerinfo | Reggie Williams      | <NA>             | <NA>               | rejected_suspicious_age |
| james mcadoo    |         2014 |            999 | 203949           | 1993-01-04   | 2014-06-26   |      21.473 | nba_api_commonplayerinfo | James Michael McAdoo | <NA>             | <NA>               | rejected_name_mismatch  |
| vince hunter    |         2015 |            999 |      1.6262e+06  | 1994-08-05   | 2015-06-25   |      20.887 | nba_api_commonplayerinfo | Vincent Hunter       | <NA>             | <NA>               | rejected_name_mismatch  |
| nigel hayes     |         2016 |            999 |      1.6285e+06  | 1994-12-16   | 2016-06-23   |      21.52  | nba_api_commonplayerinfo | Nigel Hayes-Davis    | <NA>             | <NA>               | rejected_name_mismatch  |
| nigel hayes     |         2017 |            999 |      1.6285e+06  | 1994-12-16   | 2017-06-22   |      22.516 | nba_api_commonplayerinfo | Nigel Hayes-Davis    | <NA>             | <NA>               | rejected_name_mismatch  |
| jalen hoard     |         2019 |            999 |      1.62966e+06 | 1999-03-30   | 2019-06-20   |      20.225 | nba_api_commonplayerinfo | Jaylen Hoard         | <NA>             | <NA>               | rejected_name_mismatch  |
| joshua hall     |         2020 |            999 |      1.63022e+06 | 2000-10-08   | 2020-11-18   |      20.112 | nba_api_commonplayerinfo | Josh Hall            | <NA>             | <NA>               | rejected_name_mismatch  |
| fanbo zeng      |         2022 |            999 |      1.63086e+06 | 2003-01-11   | 2022-06-23   |      19.447 | nba_api_commonplayerinfo | Zeng Zeng            | <NA>             | <NA>               | rejected_name_mismatch  |
| david jones     |         2024 |            999 |      1.64236e+06 | 2001-11-24   | 2024-06-26   |      22.587 | nba_api_commonplayerinfo | David Jones Garcia   | <NA>             | <NA>               | rejected_name_mismatch  |

## Rows By Birth Date Source

| birth_date_source                 |   rows |
|:----------------------------------|-------:|
| common_player_info_error:KeyError |    546 |
| nba_api_commonplayerinfo          |   1723 |
| wikidata_fallback                 |     78 |

## Rows By Age Validation Status

| age_validation_status   |   rows |
|:------------------------|-------:|
| missing_birth_date      |    546 |
| rejected_name_mismatch  |      8 |
| rejected_suspicious_age |      1 |
| valid_nba_api           |   1714 |
| valid_wikidata_fallback |     78 |

## Draft Age Distribution

| index   |   draft_age |
|:--------|------------:|
| count   |     1792    |
| unique  |     1165    |
| top     |       20.14 |
| freq    |        6    |

## Youngest 30 Valid Players

| name                  |   draft_year |   overall_pick | birth_date   | draft_date   |   draft_age | birth_date_source        | birth_date_confidence   | age_validation_status   | draft_group   |
|:----------------------|-------------:|---------------:|:-------------|:-------------|------------:|:-------------------------|:------------------------|:------------------------|:--------------|
| andrew bynum          |         2005 |             10 | 1987-10-27   | 2005-06-28   |      17.67  | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| darko milicic         |         2003 |              2 | 1985-06-20   | 2003-06-26   |      18.015 | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| ersan ilyasova        |         2005 |             36 | 1987-05-15   | 2005-06-28   |      18.122 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| yaroslav korolev      |         2005 |             12 | 1987-05-07   | 2005-06-28   |      18.144 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| amir johnson          |         2005 |             56 | 1987-05-01   | 2005-06-28   |      18.16  | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| cenk akyol            |         2005 |             59 | 1987-04-16   | 2005-06-28   |      18.201 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| andris biedrins       |         2004 |             11 | 1986-04-02   | 2004-06-24   |      18.229 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| cj miles              |         2005 |             34 | 1987-03-18   | 2005-06-28   |      18.281 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| maciej lampe          |         2003 |             30 | 1985-02-05   | 2003-06-26   |      18.385 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| pavel podkolzin       |         2003 |            999 | 1985-01-15   | 2003-06-26   |      18.442 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| lebron james          |         2003 |              1 | 1984-12-30   | 2003-06-26   |      18.486 | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| ulrich chomche        |         2024 |             57 | 2005-12-30   | 2024-06-26   |      18.489 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| sekou doumbouya       |         2019 |             15 | 2000-12-23   | 2019-06-20   |      18.489 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| gg jackson            |         2023 |             45 | 2004-12-17   | 2023-06-22   |      18.511 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| cooper flagg          |         2025 |              1 | 2006-12-21   | 2025-06-25   |      18.511 | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| noa essengue          |         2025 |             12 | 2006-12-18   | 2025-06-25   |      18.519 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| dwight howard         |         2004 |              1 | 1985-12-08   | 2004-06-24   |      18.543 | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| josh smith            |         2004 |             17 | 1985-12-05   | 2004-06-24   |      18.552 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| robert swift          |         2004 |             12 | 1985-12-03   | 2004-06-24   |      18.557 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| giannis antetokounmpo |         2013 |             15 | 1994-12-06   | 2013-06-27   |      18.557 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| dorell wright         |         2004 |             19 | 1985-12-02   | 2004-06-24   |      18.56  | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| eddy curry            |         2001 |              4 | 1982-12-05   | 2001-06-27   |      18.56  | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| talen horton tucker   |         2019 |             46 | 2000-11-25   | 2019-06-20   |      18.565 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| martell webster       |         2005 |              6 | 1986-12-04   | 2005-06-28   |      18.565 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| leonard miller        |         2022 |            999 | 2003-11-26   | 2022-06-23   |      18.574 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| jalen duren           |         2022 |             13 | 2003-11-18   | 2022-06-23   |      18.595 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| joshua primo          |         2021 |             12 | 2002-12-24   | 2021-07-29   |      18.595 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_6_14    |
| jontay porter         |         2018 |            999 | 1999-11-15   | 2018-06-21   |      18.598 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| dragan bender         |         2016 |              4 | 1997-11-17   | 2016-06-23   |      18.598 | nba_api_commonplayerinfo | high                    | valid_nba_api           | top_5         |
| yannick nzosa         |         2022 |             54 | 2003-11-15   | 2022-06-23   |      18.604 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |

## Oldest 30 Valid Players

| name                |   draft_year |   overall_pick | birth_date   | draft_date   |   draft_age | birth_date_source        | birth_date_confidence   | age_validation_status   | draft_group   |
|:--------------------|-------------:|---------------:|:-------------|:-------------|------------:|:-------------------------|:------------------------|:------------------------|:--------------|
| marcus thornton     |         2015 |             45 | 1987-06-05   | 2015-06-25   |      28.055 | wikidata_fallback        | medium                  | valid_wikidata_fallback | second_round  |
| bernard james       |         2012 |             33 | 1985-02-07   | 2012-06-28   |      27.387 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| chris massie        |         2003 |            999 | 1976-09-10   | 2003-06-26   |      26.79  | wikidata_fallback        | medium                  | valid_wikidata_fallback | undrafted_999 |
| horace jenkins      |         2001 |            999 | 1974-10-14   | 2001-06-27   |      26.702 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| predrag savovic     |         2002 |            999 | 1976-05-21   | 2002-06-26   |      26.097 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| michel morandais    |         2004 |            999 | 1979-01-10   | 2004-06-24   |      25.454 | wikidata_fallback        | medium                  | valid_wikidata_fallback | undrafted_999 |
| souleymane wane     |         2001 |            999 | 1976-01-28   | 2001-06-27   |      25.413 | wikidata_fallback        | medium                  | valid_wikidata_fallback | undrafted_999 |
| travis hansen       |         2003 |             37 | 1978-04-15   | 2003-06-26   |      25.196 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| mamadou n diaye     |         2000 |             26 | 1975-06-16   | 2000-06-28   |      25.035 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| lester hudson       |         2009 |             58 | 1984-08-07   | 2009-06-25   |      24.882 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| vernon macklin      |         2011 |             52 | 1986-09-25   | 2011-06-23   |      24.742 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| tony bobbitt        |         2004 |            999 | 1979-10-22   | 2004-06-24   |      24.674 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| stephane lasme      |         2007 |             46 | 1982-12-17   | 2007-06-28   |      24.528 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| joey dorsey         |         2008 |             33 | 1983-12-16   | 2008-06-26   |      24.528 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| sam merrill         |         2020 |             60 | 1996-05-15   | 2020-11-18   |      24.512 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| sean kilpatrick     |         2014 |            999 | 1990-01-06   | 2014-06-26   |      24.468 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| damien wilkins      |         2004 |            999 | 1980-01-11   | 2004-06-24   |      24.452 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| chris boucher       |         2017 |            999 | 1993-01-11   | 2017-06-22   |      24.444 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| jamel artis         |         2017 |            999 | 1993-01-12   | 2017-06-22   |      24.441 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| kadeem allen        |         2017 |             53 | 1993-01-15   | 2017-06-22   |      24.433 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| george king         |         2018 |             59 | 1994-01-15   | 2018-06-21   |      24.43  | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| mark madsen         |         2000 |             29 | 1976-01-28   | 2000-06-28   |      24.416 | nba_api_commonplayerinfo | high                    | valid_nba_api           | picks_15_30   |
| eric dixon          |         2025 |            999 | 2001-01-26   | 2025-06-25   |      24.411 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |
| dan gadzuric        |         2002 |             33 | 1978-02-02   | 2002-06-26   |      24.394 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| darius songaila     |         2002 |             49 | 1978-02-14   | 2002-06-26   |      24.361 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| marco killingsworth |         2006 |            999 | 1982-02-21   | 2006-06-28   |      24.348 | wikidata_fallback        | medium                  | valid_wikidata_fallback | undrafted_999 |
| magnum rolle        |         2010 |             51 | 1986-02-23   | 2010-06-24   |      24.331 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| antonio burks       |         2004 |             36 | 1980-02-25   | 2004-06-24   |      24.329 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| robert vaden        |         2009 |             54 | 1985-03-03   | 2009-06-25   |      24.312 | nba_api_commonplayerinfo | high                    | valid_nba_api           | second_round  |
| jesse edwards       |         2024 |            999 | 2000-03-18   | 2024-06-26   |      24.274 | nba_api_commonplayerinfo | high                    | valid_nba_api           | undrafted_999 |

## First 80 Missing Birth Date Examples

| name                 |   draft_year |   overall_pick |   birth_date | draft_date   | draft_age   | birth_date_source                 | birth_date_confidence   | age_validation_status   | draft_group   |
|:---------------------|-------------:|---------------:|-------------:|:-------------|:------------|:----------------------------------|:------------------------|:------------------------|:--------------|
| cory hightower       |         2000 |             54 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| a j granger          |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| bootsy thornton      |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| brandon kurtz        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| brian montonati      |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| caswell cyrus        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| ceedric goodwyn      |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| damon reed           |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| ed cota              |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| eric coley           |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| gabe muoneke         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| harold arceneaux     |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jacob jaacks         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jameel watkins       |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jarrett stephens     |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jimmie hunter        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| johnny hemsley       |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| julius doc robinson  |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| justin love          |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| karim shabazz        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| kenyon jones         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| lamont barnes        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| marcus goree         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| mario bland          |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| matt santangelo      |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| matthew nielsen      |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| michael hermon       |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| nate johnson         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| ndongo n diaye       |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| nick sheppard        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| pepe sanchez         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| reed rawlings        |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| ron hale             |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| schea cotton         |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| shaheen holloway     |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| vassil evtimov       |         2000 |            999 |          nan | 2000-06-28   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| michael wright       |         2001 |             38 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| eric chenowith       |         2001 |             42 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| kyle hill            |         2001 |             43 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| ousmane cisse        |         2001 |             46 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| maurice jeffers      |         2001 |             54 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| robertas javtokas    |         2001 |             55 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| bryan bracey         |         2001 |             57 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| adam allenspach      |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| anthony evans        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| benjamin eze         |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| brent wright         |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| calvin bowman        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| charles hathaway     |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| cookie belcher       |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| damone thornton      |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| darrell johns        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| darren kelly         |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| demarcus minor       |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| demetrius porter     |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| greg stevenson       |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| gyasi cline heard    |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jason gardner        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| jerry green          |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| kenny gregory        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| kimani ffriend       |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| lazaros papadopoulos |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| lee scruggs          |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| martin rancik        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| michael hicks        |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| ryan carroll         |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| tory walker          |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| troy ostler          |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| zach marbury         |         2001 |            999 |          nan | 2001-06-27   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| steve logan          |         2002 |             29 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | picks_15_30   |
| rod grizzard         |         2002 |             38 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| jason jennings       |         2002 |             42 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| sam clancy           |         2002 |             44 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| peter fehse          |         2002 |             48 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| federico kammerichs  |         2002 |             50 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| marcus taylor        |         2002 |             51 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| mladen sekularac     |         2002 |             54 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | second_round  |
| aaron mcghee         |         2002 |            999 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| andy ellis           |         2002 |            999 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |
| brian brown          |         2002 |            999 |          nan | 2002-06-26   | <NA>        | common_player_info_error:KeyError | none                    | missing_birth_date      | undrafted_999 |

## Output Columns

- name
- draft_year
- overall_pick
- birth_date
- draft_date
- draft_age
- birth_date_source
- birth_date_confidence
- age_validation_status