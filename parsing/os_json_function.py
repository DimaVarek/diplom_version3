import os
import json
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')


def to_json_after_firs_parsing(game_dict):
    name = f'{config["default"]["folder_data"]}/' \
           f'{config["default"]["folder_without_result"]}/' \
           f'[{game_dict["number_of_confrontation"]}]' \
           f'_result[{game_dict["result"]}]' \
           f'_date[{game_dict["datetime1"][:-9]}]' \
           f'_version[{game_dict["version"]}].json'
    with open(name, 'w') as f:
        json.dump(game_dict, f)


def to_json_after_parsing_results(game_dict):
    name = f'{config["default"]["folder_data"]}/' \
           f'{config["default"]["folder_difficult_result"]}/' \
           f'[{game_dict["number_of_confrontation"]}]' \
           f'_result[{game_dict["result"]}]' \
           f'_date[{game_dict["datetime1"][:-9]}]' \
           f'_version[{game_dict["version"]}].json'
    with open(name, 'w') as f:
        json.dump(game_dict, f)


def delete_file_from_wo_result(game_dict):
    name = f'{config["default"]["folder_data"]}/' \
           f'{config["default"]["folder_without_result"]}/' \
           f'[{game_dict["number_of_confrontation"]}]' \
           f'_result[{0}]' \
           f'_date[{game_dict["datetime1"][:-9]}]' \
           f'_version[{game_dict["version"]}].json'
    os.remove(name)


# checking game in folder
def check_games_in_folder(game_id, type_folder='all'):
    # type_folder can be only 4 types:
    #     wo - without result folder
    #     ws - with simple result folder
    #     wd - with difficult result folder
    #     all - all folders
    if type_folder == 'wo':
        name = f"{config['default']['folder_data']}/" \
           f'{config["default"]["folder_without_result"]}'
    elif type_folder == 'ws':
        name = f"{config['default']['folder_data']}/" \
           f'{config["default"]["folder_simple_result"]}'
    elif type_folder == 'wd':
        name = f'{config["default"]["folder_data"]}/' \
           f'{config["default"]["folder_difficult_result"]}'
    else:
        name = f'{config["default"]["folder_data"]}'
        for folder_name in os.listdir(name):
            for file_name in os.listdir(f'{name}/{folder_name}'):
                if str(game_id) in file_name:
                    return True
        return False
    for file_name in os.listdir(name):
        if str(game_id) in file_name:
            return True
    return False


def get_dicts_array_for_parsing_results():
    games_array = []
    name_folder = f'{config["default"]["folder_data"]}/' \
                  f'{config["default"]["folder_without_result"]}'
    for game_file_name in os.listdir(name_folder):
        with open(f'{name_folder}/{game_file_name}') as f:
            games_array.append(json.load(f))
    return games_array
