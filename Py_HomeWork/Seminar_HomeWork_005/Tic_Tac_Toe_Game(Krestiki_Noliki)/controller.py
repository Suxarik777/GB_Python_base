from imports import view_playing_area, collect_array
from input import user_input_position, index_pos_line, index_pos_row, user_name_1, user_name_2, user_symbol
from edits import update_arr
from export import recording_file
from check_game import check_game, swich_game_click
from winner import winner_user

arr_game = collect_array('start_playing_area')  # считываем "нулевой файл" в lst
recording_file(arr_game)                        # сбрасываем (перезаписываем) игровой файл

view_playing_area('enumerate_playing_area')

user_name_1 = user_name_1()
user_name_2 = user_name_2()
who_gamer = 'user_1'

count = 0
switch_game = 'game'
while switch_game == 'game':
    number_pos = user_input_position(who_gamer, user_name_1, user_name_2)
    i_line = index_pos_line(number_pos)
    i_row = index_pos_row(number_pos)
    arr_game2 = update_arr(i_line, i_row, user_symbol(who_gamer), arr_game)
    recording_file(arr_game)
    view_playing_area('playing_area')
    who_gamer = swich_game_click(who_gamer)
    count += 1
    switch_game = check_game(arr_game)

if switch_game == 'stop_game':
    winner_user(who_gamer, user_name_1, user_name_2)
elif switch_game == 'game_over':
    print('Ну вот вы оба и проиграли! \nНе беда, попробуйте ещё раз!')