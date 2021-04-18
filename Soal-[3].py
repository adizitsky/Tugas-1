# menilai kelulusan siswa
a = float(input("Input nilai teori: "))
b = float(input("Input nilai praktik: "))
if a >=70 and b>=70:
    print("Selamat, anda lulus !")
elif a>=70 and b<=70:
        print("Anda harus mengulang ujian praktik!")
elif a<70 and b>=70:
        print("Anda harus mengulan ujian teori!")
else:
    print("Anda harus mengulan ujian teori dan praktik! Bodoh kali kau!")
