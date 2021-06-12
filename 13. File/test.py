import sys
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'w')
    f.write(memo)
    f.write('\n')
    f.close()
    print('memo is saved')