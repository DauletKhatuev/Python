#1 Задание
def num_Fibb():
    Fibb = 0
    last_num = 1
    while True:
        yield Fibb
        Fibb, last_num = last_num, Fibb + last_num


#2 Задание
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
set_data = set()
def unique_val(data):
    for i in data:
        if i not in set_data:
            set_data.add(i) 
            yield i

for i in unique_val(data):
    print(i)