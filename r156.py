#!/usr/bin/env python
import psutil
# gives a single float value
print(psutil.cpu_percent())
print("\n")
# gives an object with many fields
print(psutil.virtual_memory())
print("\n")
# you can convert that object to a dictionary 
print(dict(psutil.virtual_memory()._asdict()))