def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n:
        print('天哪，费马弄错了！')
    else:
        print('不，那样不行')


check_fermat(1, 1, 2, 3)
