from collections import Counter
from list_of_friends import get_age, GetFriendsAges, GetUser
import matplotlib.pyplot as graph

a = GetUser('id33732528')
us_id = a.execute()

# для хранения друзей с возрастом

friends_list = GetFriendsAges(us_id)
result = friends_list.execute()

#гистограмма
#объект класса Counter, очень похожий на словарь (который dictionary), которому передан список
result_1 = Counter(result)
#print(result_1)
data1 = result_1
#массив для возраста друзей пользователя
friends_ages = []

for i in list(result_1):
    friends_ages.append(result_1[i])
print(result_1)

#Сетка
graph.grid()
graph.minorticks_on()
# интервалы значений по x и y
graph.figure(num=1, figsize=(10, 4))
graph.axis([0, 70, 0, 30])
#Метка по оси х в формате TeX
graph.xlabel('Age of friends', size=12)
#Метка по оси y в формате TeX
graph.ylabel('Amount of friends', size=12)
graph.bar(data1, friends_ages, width=1.5)
#показать график
graph.show()
