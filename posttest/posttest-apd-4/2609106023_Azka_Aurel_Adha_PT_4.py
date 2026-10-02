username_benar = "azka"
nim_benar = "023"
status = True
data_nama = []
data_kelas = []
data_ikut_ujian = []
data_nilai = []
data_kategori = []

print("-------- Validasi Login ---------")
for i in range(1,4):
    username_input = input("Silahkan Masukkan Username Anda: ")
    nim_input = input("Silahkan Masukkan Password Anda: ")
    if username_input == username_benar and nim_input == nim_benar:
        print("-------- Login Berhasil --------")
        while status == True:
            print("\n-------- Data Siswa --------")
            nama = input("Masukkan Nama Siswa: ")
            kelas = input("Masukkan Kelas Siswa: ")

            status_ujian = input("\nApakah Siswa Tersebut Ikut Ujian? (ya/tidak): ")
            while status_ujian not in ["ya", "tidak"]:
                print("\nSilahkan Jawab ya/tidak")
                status_ujian = input("\nApakah Siswa Tersebut Ikut Ujian? (ya/tidak): ")
            if status_ujian == "ya":
                soal_benar = int(input("\nDari 20 Soal, Masukkan Jumlah Soal Benar: "))
                soal_salah = int(input("Masukkan Jumlah Soal Salah: "))
                nilai_ujian = soal_benar * 5
                if 80 <= nilai_ujian <= 100:
                    kategori_ujian = "Sangat Baik"
                elif 60 <= nilai_ujian <= 79:
                    kategori_ujian = "Baik"
                elif 40 <= nilai_ujian <= 59:
                    kategori_ujian = "Cukup"
                else:
                    kategori_ujian = "Perlu Belajar Lagi"
            elif status_ujian == "tidak":
                nilai_ujian = 0
                kategori_ujian = "Tidak Ikut Ujian"

            data_nama += [nama]
            data_kelas += [kelas]
            data_ikut_ujian += [status_ujian]
            data_nilai += [nilai_ujian]
            data_kategori += [kategori_ujian]

            cek = input("\nApakah ingin menginput data lagi? (ya/tidak): ")
            if cek == "tidak":
                status = False
                break
        break
    else:
        sisa_percobaan = 3 - i
        print("Login Gagal, Username atau Password Salah")
        if sisa_percobaan > 0:
            print(f"Sisa Percobaan Anda: {sisa_percobaan}x lagi\n")
        else:
            print("\nKesempatan Habis, Akun Diblokir\n")
print("\n============= Laporan Data NIlai Siswa ==============")
kelas_tanpa_duplikat = []
for i in data_kelas:
    if i not in kelas_tanpa_duplikat:
        kelas_tanpa_duplikat += [i]

for i in kelas_tanpa_duplikat:
    no = 1
    print("\nKelas: ",i)
    print("----------------------------------------")
    for j in range(len(data_nama)):
        if data_kelas[j] == i:
            print(f"No: {no}")
            print("----------------------------------------")
            print(f"Nama Siswa: {data_nama[j]}")
            print("----------------------------------------")
            print(f"Status Ikut Ujian: {data_ikut_ujian[j]}")
            print("----------------------------------------")
            print(f"Nilai Ujian: {data_nilai[j]}")
            print("----------------------------------------")
            print(f"Kategori Ujian: {data_kategori[j]}\n")
            no += 1