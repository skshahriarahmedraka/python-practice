from pathlib import Path
import os
print(Path.home())
p1=Path.cwd()

print(Path.stat(p1))
p2=Path("E:/python code/r165_path_prac.py")
os.rename("E:/python code/r165_path_prac.py","E:/python code/r165_path_practice.py")