import Final_modul as md             #modul yang dibuat dengan nama Final_modul.py harus diperhatikan juga
# md.handling_email()                #diekstrak menjadi function handling email
# md.list_email()                    #diekstrak menjadi function list email
# md.add_email(masukan)              #diekstrak menjadi function add list email
# md.hapus_data()                    #diekstrak menjadi function hapus list email
# md.logger_act()                    #diekstrak menjadi function melihat aktivitas

awal = """----Menu---- 
1. Kirim E-mail
2. List E-mail
3. Tambah E-mail
4. Hapus Data
5. Logger Activity
6. Keluar \n"""

while (True):                                               #looping program utama
    print (awal)                                            #menampilkan opsi menu
    pilihan = input("Pilih Menu => ")
    
    if (pilihan == "1") :
        print ("Kirim E-mail")
        md.handling_email() 
        
    elif (pilihan == "2") :
        print ("List E-mail")
        try:
            for daftar in md.list_email():
                print (daftar)
            print ("\n")
        except :
            print ("Belum Ada List")

    elif (pilihan == "3") :
        print ("Tambah E-mail")
        email = input("E-mail = ") 
        md.add_email(email)  

    elif (pilihan == "4") :
        print ("Hapus Data")
        md.hapus_data()
    
    elif (pilihan == "5") :
        print ("Logger E-mail") 
        md.logger_act()
   
    elif (pilihan == "6") :
        print ("Terima Kasih")
        break                                               #keluar dari looping

    else :
        print ("Maaf Tidak Tersedia")                       #ketika salah memasukan pilihan
        print("\n")
