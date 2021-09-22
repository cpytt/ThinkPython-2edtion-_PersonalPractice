# practice3-1
def right_justify(s):
    if len(s) > 70:
        print('error:length of s is more than 70')
    else:
        print(" " * (70 - len(s)), s)


right_justify('dasodas')
