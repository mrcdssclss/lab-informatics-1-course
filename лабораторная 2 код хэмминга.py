sh = str(input())
st = ''
s1 = str((int(sh[0]) + int(sh[2]) + int(sh[4]) + int(sh[6])) % 2)
s2 = str((int(sh[1]) + int(sh[2]) + int(sh[5]) + int(sh[6])) % 2)
s3 = str((int(sh[3]) + int(sh[4]) + int(sh[5]) + int(sh[6])) % 2)
s = s1 + s2 + s3
if s == '110':
    st = str(abs(int(sh[2]) - 1)) + sh[4] + sh[5] + sh[6]
    print('Была ошибка в i1, исправленное сообщение:' + '\n' + st)
elif s == '101':
    st = sh[2] + str(abs(int(sh[4]) - 1)) + sh[5] + sh[6]
    print('Была ошибка в i2, исправленное сообщение:' + '\n' + st)
elif s == '011':
    st = sh[2] + sh[4] + str(abs(int(sh[5]) - 1)) + sh[6]
    print('Была ошибка в i3, исправленное сообщение:' + '\n' + st)
elif s == '111':
    st = sh[2] + sh[4] + sh[5] + str(abs(int(sh[6]) - 1))
    print('Была ошибка в i4, исправленное сообщение:' + '\n' + st)
else:
    st = sh[2] + sh[4] + sh[5] + sh[6]
    print('Ошибок не обнаружено, ваше сообщение:' + '\n' + st)
