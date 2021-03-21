phi = 22/7

def rumus_lingkaran (r):
    luas = phi * r * r
    kll = 2 * phi * r
    return luas, kll

nilai = float(input("masukan jari-jari (cm) ="))
data = rumus_lingkaran(nilai) 
print ("Luas =", "{:.2f}".format(data[0]), "cm\u00b2")
print ("Keliling =", "{:.2f}".format(data[1]), "cm")