import datetime as dt
import string_tools


# find type bo1, bo3, bo5
def get_type_game(soup_game):
    text_in_div = soup_game.find('div', class_="padding preformatted-text").get_text()
    return string_tools.find_game_type(str(text_in_div))


# return dict with played maps
def selected_maps(soup_game):
    frame_result = soup_game.find_all('div', 'padding')[1]
    map_dict = {}
    for string_map in frame_result.find_all('div'):
        current_string = str(string_map)[8:-6]
        if 'removed' in current_string:
            map_dict[current_string.split()[-1]] = 0
        elif 'picked' in current_string:
            map_dict[current_string.split()[-1]] = 1
        else:
            map_dict[current_string.split()[0]] = 1

    return map_dict


# return result on selected maps
def get_result_on_selected_maps(soup_game, best_of):
    results_array_html = soup_game.find_all('div', class_='results-team-score')
    results_array = []
    for i in results_array_html:
        if i.get_text() != '-':
            results_array.append(int(i.get_text()))
        else:
            results_array.append(0)
    if best_of == 1:
        results_dict = {'1_1st_map': results_array[0], '2_1st_map': results_array[1]}
    elif best_of == 3:
        results_dict = {'1_1st_map': results_array[0], '2_1st_map': results_array[1], '1_2st_map': results_array[2],
                        '2_2st_map': results_array[3], '1_3st_map': results_array[4], '2_3st_map': results_array[5]}
    else:
        results_dict = {'1_1st_map': results_array[0], '2_1st_map': results_array[1], '1_2st_map': results_array[2],
                        '2_2st_map': results_array[3], '1_3st_map': results_array[4], '2_3st_map': results_array[5],
                        '1_4st_map': results_array[6], '2_4st_map': results_array[7], '1_5st_map': results_array[8],
                        '2_5st_map': results_array[9]}

    return results_dict


# find datetime of game from main paige
def find_datetime(soup_game):
    time = int(soup_game.find('div', class_="time")['data-unix'])
    datetime_game = str(dt.datetime.fromtimestamp(time / 1e3))
    return datetime_game


# find ratio for teams
def find_ratio(soup_game):
    ratio_array = soup_game.find_all('tr', class_='provider')
    return string_tools.calculated_ratio(ratio_array)


# find names and numbers for teams
def find_numbers_names(soup_game):
    team1_str = str(soup_game.find('div', class_='team1-gradient').find('a').get('href'))
    name1, number1 = string_tools.calculate_name_number(team1_str)
    team2_str = str(soup_game.find('div', class_='team2-gradient').find('a').get('href'))
    name2, number2 = string_tools.calculate_name_number(team2_str)
    return name1, number1, name2, number2


# find teams world rankings
def find_world_rankings(soup_game):
    team_world_rank = soup_game.find_all('div', class_='teamRanking')
    return string_tools.team_rank(str(team_world_rank[0])), string_tools.team_rank(str(team_world_rank[1]))


# calculate stat for one map, one top
def stats_one_map(stat_soup):
    stat_frame = stat_soup.find_all('div', class_='stats-row')
    returned_dict = {}
    for elem in stat_frame:
        c = elem.find_all('span')
        returned_dict[c[0].getText()] = c[1].getText()
    returned_dict = string_tools.map_preprocessing(returned_dict)
    return returned_dict


def check_game_over(soup_game):
    if soup_game.find('div', class_='countdown').getText() == 'Match over':
        return True
    return False


def simple_result(soup_game):
    result_string = str(soup_game.find('div', class_='team1-gradient'))
    if 'lost' in result_string:
        return -1
    else:
        return 1


def get_urls_by_days_games(soup_matches):
    div_array = soup_matches.find_all('div', class_='upcomingMatchesSection')
    url_matches = []
    for i in div_array[0].find_all('a', class_='match a-reset'):
        url_matches.append('https://www.hltv.org' + str(i['href']))
    return url_matches
