import turtle
import time

t = time.localtime()
s = int(time.strftime("%S",t))
m = int(time.strftime("%M",t))
h = int(time.strftime("%H",t))
print(h,m,s)