# Daftar Deklarasi Fungsi
def baca_data(filename):
    #fungsi digunakan untuk membaca file teks, kemudian merubah ke dalam
    #tipe data terstruktur
    file = open(filename, "r")  #Untuk Meembuka dan membaca file


    daftar_poin = {}       #dictionary untuk daftar poin, berdasarkan file teks yang dibaca
                           #key untuk nama pemain dan value untuk total poin dari pemain
   
    teks = file.readline()
    while teks != "":
        teks = teks.replace("-", " ")   # tanda strip(-) yang memisahkan 2 skor pemain kita ubah menjadi spasi
        player1, player2, poin1, poin2 = teks.split() 

        if poin1 == '1/2':  #jika pada poin1 ada yang bernilai 1/2, 
            poin1 = 0.5     #maka akan diubah menjadi 0.5
        if poin2 == '1/2':  #jika pada poin2 ada yang bernilai 1/2, 
            poin2 = 0.5     #maka akan diubah menjadi 0.5
        if player1 in daftar_poin :
            daftar_poin[player1] += float(poin1)
        else :
            daftar_poin[player1] =  float(poin1) 
        if player2 in daftar_poin :
            daftar_poin[player2] += float(poin2)
        else :
            daftar_poin[player2] = float(poin2)

        
        teks = file.readline()
    return daftar_poin

#Fungsi Untuk Menghitung banyaknya pemain
def pemain(daftar_poin):
    pemain = len(daftar_poin)
    return pemain

#Fungsi untuk menentukan siapa yang juara dan mendapatkan poin tertinggi
def juara(daftar_poin) :
    poin_pemain = list(daftar_poin.values ())
    poin_juara = max(poin_pemain)

    for pemain in daftar_poin :
        if daftar_poin[pemain] == poin_juara :
            return pemain

#Main program
nama_file = "file_catur.txt"
daftar_poin = baca_data(nama_file)
print (daftar_poin)
print("Banyaknya pemain yang bertanding yaitu ada: ", pemain(daftar_poin), "orang")
print("Juara dan yang mendapatkan poin tertinggi dari pertandingan tersebut adalah: ", juara(daftar_poin))

