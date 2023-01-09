from telebot import TeleBot, types
from func_for_work_bot import read_file, recording_file


def recording_str_keyboard(msg: types.Message):
    text = str(msg.text)
    data_list = text.split()
    array = read_file()
    array.append(data_list)
    recording_file(array)