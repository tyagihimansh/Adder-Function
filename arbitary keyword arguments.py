def adder(**arg):
    print(arg)     
    return(sum(arg.values()))

print(adder(first=1,secodn=3,third=5))
