def przeliczanie_ip():
    print('hello')
    
    global ip_bin, list_ip_bin, int_list_ip
    ip = input('podaj ip w formacie xxx xxx xxx xxx ')
    ip_list = ip.split()
    list_ip_bin = []
    for i in ip_list:
        list_ip_bin.append(bin(int(i))[2:].zfill(8))
    print(list_ip_bin)


def przeliczanie_maski():
    global prefix_int, mask_bin, list_mask_bin
    mask = input('podaj maske w formacie xxx xxx xxx xxx ')
    mask_list = mask.split()
    list_mask_bin = []
    for i in mask_list:
        list_mask_bin.append(bin(int(i))[2:].zfill(8))
    print(list_mask_bin)


def prefix():
    global pref
    pref = 0

    for i in list_mask_bin:
        for j in i:
            if j == ('1'):
                pref = pref + 1
    print('prefiks: ', pref)


def adres_sieci():
    global siecg, t, g, b, n
    # print(list_ip_bin)
    c = 0
    siec = []
    d = 0

    for a in list_mask_bin:
        # print(a)
        for b in a:
            # print(c,d)
            if b == ('1'):
                siec.append(list_ip_bin[d][c])
            c += 1
        c = 0
        d += 1

    for x in range(pref, 32):
        siec.append('0')
    # print(siec)

    i = 0
    j = 8
    siec_1 = []
    for z in siec:
        # siec_1.append(siec[i:j])
        s = ''.join(siec[i:j])
        siec_1.append(s)
        i += 8
        j += 8
        if j > 32:
            break
    siec_2 = [int(i) for i in siec_1]
    # print(siec_2)
    t = int(siec_1[0], 2)
    g = int(siec_1[1], 2)
    b = int(siec_1[2], 2)
    n = int(siec_1[3], 2)
    print('adres sieci to : ', t, '.', g, '.', b, '.', n)


def broadcast():
    c = 0
    siec = []
    d = 0

    for a in list_mask_bin:
        # print(a)
        for b in a:
            # print(c,d)
            if b == ('1'):
                siec.append(list_ip_bin[d][c])
            c += 1
        c = 0
        d += 1

    for x in range(pref, 32):
        siec.append('1')
    # print(siec)
    global y, u, o, p
    i = 0
    j = 8
    siec_1 = []
    for z in siec:
        # siec_1.append(siec[i:j])
        s = ''.join(siec[i:j])
        siec_1.append(s)
        i += 8
        j += 8
        if j > 32:
            break
    siec_2 = [int(i) for i in siec_1]
    # print(siec_2)
    p = int(siec_1[0], 2)
    o = int(siec_1[1], 2)
    u = int(siec_1[2], 2)
    y = int(siec_1[3], 2)
    print('adres rozgloszeniowy : ', p, '.', o, '.', u, '.', y)


def max_min():
    maks = n + 1
    mini = y - 1

    host = ((u - b + 1) * 256) - 2
    print('liczba hostow: ', host)
    print('Pierwszy Host: ', t, '.', g, '.', b, '.', maks)
    print('Ostatni Host: ', p, '.', o, '.', u, '.', mini)


print('-----------IP----------------')
przeliczanie_ip()
print('-----------MASKA--------------')
przeliczanie_maski()
prefix()
adres_sieci()
broadcast()
max_min()
