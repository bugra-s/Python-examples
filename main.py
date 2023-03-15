def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    return sayi1 / sayi2

islemTipi = {
    "+": toplama,
    "-": cikarma,
    "*": carpma,
    "/": bolme
}

def hesap_makinesi():
    for simge in islemTipi:
        print(f"{simge}")

    devam = True

    while devam:
        secilenSimge = input(f"Yapmak istediğiniz işlem tipini seçiniz.\n")
        sayi1 = int(input("Birinci sayıyıyı giriniz..."))
        sayi2 = int(input("İkinci sayıyı giriniz..."))
        hesaplama = islemTipi[secilenSimge]
        cevap = hesaplama(sayi1, sayi2)
        print(f"{sayi1} {secilenSimge} {sayi2} = {cevap}")

        son = input("Yeni bir işlem yapmak istiyor musunuz? '1=Evet','2=Hayır'\n")
        if son == "1":
            devam = True
        else:
            devam = False


hesap_makinesi()