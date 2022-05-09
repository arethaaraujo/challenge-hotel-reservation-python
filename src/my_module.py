import re


def f_min(aux_min):
    if aux_min[0] < aux_min[1] < aux_min[2]: return "Lakewood"    
    elif aux_min[1] < aux_min[2]: return "Bridgewood"
    else: return "Ridgewood"


def normal_costumer(amount): #Regular costumer function
    aux_amount = [0, 0, 0]
    for data in enumerate(amount, 1):
        if re.search('sat|sun', str(data)):
            aux_amount[0] += 90
            aux_amount[1] += 60
            aux_amount[2] += 150
        elif re.search('mon|tues|wed|thur|fri', str(data)):
            aux_amount[0] += 110
            aux_amount[1] += 160
            aux_amount[2] += 220
    return f_min(aux_amount)


def premium_custumer(amount): #Fidelity program costumer function
    aux_amount = [0, 0, 0]
    for data in enumerate(amount, 1):
        if re.search('sat|sun', str(data)):
            aux_amount[0] += 80
            aux_amount[1] += 50
            aux_amount[2] += 40
        elif re.search('mon|tues|wed|thur|fri', str(data)):
            aux_amount[0] += 80
            aux_amount[1] += 110
            aux_amount[2] += 100
    return f_min(aux_amount)


def get_cheapest_hotel(number):   #DO NOT change the function's name
    costumer_data = number.split(" ")
    if costumer_data[0] == 'Regular:' : return(normal_costumer(costumer_data))
    else: return(premium_custumer(costumer_data))