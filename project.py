from datetime import datetime
import random
import matplotlib.pyplot as plt
from first import prime_first
from first import prime_first_non_optimal
array = [1,2,3,4,5,6,7,8,9,10,
         20,30,40,50,60,70,80,90,100,
         200,300,400,500,600,700,800,900,1000,
         2000,3000,4000,5000,6000,7000,8000,9000,10000,
         20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
def create_plot(function_array):
    for f in function_array:
        result_array = []
        x_array = []
        for i in array:
            now = datetime.now()
            f(i)
            if (datetime.now() - now).seconds > 10:
                break
            x_array.append(i)   
            result_array.append((datetime.now() - now).seconds +     round(((datetime.now() - now).microseconds * ((1 / 10) ** 6)), 3))
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)        
        plt.plot(x_array, result_array , label=f.__name__ ,)
    
    plt.title(f'Plots')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.savefig(f'plots.png')
    
function_array = [prime_first_non_optimal , prime_first]
create_plot(function_array)