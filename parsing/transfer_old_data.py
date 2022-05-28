import os
import json
import configparser

import html_tools
from soup_function import selected_maps, get_type_game, get_result_on_selected_maps
import bs4


'''This is a one-time file that is used to process the results of the previous version of the parser'''

config = configparser.ConfigParser()
config.read('../settings.ini')

with open('../settings.ini') as f:
    print(f.read())

before_process_folder = f"../{config['default']['folder_data']}/{config['default']['folder_simple_result']}"
after_process_folder = f"../{config['default']['folder_data']}/{config['default']['folder_difficult_result']}"

for file in os.listdir(before_process_folder):
    if file not in os.listdir(after_process_folder):
        with open(f'{before_process_folder}/{file}') as f:
            data_about_game = json.load(f)
        page_html = html_tools.get_html(data_about_game['url'])
        soup_game = bs4.BeautifulSoup(page_html, features='html.parser')
        data_about_game['best_of'] = get_type_game(soup_game)
        data_about_game['selected_maps'] = selected_maps(soup_game)
        data_about_game['results_on_maps'] = get_result_on_selected_maps(soup_game, data_about_game['best_of'])

        with open(f'{after_process_folder}/{file}', 'w') as f:
            json.dump(data_about_game,f)
