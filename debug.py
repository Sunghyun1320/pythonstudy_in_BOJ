import math
import numpy as np

start = np.array([42.3, 63.5])    # 내공 위치
end = np.array([0, 0])     # 홀 위치
ball = np.array([15.5, 14])   # 목적구 위치

a_v = end - start

r = 5.73     # 반지름

a = end - start
b = end - ball
c = ball - start
# a = math.sqrt(x**2 + y**2)
# b = math.sqrt((end[0]-ball[0])**2+(end[1]-ball[1])**2)
# c = math.sqrt((ball[0]-start[0])**2 + (ball[1]-start[1])**2)

b = b + b * r / np.linalg.norm(b)
d = a - b

theta = np.arctan(d[1]/d[0])
theta = np.rad2deg(theta)

# da = np.arccos()
# ga = math.atan(x/y)
# print(math.degrees(ga))
# da = math.acos((a**2 + b**2 - c**2)/(2*a*b))
# d = math.sqrt((a*math.sin(da))**2+((b+2*r)-(a*(math.cos(da))))**2)
# na = math.acos((a**2+d**2-(b+2*r)**2)/(2*a*d))
# theta = ga + na
# temp_ga = math.degrees(ga)
# temp_na = math.degrees(na)

print(math.degrees(theta))


