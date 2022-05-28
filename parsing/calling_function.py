import os_json_function
import html_function
import string_tools
import time


def parsing_by_one_url_before(url_game):
    if not os_json_function.check_games_in_folder(string_tools.get_number_of_confrontation(url_game), 'wo'):
        game_dict = html_function.parsing_game_before(url_game)
        os_json_function.to_json_after_firs_parsing(game_dict)


def parsing_by_all_folder_after():
    games_array = os_json_function.get_dicts_array_for_parsing_results()
    for index_game in range(len(games_array)):
        result_flag, games_array[index_game] = html_function.parsing_results_for_game(games_array[index_game])
        if result_flag:
            os_json_function.to_json_after_parsing_results(games_array[index_game])
            os_json_function.delete_file_from_wo_result(games_array[index_game])


def parsing_games_by_day():
    time_start = time.time()
    games_urls = html_function.get_urls_for_days_games()
    parsed_counter = 0
    error_games = []
    for game_url in games_urls:
        try:
            parsing_by_one_url_before(game_url)
            parsed_counter += 1
        except:
            error_games.append(game_url)
    time_end = time.time()
    print(f'All time: {time_end-time_start}')
    print(f'Count of games: {parsed_counter}')
    print(f'Unparsed games: {error_games}')
