# NCAA Torvik Sanity Check

## Summary

| metric                | value |
| --------------------- | ----- |
| rows                  | 90022 |
| columns               | 32    |
| checked_players       | 21    |
| found_checked_players | 16    |
| missing_as_expected   | 5     |
| suspicious_cases      | 0     |

## Checked Prospects

| queried_raw_name  | cleaned_name      | draft_year | found_in_ncaa_csv | expected_presence | status | match_method     |
| ----------------- | ----------------- | ---------- | ----------------- | ----------------- | ------ | ---------------- |
| zion williamson   | zion williamson   | 2019       | yes               | yes               | ok     | exact_clean_name |
| ja morant         | ja morant         | 2019       | yes               | yes               | ok     | exact_clean_name |
| rj barrett        | rj barrett        | 2019       | yes               | yes               | ok     | initials_compact |
| de andre hunter   | de andre hunter   | 2019       | yes               | yes               | ok     | exact_clean_name |
| anthony edwards   | anthony edwards   | 2020       | yes               | yes               | ok     | exact_clean_name |
| lamelo ball       | lamelo ball       | 2020       | no                | no                | ok     | not_found        |
| cade cunningham   | cade cunningham   | 2021       | yes               | yes               | ok     | exact_clean_name |
| evan mobley       | evan mobley       | 2021       | yes               | yes               | ok     | exact_clean_name |
| jalen green       | jalen green       | 2021       | no                | no                | ok     | not_found        |
| paolo banchero    | paolo banchero    | 2022       | yes               | yes               | ok     | exact_clean_name |
| chet holmgren     | chet holmgren     | 2022       | yes               | yes               | ok     | exact_clean_name |
| jabari smith      | jabari smith      | 2022       | yes               | yes               | ok     | exact_clean_name |
| victor wembanyama | victor wembanyama | 2023       | no                | no                | ok     | not_found        |
| brandon miller    | brandon miller    | 2023       | yes               | yes               | ok     | exact_clean_name |
| scoot henderson   | scoot henderson   | 2023       | no                | no                | ok     | not_found        |
| zach edey         | zach edey         | 2024       | yes               | yes               | ok     | exact_clean_name |
| reed sheppard     | reed sheppard     | 2024       | yes               | yes               | ok     | exact_clean_name |
| alexandre sarr    | alexandre sarr    | 2024       | no                | no                | ok     | not_found        |
| cooper flagg      | cooper flagg      | 2025       | yes               | yes               | ok     | exact_clean_name |
| ace bailey        | ace bailey        | 2025       | yes               | yes               | ok     | exact_clean_name |
| dylan harper      | dylan harper      | 2025       | yes               | yes               | ok     | exact_clean_name |

## Found Prospect Detail Rows

| queried_raw_name | name            | draft_year | ncaa_player_raw | ncaa_team    | ncaa_conf | ncaa_pos   | ncaa_height | ncaa_games | ncaa_mpg | ncaa_ppg | ncaa_rpg | ncaa_apg | ncaa_spg | ncaa_bpg | ncaa_fg_pct | ncaa_two_pct | ncaa_three_pct | ncaa_ft_pct | ncaa_usage | ncaa_bpm |
| ---------------- | --------------- | ---------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | -------- | -------- | -------- | -------- | -------- | -------- | ----------- | ------------ | -------------- | ----------- | ---------- | -------- |
| zion williamson  | zion williamson | 2019       | Zion Williamson | Duke         | ACC       | Wing F     | 6-7         | 33         | 29.9697  | 22.6061  | 8.8788   | 2.0606   | 2.1212   | 1.7879   | 0.716       | 0.747        | 0.338          | 0.64        | 28.2       | 18.6726  |
| ja morant        | ja morant       | 2019       | Ja Morant       | Murray St.   | OVC       | Pure PG    | 6-3         | 31         | 36.6061  | 24.4848  | 5.697    | 9.9394   | 1.7576   | 0.8182   | 0.5158      | 0.545        | 0.368          | 0.815       | 36         | 9.953    |
| rj barrett       | r j barrett     | 2019       | R.J. Barrett    | Duke         | ACC       | Wing G     | 6-7         | 38         | 35.2632  | 22.6316  | 7.5789   | 4.3158   | 0.8947   | 0.4211   | 0.4825      | 0.529        | 0.308          | 0.665       | 31.3       | 7.1766   |
| de andre hunter  | de andre hunter | 2019       | De'Andre Hunter | Virginia     | ACC       | Wing F     | 6-7         | 38         | 32.4737  | 15.2368  | 5.0789   | 1.9737   | 0.5789   | 0.5789   | 0.5424      | 0.55         | 0.438          | 0.783       | 23.5       | 9.4115   |
| anthony edwards  | anthony edwards | 2020       | Anthony Edwards | Georgia      | SEC       | Wing G     | 6-5         | 31         | 33.0312  | 19.0625  | 5.2188   | 2.8438   | 1.3438   | 0.5625   | 0.4311      | 0.502        | 0.291          | 0.77        | 28.8       | 4.9285   |
| cade cunningham  | cade cunningham | 2021       | Cade Cunningham | Oklahoma St. | B12       | Wing F     | 6-8         | 27         | 35.4074  | 20.2222  | 6.1852   | 3.4444   | 1.5926   | 0.7778   | 0.4463      | 0.463        | 0.4            | 0.846       | 28.6       | 7.4164   |
| evan mobley      | evan mobley     | 2021       | Evan Mobley     | USC          | P12       | C          | 7-0         | 33         | 33.9394  | 16.3636  | 8.6667   | 2.3939   | 0.7879   | 2.8485   | 0.6388      | 0.615        | 0.3            | 0.694       | 23.4       | 12.6405  |
| paolo banchero   | paolo banchero  | 2022       | Paolo Banchero  | Duke         | ACC       | Wing F     | 6-10        | 39         | 32.9744  | 17.2051  | 7.8205   | 3.1795   | 1.0513   | 0.9231   | 0.5135      | 0.525        | 0.338          | 0.729       | 27.2       | 7.1099   |
| chet holmgren    | chet holmgren   | 2022       | Chet Holmgren   | Gonzaga      | WCC       | PF/C       | 7-0         | 32         | 26.9062  | 14.125   | 9.9062   | 1.9062   | 0.8125   | 3.4688   | 0.6736      | 0.737        | 0.39           | 0.717       | 21.4       | 14.0964  |
| jabari smith     | jabari smith    | 2022       | Jabari Smith    | Auburn       | SEC       | Stretch 4  | 6-10        | 34         | 28.7941  | 16.9412  | 7.3824   | 1.9706   | 1.0882   | 1.0294   | 0.4467      | 0.435        | 0.422          | 0.799       | 26.2       | 10.1238  |
| brandon miller   | brandon miller  | 2023       | Brandon Miller  | Alabama      | SEC       | Stretch 4  | 6-9         | 37         | 32.6486  | 18.8108  | 8.2432   | 2.0541   | 0.8919   | 0.8649   | 0.452       | 0.483        | 0.384          | 0.859       | 25         | 10.9621  |
| zach edey        | zach edey       | 2024       | Zach Edey       | Purdue       | B10       | C          | 7-4         | 39         |          | 25.2051  | 12.1538  | 2.0256   | 0.2821   | 2.1538   |             | 0.624        | 0.5            | 0.711       | 33.4       | 13.6776  |
| reed sheppard    | reed sheppard   | 2024       | Reed Sheppard   | Kentucky     | SEC       | Scoring PG | 6-3         | 33         |          | 12.4545  | 4.1212   | 4.4545   | 2.4848   | 0.697    |             | 0.555        | 0.521          | 0.831       | 18.7       | 10.5482  |
| cooper flagg     | cooper flagg    | 2025       | Cooper Flagg    | Duke         | ACC       | Stretch 4  | 6-9         | 37         |          | 19.1622  | 7.4865   | 4.2162   | 1.4054   | 1.3514   |             | 0.517        | 0.385          | 0.84        | 30.8       | 14.1669  |
| ace bailey       | ace bailey      | 2025       | Ace Bailey      | Rutgers      | B10       | Stretch 4  | 6-10        | 30         |          | 17.5667  | 7.1667   | 1.2667   | 1        | 1.2667   |             | 0.511        | 0.346          | 0.692       | 26.2       | 3.6793   |
| dylan harper     | dylan harper    | 2025       | Dylan Harper    | Rutgers      | B10       | Combo G    | 6-6         | 29         |          | 19.4483  | 4.5862   | 4.0345   | 1.4483   | 0.5862   |             | 0.574        | 0.333          | 0.75        | 28.8       | 8.0957   |

## Duplicate name + draft_year Rows

Duplicate groups: 0

_None_

## Year Coverage

Expected years present: yes

Missing years: None

Extra years: None

## Key Columns Present

| column          | present |
| --------------- | ------- |
| name            | yes     |
| draft_year      | yes     |
| ncaa_player_raw | yes     |
| ncaa_team       | yes     |
| ncaa_conf       | yes     |
| ncaa_pos        | yes     |
| ncaa_height     | yes     |
| ncaa_games      | yes     |
| ncaa_mpg        | yes     |
| ncaa_ppg        | yes     |
| ncaa_rpg        | yes     |
| ncaa_apg        | yes     |
| ncaa_spg        | yes     |
| ncaa_bpg        | yes     |
| ncaa_fg_pct     | yes     |
| ncaa_two_pct    | yes     |
| ncaa_three_pct  | yes     |
| ncaa_ft_pct     | yes     |
| ncaa_usage      | yes     |
| ncaa_bpm        | yes     |

## Numeric Column Checks

| column         | present | numeric | non_numeric_values |
| -------------- | ------- | ------- | ------------------ |
| draft_year     | yes     | yes     |                    |
| ncaa_games     | yes     | yes     |                    |
| ncaa_mpg       | yes     | yes     |                    |
| ncaa_ppg       | yes     | yes     |                    |
| ncaa_rpg       | yes     | yes     |                    |
| ncaa_apg       | yes     | yes     |                    |
| ncaa_spg       | yes     | yes     |                    |
| ncaa_bpg       | yes     | yes     |                    |
| ncaa_fg_pct    | yes     | yes     |                    |
| ncaa_two_pct   | yes     | yes     |                    |
| ncaa_three_pct | yes     | yes     |                    |
| ncaa_ft_pct    | yes     | yes     |                    |
| ncaa_usage     | yes     | yes     |                    |
| ncaa_bpm       | yes     | yes     |                    |

## Missing-Value Percentages

| column         | missing_pct |
| -------------- | ----------- |
| ncaa_fg_pct    | 19.61       |
| ncaa_mpg       | 16.64       |
| ncaa_ppg       | 0.05        |
| ncaa_rpg       | 0.05        |
| ncaa_apg       | 0.05        |
| ncaa_bpm       | 0.04        |
| ncaa_two_pct   | 0           |
| ncaa_three_pct | 0           |
| ncaa_ft_pct    | 0           |
| ncaa_usage     | 0           |
