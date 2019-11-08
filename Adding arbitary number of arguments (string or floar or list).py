def adder(*arg):
    su=arg[0]
    for i in range(len(arg)-1):
        su=su+arg[i+1]
    return(su)

print(adder('cold',' play',' band'))
print(adder([1,2,3],[4,5,6]))
print(adder(4.3,1.3))
