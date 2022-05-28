import os_json_tools
import preprocessing_one_dict


def df_splitter_by_games(name='df_games'):
    games = os_json_tools.get_dicts_for_preproc()
    counter = 0
    results = []
    for game in games:
        game_string = preprocessing_one_dict.from_dict_to_df_string(game)
        counter += 1
        results.append(game_string)
    print(f'{counter}/{len(games)}')
    os_json_tools.from_array_to_df(results, name)


def df_splitter_by_maps_all_data(name='df_split_by_map_all_info'):
    games = os_json_tools.get_dicts_for_preproc()
    counter = 0
    results = []
    for game in games:
        for game_string in preprocessing_one_dict.map_splitter_all_info(game):
            counter += 1
            results.append(game_string)
    print(f'{counter}/{len(games)}')
    os_json_tools.from_array_to_df(results, name)


def df_splitter_by_maps_part_data(name='df_split_by_map_part_info'):
    games = os_json_tools.get_dicts_for_preproc()
    counter = 0
    results = []
    for game in games:
        for game_string in preprocessing_one_dict.map_splitter_part_info(game):
            counter += 1
            results.append(game_string)
    print(f'{counter}/{len(games)}')
    os_json_tools.from_array_to_df(results, name)


# def df_splitter_by_maps_part_data(name='df_split_by_map_part_info'):
#     games = os_json_tools.get_dicts_for_preproc()
#     counter = 0
#     results = []
#     for game in games:
#         for game_string in preprocessing_one_dict.map_splitter(game):
#             counter += 1
#             results.append(game_string)
#     print(f'{counter}/{len(games)}')
#     os_json_tools.from_array_to_df(results, name)
