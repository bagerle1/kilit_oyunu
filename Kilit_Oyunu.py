#!!!Programa bakarken rapordaki Programcı Kataloğuna bakmanız şiddetle tavsiye edilir.

def input_alici(min=-1000000, max=1000000, normal_mesaj="", hata_mesaji=""):
    try:
        deger = int(input(normal_mesaj))
        if deger < min or deger > max:
            print(f"Değer {min} ve {max} aralığında olmalıdır. ")
            return input_alici(min, max, normal_mesaj,hata_mesaji)
        else:
            return deger
    except ValueError:
        print(hata_mesaji)
        return input_alici(min, max, normal_mesaj,hata_mesaji)

def alan_yapici(oyun_alani, sutun_satir, kar1, kar2, suanki_oyuncu_tas_kordinat, siradaki_oyuncu_tas_kordinat):
    for no in range(sutun_satir):                     #Gerekli iki boyutlu listeyi ve oyun alanının ilk halini hazırlayan
        temp_liste = [1,no + 1]                       #fonksyon
        siradaki_oyuncu_tas_kordinat.append(temp_liste)
        temp_liste = [sutun_satir, no + 1]
        suanki_oyuncu_tas_kordinat.append(temp_liste)
    temp_liste = ["/"] * (sutun_satir+2)
    oyun_alani.append(temp_liste)
    temp_liste = [kar2] * (sutun_satir+2)
    temp_liste[0], temp_liste[sutun_satir + 1] = "/", "/"
    oyun_alani.append(temp_liste)
    for sayac in range(sutun_satir - 2):
        temp_liste = [" "]*(sutun_satir+2)
        temp_liste[0],temp_liste[sutun_satir+1] = "/", "/"
        oyun_alani.append(temp_liste)
    temp_liste = [kar1] * (sutun_satir+2)
    temp_liste[0], temp_liste[sutun_satir + 1] = "/", "/"
    oyun_alani.append(temp_liste)
    temp_liste = ["/"] * (sutun_satir + 2)
    oyun_alani.append(temp_liste)

def alan_yazdirici(oyun_alani, sutun_satir, harfler):          #Genel olarak oyun alanını yazdıran fonksyon.
    print("   ", end="")                                       #Karmaşık gözükse de birebir düzgün gözükmesi için
    for no in range(sutun_satir):                              #gereken detaylardan başka bişey yok.
        print(f" {harfler[no]}  ", end="")
    print("")
    for satir_no in range(1,sutun_satir+1):
        print("  ", end="")
        for x in range(sutun_satir * 4 + 1):
            print("-", end="")
        print("  ")
        print(f"{satir_no} ", end="")
        for sutun_no in range(1,sutun_satir+1):
            print(f"| {oyun_alani[satir_no][sutun_no]} ", end="")
        print("|", end="")
        print(f" {satir_no}")
    print("  ", end="")
    for x in range(sutun_satir * 4 + 1):
        print("-", end="")
    print("")
    print("  ", end="")
    for no in range(sutun_satir):
        print(f"  {harfler[no]} ", end="")
    print("")
def etraftaki_sembol_bulucu(oyun_alani,istenilen_kordinat):
    etraftaki_semboller_list = []                                              #Bu fonksyon bir kordinat etrafındaki sembolleri bulup
    etraftaki_semboller_list.append(oyun_alani[istenilen_kordinat[0] - 1][istenilen_kordinat[1]])  #bunları bir listeye atar. Bu liste üstteki sembol 0.
    etraftaki_semboller_list.append(oyun_alani[istenilen_kordinat[0]][istenilen_kordinat[1] + 1])  #eleman olacak şekilde başlayıp saat yönüne doğru dönerek
    etraftaki_semboller_list.append(oyun_alani[istenilen_kordinat[0] + 1][istenilen_kordinat[1]])  #sembollerden bir liste yapar.
    etraftaki_semboller_list.append(oyun_alani[istenilen_kordinat[0]][istenilen_kordinat[1] - 1])
    return etraftaki_semboller_list

def tas_alma_kontrolu(oyun_alani,oynatilan_tas_kordinat, suanki_oyuncu, siradaki_oyuncu):   #Alınacak taşı bulma işlemi burda yapılır
    etraftaki_semboller = etraftaki_sembol_bulucu(oyun_alani, oynatilan_tas_kordinat)
    kordinat = [-1, -1]
    sembol_no = 0
    for sembol in etraftaki_semboller:                  #Açıklama programcı kataloğunda
        if sembol == siradaki_oyuncu:
            if sembol_no == 0:
                kose_kontrol_sembolleri = etraftaki_sembol_bulucu(oyun_alani, [oynatilan_tas_kordinat[0] - 1,oynatilan_tas_kordinat[1]])
                if kose_kontrol_sembolleri.count("/") == 2 and kose_kontrol_sembolleri.count(suanki_oyuncu) == 2:kordinat = [oynatilan_tas_kordinat[0]-1, oynatilan_tas_kordinat[1]]
                elif oyun_alani[oynatilan_tas_kordinat[0]-2][oynatilan_tas_kordinat[1]] == suanki_oyuncu:kordinat = [oynatilan_tas_kordinat[0]-1, oynatilan_tas_kordinat[1]]
            elif sembol_no == 1:
                kose_kontrol_sembolleri = etraftaki_sembol_bulucu(oyun_alani, [oynatilan_tas_kordinat[0],oynatilan_tas_kordinat[1] + 1])
                if kose_kontrol_sembolleri.count("/") == 2 and kose_kontrol_sembolleri.count(suanki_oyuncu) == 2:kordinat = [oynatilan_tas_kordinat[0], oynatilan_tas_kordinat[1] + 1]
                elif oyun_alani[oynatilan_tas_kordinat[0]][oynatilan_tas_kordinat[1] + 2] == suanki_oyuncu:
                    kordinat = [oynatilan_tas_kordinat[0] , oynatilan_tas_kordinat[1] + 1]
            elif sembol_no == 2:
                kose_kontrol_sembolleri = etraftaki_sembol_bulucu(oyun_alani, [oynatilan_tas_kordinat[0] + 1,oynatilan_tas_kordinat[1]])
                if kose_kontrol_sembolleri.count("/") == 2 and kose_kontrol_sembolleri.count(suanki_oyuncu) == 2:
                    kordinat = [oynatilan_tas_kordinat[0] + 1, oynatilan_tas_kordinat[1]]
                elif oyun_alani[oynatilan_tas_kordinat[0] + 2][oynatilan_tas_kordinat[1]] == suanki_oyuncu:
                    kordinat = [oynatilan_tas_kordinat[0], oynatilan_tas_kordinat[1]+1]
            else:
                kose_kontrol_sembolleri = etraftaki_sembol_bulucu(oyun_alani, [oynatilan_tas_kordinat[0],oynatilan_tas_kordinat[1] - 1])
                if kose_kontrol_sembolleri.count("/") == 2 and kose_kontrol_sembolleri.count(suanki_oyuncu) == 2:
                    kordinat = [oynatilan_tas_kordinat[0], oynatilan_tas_kordinat[1] - 1]
                if oyun_alani[oynatilan_tas_kordinat[0]][oynatilan_tas_kordinat[1] - 2] == suanki_oyuncu:
                    kordinat = [oynatilan_tas_kordinat[0], oynatilan_tas_kordinat[1]-1]
        sembol_no+=1
    return kordinat

def oyun_update(oyun_alani, oyuncu1, oyuncu2, sutun_satir, harfler, suanki_oyuncu_tas_kordinat, siradaki_oyuncu_tas_kordinat):
    KORDINAT_GIRDI_MAX_UZUNLUK = 4
    kazanan = "yok"
    suanki_oyuncu = oyuncu1
    siradaki_oyuncu = oyuncu2
    suanki_oyuncu_tas_sayi = sutun_satir
    siradaki_oyuncu_tas_sayi = sutun_satir
    while kazanan == "yok":
        hatali = True
        while hatali:
            hareket_konumlari = input(f"Oyuncu {suanki_oyuncu}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ")
            try:
                hareket_konumlari = hareket_konumlari.replace(" ", "")
                hareket_konumlari = hareket_konumlari.upper()
                hareket_konumlari = hareket_konumlari.replace(hareket_konumlari[1], str(harfler.index(hareket_konumlari[1]) + 1), 1)
                hareket_konumlari = hareket_konumlari.replace(hareket_konumlari[3], str(harfler.index(hareket_konumlari[3]) + 1), 1)
                hareket_konumlari = list(map(int, hareket_konumlari))       #Burada stringi eleman eleman bir liste yapabilmek için
                if len(hareket_konumlari) > KORDINAT_GIRDI_MAX_UZUNLUK:     #map fonksyonunu kullandım.
                    print("Fazla karakter girdiniz.")
                elif (int(hareket_konumlari[0]) not in range(1, sutun_satir + 1)) or (int(hareket_konumlari[1]) not in range(1, sutun_satir + 1)) or (int(hareket_konumlari[2]) not in range(1, sutun_satir + 1)) or (int(hareket_konumlari[3]) not in range(1, sutun_satir + 1)):
                    print("Hatalı giriş yapılmıştır.")
                elif hareket_konumlari[0:2] not in suanki_oyuncu_tas_kordinat:
                    print("Seçilen yerde taşınız yok")
                elif hareket_konumlari[0] == hareket_konumlari[3] and hareket_konumlari[1] == hareket_konumlari[2]:
                    print("Taşı aynı yere oynadınız.")
                elif hareket_konumlari[2:4] in suanki_oyuncu_tas_kordinat or hareket_konumlari[2:4] in siradaki_oyuncu_tas_kordinat:
                    print("Gidilecek yerde başka bir taş var.")
                elif hareket_konumlari[0] != hareket_konumlari[2] and hareket_konumlari[1] != hareket_konumlari[3]:
                    print("Taşlar sadece çizgisel hareket edebilir.")
                else:
                    hatali = False
                    if hareket_konumlari[1] == hareket_konumlari[3]:          #Gidilecek yer ile arada taşın olup olmadığının kontrolü
                        sirali_aralik = sorted([hareket_konumlari[0],hareket_konumlari[2]])
                        for satir in range(sirali_aralik[0]+1, sirali_aralik[1]):
                            if oyun_alani[satir][hareket_konumlari[1]] == siradaki_oyuncu or oyun_alani[satir][hareket_konumlari[1]] == suanki_oyuncu:
                                print("Gidilecek yer ile taş arasında başka bir taş var.")
                                hatali = True
                                break
                    else:
                        sirali_aralik = sorted([hareket_konumlari[1],hareket_konumlari[3]])
                        for sutun in range(sirali_aralik[0]+1, sirali_aralik[1]):
                            if oyun_alani[hareket_konumlari[0]][sutun] == siradaki_oyuncu or oyun_alani[hareket_konumlari[0]][sutun] == suanki_oyuncu:
                                print("Gidilecek yer ile taş arasında başka bir taş var.")
                                hatali = True
                                break
                    if hatali == False:
                        oyun_alani[hareket_konumlari[2]][hareket_konumlari[3]]= oyun_alani[hareket_konumlari[0]][hareket_konumlari[1]]
                        oyun_alani[hareket_konumlari[0]][hareket_konumlari[1]]= " "
                        suanki_oyuncu_tas_kordinat[suanki_oyuncu_tas_kordinat.index([hareket_konumlari[0] , hareket_konumlari[1]])] = [hareket_konumlari[2], hareket_konumlari[3]]
            except IndexError:
                print("Hatalı giriş yapılmıştır.")
            except ValueError:
                print("Hatalı giriş yapılmıştır.")
        alinan_tas_kordinat_gecici = tas_alma_kontrolu(oyun_alani,hareket_konumlari[2:4], suanki_oyuncu, siradaki_oyuncu)
        alinan_tas_kordinat_sakla = []
        while alinan_tas_kordinat_gecici != [-1, -1]:
            oyun_alani[alinan_tas_kordinat_gecici[0]][alinan_tas_kordinat_gecici[1]] = " "
            alinan_tas_kordinat_sakla.append(alinan_tas_kordinat_gecici)
            siradaki_oyuncu_tas_kordinat.remove(alinan_tas_kordinat_gecici)
            siradaki_oyuncu_tas_sayi -= 1
            alinan_tas_kordinat_gecici = tas_alma_kontrolu(oyun_alani, hareket_konumlari[2:4], suanki_oyuncu, siradaki_oyuncu)
        alan_yazdirici(oyun_alani, sutun_satir, harfler)
        for kordinat in alinan_tas_kordinat_sakla:
            print(f"{kordinat[0]}{harfler[kordinat[1] - 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
        if suanki_oyuncu_tas_sayi == 1:
            kazanan = oyuncu2
        elif siradaki_oyuncu_tas_sayi == 1:
            kazanan = oyuncu1
        suanki_oyuncu_tas_sayi,siradaki_oyuncu_tas_sayi=siradaki_oyuncu_tas_sayi,suanki_oyuncu_tas_sayi
        suanki_oyuncu, siradaki_oyuncu = siradaki_oyuncu, suanki_oyuncu
        suanki_oyuncu_tas_kordinat, siradaki_oyuncu_tas_kordinat = siradaki_oyuncu_tas_kordinat[:], suanki_oyuncu_tas_kordinat[:]
    return kazanan

def main():
    MIN_SUTUN = 4
    MAX_SUTUN = 8
    KARAKTER_UZUNLUGU = 1
    devam = "E"
    while devam in "Ee":
        oyun_alani = []
        suanki_oyuncu_tas_kordinat = []
        siradaki_oyuncu_tas_kordinat = []
        harfler = ["A", "B", "C", "D", "E", "F", "G", "H"]
        kar1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz: ")
        kar2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz: ")
        while len(kar1) != KARAKTER_UZUNLUGU or len(kar2) != KARAKTER_UZUNLUGU or kar1 == "/" or kar2 == "/":
            print("Kişi başı en fazla bir karakter olmalıdır, boşluk olmamalı ve / karakteri olmamalıdır.")
            kar1 = input("karakter1: ")
            kar2 = input("karakter2: ")
        sutun_satir = input_alici(MIN_SUTUN, MAX_SUTUN, "Oyun alanının satır/sütun sayısını giriniz(4-8): ","Yanlış karakter girdiniz.")
        alan_yapici(oyun_alani, sutun_satir, kar1, kar2, suanki_oyuncu_tas_kordinat, siradaki_oyuncu_tas_kordinat)
        alan_yazdirici(oyun_alani,sutun_satir,harfler)
        kazanan = oyun_update(oyun_alani, kar1, kar2, sutun_satir, harfler, suanki_oyuncu_tas_kordinat, siradaki_oyuncu_tas_kordinat)

        print(f"Oyuncu {kazanan} oyunu kazandı.")
        devam = input("Tekrar oynamak ister misiniz(E/H)?:")
        while devam not in"EeHh":
            devam = input("Yanlış Harf girdiniz. Yeniden giriniz: ")
main()
