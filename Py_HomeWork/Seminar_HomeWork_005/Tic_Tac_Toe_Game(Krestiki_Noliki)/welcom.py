from imports import view_playing_area

print('''Погнали играть в крестики нолики!
 Правила игры: 
 - в игре два символа: 
 ---------> + - крестик
 ---------> 0 - нолик
 твоя задача поставить символ в ячейку под номером:
 1 или 2 или 3 итд. 
 Смотри на картику:''')
view_playing_area('enumerate_playing_area')

input('Чтобы продолжить, ЖМИ на ENTER')

