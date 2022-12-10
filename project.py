from datetime import datetime
import random
import pickle
import matplotlib.pyplot as plt
from first import prime_first
from first import prime_first_not_optimal
from second import *
from third import *
array = [1,2,3,4,5,6,7,8,9,10,
         20,30,40,50,60,70,80,90,100,
         200,300,400,500,600,700,800,900,1000,
         2000,3000,4000,5000,6000,7000,8000,9000,10000,
         20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]

tables = []

def create_plot(function_array):
    table_number = 1
    for f in function_array:
        result_array = []
        x_array = []
        table_x = []
        table_y = []
        c = 0
        for i in array:
            now = datetime.now()
            f(i)
            if (datetime.now() - now).seconds > 10:
                break
            x_array.append(i)   
            result_array.append((datetime.now() - now).seconds +     round(((datetime.now() - now).microseconds * ((1 / 10) ** 6)), 3))
            
            table_x.append(i)
            table_y.append((datetime.now() - now).seconds +     round(((datetime.now() - now).microseconds * ((1 / 10) ** 6)), 5))
            c +=1
        # plt.table(cellText=[table_x, table_y], rowLabels=['n', 'time'], loc='bottom')
        with open(f"{table_number}.pickle", "wb") as outfile:
            pickle.dump([table_x,table_y], outfile)        
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)        
        plt.plot(x_array, result_array , label=f.__name__ ,)
        table_number += 1
    
    plt.title(f'Plots')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.savefig(f'plots.png')



function_array = [prime_first_not_optimal , prime_first ,
                second_prime , second_prime_not_optimal , 
                prime_fourth , prime_third]
create_plot(function_array)

