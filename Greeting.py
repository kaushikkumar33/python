import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
H=int(time.strftime("%H"))
M=int(time.strftime("%M"))
s=int(time.strftime("%S"))
if (H<=12):
    print("Good morning")
else:
    print("Good evening")

