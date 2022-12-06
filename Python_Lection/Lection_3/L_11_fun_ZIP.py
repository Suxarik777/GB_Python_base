# Функция ZIP

user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

data = zip(user, ids)
print(data) #покажет собственный тип

# записываем data 
data = list(zip(user, ids))
print(data)


#важная фишка, если наборы данных != то пробежка будет по минимальному набору
user2 = ['user1', 'user2', 'user3', 'user4', 'user5']
salary = [200, 500, 400]

data = list(zip(user2, salary))
print(data) #выведит только 3-х user

# пример ZIP три входных данных

data = list(zip(user2, ids, salary))
print(data)