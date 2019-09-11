try:
    f=open("raka1.txt")
    n=int(input("give me a int : "))
except ValueError as e :
    print("you have entered a non int value  ")
    print(e)
    print(type(e))
except (ZeroDivisionError,ValueError):
    print("zero division error")
else:
    print("no error has encountered")
finally:
    f.close()

print("program is running")