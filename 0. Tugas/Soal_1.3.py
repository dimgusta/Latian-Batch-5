# Tugas 1.3 Pelatihan Basic Python AI Indonesia

standart = 70                                           #standart nilai kelulusan

teori = int (input("Nilai Teori = "))                   #tipe data untuk nilai integer
praktek = int (input("Nilai Praktek = "))               #tipe data untuk nilai integer

if ((teori >= standart) and (praktek >= standart)):
    print("Selamat anda lulus keduanya !")
elif ((teori >= standart) and (praktek < standart)):
    print("Anda harus mengulang ujian praktek")
elif ((teori < standart) and (praktek >= standart)):
    print("Anda harus mengulang ujian teori")
elif ((teori < standart) and (praktek < standart)):
    print("Anda harus mengulang ujian teori dan praktek")