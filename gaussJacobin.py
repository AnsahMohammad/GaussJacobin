#program to solve gauss jacobin Linear equation

# eqs = int(input("Enter number of equations : "))
# eqs_ = []
# for _ in range(eqs):
#     k = list(map(int,input("enter the coefficient in (ax1+bx2=c) order : \n").split(" ")))
#     eqs_.append(k)

def display(arr):
    fin = ""
    k = 0
    for each in arr[:-1]:
        fin += "({})x{} + ".format(str(each),k)
        k+=1
    fin = fin[:-2]
    fin += "= "+str(arr[-1])
    print(fin)

# print("Your equations are : ")
# for each in eqs_:
#     display(each)


def __rearrange(arr):
    for i in range(len(arr)):
        if(arr[i][i] != max(arr[i][:-1])):
            temp = arr[i]
            #finding the pposition of max
            for j in range(len(arr[i][:-1])):
                if arr[i][j] == max(arr[i][:-1]):
                    # print("re-arranging {0} to {1} and {1} to {0}".format(i,j))
                    arr[i] = arr[j]
                    arr[j] = temp
                    break

# for _ in range(int(eqs/2)):
#     __rearrange(eqs_)

# vars = [0 for i in range(len(eqs_[0]))]
# vars[-1] = 1

def __equating(arrk):
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

# iters = int(input("Enter number of iterations : "))
# for _ in range(iters):
#     __equating(eqs_)

def displaySol(sol):
    fin = ""
    k=0
    for each in sol:
        fin += "x{} = {}\n".format(k,sol[k])
        k+=1
    
    print(fin)


# print("Final coefficients are : ")
# displaySol(vars)

def gaussJacobin(eqs_,iters):
    eqs = len(eqs_)
    #re-arranging
    for _ in range(int(eqs/2)):
        __rearrange(eqs_)

    vars = [0 for i in range(len(eqs_[0]))]
    vars[-1] = 1

    for _ in range(iters):
        __equating(eqs_)

    return vars

def isGaussJacobin(eqs_):
    eqs = len(eqs_)
    #re-arranging
    for _ in range(int(eqs/2)):
        __rearrange(eqs_)
    
    for i in range(len(eqs_)):
        if eqs_[i][i] != max(eqs_[i][:-1]):
            return False
        
    return True
