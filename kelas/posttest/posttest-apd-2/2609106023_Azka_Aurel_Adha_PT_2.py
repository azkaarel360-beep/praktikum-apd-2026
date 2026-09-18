bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

bagasi = [bagasi_1,bagasi_2,bagasi_3,bagasi_4,bagasi_5,bagasi_6]

berat_total_akhir_kg = bagasi[0] + bagasi[1] + bagasi[2] + bagasi[3] + bagasi[4] + bagasi[5] 
berat_total_akhir_gram = berat_total_akhir_kg * 1000
rata_rata = berat_total_akhir_kg / len(bagasi)
kompensasi = 0.05
biaya_kompensasi = berat_total_akhir_kg * kompensasi

nim = 23
bolean = nim < rata_rata

print("bagasi 1 adalah ",bagasi_1)
print("bagasi 2 adalah ",bagasi_2)
print("bagasi 3 adalah ",bagasi_3)
print("bagasi 4 adalah ",bagasi_4)
print("bagasi 5 adalah ",bagasi_5)
print("bagasi 6 adalah ",bagasi_6)
print("berikut list bagasinya ",bagasi)
print("berikut adalah berat total bagasi dalam Kg ", berat_total_akhir_kg)
print("berikut adalah berat total bagasi dalam Gram ", berat_total_akhir_gram)
print("berikut rata rata dari berat total ", rata_rata)
print("total biayanya adalah ",biaya_kompensasi)
print("nim < rata_rata bernilai ",bolean)
print(bagasi[2:5])