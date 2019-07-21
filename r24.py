dic={"raka":"7/8","rakib":"18/3","shahin":"1/1"}
while True:
    print("enter a name(space to quit) : ")
    n=input()
    if(n==' '):
        break
    elif n in dic:
        print("the birthday of "+n+" is "+dic[n])
        continue
    else :
        print("i have no information of him/her")
        print("give me his/her birth date")
        b=input()
        dic[n]=b
        print("document is updated")