import os
import configparser
import json
import pandas as pd


config = configparser.ConfigParser()
config.read('settings.ini')


def get_dicts_for_preproc():
    games_array = []
    name_folder = f'{config["default"]["folder_data"]}/' \
                  f'{config["default"]["folder_difficult_result"]}'
    for game_file_name in os.listdir(name_folder):
        with open(f'{name_folder}/{game_file_name}') as f:
            games_array.append(json.load(f))
    return games_array


def from_array_to_df(array_maps, name):
    df = pd.DataFrame(array_maps)
    name_folder = f'{config["default"]["folder_data"]}/' \
                  f'{config["default"]["folder_dataframes"]}'
    df.to_csv(f'{name_folder}/{name}.csv', index=False)
