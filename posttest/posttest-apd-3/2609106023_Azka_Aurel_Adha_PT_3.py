data_diri = str(input("Masukkan Nama Anda: ").lower())
nim = int(input("Masukkan NIM Anda: "))

if data_diri != "azka" or nim != 23:
    print("Data yang dimasukkan tidak sesuai.")
else:
    print("Data yang dimasukkan sesuai.")

    Pertalite =10000
    Pertamax =12500    
    Pertamax_Turbo =15000

    jenis_bbm = [Pertalite, Pertamax, Pertamax_Turbo]

    print("Jenis BBM yang tersedia adalah Pertalite, Pertamax, Pertamax Turbo")
    bbm = int(input("Silahkan pilih jenis BBM Anda: "))

    # if bbm == 1:
    #     print("Harga Pertalite adalah Rp. ",jenis_bbm[0])
    # elif bbm == 2:
    #     print("Harga Pertamax adalah Rp. ",jenis_bbm[1])
    # else:
    #     print("Harga Pertamax Turbo adalah Rp. ",jenis_bbm[2])


# ini pertalite
    if bbm == 1:
        print("Harga Pertalite adalah Rp. ", jenis_bbm[0])
        jumlah_liter = int(input("Masukkan jumlah liter yang ingin dibeli: "))
        if jumlah_liter >= 10:
            total_harga = (jenis_bbm[0] * jumlah_liter)
            diskon = 0.1 * total_harga
            total_bayar = total_harga - diskon
            print("Anda Mendapatkan diskon 10%. Total yang harus dibayar adalah Rp. ", total_bayar)
        elif jumlah_liter >= 5:
            total_harga = (jenis_bbm[0] * jumlah_liter)
            diskon = 0.05 * total_harga
            total_bayar = total_harga - diskon
            print("Anda mendapatkan diskon 5%. Total yang harus dibayar adalah Rp. ", total_bayar)
        else:
            total_harga = jenis_bbm[0] * jumlah_liter
            print("Anda tidak mendapatkan diskon. Total yang harus dibayar adalah Rp. ", total_harga)

# ini pertamax
    elif bbm == 2:
        print("Harga Pertamax adalah Rp. ",jenis_bbm[1])
        jumlah_liter = int(input("Masukkan jumlah liter yang ingin dibeli: "))
        if jumlah_liter >= 10:
            total_harga = (jenis_bbm[1] * jumlah_liter)
            diskon = 0.1 * total_harga
            total_bayar = total_harga - diskon
            print("Anda Mendapatkan diskon 10%. Total yang harus dibayar adalah Rp. ", total_bayar)
        elif jumlah_liter >= 5:
            total_harga = (jenis_bbm[1] * jumlah_liter)
            diskon = 0.05 * total_harga
            total_bayar = total_harga - diskon
            print("Anda mendapatkan diskon 5%. Total yang harus dibayar adalah Rp. ", total_bayar)
        else:
            total_harga = jenis_bbm[1] * jumlah_liter
            print("Anda tidak mendapatkan diskon. Total yang harus dibayar adalah Rp. ", total_harga)

# ini pertamax turbo
    else:
        print("Harga Pertamax Turbo adalah Rp. ",jenis_bbm[2])
        jumlah_liter = int(input("Masukkan jumlah liter yang ingin dibeli: "))
        if jumlah_liter >= 10:
            total_harga = (jenis_bbm[2] * jumlah_liter)
            diskon = 0.1 * total_harga
            total_bayar = total_harga - diskon
            print("Anda Mendapatkan diskon 10%. Total yang harus dibayar adalah Rp. ", total_bayar)
        elif jumlah_liter >= 5:
            total_harga = (jenis_bbm[2] * jumlah_liter)
            diskon = 0.05 * total_harga
            total_bayar = total_harga - diskon
            print("Anda mendapatkan diskon 5%. Total yang harus dibayar adalah Rp. ", total_bayar)
        else:
            total_harga = jenis_bbm[2] * jumlah_liter
            print("Anda tidak mendapatkan diskon. Total yang harus dibayar adalah Rp. ", total_harga)