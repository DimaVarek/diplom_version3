def map_splitter_all_info(game_dict):
    game_one_string = {}
    result_dict = {}
    results = []
    count_played_maps = 0
    for column in game_dict:
        if column not in ['url_maps_1', 'url_maps_2', 'selected_maps', 'results_on_maps']:
            game_one_string[column] = game_dict[column]
        elif column in ['url_maps_1', 'url_maps_2']:
            for map_top in game_dict[column]:
                for feature_on_map in game_dict[column][map_top]:
                    game_one_string[f'{column[-1]}_{map_top}_{feature_on_map}'] = game_dict[column][map_top][feature_on_map]
        elif column == 'selected_maps':
            result_dict['1_map'] = 'did not play'
            result_dict['2_map'] = 'did not play'
            result_dict['3_map'] = 'did not play'
            result_dict['4_map'] = 'did not play'
            result_dict['5_map'] = 'did not play'
            maps = []
            for game_map in game_dict['selected_maps']:
                if game_dict['selected_maps'][game_map] == 1:
                    maps.append(game_map)
            for i in range(len(maps)):
                result_dict[f'{i+1}_map'] = maps[i]
        else:
            for result_on_map in range(1,game_dict['best_of']+1):
                if game_dict[column][f'1_{result_on_map}st_map'] < game_dict[column][f'2_{result_on_map}st_map']:
                    result_dict[f'result_map_{result_on_map}'] = -1
                elif game_dict[column][f'1_{result_on_map}st_map'] > game_dict[column][f'2_{result_on_map}st_map']:
                    result_dict[f'result_map_{result_on_map}'] = 1
                else:
                    break
                count_played_maps += 1
    for num_map in range(count_played_maps):
        game_one_map = game_one_string.copy()
        game_one_map['map'] = result_dict[f'{num_map+1}_map']
        game_one_map['result'] = result_dict[f'result_map_{num_map+1}']
        if game_one_map['map'] != 'did not play':
            results.append(game_one_map)
    return results


def map_splitter_part_info(game_dict):
    results = []
    for game in map_splitter_all_info(game_dict):
        stat1_top, stat1_all, stat2_top, stat2_all = get_names_for_urls_maps(int(game['team1_world_rank']),
                                                                             int(game['team2_world_rank']),
                                                                             game['map'])
        part_key_names = [f'1_{stat1_top}', f'1_{stat1_all}',
                          f'2_{stat2_top}', f'2_{stat2_all}']
        key_names = {'map': 'map', 'result': 'result',
                     'team1_world_rank': 'team1_world_rank',
                     'team2_world_rank': 'team2_world_rank'}
        for key in list(game.keys()):
            for part_key_num in range(len(part_key_names)):
                if part_key_names[part_key_num] in key:
                    new_key = key.split('_')
                    if part_key_num % 2 == 0:
                        key_names[f'{new_key[0]}_top_{new_key[3]}'] = key
                    else:
                        key_names[f'{new_key[0]}_All_{new_key[3]}'] = key


        new_game = {}
        for key in key_names:
            print(key, key_names[key])
            new_game[key] = game[key_names[key]]
        results.append(new_game)
    return results





def map_splitter(game_dict):
    if game_dict['best_of'] == 3:
        maps = []
        for game_map in game_dict['selected_maps']:
            if game_dict['selected_maps'][game_map] == 1:
                maps.append(game_map)
        first_map_dict = {'map': maps[0]}
        second_map_dict = {'map': maps[1]}
        third_map_dict = {'map': maps[2]}

        rank1 = int(game_dict['team1_world_rank'])
        rank2 = int(game_dict['team2_world_rank'])

        first_map_dict['rank1'] = rank1
        first_map_dict['rank2'] = rank2
        first_map_dict['diff_rank'] = rank2 - rank1
        # для начала супер простенько, только количество игр и доля побед
        stat1_top, stat1_all, stat2_top, stat2_all = get_names_for_urls_maps(rank1,
                                                                             rank2,
                                                                             maps[0])
        first_map_dict['stat1_times_played_top'] = game_dict['url_maps_1'][stat1_top]['Times played']
        try:
            first_map_dict['stat1_win_rate_top'] = game_dict['url_maps_1'][stat1_top]['wins'] / \
                game_dict['url_maps_1'][stat1_top]['Times played']
        except ZeroDivisionError:
            first_map_dict['stat1_win_rate_top'] = 0

        first_map_dict['stat1_times_played_all'] = game_dict['url_maps_1'][stat1_all]['Times played']
        try:
            first_map_dict['stat1_win_rate_all'] = game_dict['url_maps_1'][stat1_all]['wins'] / \
                game_dict['url_maps_1'][stat1_all]['Times played']
        except ZeroDivisionError:
            first_map_dict['stat1_win_rate_all'] = 0

        first_map_dict['stat2_times_played_top'] = game_dict['url_maps_2'][stat2_top]['Times played']
        try:
            first_map_dict['stat2_win_rate_top'] = game_dict['url_maps_2'][stat2_top]['wins'] / \
                game_dict['url_maps_2'][stat2_top]['Times played']
        except ZeroDivisionError:
            first_map_dict['stat2_win_rate_top'] = 0

        first_map_dict['stat2_times_played_all'] = game_dict['url_maps_2'][stat2_all]['Times played']
        try:
            first_map_dict['stat2_win_rate_all'] = game_dict['url_maps_2'][stat2_all]['wins'] / \
                game_dict['url_maps_2'][stat2_all]['Times played']
        except ZeroDivisionError:
            first_map_dict['stat2_win_rate_all'] = 0

        first_map_dict['result'] = 1 if game_dict['results_on_maps']['1_1st_map'] > \
                                        game_dict['results_on_maps']['2_1st_map'] else -1

        second_map_dict['rank1'] = rank1
        second_map_dict['rank2'] = rank2
        second_map_dict['diff_rank'] = rank2 - rank1

        stat1_top, stat1_all, stat2_top, stat2_all = get_names_for_urls_maps(rank1,
                                                                             rank2,
                                                                             maps[1])

        second_map_dict['stat1_times_played_top'] = game_dict['url_maps_1'][stat1_top]['Times played']
        try:
            second_map_dict['stat1_win_rate_top'] = game_dict['url_maps_1'][stat1_top]['wins'] / \
                game_dict['url_maps_1'][stat1_top]['Times played']
        except ZeroDivisionError:
            second_map_dict['stat1_win_rate_top'] = 0

        second_map_dict['stat1_times_played_all'] = game_dict['url_maps_1'][stat1_all]['Times played']
        try:
            second_map_dict['stat1_win_rate_all'] = game_dict['url_maps_1'][stat1_all]['wins'] / \
                game_dict['url_maps_1'][stat1_all]['Times played']
        except ZeroDivisionError:
            second_map_dict['stat1_win_rate_all'] = 0

        second_map_dict['stat2_times_played_top'] = game_dict['url_maps_2'][stat2_top]['Times played']
        try:
            second_map_dict['stat2_win_rate_top'] = game_dict['url_maps_2'][stat2_top]['wins'] / \
                game_dict['url_maps_2'][stat2_top]['Times played']
        except ZeroDivisionError:
            second_map_dict['stat2_win_rate_top'] = 0

        second_map_dict['stat2_times_played_all'] = game_dict['url_maps_2'][stat2_all]['Times played']
        try:
            second_map_dict['stat2_win_rate_all'] = game_dict['url_maps_2'][stat2_all]['wins'] / \
                game_dict['url_maps_2'][stat2_all]['Times played']
        except ZeroDivisionError:
            second_map_dict['stat2_win_rate_all'] = 0

        second_map_dict['result'] = 1 if game_dict['results_on_maps']['1_2st_map'] > game_dict['results_on_maps'][
            '2_2st_map'] else -1

        if game_dict['results_on_maps']['1_3st_map'] != 0:
            third_map_dict['rank1'] = rank1
            third_map_dict['rank2'] = rank2
            third_map_dict['diff_rank'] = rank2 - rank1

            stat1_top, stat1_all, stat2_top, stat2_all = get_names_for_urls_maps(rank1,
                                                                                 rank2,
                                                                                 maps[1])

            third_map_dict['stat1_times_played_top'] = game_dict['url_maps_1'][stat1_top]['Times played']
            try:
                third_map_dict['stat1_win_rate_top'] = game_dict['url_maps_1'][stat1_top]['wins'] / \
                    game_dict['url_maps_1'][stat1_top]['Times played']
            except ZeroDivisionError:
                third_map_dict['stat1_win_rate_top'] = 0

            third_map_dict['stat1_times_played_all'] = game_dict['url_maps_1'][stat1_all]['Times played']
            try:
                third_map_dict['stat1_win_rate_all'] = game_dict['url_maps_1'][stat1_all]['wins'] / \
                    game_dict['url_maps_1'][stat1_all]['Times played']
            except ZeroDivisionError:
                third_map_dict['stat1_win_rate_all'] = 0

            third_map_dict['stat2_times_played_top'] = game_dict['url_maps_2'][stat2_top]['Times played']
            try:
                third_map_dict['stat2_win_rate_top'] = game_dict['url_maps_2'][stat2_top]['wins'] / \
                    game_dict['url_maps_2'][stat2_top]['Times played']
            except ZeroDivisionError:
                third_map_dict['stat2_win_rate_top'] = 0

            third_map_dict['stat2_times_played_all'] = game_dict['url_maps_2'][stat2_all]['Times played']
            try:
                third_map_dict['stat2_win_rate_all'] = game_dict['url_maps_2'][stat2_all]['wins'] / \
                    game_dict['url_maps_2'][stat2_all]['Times played']
            except ZeroDivisionError:
                third_map_dict['stat2_win_rate_all'] = 0

            third_map_dict['result'] = 1 if game_dict['results_on_maps']['1_3st_map'] > game_dict['results_on_maps'][
                '2_3st_map'] else -1
            return first_map_dict, second_map_dict, third_map_dict
        return first_map_dict, second_map_dict

    else:
        return []


def from_dict_to_df_string(game_dict):
    result = {}
    for column in game_dict:
        if column not in ['url_maps_1', 'url_maps_2', 'selected_maps', 'results_on_maps']:
            result[column] = game_dict[column]
        elif column in ['url_maps_1', 'url_maps_2']:
            for map_top in game_dict[column]:
                for feature_on_map in game_dict[column][map_top]:
                    result[f'{column[-1]}_{map_top}_{feature_on_map}'] = game_dict[column][map_top][feature_on_map]
        elif column == 'selected_maps':
            result['1_map'] = 'did not play'
            result['2_map'] = 'did not play'
            result['3_map'] = 'did not play'
            result['4_map'] = 'did not play'
            result['5_map'] = 'did not play'
            maps = []
            for game_map in game_dict['selected_maps']:
                if game_dict['selected_maps'][game_map] == 1:
                    maps.append(game_map)
            for i in range(len(maps)):
                result[f'{i+1}_map'] = maps[i]

    return result


# эта функция дает ссылки на статистику для карта,
# причем для каждой команды это 2 ссылки, с оппонентами аналогичного уровня и для всех
def get_names_for_urls_maps(rank1, rank2, map_name):
    maps = {'Ancient': 47,
            'Dust2': 31,
            'Inferno': 33,
            'Mirage': 32,
            'Nuke': 34,
            'Overpass': 40,
            'Vertigo': 46}
    map_number = maps[map_name]
    name1_top = f'{map_number}_top{get_top(rank2)}'
    name1_all = f'{map_number}_topAll'
    name2_top = f'{map_number}_top{get_top(rank1)}'
    name2_all = f'{map_number}_topAll'
    return name1_top, name1_all, name2_top, name2_all


def get_top(rank):
    if rank < 6:
        return '5'
    elif rank < 11:
        return '10'
    elif rank < 21:
        return '20'
    elif rank < 31:
        return '30'
    elif rank < 51:
        return '50'
    else:
        return 'All'
