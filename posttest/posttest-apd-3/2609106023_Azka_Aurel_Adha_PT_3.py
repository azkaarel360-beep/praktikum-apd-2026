nama = "azka"
NIM = 23
print("-- Selamat Datang di SPBU --")
data_diri = str(input("Masukkan Nama Panggilan Anda: ").lower())
nim = int(input("Masukkan NIM Anda: "))

if data_diri != nama or nim != NIM:
    print("Data yang dimasukkan tidak sesuai.")
else:
    print("Data yang dimasukkan sesuai.\n")

    Pertalite =10000.0
    Pertamax =12500.0
    Pertamax_Turbo =15000.0

    print("-------- Pilihan BBM ---------")
    print("Jenis BBM yang tersedia adalah: ")
    print("1. Pertalite       : Rp.", Pertalite)
    print("2. Pertamax        : Rp.", Pertamax)
    print("3. Pertamax Turbo  : Rp.", Pertamax_Turbo)
    bbm = int(input("Silahkan pilih jenis BBM Anda sesuai angka yang tertera: "))

    if bbm == 1:
        nama_bbm = "Pertalite"
        harga_bbm = Pertalite
        bensin = True
    elif bbm == 2:
        nama_bbm = "Pertamax"
        harga_bbm = Pertamax
        bensin = True
    elif bbm == 3:
        nama_bbm = "Pertamax Turbo"
        harga_bbm = Pertamax_Turbo
        bensin = True
    else:
        print("\nPilihan Tidak Tersedia")
        bensin = False

    if bensin == True:
        jumlah_liter = float(input("\nMasukkan jumlah liter yang ingin dibeli: "))
        total_harga = harga_bbm * jumlah_liter
        if jumlah_liter >= 10:
            diskon = total_harga * 0.1
        elif jumlah_liter >= 5:
            diskon = total_harga * 0.05
        else:
            diskon = 0

        print("\n------------- Cek Diskon Member -------------")
        status_member = str(input("\nApakah Anda merupakan member SPBU? (ya/tidak): ").lower())

        if status_member == "ya":
            diskon_member = total_harga * 0.02
        else:
            diskon_member = 0
        
        total_bayar_akhir = total_harga - diskon - diskon_member

        print("\n=================================================")
        print("                Struk Pembayaran       ")
        print("=================================================")
        print("|Data Pembeli          : ",data_diri)
        print("------------------------------------------------")
        print("|Jenis BBM yang dibeli : ",nama_bbm)
        print("------------------------------------------------")
        print("|Jumlah Liter          : ",jumlah_liter,"Liter")
        print("------------------------------------------------")
        print("|Total Harga           : Rp.",total_harga)
        print("------------------------------------------------")
        print("|Diskon                : Rp.",diskon)
        print("------------------------------------------------")
        print("|Diskon Member         : Rp.",diskon_member)
        print("------------------------------------------------")
        print("|Total Bayar Akhir     : Rp.",total_bayar_akhir)
        print("================================================")