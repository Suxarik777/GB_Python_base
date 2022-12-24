array = [1, 5, 2, 3, 4, 9, 6, 1, 6, 7, 8, 10, 10]

length = len(array)
spread_collection = {}
for i in range(length):
    spread_collection.update({i: [[array[i]]]})   # создание библиотеки

print(spread_collection)

for i in range(length):
    tmp_item = spread_collection[i]
    tmp_small_item = []
    for small_item in tmp_item:
        for j in range(i + 1, length):
            if array[j] > small_item[-1]:
                tmp_small_item = small_item.copy()
                tmp_small_item.append(array[j])
                spread_collection[j].append(tmp_small_item)

tmp_length = 0
for v in spread_collection:
    print(v, spread_collection[v])
    for item in spread_collection[v]:
        if len(item) > tmp_length:
            tmp_arr = [item]
            tmp_length = len(item)
        elif len(item) == tmp_length:
            tmp_arr.append(item)
print(tmp_length)
print(tmp_arr)