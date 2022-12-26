import os


os.chdir(os.path.dirname(__file__))


def recording_file(arr, file_name='playing_area'):
    with open(f'{file_name}.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(' '.join(map(str, sublist)) for sublist in arr))

# def reset_file(inp_file='start_playing_area', out_file='playing_area')
