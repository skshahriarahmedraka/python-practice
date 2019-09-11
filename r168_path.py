from pathlib import Path
p1=Path("E:\python code\some_code")
print(p1.iterdir())
print(list(p1.iterdir()))
for a in p1.iterdir():
    print(a)
li=[p for p in p1.iterdir() if p.is_dir()]
print(li)
li1=[p for p in p1.glob("*.py")]
print(li1)