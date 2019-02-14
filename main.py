from good import*
from job import*
import sys

list_of_goods=[]
def count():
    print('If there is an extra-margin, type "extra-margin", else press Enter. Then type all goods you want to order.')
    extra_margin = sys.stdin.readline()
    while True: #я хз, почему оно записывает в список только второй товар
        if sys.stdin.readline() != '\n':
            good = sys.stdin.readline().split()
            list_of_goods.append(good)      
        else:
            break    
    for i in range(0, len(list_of_goods)):
        job.add_new_good(Good(list_of_goods[i][0], float(list_of_goods[i][1]), list_of_goods[i][2])      
    job.count_total()

if __name__ == "__main__":
    count()































