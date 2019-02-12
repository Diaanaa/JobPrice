import sys
"""
goods = []
def job():
    print('If there is an extra margin, type "extra margin". Then type all needed goods.')
    extra_margin = sys.stdin.readline()
    good = 0
    while good != '\n':
        good = sys.stdin.readline().split()     
        goods.append(good)
"""
goods=[]
goods_copy=[]
def job():
    print('If there is an extra-margin, type "extra-margin", else press Enter. Then type all goods you want to order.')
    extra_margin = sys.stdin.readline()

    for i in range(0,2):
        good = sys.stdin.readline().split() 
        goods_copy.append(good)    
        goods.append(good)
    
    make_price_float(goods)
    count_price_of_thing(goods)
    count_total(goods_copy)
    return
almost_total_free=[]
almost_total_tax=[]
def count_total(extra_margin):
    if extra_margin == 'extra-margin\n':
        for i in range(0, len(goods_copy)):
            if len(goods_copy[i]) == 2:
                goods_copy[i][1] = goods_copy[i][1]*1.23
                almost_total_tax.append(goods_copy[i][1])
                i=+1
            else:
                goods_copy[i][1] = goods_copy[i][1]*1.23
                almost_total_free.append(goods_copy[i][1])
                i=+1
    else: 
        for i in range(0, len(goods_copy)):
            if len(goods_copy[i]) == 2:
                goods_copy[i][1] = goods_copy[i][1]*1.16
                almost_total_tax.append(goods_copy[i][1])
                i=+1
            else:
                goods_copy[i][1] = goods_copy[i][1]*1.16
                almost_total_free.append(goods_copy[i][1])
                i=+1
    print ("total: $" + str(sum(almost_total_free+almost_total_tax)))         
    return 





def make_price_float(good):
    for i in range(0, len(goods)):
        goods[i][1] = float(goods[i][1])
        i = i + 1
    return

def count_price_of_thing(price):
    for i in range(0, len(goods)):
        if len(goods[i]) == 2: #2 элемента в списке, значит пользователь не ввел информацию про налог
            goods[i][1] = goods[i][1]+goods[i][1]*0.07
            i=+1
        else:
            goods[i][1] = goods[i][1]
    for i in range (0,len(goods)):
        print (goods[i][0] + ": $" + str(goods[i][1]))    
    return 
   



"""try:
    for i in range(0,len(ex)):
        total = ex[i][1]+ ex[i+1][1]
except IndexError:
    print(total)
"""


job()