# Tugas 2.1 Pelatihan Basic Python AI Indonesia

print ("Selamat Datang")
awal = """----Menu---- 
1. Daftar Kontak
2. Tambah Kontak
3. Keluar \n"""

daftar_kontak=[]                                                    #list untuk menampung data dictionary

def tulis_data(name, number) :                                      #fungsi menulis data ke dalam dictionary                                                   
    kontak = {}                                                     #mempersiapakan dictionary kontak
    kontak["Nama"] = name                                           #mengisi dictionary dengan nama
    kontak["Nomor"] = number                                        #mengisi dictionary dengan nomor
            
    simpan = str(input("Simpan Nomor (Y/N) => "))                  
    if (simpan =="Y") or (simpan =="y"):                             #jika menekan y atau Y
        daftar_kontak.append(kontak)                                 #ddata pada dictionary akan dimasukan ke dalam list daftar kontak
        print ("Data Tersimpan ... \n")                              #mencetak data tersimpan
            
    else :
        print ("Data Tidak Tersimpan ... \n")                       #mencetak data gagal tersimpan
            
    return

def tampil_data():
    for value in daftar_kontak :                                    #looping untuk memproses banyaknya data di list daftar kontak
        #print("Nama : ", value['Nama'])
        #print("Telp : ", value['Nomor'])
        print("Nama :" + value['Nama'] + "   ==>   Telp : " + value['Nomor']) #melakukan pencetakan data di list daftar kontak
    return


while (True):                                               #looping program utama
    print (awal)                                            #menampilkan opsi menu
    pilihan = input("Pilih Menu => ")
    
    if (pilihan == "1") :
        print ("Daftar Kontak = ", len(daftar_kontak))      #menghitung jumlah data pada list daftar kontak
        tampil_data()                                       #fungsi menampilkan data
        print("\n")

    elif (pilihan == "2") :
        print ("Kontak Baru")
        nama = input("Nama = ")
        nomor = input("Nomor = ")
        tulis_data(nama, nomor)                             #fungsi menuliskan nama & kontak dengan parameter yang diinputkan 
        
    elif (pilihan == "3") :
        print ("Terima kasih")
        break                                               #keluar dari looping

    else :
        print ("Maaf Tidak Tersedia")                       #ketika salah memasukan pilihan
        print("\n")