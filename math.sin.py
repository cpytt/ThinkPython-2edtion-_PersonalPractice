import math

degree = 60.0
radians = degree / 180.0 * math.pi

print(math.cos(math.pi))
print((math.cos(radians)))
print(math.cos(math.pi/3.0))
print(math.cos(math.pi/2.0))
print(math.sin(math.pi))
print(1/2.0)
if math.cos(radians) == 1/2.0:
    print('cos is ok')
else:
    print('no')

print(math.sin(radians))
print(math.sqrt(3)/2)
if math.sin(radians) == math.sqrt(3)/2:
    print('sin is ok')
else:
    print('no')

print(math.tan(radians))
print(math.sqrt(3))
if math.tan(radians) == math.sqrt(3):
    print('tan is ok')
else:
    print('no')
