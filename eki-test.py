# #API取得テスト
# import requests

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# params = {
#     'key': api_key,
#     'viaList': '三軒茶屋:渋谷',
#     'date': '20230820',
#     'time': '0800',
#     }

# res = requests.get(api_url, params=params)
# result = res.json()
# departure_state = result['ResultSet']['Course'][0]['Route']['Line'][0]['DepartureState']['Datetime']['text']

# print(departure_state)

### ver1:ループなし

# import requests

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# # ユーザーからの入力駅
# user_input_station = input("駅名を入力してください: ")

# # グループに含まれる駅の情報
# groups = {
#     'A': ['渋谷', '三軒茶屋', '下高井戸'],
#     'B': ['中目黒', '田園調布', '目黒'],
#     'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
#     'D': ['大井町', '五反田', '蒲田'],
#     'E': ['自由が丘', '二子玉川', '溝の口'],
#     'F': ['鷺沼', '青葉台', '長津田']
# }

# from_station = user_input_station

# min_travel_time = float('inf')  # 初期値を正の無限大に設定
# min_travel_station = None  # 最短所要時間の駅
# min_travel_group = None  # 最短所要時間の駅が含まれるグループ

# # 最短所要時間の駅を特定
# for group, to_stations in groups.items():
#     # 各グループの駅を繰り返し処理
#     for to_station in to_stations:
#         # クエリパラメータ
#         params = {
#             'key': api_key,
#             'viaList': f'{from_station}:{to_station}',
#             'date': '20230818',
#             'time': '0800',
#             'searchType': 'departure',
#         }

#         # APIリクエストを送信
#         res = requests.get(api_url, params=params)
#         result = res.json()

#         travel_time = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#         if travel_time < min_travel_time:
#             min_travel_time = travel_time
#             min_travel_station = to_station
#             min_travel_group1 = group

# # 最も近い駅に対してのみルートを表示
# if min_travel_station is not None:
#     print(f"From: {from_station}, To: {min_travel_station}")
#     print(f"Travel Time: {min_travel_time} minutes")
#     print("-----")

#     # 最短所要時間の駅を含むグループを除外して、乗車時間が短い駅を検索
#     min_to_first_time = float('inf')  # firstからの最短所要時間の初期値を正の無限大に設定
#     min_to_first_station = None  # firstからの最短所要時間の駅

#     # ①1つ目のルートを探索
#     for group, to_stations in groups.items():
#         if group != min_travel_group1:
#             for to_station in to_stations:
#                 # クエリパラメータ
#                 params = {
#                     'key': api_key,
#                     'viaList': f'{min_travel_station}:{to_station}',
#                     'date': '20230818',
#                     'time': '0800',
#                     'searchType': 'departure',
#                 }

#                 # APIリクエストを送信
#                 res = requests.get(api_url, params=params)
#                 result = res.json()

#                 travel_time_to_first = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#                 if travel_time_to_first < min_to_first_time:
#                     min_to_first_time = travel_time_to_first
#                     min_to_first_station = to_station
#                     min_travel_group2 = group

#     # 最短ルートの駅からのルートを表示
#     if min_to_first_station is not None:
#         print(f"From: {min_travel_station}, To: {min_to_first_station}")
#         print(f"Travel Time: {min_to_first_time} minutes")
#         print("-----")


#     # ②最短ルートの駅を含むグループを除外して、乗車時間が短い駅を検索
#     min_to_second_time = float('inf')  # secondからの最短所要時間の初期値を正の無限大に設定
#     min_to_second_station = None  # secondからの最短所要時間の駅

#     for group, to_stations in groups.items():
#         if group != min_travel_group1 and group != min_travel_group2:  # mintravel駅とfirst駅が属するグループ以外を対象に
#             for to_station in to_stations:
#                 # クエリパラメータ
#                 params = {
#                     'key': api_key,
#                     'viaList': f'{min_to_first_station}:{to_station}',  # ここを修正
#                     'date': '20230818',
#                     'time': '0800',
#                     'searchType': 'departure',
#                 }

#                 # APIリクエストを送信
#                 res = requests.get(api_url, params=params)
#                 result = res.json()

#                 travel_time_to_second = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#                 if travel_time_to_second < min_to_second_time:
#                     min_to_second_time = travel_time_to_second
#                     min_to_second_station = to_station
#                     min_travel_group3 = group

#     # 最短ルートの駅からのルートを表示
#     if min_to_second_station is not None:
#         print(f"From: {min_to_first_station}, To: {min_to_second_station}")  # ここも修正
#         print(f"Travel Time: {min_to_second_time} minutes")
#         print("-----")


#     # ③最短ルートの駅を含むグループを除外して、乗車時間が短い駅を検索
#     min_to_third_time = float('inf')  # secondからの最短所要時間の初期値を正の無限大に設定
#     min_to_third_station = None  # secondからの最短所要時間の駅

#     for group, to_stations in groups.items():
#         if group != min_travel_group1 and group != min_travel_group2 and group != min_travel_group3:  # mintravel駅とfirst駅が属するグループ以外を対象に
#             for to_station in to_stations:
#                 # クエリパラメータ
#                 params = {
#                     'key': api_key,
#                     'viaList': f'{min_to_second_station}:{to_station}',  # ここを修正
#                     'date': '20230818',
#                     'time': '0800',
#                     'searchType': 'departure',
#                 }

#                 # APIリクエストを送信
#                 res = requests.get(api_url, params=params)
#                 result = res.json()

#                 travel_time_to_third = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#                 if travel_time_to_third < min_to_third_time:
#                     min_to_third_time = travel_time_to_third
#                     min_to_third_station = to_station
#                     min_travel_group4 = group


#     # 最短ルートの駅からのルートを表示
#     if min_to_third_station is not None:
#         print(f"From: {min_to_second_station}, To: {min_to_third_station}")  # ここも修正
#         print(f"Travel Time: {min_to_third_time} minutes")
#         print("-----")


#     #④最短ルートの駅を含むグループを除外して、乗車時間が短い駅を検索
#     min_to_fourth_time = float('inf')  # secondからの最短所要時間の初期値を正の無限大に設定
#     min_to_fourth_station = None  # secondからの最短所要時間の駅

#     for group, to_stations in groups.items():
#         if group != min_travel_group1 and group != min_travel_group2 and group != min_travel_group3 and group != min_travel_group4:  # mintravel駅とfirst駅が属するグループ以外を対象に
#             for to_station in to_stations:
#                 # クエリパラメータ
#                 params = {
#                     'key': api_key,
#                     'viaList': f'{min_to_third_station}:{to_station}',  # ここを修正
#                     'date': '20230818',
#                     'time': '0800',
#                     'searchType': 'departure',
#                 }

#                 # APIリクエストを送信
#                 res = requests.get(api_url, params=params)
#                 result = res.json()

#                 travel_time_to_fourth = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#                 if travel_time_to_fourth < min_to_fourth_time:
#                     min_to_fourth_time = travel_time_to_fourth
#                     min_to_fourth_station = to_station
#                     min_travel_group5 = group


#     # 最短ルートの駅からのルートを表示
#     if min_to_fourth_station is not None:
#         print(f"From: {min_to_third_station}, To: {min_to_fourth_station}")  # ここも修正
#         print(f"Travel Time: {min_to_fourth_time} minutes")
#         print("-----")


#     #⑤最短ルートの駅を含むグループを除外して、乗車時間が短い駅を検索
#     min_to_fifth_time = float('inf')  # secondからの最短所要時間の初期値を正の無限大に設定
#     min_to_fifth_station = None  # secondからの最短所要時間の駅

#     for group, to_stations in groups.items():
#         if group != min_travel_group1 and group != min_travel_group2 and group != min_travel_group3 and group != min_travel_group4 and group != min_travel_group5:  # mintravel駅とfirst駅が属するグループ以外を対象に
#             for to_station in to_stations:
#                 # クエリパラメータ
#                 params = {
#                     'key': api_key,
#                     'viaList': f'{min_to_fourth_station}:{to_station}',  # ここを修正
#                     'date': '20230818',
#                     'time': '0800',
#                     'searchType': 'departure',
#                 }

#                 # APIリクエストを送信
#                 res = requests.get(api_url, params=params)
#                 result = res.json()

#                 travel_time_to_fifth = float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

#                 if travel_time_to_fifth < min_to_fifth_time:
#                     min_to_fifth_time = travel_time_to_fifth
#                     min_to_fifth_station = to_station
#                     min_travel_group5 = group


#     # 最短ルートの駅からのルートを表示
#     if min_to_fifth_station is not None:
#         print(f"From: {min_to_fourth_station}, To: {min_to_fifth_station}")  # ここも修正
#         print(f"Travel Time: {min_to_fifth_time} minutes")
#         print("-----")



### ver2:ループあり（すべて上記のコードをもとにgptが添削）

# import requests

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# # ユーザーからの入力駅
# user_input_station = input("駅名を入力してください: ")

# # グループに含まれる駅の情報
# groups = {
#     'A': ['渋谷', '三軒茶屋', '下高井戸'],
#     'B': ['中目黒', '田園調布', '目黒'],
#     'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
#     'D': ['大井町', '五反田', '蒲田'],
#     'E': ['自由が丘', '二子玉川', '溝の口'],
#     'F': ['鷺沼', '青葉台', '長津田']
# }

# from_station = user_input_station

# def get_travel_time(from_station, to_station):
#     params = {
#         'key': api_key,
#         'viaList': f'{from_station}:{to_station}',
#         'date': '20230818',
#         'time': '0800',
#         'searchType': 'departure',
#     }

#     res = requests.get(api_url, params=params)
#     result = res.json()
#     return float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

# min_travel_time = float('inf')  # 初期値を正の無限大に設定
# min_travel_station = None  # 最短所要時間の駅
# min_travel_group = None  # 最短所要時間の駅が含まれるグループ

# # 最短所要時間の駅を特定
# for group, to_stations in groups.items():
#     for to_station in to_stations:
#         travel_time = get_travel_time(from_station, to_station)

#         if travel_time < min_travel_time:
#             min_travel_time = travel_time
#             min_travel_station = to_station
#             min_travel_group = group

# if min_travel_station is not None:
#     print(f"From: {from_station}, To: {min_travel_station}")
#     print(f"Travel Time: {min_travel_time} minutes")
#     print("-----")

#     excluded_groups = {min_travel_group}

#     for _ in range(len(groups) - 1):  # グループ数から1つを引いた回数だけ繰り返し
#         min_to_next_time = float('inf')
#         min_to_next_station = None
#         min_to_next_group = None

#         for group, to_stations in groups.items():
#             if group not in excluded_groups:
#                 for to_station in to_stations:
#                     travel_time_to_next = get_travel_time(min_travel_station, to_station)

#                     if travel_time_to_next < min_to_next_time:
#                         min_to_next_time = travel_time_to_next
#                         min_to_next_station = to_station
#                         min_to_next_group = group

#         if min_to_next_station is not None:
#             print(f"From: {min_travel_station}, To: {min_to_next_station}")
#             print(f"Travel Time: {min_to_next_time} minutes")
#             print("-----")

#             excluded_groups.add(min_to_next_group)
#             min_travel_station = min_to_next_station

# print("ルート検索が完了しました。")


# ver4:user_inputと同じ駅がグループにある場合は、スキップ（すべて上記のコードをもとにgptが添削）

# import requests
# from datetime import datetime

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# user_input_station = input("駅名を入力してください: ")
# from_station = user_input_station

# グループに含まれる駅の情報
# groups = {
#     'A': ['渋谷', '三軒茶屋', '下高井戸'],
#     'B': ['中目黒', '田園調布', '目黒'],
#     'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
#     'D': ['大井町', '五反田', '蒲田'],
#     'E': ['自由が丘', '二子玉川', '溝の口'],
#     'F': ['鷺沼', '青葉台', '長津田']
# }

# def get_travel_time(from_station, to_station, date, time):
#     params = {
#         'key': api_key,
#         'viaList': f'{from_station}:{to_station}',
#         'date': date,
#         'time': time,
#         'searchType': 'departure',
#     }

#     res = requests.get(api_url, params=params)
#     result = res.json()
#     return float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

# def print_route(from_station, to_station, travel_time):
#     print(f"From: {from_station}, To: {to_station}")
#     print(f"Travel Time: {travel_time} minutes")
#     print("-----")

# current_time = datetime.now()
# date = current_time.strftime('%Y%m%d')
# current_time_str = current_time.strftime('%H%M')

# user_station_group = None
# for group, stations in groups.items():
#     if from_station in stations:
#         user_station_group = group
#         break

# min_travel_time = float('inf')
# min_travel_station = None
# min_travel_group = None

# 最短所要時間の駅を特定
# for group, to_stations in groups.items():
#     if group == user_station_group:
#         continue  # ユーザーの駅が属するグループはスキップ

#     for to_station in to_stations:
#         travel_time = get_travel_time(from_station, to_station, date, current_time_str)

#         if travel_time < min_travel_time:
#             min_travel_time = travel_time
#             min_travel_station = to_station
#             min_travel_group = group

# if min_travel_station is not None:
#     print_route(from_station, min_travel_station, min_travel_time)

#     excluded_groups = {min_travel_group}
#     current_station = min_travel_station
#     current_time_str = str(int(current_time_str) + int(min_travel_time))

#     for _ in range(len(groups) - 1):
#         min_to_next_time = float('inf')
#         min_to_next_station = None
#         min_to_next_group = None

#         for group, to_stations in groups.items():
#             if group not in excluded_groups:
#                 for to_station in to_stations:
#                     travel_time_to_next = get_travel_time(current_station, to_station, date, current_time_str)

#                     if travel_time_to_next < min_to_next_time:
#                         min_to_next_time = travel_time_to_next
#                         min_to_next_station = to_station
#                         min_to_next_group = group

#         if min_to_next_station is not None:
#             print_route(current_station, min_to_next_station, min_to_next_time)
#             excluded_groups.add(min_to_next_group)
#             current_station = min_to_next_station
#             current_time_str = str(int(current_time_str) + int(min_to_next_time))

# print("ルート検索が完了しました。")


### ver3:ループあり（すべて上記のコードをもとにgptが添削）

# import requests

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# # ユーザーからの入力駅
# user_input_station = input("駅名を入力してください: ")

# # グループに含まれる駅の情報
# groups = {
#     'A': ['渋谷', '三軒茶屋', '下高井戸'],
#     'B': ['中目黒', '田園調布', '目黒'],
#     'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
#     'D': ['大井町', '五反田', '蒲田'],
#     'E': ['自由が丘', '二子玉川', '溝の口'],
#     'F': ['鷺沼', '青葉台', '長津田']
# }

# from_station = user_input_station

# def get_travel_time(from_station, to_station):
#     params = {
#         'key': api_key,
#         'viaList': f'{from_station}:{to_station}',
#         'date': '20230818',
#         'time': '0800',
#         'searchType': 'departure',
#     }

#     res = requests.get(api_url, params=params)
#     result = res.json()
#     return float(result['ResultSet']['Course'][0]['Route']['timeOnBoard'])

# min_travel_time = float('inf')  # 初期値を正の無限大に設定
# min_travel_station = None  # 最短所要時間の駅
# min_travel_group = None  # 最短所要時間の駅が含まれるグループ

# # ユーザーの駅がどのグループに属するかを確認
# user_station_group = None
# for group, stations in groups.items():
#     if from_station in stations:
#         user_station_group = group
#         break

# # 最短所要時間の駅を特定
# for group, to_stations in groups.items():
#     if group == user_station_group:
#         continue  # ユーザーの駅が属するグループはスキップ

#     for to_station in to_stations:
#         travel_time = get_travel_time(from_station, to_station)

#         if travel_time < min_travel_time:
#             min_travel_time = travel_time
#             min_travel_station = to_station
#             min_travel_group = group

# if min_travel_station is not None:
#     print(f"From: {from_station}, To: {min_travel_station}")
#     print(f"Travel Time: {min_travel_time} minutes")
#     print("-----")

#     excluded_groups = {min_travel_group}

#     for _ in range(len(groups) - 1):  # グループ数から1つを引いた回数だけ繰り返し
#         min_to_next_time = float('inf')
#         min_to_next_station = None
#         min_to_next_group = None

#         for group, to_stations in groups.items():
#             if group not in excluded_groups:
#                 for to_station in to_stations:
#                     travel_time_to_next = get_travel_time(min_travel_station, to_station)

#                     if travel_time_to_next < min_to_next_time:
#                         min_to_next_time = travel_time_to_next
#                         min_to_next_station = to_station
#                         min_to_next_group = group

#         if min_to_next_station is not None:
#             print(f"From: {min_travel_station}, To: {min_to_next_station}")
#             print(f"Travel Time: {min_to_next_time} minutes")
#             print("-----")

#             excluded_groups.add(min_to_next_group)
#             min_travel_station = min_to_next_station

# print("ルート検索が完了しました。")


# import requests

# api_key = "test_J9XQ9fXTgaw"
# api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

# user_input_station = input("駅名を入力してください: ")
# from_station = user_input_station

# # グループに含まれる駅の情報
# groups = {
#     'A': ['渋谷', '三軒茶屋', '下高井戸'],
#     'B': ['中目黒', '田園調布', '目黒'],
#     'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
#     'D': ['大井町', '五反田', '蒲田'],
#     'E': ['自由が丘', '二子玉川', '溝の口'],
#     'F': ['鷺沼', '青葉台', '長津田']
# }

# def get_travel_info(from_station, to_station):
#     params = {
#         'key': api_key,
#         'viaList': f'{from_station}:{to_station}',
#         'date': '20230818',
#         'time': '0800',
#         'searchType': 'departure',
#     }

#     res = requests.get(api_url, params=params)
#     result = res.json()
#     return result['ResultSet']['Course'][0]

# def print_route_info(route_info):
#     display_route = route_info['Teiki']['DisplayRoute']

#     print(f"Display Route: {display_route}")
#     print("-----")

# min_travel_time = float('inf')  # 初期値を正の無限大に設定
# min_travel_station = None  # 最短所要時間の駅
# min_travel_group = None  # 最短所要時間の駅が含まれるグループ

# # ユーザーの駅がどのグループに属するかを確認
# user_station_group = None
# for group, stations in groups.items():
#     if from_station in stations:
#         user_station_group = group
#         break

# # 最短所要時間の駅を特定
# for group, to_stations in groups.items():
#     if group == user_station_group:
#         continue  # ユーザーの駅が属するグループはスキップ

#     for to_station in to_stations:
#         travel_info = get_travel_info(from_station, to_station)
#         travel_time = float(travel_info['Route']['timeOnBoard'])

#         if travel_time < min_travel_time:
#             min_travel_time = travel_time
#             min_travel_station = to_station
#             min_travel_group = group

# if min_travel_station is not None:
#     print_route_info(get_travel_info(from_station, min_travel_station))

#     excluded_groups = {min_travel_group}

#     for _ in range(len(groups) - 1):  # グループ数から1つを引いた回数だけ繰り返し
#         min_to_next_time = float('inf')
#         min_to_next_station = None
#         min_to_next_group = None

#         for group, to_stations in groups.items():
#             if group not in excluded_groups:
#                 for to_station in to_stations:
#                     travel_info_to_next = get_travel_info(min_travel_station, to_station)
#                     travel_time_to_next = float(travel_info_to_next['Route']['timeOnBoard'])

#                     if travel_time_to_next < min_to_next_time:
#                         min_to_next_time = travel_time_to_next
#                         min_to_next_station = to_station
#                         min_to_next_group = group

#         if min_to_next_station is not None:
#             print_route_info(get_travel_info(min_travel_station, min_to_next_station))
#             excluded_groups.add(min_to_next_group)
#             min_travel_station = min_to_next_station

# print("ルート検索が完了しました。")



import requests

api_key = "test_J9XQ9fXTgaw"
api_url = "https://api.ekispert.jp/v1/json/search/course/extreme"

user_input_station = input("駅名を入力してください: ")
from_station = user_input_station

#グループに含まれる駅の情報
groups = {
    'A': ['渋谷', '三軒茶屋', '下高井戸'],
    'B': ['中目黒', '田園調布', '目黒'],
    'C': ['武蔵小杉', '新横浜', '菊名', '横浜'],
    'D': ['大井町', '五反田', '蒲田'],
    'E': ['自由が丘', '二子玉川', '溝の口'],
    'F': ['鷺沼', '青葉台', '長津田']
}

def get_travel_info(from_station, to_station):
    params = {
        'key': api_key,
        'viaList': f'{from_station}:{to_station}',
        'date': '20230818',
        'time': '0800',
        'searchType': 'departure',
    }

    res = requests.get(api_url, params=params)
    result = res.json()
    return result['ResultSet']['Course'][0]

def print_route_info(route_info):
    display_route = route_info['Teiki']['DisplayRoute']

    print(f"Display Route: {display_route}")
    print("-----")

min_travel_time = float('inf')  # 初期値を正の無限大に設定
min_travel_station = None  # 最短所要時間の駅
min_travel_group = None  # 最短所要時間の駅が含まれるグループ

#ユーザーの駅がどのグループに属するかを確認
user_station_group = None
for group, stations in groups.items():
    if from_station in stations:
        user_station_group = group
        break

#最短所要時間の駅を特定
for group, to_stations in groups.items():
    if group == user_station_group:
        continue  # ユーザーの駅が属するグループはスキップ

    for to_station in to_stations:
        travel_info = get_travel_info(from_station, to_station)
        travel_time = float(travel_info['Route']['timeOnBoard'])

        if travel_time < min_travel_time:
            min_travel_time = travel_time
            min_travel_station = to_station
            min_travel_group = group

if min_travel_station is not None:
    route_info = get_travel_info(from_station, min_travel_station)
    print_route_info(route_info)

    excluded_groups = {min_travel_group}

    for _ in range(len(groups) - 1):  # グループ数から1つを引いた回数だけ繰り返し
        min_to_next_time = float('inf')
        min_to_next_station = None
        min_to_next_group = None

        for group, to_stations in groups.items():
            if group not in excluded_groups:
                for to_station in to_stations:
                    travel_info_to_next = get_travel_info(min_travel_station, to_station)
                    travel_time_to_next = float(travel_info_to_next['Route']['timeOnBoard'])

                    if travel_time_to_next < min_to_next_time:
                        min_to_next_time = travel_time_to_next
                        min_to_next_station = to_station
                        min_to_next_group = group

        if min_to_next_station is not None:
            route_info_to_next = get_travel_info(min_travel_station, min_to_next_station)
            print_route_info(route_info_to_next)
            excluded_groups.add(min_to_next_group)
            min_travel_station = min_to_next_station

print("ルート検索が完了しました。")