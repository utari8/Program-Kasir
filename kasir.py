# code by utari8

print("SELAMAT DATANG DI RESTORAN PYTHON")
print("DAFTAR MAKANAN")
print("SOTO        : Rp. 15000")
print("SATE        : Rp. 20000")
print("NASI GORENG : Rp. 25000")
print("MI GORENG   : Rp. 35000")
print("BAKSO       : Rp. 30000")
print("-----------------------")
print("DAFTAR MINUMAN")
print("TEH         : Rp. 10000")
print("KOPI        : Rp. 15000")
print("SUSU        : Rp. 18000")

jml = []
fd = []

def kasir():
    if pesan == "soto" or pesan == "SOTO":
        print(makan[0]," : ", h_mkn[0])
        jml.append(15000)
        fd.append("SOTO")
    elif pesan == "sate" or pesan == "SATE":
        print(makan[1]," : ", h_mkn[1])
        jml.append(20000)
        fd.append("SATE")
    elif pesan == "nasi goreng" or pesan == "NASI GORENG":
        print(makan[2]," : ", h_mkn[2])
        jml.append(25000)
        fd.append("NASI GORENG")
    elif pesan == "mi goreng" or pesan == "MI GORENG":
        print(makan[3]," : ", h_mkn[3])
        jml.append(35000)
        fd.append("MI GORENG")
    elif pesan == "teh" or pesan == "TEH":
        print(minum[0]," : ", h_mn[0])
        jml.append(10000)
        fd.append("TEH")
    elif pesan == "kopi" or pesan == "KOPI":
        print(minum[1]," : ", h_mn[1])
        jml.append(15000)
        fd.append("KOPI")
    elif pesan == "susu" or pesan == "SUSU":
        print(minum[2]," : ", h_mn[2])
        jml.append(18000)
        fd.append("SUSU")
    else:
        print("Tolong masukkan pesanan dengan benar")


pilih = str(input("Apakah anda ingin memesan makanan (y/n) : "))
makan = ["SOTO", "SATE", "NASI GORENG", "MI GORENG", "BAKSO"]
minum = ["TEH", "KOPI", "SUSU"]
h_mn  = [10000,15000,18000]
h_mkn = [15000, 20000, 25000, 35000, 30000]    

if pilih == "y":
    pesan = str(input("Anda ingin pesan apa? : "))
    kasir()
    ask = input("Apakah anda ingin memesan kembali (y/n) : ")
    while ask == "y":
        pesan = str(input("Anda ingin pesan apa? : "))
        kasir()
        ask = input("Apakah anda ingin memesan kembali (y/n) : ")
    if ask == "n":
        print("Pesanan anda : ")
        for i in range(len(fd) and len(jml)):
            print(fd[i]," : ",jml[i])
        print("----------------------")
        print("Total pesanan anda : ", sum(jml))
        print("Terimakasih sudah datang")
else:
    print("Terimakasih sudah datang")


# code by utari8