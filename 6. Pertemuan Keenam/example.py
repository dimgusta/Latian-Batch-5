class biodata :
    def __init__(self, name, age): #constructor
        self.nama = name
        self.umur = age

    def tampil_nama(self):
        print("Namaku =", self.nama)
      

    def tampil_umur(self):
        print("Umurku =", self.umur)


input1 = input ("Nama = ")
input2 = input ("Umur = ")
print("=====================\n")

hasil = biodata(input1, input2)

hasil.tampil_nama()
hasil.tampil_umur()