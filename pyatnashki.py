
def show(a):
    print('_' * 13)
    for i in a:
        for j in i:
            if j == 16 and not win:
                print("|  ", end='')
            else:
                print("|", j, ' ' * (1 - j // 10), sep='', end='')
        print('|')
        print('_' * 13)
