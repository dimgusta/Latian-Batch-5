
# awal = """----Menu---- 
# 1. Kirim E-mail
# 2. Logger E-mail
# 3. List E-mail
# 4. Tambah E-mail
# 5. Hapus Data
# 6. Keluar \n"""

# def tulis_data(masukan) :
#     email = masukan + "\n"                                        

#     simpan = str(input("Simpan E-mail (Y/N) => "))                  
#     if (simpan =="Y") or (simpan =="y"):                             #jika menekan y atau Y
#         f = open("receiver_list.txt", "a")                           #membuat file txt dengan nama data_orang, "a" berfungsi untuk melanjutkan penulisan data tanpa merubah data lama
#         f.write(email)                                               #menuliskan data kedalam file .txt
#         f.close()                                                              
#         print ("Data Tersimpan ... \n")                              #mencetak data tersimpan  
#     else :
#         print ("Data Tidak Tersimpan ... \n")                        #mencetak data gagal tersimpan       

# def list_kontak() :
#     f = open("receiver_list.txt", "r")  #membaca file receiver_list.txt
#     teks = f.read()                     
#     receiver_email=teks.split('\n')     #melakukan parsing data dengan tanda \n atau new line
#     receiver_email.pop()                #menghapus elemen list '' paling akhir dan list ini sudah bisa digunakan
#     f.close() 
#     return receiver_email               #nilai return sudah dalam bentuk list

# import os
# def hapus_data() :
#     delete = str(input("Anda Yakin Menghapus data (Y/N) => "))                  
#     if (delete =="Y") or (delete =="y"):                             #jika menekan y atau Y
#         if os.path.exists("receiver_list.txt"):
#             os.remove("receiver_list.txt")
#             print ("Data Terhapus \n") 
#         else:
#             print("File belum dibuat")    
#     else :
#         print ("Gagal Menghapus Data \n") 


# while (True):                                               #looping program utama
#     print (awal)                                            #menampilkan opsi menu
#     pilihan = input("Pilih Menu => ")
    
#     if (pilihan == "1") :
#         print ("Kirim E-mail")
        
#     elif (pilihan == "2") :
#         print ("Logger E-mail") 

#     elif (pilihan == "3") :
#         print ("List E-mail")
#         for x in list_kontak() :
#             print (x)

#     elif (pilihan == "4") :
#         print ("Tambah E-mail")
#         email = input("E-mail = ") 
#         tulis_data(email)   

#     elif (pilihan == "5") :
#         print ("Hapus Data")
#         hapus_data()
   
#     elif (pilihan == "6") :
#         print ("Terima Kasih")
#         break                                               #keluar dari looping

#     else :
#         print ("Maaf Tidak Tersedia")                       #ketika salah memasukan pilihan
#         print("\n")




    










import os
import sys
import time

import smtplib, ssl                                              #modul SMTLIB mode SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

port = 465                                                       #port untuk mode SSL 465  | TLS 587
smtp_server = "smtp.gmail.com"                                   #server SMTP untusk gmail
sender_email = "projectsolderku@gmail.com"                       #Email pengirim
def list_kontak() :
    f = open("receiver_list.txt", "r")                           #membaca file receiver_list.txt
    teks = f.read()                     
    daftar_email=teks.split('\n')                                #melakukan parsing data dengan tanda \n atau new line
    daftar_email.pop()                                           #menghapus elemen list '' paling akhir dan list ini sudah bisa digunakan
    f.close() 
    return daftar_email                                          #nilai return sudah dalam bentuk list
receiver_email = list_kontak()                                   #email penerima bisa menggunakan list / string tapi beda cara aksesnya


def tambah_lampiran() :
    storage = "D:/Github/Latian-Batch-5/Final_Project/Programnya/Lampiran/" #file direktori menyesuaikan dengan lampiran yang mau dikirim
    directory = os.listdir(storage)                                         #menampilkan isi direktori
    print ("Isi Lampiran : ")
    for lampiran in directory :
        print("- ", lampiran)

    try:   
        filename = input("Lampirkan : ")
        attachment = open(storage + filename, "rb")
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)
        print("File berhasil ditambahkan")
    except:
        print("File gagal ditambahkan ", sys.exc_info()[0])

    time.sleep(2)
    os.system('cls')


def kirim_email() :
    print("Mengirim Email...")
    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.ehlo()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.close()
        print ("E-mail Terkirim...")
    except:
        print ("E-mail Gagal")


def handle_email():
    msg = MIMEMultipart()
    msg['From'] = sender_email                          
    if (len(receiver_email) > 1) :                                  #mendeteksi jumlah email penerima di dalam list jika ada lebih dari satu maka 
        msg['To'] = ', '.join(receiver_email)                       #elemen email di dalam list akan digabung dengan separator , "dede@gmail.com , dimgusta@wkwkw.com"
    else :
        msg['To'] = receiver_email[0]                               #jika elemen list hanya satu maka akan mengirim ke indeks 0 aja

    #msg['To'] = receiver_email                                     #contoh deklarasi jika menggunakan satu string aja 
    #msg["Cc"] = "  "                                               #optional jika ada email yang mau di CC


    password = input("Pasword : ")
    judul = input("Judul : ")
    isi = input("Pesan : ")

    msg['Subject'] = judul
    body = isi
    msg.attach(MIMEText(body, 'plain'))

    perlu = input("Menambahkan Lampiran (Y/N) ?")
    if (perlu =="Y") or (perlu =="y"):                             #jika menekan y atau Y
        tambah_lampiran()

    time.sleep(2)
    os.system('cls')
    kirim_email()

handle_email()






