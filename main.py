s = input('Введите слово ')
def dz(s):
    return s[::-1]==s
while True:
    if dz(s):
        print('True')
        break
    else:
        print('False')
        break