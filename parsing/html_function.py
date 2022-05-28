import bs4

import os_json_function
import soup_function
import html_tools
import string_tools


def parsing_game_before(url_game):
    game_dict = {}
    main_page_html = html_tools.get_html(url_game)
    main_soup_game = bs4.BeautifulSoup(main_page_html, features='html.parser')
    game_dict['version'] = 1.1
    game_dict['url'] = url_game
    game_dict['number_of_confrontation'] = string_tools.get_number_of_confrontation(url_game)
    game_dict['datetime1'] = soup_function.find_datetime(main_soup_game)
    game_dict['ratio1'], game_dict['ratio2'] = soup_function.find_ratio(main_soup_game)
    game_dict['best_of'] = soup_function.get_type_game(main_soup_game)

    game_dict['name1'], game_dict['number1'], \
        game_dict['name2'], game_dict['number2'] = soup_function.find_numbers_names(main_soup_game)
    game_dict['team1_world_rank'], game_dict['team2_world_rank'] = soup_function.find_world_rankings(main_soup_game)
    game_dict['url_maps_1'] = data_from_maps(game_dict['number1'], game_dict['name1'])
    game_dict['url_maps_2'] = data_from_maps(game_dict['number2'], game_dict['name2'])
    game_dict['result'] = 0
    return game_dict


# calculate stats on all maps for team
def data_from_maps(number, name):
    maps = {47: 'ancient', 31: 'dust2', 33: 'inferno', 32: 'mirage', 34: 'nuke', 40: 'overpass', 46: 'vertigo'}
    url_maps = {}
    k_time = 0
    for curr_map in maps:
        for top in ['5', '10', '20', '30', '50', 'All']:
            url_maps[f'{str(curr_map)}_top{top}'] = \
                f'https://www.hltv.org/stats/teams/map/' \
                f'{curr_map}/' \
                f'{number}/' \
                f'{name}/' \
                f'{string_tools.start_end_date()}' \
                f'&rankingFilter=Top{top}'
            k_time += 1
            print(k_time)
    return_stat = {}
    for curr_map in url_maps:
        print(f'map being processed:{curr_map} - {maps[int(curr_map[:2])]}')
        html_state_paige = html_tools.get_html(url_maps[curr_map])
        stat_soup = bs4.BeautifulSoup(html_state_paige, features='html.parser')
        return_stat[curr_map] = soup_function.stats_one_map(stat_soup)

    return return_stat


# parsing results after game
def parsing_results_for_game(game_dict):
    main_soup_game = bs4.BeautifulSoup(html_tools.get_html(game_dict['url']), features='html.parser')
    if soup_function.check_game_over(main_soup_game):
        game_dict['result'] = soup_function.simple_result(main_soup_game)
        game_dict['selected_maps'] = soup_function.selected_maps(main_soup_game)
        game_dict['results_on_maps'] = soup_function.get_result_on_selected_maps(main_soup_game, game_dict['best_of'])
        return True, game_dict
    return False, game_dict


def get_urls_for_days_games():
    matches_url = 'https://www.hltv.org/matches'
    matches_html = html_tools.get_html(matches_url)
    matches_soup = bs4.BeautifulSoup(matches_html, features='html.parser')
    games_urls = soup_function.get_urls_by_days_games(matches_soup)
    returned_games_urls = []
    for game_url in games_urls:
        if not os_json_function.check_games_in_folder(string_tools.get_number_of_confrontation(game_url)):
            returned_games_urls.append(game_url)
    return returned_games_urls
