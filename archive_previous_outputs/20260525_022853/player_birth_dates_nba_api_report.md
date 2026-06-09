# NBA API Birth Date / Draft Age Layer Report

This is a standalone layer. The final project dataset was not modified.

## Summary

| metric                   |   value |
|:-------------------------|--------:|
| base_rows                |  2347   |
| candidate_person_id_rows |  2347   |
| unique_person_ids        |  2264   |
| birth_date_rows          |  1724   |
| birth_date_coverage_pct  |    73.5 |
| draft_age_rows           |  1724   |
| draft_age_coverage_pct   |    73.5 |

## Draft Date Audit

|   draft_year | draft_date   | draft_date_source   |
|-------------:|:-------------|:--------------------|
|         2000 | 2000-06-25   | approximate_june_25 |
|         2001 | 2001-06-25   | approximate_june_25 |
|         2002 | 2002-06-25   | approximate_june_25 |
|         2003 | 2003-06-25   | approximate_june_25 |
|         2004 | 2004-06-25   | approximate_june_25 |
|         2005 | 2005-06-25   | approximate_june_25 |
|         2006 | 2006-06-25   | approximate_june_25 |
|         2007 | 2007-06-25   | approximate_june_25 |
|         2008 | 2008-06-25   | approximate_june_25 |
|         2009 | 2009-06-25   | approximate_june_25 |
|         2010 | 2010-06-25   | approximate_june_25 |
|         2011 | 2011-06-25   | approximate_june_25 |
|         2012 | 2012-06-25   | approximate_june_25 |
|         2013 | 2013-06-25   | approximate_june_25 |
|         2014 | 2014-06-25   | approximate_june_25 |
|         2015 | 2015-06-25   | approximate_june_25 |
|         2016 | 2016-06-25   | approximate_june_25 |
|         2017 | 2017-06-25   | approximate_june_25 |
|         2018 | 2018-06-25   | approximate_june_25 |
|         2019 | 2019-06-25   | approximate_june_25 |
|         2020 | 2020-06-25   | approximate_june_25 |
|         2021 | 2021-06-25   | approximate_june_25 |
|         2022 | 2022-06-25   | approximate_june_25 |
|         2023 | 2023-06-25   | approximate_june_25 |
|         2024 | 2024-06-25   | approximate_june_25 |
|         2025 | 2025-06-25   | approximate_june_25 |
|         2026 | 2026-06-23   | fallback_manual     |

## Birth Date Coverage By draft_year

|   draft_year |   rows |   birth_dates |   missing_birth_dates |   birth_date_coverage_pct |
|-------------:|-------:|--------------:|----------------------:|--------------------------:|
|         2000 |     99 |            55 |                    44 |                      55.6 |
|         2001 |     96 |            55 |                    41 |                      57.3 |
|         2002 |    102 |            58 |                    44 |                      56.9 |
|         2003 |    106 |            58 |                    48 |                      54.7 |
|         2004 |    103 |            61 |                    42 |                      59.2 |
|         2005 |    107 |            78 |                    29 |                      72.9 |
|         2006 |    107 |            65 |                    42 |                      60.7 |
|         2007 |     98 |            58 |                    40 |                      59.2 |
|         2008 |    102 |            57 |                    45 |                      55.9 |
|         2009 |     66 |            53 |                    13 |                      80.3 |
|         2010 |     68 |            56 |                    12 |                      82.4 |
|         2011 |     71 |            54 |                    17 |                      76.1 |
|         2012 |     71 |            61 |                    10 |                      85.9 |
|         2013 |     78 |            61 |                    17 |                      78.2 |
|         2014 |     73 |            59 |                    14 |                      80.8 |
|         2015 |     80 |            56 |                    24 |                      70   |
|         2016 |     78 |            69 |                     9 |                      88.5 |
|         2017 |     82 |            73 |                     9 |                      89   |
|         2018 |     85 |            73 |                    12 |                      85.9 |
|         2019 |     88 |            84 |                     4 |                      95.5 |
|         2020 |     78 |            77 |                     1 |                      98.7 |
|         2021 |     87 |            86 |                     1 |                      98.9 |
|         2022 |     91 |            87 |                     4 |                      95.6 |
|         2023 |     83 |            80 |                     3 |                      96.4 |
|         2024 |     84 |            79 |                     5 |                      94   |
|         2025 |     86 |            71 |                    15 |                      82.6 |
|         2026 |     78 |             0 |                    78 |                       0   |

## Rows By ID Source

| id_source               |   rows |
|:------------------------|-------:|
| combine_player_id       |    805 |
| draft_history_person_id |   1542 |

## Rows By Birth Date Source

| birth_date_source                 |   rows |
|:----------------------------------|-------:|
| common_player_info_error:KeyError |    623 |
| nba_api_commonplayerinfo          |   1724 |

## Draft Age Distribution

| index   |   draft_age |
|:--------|------------:|
| count   |    1724     |
| unique  |    1153     |
| top     |      21.818 |
| freq    |       7     |

## Youngest 30 Players With Draft Age

| name                  |   draft_year |   overall_pick | birth_date   | draft_date   |   draft_age | birth_date_source        | id_source               |
|:----------------------|-------------:|---------------:|:-------------|:-------------|------------:|:-------------------------|:------------------------|
| andrew bynum          |         2005 |             10 | 1987-10-27   | 2005-06-25   |      17.662 | nba_api_commonplayerinfo | draft_history_person_id |
| darko milicic         |         2003 |              2 | 1985-06-20   | 2003-06-25   |      18.012 | nba_api_commonplayerinfo | draft_history_person_id |
| ersan ilyasova        |         2005 |             36 | 1987-05-15   | 2005-06-25   |      18.114 | nba_api_commonplayerinfo | draft_history_person_id |
| yaroslav korolev      |         2005 |             12 | 1987-05-07   | 2005-06-25   |      18.136 | nba_api_commonplayerinfo | draft_history_person_id |
| amir johnson          |         2005 |             56 | 1987-05-01   | 2005-06-25   |      18.152 | nba_api_commonplayerinfo | draft_history_person_id |
| cenk akyol            |         2005 |             59 | 1987-04-16   | 2005-06-25   |      18.193 | nba_api_commonplayerinfo | draft_history_person_id |
| andris biedrins       |         2004 |             11 | 1986-04-02   | 2004-06-25   |      18.231 | nba_api_commonplayerinfo | draft_history_person_id |
| cj miles              |         2005 |             34 | 1987-03-18   | 2005-06-25   |      18.272 | nba_api_commonplayerinfo | draft_history_person_id |
| maciej lampe          |         2003 |             30 | 1985-02-05   | 2003-06-25   |      18.382 | nba_api_commonplayerinfo | draft_history_person_id |
| pavel podkolzin       |         2003 |            999 | 1985-01-15   | 2003-06-25   |      18.439 | nba_api_commonplayerinfo | combine_player_id       |
| lebron james          |         2003 |              1 | 1984-12-30   | 2003-06-25   |      18.483 | nba_api_commonplayerinfo | draft_history_person_id |
| ulrich chomche        |         2024 |             57 | 2005-12-30   | 2024-06-25   |      18.486 | nba_api_commonplayerinfo | draft_history_person_id |
| aleksej pokusevski    |         2020 |             17 | 2001-12-26   | 2020-06-25   |      18.497 | nba_api_commonplayerinfo | draft_history_person_id |
| joshua primo          |         2021 |             12 | 2002-12-24   | 2021-06-25   |      18.502 | nba_api_commonplayerinfo | draft_history_person_id |
| sekou doumbouya       |         2019 |             15 | 2000-12-23   | 2019-06-25   |      18.502 | nba_api_commonplayerinfo | draft_history_person_id |
| cooper flagg          |         2025 |              1 | 2006-12-21   | 2025-06-25   |      18.511 | nba_api_commonplayerinfo | draft_history_person_id |
| gg jackson            |         2023 |             45 | 2004-12-17   | 2023-06-25   |      18.519 | nba_api_commonplayerinfo | draft_history_person_id |
| noa essengue          |         2025 |             12 | 2006-12-18   | 2025-06-25   |      18.519 | nba_api_commonplayerinfo | draft_history_person_id |
| dwight howard         |         2004 |              1 | 1985-12-08   | 2004-06-25   |      18.546 | nba_api_commonplayerinfo | draft_history_person_id |
| giannis antetokounmpo |         2013 |             15 | 1994-12-06   | 2013-06-25   |      18.552 | nba_api_commonplayerinfo | draft_history_person_id |
| eddy curry            |         2001 |              4 | 1982-12-05   | 2001-06-25   |      18.554 | nba_api_commonplayerinfo | draft_history_person_id |
| josh smith            |         2004 |             17 | 1985-12-05   | 2004-06-25   |      18.554 | nba_api_commonplayerinfo | draft_history_person_id |
| martell webster       |         2005 |              6 | 1986-12-04   | 2005-06-25   |      18.557 | nba_api_commonplayerinfo | draft_history_person_id |
| robert swift          |         2004 |             12 | 1985-12-03   | 2004-06-25   |      18.56  | nba_api_commonplayerinfo | draft_history_person_id |
| dorell wright         |         2004 |             19 | 1985-12-02   | 2004-06-25   |      18.563 | nba_api_commonplayerinfo | draft_history_person_id |
| talen horton tucker   |         2019 |             46 | 2000-11-25   | 2019-06-25   |      18.579 | nba_api_commonplayerinfo | draft_history_person_id |
| leonard miller        |         2022 |            999 | 2003-11-26   | 2022-06-25   |      18.579 | nba_api_commonplayerinfo | combine_player_id       |
| jalen duren           |         2022 |             13 | 2003-11-18   | 2022-06-25   |      18.601 | nba_api_commonplayerinfo | draft_history_person_id |
| dragan bender         |         2016 |              4 | 1997-11-17   | 2016-06-25   |      18.604 | nba_api_commonplayerinfo | draft_history_person_id |
| yannick nzosa         |         2022 |             54 | 2003-11-15   | 2022-06-25   |      18.609 | nba_api_commonplayerinfo | draft_history_person_id |

## Oldest 30 Players With Draft Age

| name            |   draft_year |   overall_pick | birth_date   | draft_date   |   draft_age | birth_date_source        | id_source               |
|:----------------|-------------:|---------------:|:-------------|:-------------|------------:|:-------------------------|:------------------------|
| reggie williams |         2008 |            999 | 1964-03-05   | 2008-06-25   |      44.307 | nba_api_commonplayerinfo | combine_player_id       |
| bernard james   |         2012 |             33 | 1985-02-07   | 2012-06-25   |      27.379 | nba_api_commonplayerinfo | draft_history_person_id |
| horace jenkins  |         2001 |            999 | 1974-10-14   | 2001-06-25   |      26.697 | nba_api_commonplayerinfo | combine_player_id       |
| predrag savovic |         2002 |            999 | 1976-05-21   | 2002-06-25   |      26.094 | nba_api_commonplayerinfo | combine_player_id       |
| travis hansen   |         2003 |             37 | 1978-04-15   | 2003-06-25   |      25.194 | nba_api_commonplayerinfo | draft_history_person_id |
| mamadou n diaye |         2000 |             26 | 1975-06-16   | 2000-06-25   |      25.027 | nba_api_commonplayerinfo | draft_history_person_id |
| lester hudson   |         2009 |             58 | 1984-08-07   | 2009-06-25   |      24.882 | nba_api_commonplayerinfo | draft_history_person_id |
| vernon macklin  |         2011 |             52 | 1986-09-25   | 2011-06-25   |      24.747 | nba_api_commonplayerinfo | draft_history_person_id |
| tony bobbitt    |         2004 |            999 | 1979-10-22   | 2004-06-25   |      24.676 | nba_api_commonplayerinfo | combine_player_id       |
| joey dorsey     |         2008 |             33 | 1983-12-16   | 2008-06-25   |      24.526 | nba_api_commonplayerinfo | draft_history_person_id |
| stephane lasme  |         2007 |             46 | 1982-12-17   | 2007-06-25   |      24.52  | nba_api_commonplayerinfo | draft_history_person_id |
| sean kilpatrick |         2014 |            999 | 1990-01-06   | 2014-06-25   |      24.465 | nba_api_commonplayerinfo | combine_player_id       |
| damien wilkins  |         2004 |            999 | 1980-01-11   | 2004-06-25   |      24.454 | nba_api_commonplayerinfo | combine_player_id       |
| chris boucher   |         2017 |            999 | 1993-01-11   | 2017-06-25   |      24.452 | nba_api_commonplayerinfo | combine_player_id       |
| jamel artis     |         2017 |            999 | 1993-01-12   | 2017-06-25   |      24.449 | nba_api_commonplayerinfo | combine_player_id       |
| kadeem allen    |         2017 |             53 | 1993-01-15   | 2017-06-25   |      24.441 | nba_api_commonplayerinfo | draft_history_person_id |
| george king     |         2018 |             59 | 1994-01-15   | 2018-06-25   |      24.441 | nba_api_commonplayerinfo | draft_history_person_id |
| eric dixon      |         2025 |            999 | 2001-01-26   | 2025-06-25   |      24.411 | nba_api_commonplayerinfo | combine_player_id       |
| mark madsen     |         2000 |             29 | 1976-01-28   | 2000-06-25   |      24.408 | nba_api_commonplayerinfo | draft_history_person_id |
| dan gadzuric    |         2002 |             33 | 1978-02-02   | 2002-06-25   |      24.392 | nba_api_commonplayerinfo | draft_history_person_id |
| darius songaila |         2002 |             49 | 1978-02-14   | 2002-06-25   |      24.359 | nba_api_commonplayerinfo | draft_history_person_id |
| magnum rolle    |         2010 |             51 | 1986-02-23   | 2010-06-25   |      24.334 | nba_api_commonplayerinfo | draft_history_person_id |
| antonio burks   |         2004 |             36 | 1980-02-25   | 2004-06-25   |      24.331 | nba_api_commonplayerinfo | draft_history_person_id |
| robert vaden    |         2009 |             54 | 1985-03-03   | 2009-06-25   |      24.312 | nba_api_commonplayerinfo | draft_history_person_id |
| jesse edwards   |         2024 |            999 | 2000-03-18   | 2024-06-25   |      24.271 | nba_api_commonplayerinfo | combine_player_id       |
| quinten post    |         2024 |             52 | 2000-03-21   | 2024-06-25   |      24.263 | nba_api_commonplayerinfo | draft_history_person_id |
| cam spencer     |         2024 |             53 | 2000-04-06   | 2024-06-25   |      24.219 | nba_api_commonplayerinfo | draft_history_person_id |
| mike smith      |         2000 |             35 | 1976-04-15   | 2000-06-25   |      24.194 | nba_api_commonplayerinfo | draft_history_person_id |
| john tonje      |         2025 |             53 | 2001-04-23   | 2025-06-25   |      24.172 | nba_api_commonplayerinfo | draft_history_person_id |
| bryson williams |         2022 |            999 | 1998-04-25   | 2022-06-25   |      24.167 | nba_api_commonplayerinfo | combine_player_id       |

## First 80 Missing Birth Date Examples

| name                 |   draft_year |   overall_pick | birth_date_source                 | id_source               |
|:---------------------|-------------:|---------------:|:----------------------------------|:------------------------|
| chris carrawell      |         2000 |             41 | common_player_info_error:KeyError | draft_history_person_id |
| deeandre hulett      |         2000 |             46 | common_player_info_error:KeyError | draft_history_person_id |
| josip sesar          |         2000 |             47 | common_player_info_error:KeyError | draft_history_person_id |
| mark karcher         |         2000 |             48 | common_player_info_error:KeyError | draft_history_person_id |
| cory hightower       |         2000 |             54 | common_player_info_error:KeyError | draft_history_person_id |
| jaquay walls         |         2000 |             56 | common_player_info_error:KeyError | draft_history_person_id |
| scoonie penn         |         2000 |             57 | common_player_info_error:KeyError | draft_history_person_id |
| pete mickeal         |         2000 |             58 | common_player_info_error:KeyError | draft_history_person_id |
| a j granger          |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| aubrey reese         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| bootsy thornton      |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| brandon kurtz        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| brian montonati      |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| caswell cyrus        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| ceedric goodwyn      |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| damon reed           |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| ed cota              |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| eric coley           |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| gabe muoneke         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| harold arceneaux     |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jacob jaacks         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jameel watkins       |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jarrett stephens     |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jimmie hunter        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| johnny hemsley       |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| julius doc robinson  |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| justin love          |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| karim shabazz        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| kenyon jones         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| lamont barnes        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| marcus goree         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| mario bland          |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| matt santangelo      |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| matthew nielsen      |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| michael hermon       |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| nate johnson         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| ndongo n diaye       |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| nick sheppard        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| pepe sanchez         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| reed rawlings        |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| ron hale             |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| schea cotton         |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| shaheen holloway     |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| vassil evtimov       |         2000 |            999 | common_player_info_error:KeyError | combine_player_id       |
| michael wright       |         2001 |             38 | common_player_info_error:KeyError | draft_history_person_id |
| eric chenowith       |         2001 |             42 | common_player_info_error:KeyError | draft_history_person_id |
| kyle hill            |         2001 |             43 | common_player_info_error:KeyError | draft_history_person_id |
| ousmane cisse        |         2001 |             46 | common_player_info_error:KeyError | draft_history_person_id |
| maurice jeffers      |         2001 |             54 | common_player_info_error:KeyError | draft_history_person_id |
| robertas javtokas    |         2001 |             55 | common_player_info_error:KeyError | draft_history_person_id |
| bryan bracey         |         2001 |             57 | common_player_info_error:KeyError | draft_history_person_id |
| adam allenspach      |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| anthony evans        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| benjamin eze         |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| brent wright         |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| calvin bowman        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| charles hathaway     |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| cookie belcher       |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| damone thornton      |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| darrell johns        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| darren kelly         |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| demarcus minor       |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| demetrius porter     |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| greg stevenson       |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| gyasi cline heard    |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jason gardner        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| jerry green          |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| kenny gregory        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| kimani ffriend       |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| lazaros papadopoulos |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| lee scruggs          |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| martin rancik        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| michael hicks        |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| mike mardesich       |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| nate james           |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| rashad phillips      |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| robb dryden          |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| ryan carroll         |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| sam clancy           |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |
| sirvaliant brown     |         2001 |            999 | common_player_info_error:KeyError | combine_player_id       |

## Output Columns

- name
- draft_year
- overall_pick
- birth_date
- draft_date
- draft_age
- birth_date_source
- id_source