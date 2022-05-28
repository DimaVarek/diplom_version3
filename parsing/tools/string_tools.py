import re
import datetime as dt
import numpy as np


def find_game_type(string_game_type):
    a = re.search('Best of ([135])', string_game_type)
    return int(a.group(1))


def get_number_of_confrontation(url_game):
    pattern = r'\/(\d+?)\/'
    return re.findall(pattern, url_game)[0]


def calculated_ratio(ratio_array):
    for i in ratio_array:
        if 'parimatch' in str(i):
            c = re.findall(r'[0-9]*[.,][0-9]+', str(i))
            if not c:
                final_ratio_array = [0.0, 0.0]
                return final_ratio_array
            final_ratio_array = [float(c[0]), float(c[1])]
            return final_ratio_array
    final_ratio_array = [0.0, 0.0]
    return final_ratio_array


def calculate_name_number(href_str):
    a = href_str.split('/')
    name = a[3]
    number = a[2]
    return name, number


def team_rank(str_world_ranking):
    try:
        world_rank = re.findall(r'#[0-9]+', str_world_ranking)[0]
        world_rank = re.findall(r'[0-9]+', world_rank)[0]
        world_rank = int(world_rank)
    except IndexError:
        world_rank = 200
    return world_rank


def start_end_date():
    end_date = dt.date.today()
    start_date = end_date - dt.timedelta(days=90)
    return f'?startDate={str(start_date)}&endDate={str(end_date)}'


def map_preprocessing(before_dict):
    after_dict = {}
    for i in before_dict:
        if i in ['Times played', 'Total rounds played', 'Rounds won', 'Pistol rounds', 'Pistol rounds won']:
            after_dict[i] = int(before_dict[i])
        elif i in ['Win percent', 'Pistol round win percent', 'CT round win percent', 'T round win percent']:
            m = before_dict[i]
            after_dict[i] = np.around(float(m[:-1]) / 100, 6)
        else:
            win_draw_losses = [int(j) for j in before_dict[i].split('/')]
            after_dict['wins'] = win_draw_losses[0]
            after_dict['draws'] = win_draw_losses[1]
            after_dict['losses'] = win_draw_losses[2]
    return after_dict
