print("masukan umur anda")
umur = int(input())
if umur < 13:
    print(" INI ADALAH ANAK ANAK silahkan isi apakah anda sendirian atau di antar, kalau di antar ketikan (y)dan kalau sendirian ketik (n)")
    untukAnak = input()
    if untukAnak == "y":
        print(untukAnak + " silahkan untuk mengisi data apakah sudah vaksin atau belum")
    else:
        print(untukAnak + " tidak boleh masuk")
        n = input()
        
        # pembatas
else:
    if umur < 19:
        print(str(umur) + " remaja")
    else:
        if umur < 26:
            print(str(umur) + " dewasa muda")
        else:
            if umur > 59:
                print(str(umur) + " tua")
            else:
                print(str(umur) + " dewasa")
print("apakah anda sudah di vaksin? kalau sudah ketik (sudah) kalau belum ketik (belum)")
vaksin = input()
if vaksin == "sudah":
    print(vaksin + ", silahkan boleh masuk mall")
else:
    if vaksin == "belum":
        print(vaksin + ", mohon maaf tidak boleh masuk mall")
    else:
        print(vaksin + " , mohon maaf tidak boleh masuk mall")
