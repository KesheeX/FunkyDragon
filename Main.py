import random  
from matplotlib import pyplot as pp
from tqdm import tqdm

def FiftyFifty():   #losowanie 0,1
    x = random.randint(0,1)
    return x

def CalcOne(x,y):   #pierwsze obliczenie
    xPrime = -0.4 * x - 1
    yPrime = -0.4 * y - 0.1
    results = []
    results.append(xPrime)
    results.append(yPrime)
    return results
def CalcTwo(x,y):   #2 obliczenie
    xPrime = 0.76 * x - 0.4 * y
    yPrime = 0.4 * x + 0.76 * y
    results = []
    results.append(xPrime)
    results.append(yPrime)
    return results

def avg(arr):   #średnia tablicy
    arr2 = arr
    a = sum(arr2) / len(arr2)
    return a

def size(arr):      #podaje najmniejszą i największą wartość tablicy
    arr2 = sorted(arr)
    a = [round(arr2[0], 1), round(arr2[len(arr2) - 1], 1)]
    return a

log = "a) \n"

xHold = 1   #przechowanie wartości x i y
yHold = 1

xArr = []   #tablice z wartościami x,y z każdej iteracji
yArr = []

for i in tqdm(range(0, 5000)):
    o = FiftyFifty()
    if o == 0:
        res = CalcOne(xHold,yHold)
        xHold = res[0]
        yHold = res[1]
    else:
        res = CalcTwo(xHold,yHold)
        xHold = res[0]
        yHold = res[1]

    log = log + "\n " + str(i) + "x = " + str(xHold) + ", y = " + str(yHold) + ", wylosowane = " + str(o)

    if i > 100: #dodanie wartości do tablicy
        xArr.append(xHold)
        yArr.append(yHold)


log = log + "\n c) \n Środek masy smoka to: (" + str(avg(xArr)) + ", " + str(avg(yArr)) + ")."
x = size(xArr)
y = size(yArr)
log = log + "\n d) \n Rozmiar smoka to: \n x = (" + str(x[0]) + ", " + str(x[1]) + ")\n y = (" + str(y[0]) + ", " + str(y[1]) + ")."    #okropne tworzenie tekstu


f= open("log.txt","w+") #tworzenie pliku tekstowego
f.write(log)

pp.plot(xArr,yArr, marker = ",", linewidth = 0) #tworzenie wykresu
pp.savefig("smok.png", dpi = 100)  #zapisanie wykresu
