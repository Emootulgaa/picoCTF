from string import printable as pt

bet = pt[36:62]
num = pt[:10]
def lol(a):
    dec = ''
    for i in a:
        if i < 26:
            dec+=bet[i]
        elif i < 36:
            dec+=num[i%26]
        else:
            dec+='_'
    return dec

def decode(number):
    r = number % 37
    return r

def main():
    f = open("message.txt", "r", encoding="UTF-8")
    lst = f.read().split()
    # print(lst[0])

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    print('picoCTF{'+lol(dec_lst)+'}')

if __name__ == '__main__':
    main()
