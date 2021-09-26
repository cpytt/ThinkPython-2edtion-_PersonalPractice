# minutes = 105
# print(minutes / 60)
# print('hours =', minutes // 60)  # 用向下取整除法操作符实现丢弃小数部分，得到整数的小时数
# print('minutes =', minutes % 60)  # 用求模操作符求出余数，得到剩余的分钟数

# print(5 < 5)

x = 9
if 0 < x < 10:
    print('True')
else:
    print('False')
n = 6
if n % 2 == 0 or n % 3 == 0:
    print('True')
else:
    print('False')

print(not (1 > 2))
print(36 and True)


# choice='a'
# if choice =='a':
#     draw_a()
# elif choice == 'b':
#     draw_b()
# else:
#     draw_c()

def countdown(m):
    if m <= 0:
        print('Blastoff!')
    else:
        print(m)
        countdown(m - 1)


countdown(8)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


print_n('cpy',3)

prompt = 'what...is the airspeed vleocity of an unladen swallow?\n'
speed =input(prompt)
print(int(speed))