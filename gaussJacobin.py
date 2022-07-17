#program to solve gauss jacobin Linear equation
eqs = int(input("Enter number of equations : "))
eqs_ = []
for _ in range(eqs):
    k = list(map(int,input("enter the coefficient in (ax1+bx2=c) order : \n").split(" ")))
    eqs_.append(k)

vars = [0 for i in range(len(eqs_[0]))]
vars[-1] = 1

def equating(arrk):
    global vars
    vark = []
    for arr in arrk:
        if arr != None:
            sum = 0
            coeff = arr[-1]
            sum += coeff
            div = 1
            max_ = max(arr[:-1])
            for i in range(len(arr)-1):
                if arr[i] != max_:
                    sum -= arr[i]*vars[i]
                else:
                    div = arr[i]
            
            sum /= div
            vark.append(sum)
    
    vars = vark

iters = int(input("Enter number of iterations : "))
for _ in range(iters):
    equating(eqs_)

print("Final coefficients are : "+str(vars))