import random

def rand5():
    return random.randint(1,5)

def rand7():
    sum = 0
    for i in range(5):
        sum += rand5()
    #print(f'Return: {sum} -> {((sum-5)//3)+1}')
    return ((sum-5)//3 + 1)

def rnd7():
    sum = rand5() + rand5()
    return sum

if __name__ == "__main__":
    counts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
    for x in range(10000):
        val = rnd7()
        #print(f'{val}')
        counts[val] = counts[val] + 1        
    for i,j in counts.items():
        print(f'{i} : {counts[i]}')
    print("--------------------")
    # for i in range(5,26):
    #     print((i-5)//3)


        
