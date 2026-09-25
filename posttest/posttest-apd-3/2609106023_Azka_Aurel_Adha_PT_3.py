nama = "azka"
NIM = 23
print("-- Selamat Datang di SPBU --")
data_diri = str(input("Masukkan Nama Panggilan Anda: ").lower())
nim = int(input("Masukkan NIM Anda: "))

if data_diri != nama or nim != NIM:
    print("Data yang dimasukkan tidak sesuai.")
else:
    print("Data yang dimasukkan sesuai.\n")

    Pertalite =10000
    Pertamax =12500    
    Pertamax_Turbo =15000
    jenis_bbm = [Pertalite, Pertamax, Pertamax_Turbo]

    print("-------- Pilihan BBM ---------")
    print("Jenis BBM yang tersedia adalah: ")
    print("1. Pertalite       : Rp.", jenis_bbm[0])
    print("2. Pertamax        : Rp.", jenis_bbm[1])
    print("3. Pertamax Turbo  : Rp.", jenis_bbm[2])
    bbm = int(input("Silahkan pilih jenis BBM Anda sesuai angka yang tertera: "))

# ini pertalite
    if bbm == 1:
        nama_bbm = "Pertalite"
        jumlah_liter = float(input("Masukkan jumlah liter yang ingin dibeli: "))
        total_harga = (jenis_bbm[0] * jumlah_liter)
    # cek diskon
        if jumlah_liter >= 10:
            diskon = total_harga * 0.1
            # print("\nSelamat Anda mendapatkan diskon 10%.")
        elif jumlah_liter >= 5:
            diskon = total_harga * 0.05
            # print("\nSelamat Anda mendapatkan diskon` 5%.")
        else:
            diskon = 0
            # print("\nHarga Normal yaa")
        total_bayar = total_harga - diskon
        # print("Total yang harus dibayar adalah Rp.", total_bayar)

# cek diskon member
        print("\n------------- Cek Diskon Member -------------")
        status_member = str(input("\nApakah Anda merupakan member SPBU? (ya/tidak): ").lower()) 
        if status_member == "ya":
            diskon_member = total_harga * 0.02
            # print("\nSelamat Anda mendapatkan diskon member 2%.")
        else:
            diskon_member = 0
            # print("\nMaaf Anda tidak mendapatkan diskon member.")
        total_bayar_akhir = total_bayar - diskon_member
        # print("Total yang harus dibayar adalah Rp.", total_bayar_akhir)

# ini pertamax
    if bbm == 2:
        nama_bbm = "Pertamax"
        jumlah_liter = float(input("Masukkan jumlah liter yang ingin dibeli: "))
        total_harga = (jenis_bbm[1] * jumlah_liter)
    # cek diskon
        if jumlah_liter >= 10:
            diskon = total_harga * 0.1
            # print("\nSelamat Anda mendapatkan diskon 10%.")
        elif jumlah_liter >= 5:
            diskon = total_harga * 0.05
            # print("\nSelamat Anda mendapatkan diskon 5%.")
        else:
            diskon = 0
            # print("\nHarga Normal yaa")
        total_bayar = total_harga - diskon
        # print("Total yang harus dibayar adalah Rp.", total_bayar)

# cek diskon member
        print("\n------------- Cek Diskon Member -------------")
        status_member = str(input("\nApakah Anda merupakan member SPBU? (ya/tidak): ").lower()) 
        if status_member == "ya":
            diskon_member = total_harga * 0.02
            # print("\nSelamat Anda mendapatkan diskon member 2%.")
        else:
            diskon_member = 0
            # print("\nMaaf Anda tidak mendapatkan diskon member.")
        total_bayar_akhir = total_bayar - diskon_member
        # print("Total yang harus dibayar adalah Rp.", total_bayar_akhir)

# ini pertamax turbo
    if bbm == 3:
        nama_bbm = "Pertamax Turbo"
        jumlah_liter = float(input("Masukkan jumlah liter yang ingin dibeli: "))
        total_harga = (jenis_bbm[2] * jumlah_liter)
    # cek diskon
        if jumlah_liter >= 10:
            diskon = total_harga * 0.1
            # print("\nSelamat Anda mendapatkan diskon 10%.")
        elif jumlah_liter >= 5:
            diskon = total_harga * 0.05
            # print("\nSelamat Anda mendapatkan diskon 5%.")
        else:
            diskon = 0
            # print("\nHarga Normal yaa")
        total_bayar = total_harga - diskon

# cek diskon member
        print("\n------------- Cek Diskon Member -------------")
        status_member = str(input("\nApakah Anda merupakan member SPBU? (ya/tidak): ").lower()) 
        if status_member == "ya":
            diskon_member = total_harga * 0.02
            # print("\nSelamat Anda mendapatkan diskon member 2%.")
        else:
            diskon_member = 0
            # print("\nMaaf Anda tidak mendapatkan diskon member.")
        total_bayar_akhir = total_bayar - diskon_member
        # print("Total yang harus dibayar adalah Rp.", total_bayar_akhir)

#OUTPUT 
print("\n=================================================")
print("                Struk Pembayaran       ")
print("=================================================")
print("|Jenis BBM yang dibeli : ",nama_bbm)
print("------------------------------------------------")
print("|Jumlah Liter          : ",jumlah_liter,"Liter")
print("------------------------------------------------")
print("|Total Harga           : Rp.",total_harga)
print("------------------------------------------------")
print("|Diskon                : Rp.",diskon)
print("------------------------------------------------")
print("|Total Bayar           : Rp.",total_bayar)
print("------------------------------------------------")
print("|Diskon Member         : Rp.",diskon_member)
print("------------------------------------------------")
print("|Total Bayar Akhir     : Rp.",total_bayar_akhir)
print("================================================")



