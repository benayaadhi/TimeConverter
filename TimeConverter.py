# Soal 1 Konversi Waktu
def timeConverter(second): #buat function yg bernama timeConverter dengan parameter detik
    if second < 359999: #kondisi dimana jika parameter seconds lebih dr 359999 maka tidak akan dieksekusi / lanjut ke else
        seconds = second % (24 * 3600) # rumus 24 *3600 detik / 1 hari
        hour = seconds // 3600 #menggunakan // spy tidak koma
        seconds %= 3600 #biar kehapus convert ke jam
        minutes = seconds // 60 #menggunakan // spy floor / tidak koma
        seconds %= 60 #biar kehapus nanti ke convert ke menit
        print ('Konversi : {}:{}:{}'.format(hour,minutes,seconds))#.format adalah built in funct dr python. jd nanti dia print sesuai urutan {} yaitu hour,minutes,seconds
    else : #jika tidak sesuai
        print('Invalid Input!') # menampilkan invalid input
detik = int(input('Masukan Detik : ')) #bikin variable yg gunanya untuk memasukan detik dan harus int
timeConverter(detik) #memanggil fungsi timeConv dengan parameter detik sesuai yg kita input tadi