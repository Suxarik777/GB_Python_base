def compressed_text(string):
    encoding = ''
    prev_char = ''
    count = 1

    if not string:
        return ''

    for char in string:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    # последняя буква
    encoding += str(count) + prev_char
    return encoding


def decompressed_text(string):
    decode = ''
    count = ''

    for char in string:
        if char.isdigit():
            count = char
        else:
            if count.isdigit():
                decode += char * int(count)
                count = ''
            else:
                print('Ошибка закодированного файла')
                break

    return decode
