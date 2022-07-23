from gaussJacobin import gaussJacobin, isGaussJacobin, display, displaySol

eqs = [
    [10,1,2,10],
    [1,10,1,20],
    [1,1,20,13]
]
print(isGaussJacobin(eqs))
display(eqs)
sol = gaussJacobin(eqs,3)
displaySol(sol)