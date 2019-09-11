import pathlib
p1=pathlib.Path("datetime.PNG")
p2=pathlib.Path("G:/udemy pithon")
print(p1.is_file())
print(p2.is_file())
print(p1.is_dir())
print(p2.is_dir())
print("\n")
p1=pathlib.Path("G:/udemy pithon")
p2=pathlib.Path("copy code python/UVa-master")
p3=pathlib.Path.joinpath(p1,p2)#im
print(p3)
print("\n")
print(p1/p2)
print("\n")


import glob

p4=pathlib.Path(".")
print(p4)
print(p4.iterdir())

print(list(p4.iterdir()))

for i in range(10):
    x=next(p4.iterdir())
    print(x)
print(glob.glob("*.py"))

print("\n")
p4=pathlib.Path("E:\python code")
print(p4.glob("*.py"))
for i in p4.glob("*.py"):
    print(i)

print("\n")

p5=pathlib.Path("E:/python code/File1.py")
for i in p5.open():
    print(i)
print(p5.stat().st_size)
print(p5.suffix)#im