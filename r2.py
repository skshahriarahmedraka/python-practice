x=True
while x==True:
    t=int(input())
    a=int(input())
    b=int(input())
    y=str((pow(t,a)-1)/(pow(t,b)-1))
    
    if(len(y)<100):
        print(f'({t}^{a}-1)/({t}^{b}-1) {y}')
    else:
        print(f'({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits')