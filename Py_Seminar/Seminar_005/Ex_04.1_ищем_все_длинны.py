from pprint import pprint
 
 
numbers = [1, 5, 2, 3, 4, 6, 1, 2, 7]
seq = set()
 
 
def find_sequences(arr, cur_i=0, cur_seq=tuple()):
    # Точка выхода: когда индекс вышел за границы списка
    if cur_i == len(arr):
        if len(cur_seq) > 1:
            seq.add(cur_seq)
        return
 
    # Ищем дальше, игнорируя текущий элемент
    find_sequences(arr, cur_i + 1, cur_seq)
 
    # Ищем дальше, используя текущий элемент, но только если он подходящий
    if (cur_seq and cur_seq[-1] <= arr[cur_i]) or not(cur_seq):
        find_sequences(arr, cur_i + 1, cur_seq + (arr[cur_i],))
 
 
find_sequences(numbers)
 
pprint(seq)
print(len(seq))