# Tugas 1.2 Pelatihan Basic Python AI Indonesia

phi = 22/7

r = float(input("Jari-jari (cm) = "))               #conversi string => float
rumus = phi * r * r                                 #rumus luas lingkaran
hasil = "{:.2f}".format(rumus)                      #membatasi dua digit dibelakang koma

print ("Luas Lingkaran {} cm\u00b2". format(hasil)) #mencetak semua data cm\u00b2 berfungsi untuk membuat satuan cm persegi 
