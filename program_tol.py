#PROGRAM TOL

#IMPORT
from email import header
import os


os.chdir(r'data')

import csv

#ubah csv ke list kode kota dan kode kendaraan
list_kota = []
with open('data_01_daftar_kota.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        list_kota.append(row)

list_knd = []
with open('data_02_daftar_kendaraan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        list_knd.append(row)
    

#menu 1 (tabel)
def tabel_1():
    print('')
    print('TABEL DAFTAR'.center(85))
    print('KODE KOTA DAN NAMA KOTA'.center(85))
    print('')
    print(('-'*49).center(85))
    for i in range(len(list_kota)):
        print(f'| {list_kota[i][0]:^14} | {list_kota[i][1]:^28} |'.center(85))
        print(('-'*49).center(85))

def tabel_2():
    print('')
    print('TABEL DAFTAR'.center(85))
    print('KODE DAN JENIS KENDARAAN'.center(85))
    print('')
    print(('-'*68).center(85))
    for i in range(len(list_knd)):
        print(f'|{list_knd[i][0]:^14}|{list_knd[i][1]:^24}|{list_knd[i][2]:^26}|'.center(85))
        print(('-'*68).center(85))

#menu 2
def mulai_estimasi():
    def tarif_golongan():
        if kode_golongan == 1:
            tarif = f"Rp. {(800 * 1 * km):,} ,-"
        elif kode_golongan == 2:
            tarif = f"Rp. {(800 * 1.5 * km):,} ,-"
        elif kode_golongan == 3:
            tarif = f'Rp. {(800 * 2 * km):,} ,-'
        else :
            print('''
        ERROR
        Periksa kembali kode kendaraan anda!
        Hint : - Masukkan kode berupa angka
                 1 sampai dengan 3
            ''')
            input("Tekan ENTER untuk kembali mengulang estimasi")
            mulai_estimasi()
        kata2 = "ESTIMASI TARIF ADALAH {}".format(tarif)
        print(kata2.center(85))

    try :
        kode_plat = str(input("Masukkan nomor plat kendaraan anda : ")).upper()
        kode_golongan = int(input("Masukkan kode golongan kendaraan anda : "))
        kode_kota_asal = int(input("Masukkan kode kota asal : "))
        kode_kota_tujuan = int(input("Masukkan kode kota tujuan : "))
    except ValueError:
        print('!!! PERIKSA INPUT ANDA KEMBALI !!!'.center(85))
        input("Tekan ENTER untuk kembali mengulang estimasi")
        mulai_estimasi()
        input("Tekan ENTER untuk kembali ke menu utama")
        main_menu()
    
    #cabang1
    if (kode_kota_asal == 1 and  kode_kota_tujuan == 2) or (kode_kota_tujuan == 1 and kode_kota_asal == 2):
        km = 12 ; kata = "JAKARTA OUTER RINGROAD - JAKARTA PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 3) or (kode_kota_tujuan == 1 and kode_kota_asal == 3):
        km = 84 ; kata = "JAKARTA OUTER RINGROAD - CIKAMPEK PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 4) or (kode_kota_tujuan == 1 and kode_kota_asal == 4):
        km = 98 ; kata = "JAKARTA OUTER RINGROAD - CIKOPO PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 5) or (kode_kota_tujuan == 1 and kode_kota_asal == 5):
        km = 222 ; kata = "JAKARTA OUTER RINGROAD - PALIMANAN PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 6) or (kode_kota_tujuan == 1 and kode_kota_asal == 6):
        km = 243 ; kata = "JAKARTA OUTER RINGROAD - KANCI PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 1 and kode_kota_asal == 7):
        km = 274 ; kata = "JAKARTA OUTER RINGROAD - PEJAGAN PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 1 and kode_kota_asal == 8):
        km = 365 ; kata = "JAKARTA OUTER RINGROAD - PEMALANG PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 1 and kode_kota_asal == 9):
        km = 421 ; kata = "JAKARTA OUTER RINGROAD - BATANG PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 1 and kode_kota_asal == 10):
        km = 451 ; kata = "JAKARTA OUTER RINGROAD - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 1 and kode_kota_asal == 11):
        km = 460 ; kata = "JAKARTA OUTER RINGROAD - SEMARANG ABC PP"
    elif (kode_kota_asal == 1 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 1 and kode_kota_asal == 12):
        km = 550 ; kata = "JAKARTA OUTER RINGROAD - SOLO PP"

    #cabang2
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 3) or (kode_kota_tujuan == 2 and kode_kota_asal == 3):
        km = 72 ; kata = "JAKARTA - CIKAMPEK PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 4) or (kode_kota_tujuan == 2 and kode_kota_asal == 4):
        km = 86 ; kata = "JAKARTA - CIKOPO PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 5) or (kode_kota_tujuan == 2 and kode_kota_asal == 5):
        km = 205 ; kata = "JAKARTA - PALIMANAN PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 6) or (kode_kota_tujuan == 2 and kode_kota_asal == 6):
        km = 231 ; kata = "JAKARTA - KANCI PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 2 and kode_kota_asal == 7):
        km = 262 ; kata = "JAKARTA - PEJAGAN PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 2 and kode_kota_asal == 8):
        km = 353 ; kata = "JAKARTA - PEMALANG PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 2 and kode_kota_asal == 9):
        km = 409 ; kata = "JAKARTA - BATANG PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 2 and kode_kota_asal == 10):
        km = 439 ; kata = "JAKARTA - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 2 and kode_kota_asal == 11):
        km = 448 ; kata = "JAKARTA - SEMARANG ABC PP"
    elif (kode_kota_asal == 2 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 2 and kode_kota_asal == 12):
        km = 538 ; kata = "JAKARTA - SOLO PP"

    #cabang3
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 4) or (kode_kota_tujuan == 3 and kode_kota_asal == 4):
        km = 77 ; kata = "CIKAMPEK - CIKOPO PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 5) or (kode_kota_tujuan == 3 and kode_kota_asal == 5):
        km = 132 ; kata = "CIKAMPEK - PALIMANAN PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 6) or (kode_kota_tujuan == 3 and kode_kota_asal == 6):
        km = 161 ; kata = "CIKAMPEK - KANCI PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 3 and kode_kota_asal == 7):
        km = 192 ; kata = "CIKAMPEK - PEJAGAN PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 3 and kode_kota_asal == 8):
        km = 280 ; kata = "CIKAMPEK - PEMALANG PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 3 and kode_kota_asal == 9):
        km = 336 ; kata = "CIKAMPEK - BATANG PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 3 and kode_kota_asal == 10):
        km = 428 ; kata = "CIKAMPEK - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 3 and kode_kota_asal == 11):
        km = 340 ; kata = "CIKAMPEK - SEMARANG ABC PP"
    elif (kode_kota_asal == 3 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 3 and kode_kota_asal == 12):
        km = 456 ; kata = "CIKAMPEK - SOLO PP"

    #cabang4
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 5) or (kode_kota_tujuan == 4 and kode_kota_asal == 5):
        km = 116 ; kata = "CIKOPO - PALIMANAN PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 6) or (kode_kota_tujuan == 4 and kode_kota_asal == 6):
        km = 159 ; kata = "CIKOPO - KANCI PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 4 and kode_kota_asal == 7):
        km = 189 ; kata = "CIKOPO - PEJAGAN PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 4 and kode_kota_asal == 8):
        km = 238 ; kata = "CIKOPO - PEMALANG PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 4 and kode_kota_asal == 9):
        km = 279 ; kata = "CIKOPO - BATANG PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 4 and kode_kota_asal == 10):
        km = 341 ; kata = "CIKOPO - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 4 and kode_kota_asal == 11):
        km = 366 ; kata = "CIKOPO - SEMARANG ABC PP"
    elif (kode_kota_asal == 4 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 4 and kode_kota_asal == 12):
        km = 443 ; kata = "CIKOPO - SOLO PP"

    #cabang5
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 6) or (kode_kota_tujuan == 5 and kode_kota_asal == 6):
        km = 44 ; kata = "PALIMANAN - KANCI PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 5 and kode_kota_asal == 7):
        km = 72 ; kata = "PALIMANAN - PEJAGAN PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 5 and kode_kota_asal == 8):
        km = 121 ; kata = "PALIMANAN - PEMALANG PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 5 and kode_kota_asal == 9):
        km = 162 ; kata = "PALIMANAN - BATANG PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 5 and kode_kota_asal == 10):
        km = 224 ; kata = "PALIMANAN - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 5 and kode_kota_asal == 11):
        km = 249 ; kata = "PALIMANAN - SEMARANG ABC PP"
    elif (kode_kota_asal == 5 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 5 and kode_kota_asal == 12):
        km = 350 ; kata = "PALIMANAN - SOLO PP"

    #cabang6
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 7) or (kode_kota_tujuan == 6 and kode_kota_asal == 7):
        km = 42 ; kata = "KANCI - PEJAGAN PP"
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 6 and kode_kota_asal == 8):
        km = 91 ; kata = "KANCI - PEMALANG PP"
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 6 and kode_kota_asal == 9):
        km = 133 ; kata = "KANCI - BATANG PP"
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 6 and kode_kota_asal == 10):
        km = 225 ; kata = "KANCI - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 6 and kode_kota_asal == 11):
        km = 242 ; kata = "KANCI - SEMARANG ABC PP"
    elif (kode_kota_asal == 6 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 6 and kode_kota_asal == 12):
        km = 297 ; kata = "KANCI - SOLO PP"

    #cabang7
    elif (kode_kota_asal == 7 and kode_kota_tujuan == 8) or (kode_kota_tujuan == 7 and kode_kota_asal == 8):
        km = 58 ; kata = "PEJAGAN - PEMALANG PP"
    elif (kode_kota_asal == 7 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 7 and kode_kota_asal == 9):
        km = 72 ; kata = "PEJAGAN - BATANG PP"
    elif (kode_kota_asal == 7 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 7 and kode_kota_asal == 10):
        km = 179 ; kata = "PEJAGAN - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 7 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 7 and kode_kota_asal == 11):
        km = 204 ; kata = "PEJAGAN - SEMARANG ABC PP"
    elif (kode_kota_asal == 7 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 7 and kode_kota_asal == 12):
        km = 274 ; kata = "PEJAGAN - SOLO PP"

    #cabang8
    elif (kode_kota_asal == 8 and kode_kota_tujuan == 9) or (kode_kota_tujuan == 8 and kode_kota_asal == 9):
        km = 39 ; kata = "PEMALANG - BATANG PP"
    elif (kode_kota_asal == 8 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 8 and kode_kota_asal == 10):
        km = 130 ; kata = "PEMALANG - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 8 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 8 and kode_kota_asal == 11):
        km = 155 ; kata = "PEMALANG - SEMARANG ABC PP"
    elif (kode_kota_asal == 8 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 8 and kode_kota_asal == 12):
        km = 206 ; kata = "PEMALANG - SOLO PP"

    #cabang9
    elif (kode_kota_asal == 9 and kode_kota_tujuan == 10) or (kode_kota_tujuan == 9 and kode_kota_asal == 10):
        km = 95 ; kata = "BATANG - SEMARANG (KALIANGKUNG) PP"
    elif (kode_kota_asal == 9 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 9 and kode_kota_asal == 11):
        km = 120 ; kata = "BATANG - SEMARANG ABC PP"
    elif (kode_kota_asal == 9 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 9 and kode_kota_asal == 12):
        km = 154 ; kata = "BATANG - SOLO PP"

    #cabang10 11
    elif (kode_kota_asal == 10 and kode_kota_tujuan == 11) or (kode_kota_tujuan == 10 and kode_kota_asal == 11):
        km = 25 ; kata = "SEMARANG (KALIANGKUNG) - SEMARANG ABC PP"
    elif (kode_kota_asal == 10 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 10 and kode_kota_asal == 12):
        km = 100 ; kata = "SEMARANG (KALIANGKUNG) - SOLO PP"
    elif (kode_kota_asal == 11 and kode_kota_tujuan == 12) or (kode_kota_tujuan == 11 and kode_kota_asal == 12):
        km = 75 ; kata = "SEMARANG ABC - SOLO PP"

    else :
        print ('''
        ERROR
        Periksa kembali kode kota anda!
        Hint : - Kode kota asal dan kode kota tujuan 
                 TIDAK BOLEH SAMA
               - Masukkan kode kota asal dan kode
                 kota tujuan dengan angka 1 sampai 12
        ''')
        input("Tekan ENTER untuk kembali mengulang estimasi")
        mulai_estimasi()
        input("Tekan ENTER untuk kembali ke menu utama")
        main_menu()
    
    print("")
    print(kata.center(85))
    tarif_golongan()
    print("")

    #konversi kode kendaraan
    if kode_golongan == 1:
        jenis = "GOLONGAN 1"
    elif kode_golongan == 2:
        jenis = "GOLONGAN 2"
    elif kode_golongan == 3:
        jenis = "GOLONGAN 3"
    else:
        jenis = "INVALID"
    #konversi kode kota asal
    if kode_kota_asal == 1:
        asal = "Jakarta Outer Ring Road"
    elif kode_kota_asal == 2 :
        asal = "Jakarta"
    elif kode_kota_asal == 3 :
        asal = "Cikampek"
    elif kode_kota_asal == 4 :
        asal = "Cikopo"
    elif kode_kota_asal == 5 :
        asal = "Palimanan"
    elif kode_kota_asal == 6 :
        asal = "Kanci"
    elif kode_kota_asal == 7 :
        asal = "Pejagan"
    elif kode_kota_asal == 8 :
        asal = "Pemalang"
    elif kode_kota_asal == 9 :
        asal = "Batang"
    elif kode_kota_asal == 10 :
        asal = "Semarang (Kaliangkung)"
    elif kode_kota_asal == 11 :
        asal = "Semarang ABC"
    elif kode_kota_asal == 12 :
        asal = "Solo"
    else:
        asal = "INVALID"
    #konversi kode kota tujuan
    if kode_kota_tujuan == 1:
        tujuan = "Jakarta Outer Ring Road"
    elif kode_kota_tujuan == 2 :
        tujuan = "Jakarta"
    elif kode_kota_tujuan == 3 :
        tujuan = "Cikampek"
    elif kode_kota_tujuan == 4 :
        tujuan = "Cikopo"
    elif kode_kota_tujuan == 5 :
        tujuan = "Palimanan"
    elif kode_kota_tujuan == 6 :
        tujuan = "Kanci"
    elif kode_kota_tujuan == 7 :
        tujuan = "Pejagan"
    elif kode_kota_tujuan == 8 :
        tujuan = "Pemalang"
    elif kode_kota_tujuan == 9 :
        tujuan = "Batang"
    elif kode_kota_tujuan == 10 :
        tujuan = "Semarang (Kaliangkung)"
    elif kode_kota_tujuan == 11 :
        tujuan = "Semarang ABC"
    elif kode_kota_tujuan == 12 :
        tujuan = "Solo"
    else:
        tujuan = "INVALID"
    
    #log data
    data = kode_plat, jenis, asal, tujuan
    with open('log_data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(data)

#main menu (menu utama)
def main_menu():
    print("")
    print("="*85)
    print("PROGRAM ESTIMASI BIAYA TOL".center(85))
    print("RUTE JAKARTA - SOLO".center(85))
    print("="*85)
    print("")
    print("")
    print("MENU UTAMA".center(85))
    print("")
    print("Daftar menu :".center(85))
    print("-------------".center(85))
    print('''
    1. Lihat tabel daftar kode
    2. Mulai estimasi
    3. Lainnya
    4. Keluar

    '''.center(85))
    input_menu = input("Masukkan angka pada menu pilihan anda : ")
    if input_menu == '1':
        tabel_2()
        tabel_1()
        print("")
        print('''
        1. Lanjut ke mulai estimasi
        2. Kembali ke menu utama

        '''.center(85))
        menu_utama = input("Masukkan angka pada menu pilihan anda : ")
        if menu_utama == '1':
            mulai_estimasi()
            input("Tekan ENTER untuk kembali ke menu utama")
            main_menu()
        elif menu_utama == '2':
            main_menu()
        else:
            print('!!! PERIKSA INPUT ANDA KEMBALI !!!'.center(85))
            main_menu()
    elif input_menu == '2':
        mulai_estimasi()
        print("")
        input("Tekan ENTER untuk kembali ke menu utama")
        main_menu()
    elif input_menu == '3':
        extras()
        print("")
    #menu 4
    elif input_menu == '4':
        print("PROGRAM DITUTUP")
        print("")       
    else:
        print('!!! PERIKSA INPUT ANDA KEMBALI !!!'.center(85))
        main_menu()

#menu 3
def extras():
    print("")
    def lihat_log():
        def show_log():
            log_1 = []
            with open('log_data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                for row in csv_reader:
                    log_1.append(row)
            print("-"*85)
            for i in range(len(log_1)):
                print(f'|{log_1[i][0]:^16}|{log_1[i][1]:^14}|{log_1[i][2]:^25}|{log_1[i][3]:^25}|')
                print("-"*85)
        print("Lihat file log? (y / t)")
        s_log = input("")
        s_log_2 = s_log.lower()
        if s_log_2 == "y":
            print("")
            print("FILE LOG".center(85))
            print("-------------".center(85))
            print("")
            show_log()
            input("Tekan ENTER untuk kembali")
            extras()
        elif s_log_2 == "t":
            print("FILE LOG TIDAK JADI DILIHAT".center(85))
            extras()
        else:
            input("Tekan ENTER untuk kembali")
            extras()
    def bersihkan_log():
        def clear_log():
            data = 'NO PLAT','KODE GOLONGAN','KOTA ASAL','KOTA TUJUAN'
            with open('log_data.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=";")
                csv_writer.writerow(data)
        print("Apakah anda yakin untuk bersihkan file log? (y / t)")
        c_log = input("")
        c_log_2 = c_log.lower()
        if c_log_2 == "y":
            print("FILE LOG TELAH DIHAPUS")
            print("")
            clear_log()
            input("Tekan ENTER untuk kembali")
            extras()
        else:
            print("FILE LOG TIDAK JADI DIHAPUS")
            print("")
            input("Tekan ENTER untuk kembali")
            extras()
    print("Lainnya".center(85))
    print("-------------".center(85))
    print('''
    1. Lihat data log
    2. Hapus data log
    3. Kembali ke menu utama

    '''.center(85))
    input_extras = input("Masukkan angka pada menu pilihan anda : ")
    if input_extras == "1":
        lihat_log()
    elif input_extras == "2":
        bersihkan_log()
    elif input_extras == "3":
        main_menu()
    else:
        print('!!! PERIKSA INPUT ANDA KEMBALI !!!'.center(85))
        extras()

#exception
try:
    main_menu()
except UnboundLocalError:
    pass
