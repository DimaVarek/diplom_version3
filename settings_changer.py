import configparser


config = configparser.ConfigParser()

config['default'] = {'folder_data': 'data',
                     'folder_simple_result': 'games_with_simple_result',
                     'folder_difficult_result': 'games_with_difficult_result',
                     'folder_without_result': 'games_without_result'}

with open('settings.ini', 'w') as f:
    config.write(f)
