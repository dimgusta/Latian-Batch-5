# Tugas 2.1 Pelatihan Basic Python AI Indonesia simpan data di txt

print ("Selamat Datang")
awal = """----Menu---- 
1. Daftar Kontak
2. Tambah Kontak
3. Hapus Kontak
4. Keluar \n"""

def tulis_data(nama, nomor) :
    value = nama + "," + nomor + ","                                 #format data dengan separator "," sebagai pemisah = nama,nomor,

    simpan = str(input("Simpan Nomor (Y/N) => "))                  
    if (simpan =="Y") or (simpan =="y"):                             #jika menekan y atau Y
        f = open("data_orang.txt", "a")                              #membuat file txt dengan nama data_orang, "a" berfungsi untuk melanjutkan penulisan data tanpa merubah data lama
        f.write(value)                                               #menuliskan data kedalam file .txt
        f.close()                                                              
        print ("Data Tersimpan ... \n")                              #mencetak data tersimpan  
    else :
        print ("Data Tidak Tersimpan ... \n")                        #mencetak data gagal tersimpan
            
    return

def baca_data() :
    f = open("data_orang.txt", "r")
    for data in f :
        #data =  f.readlines(i)                              #membaca baris awal data, karena jika menggunakan format read() data tersebut tidak dapat diparsing
                                                             #format var data menjadi list yang menampung isi dari data_orang
        #parsing = data[i].split(",")                        #karena data yang didapat hanya satu baris, maka memanggilnya dengan data[0]
        parsing = data.split(",")
        #print(parsing)
    f.close()

    parsing.remove('data')                                  #menghilangkan string "data" di awal data di .txt
    jumlah_data = int(len(parsing) / 2)                     #karena hanya ada dua data yang diperlukan, nama dan nomor HP
    #print (parsing)
    print ("Jumlah Kontak = ",jumlah_data)

    for x in range(jumlah_data) :
        print ("Nama : ", parsing[(x*2)], "  ==>  Tlp  : ", parsing[(x*2)+1]) #mencetak nilai list berdasarkan indeks pada list
    print ("\n")    
    return

def hapus_data() :
    delete = str(input("Anda Yakin Menghapus data (Y/N) => "))                  
    if (delete =="Y") or (delete =="y"):                             #jika menekan y atau Y
        f = open("data_orang.txt", "w")
        f.write("data,")                                             #menuliskan data default kosong kedalam file .txt
        f.close()                                                              
        print ("Data Terhapus... \n")                                 
    else :
        print ("Gagal Menghapus Data \n") 


while (True):                                               #looping program utama
    print (awal)                                            #menampilkan opsi menu
    pilihan = input("Pilih Menu => ")
    
    if (pilihan == "1") :
        print ("Daftar Kontak")
        baca_data()                                         #fungsi untuk membaca data

    elif (pilihan == "2") :
        print ("Kontak Baru")
        nama = input("Nama = ")
        nomor = input("Nomor = ")
        tulis_data(nama, nomor)                             #fungsi menuliskan nama & kontak dengan parameter yang diinputkan 
        
    elif (pilihan == "3") :
        hapus_data()                                        #fungsi untuk menghapus data   

    elif (pilihan == "4") :
        print ("Terima kasih")
        break                                               #keluar dari looping

    else :
        print ("Maaf Tidak Tersedia")                       #ketika salah memasukan pilihan
        print("\n")