number = []
menu = 9
while menu != 0:
  print("1. Input Angka")
  print("2. Tampilkan Angka")
  print("3. Tampilkan Bilangan Genap")
  print("4. Tampilkan Bilangan Ganjil")
  print("0. Keluar")
  menu = int(input("Masukkann Pilihan Anda : "))
  if menu == 1:
    jumlah = int(input("Masukkan Jumlah Angka yang ingin Dimasukkan : "))
    for angka in range(jumlah):
      angka = int(input(f"Angka Ke-{angka+1}: "))
      number.append(angka)
    print()
  elif menu == 2:
    print(number)
    print()
  elif menu == 3:
    print("Angka Keseluruhan : ",number)
    print("Bilangan Genap: ", end="")
    for x in number:
      if x % 2 == 0:
        print(x, end=" ")
    print("")
    print("")
  elif menu == 4:
    print("Angka Keseluruhan : ",number)
    print("Bilangan Ganjil: ", end="")
    for x in number:
      if x % 2 != 0:
        print(x, end=" ")
    print("")
    print("")
  elif menu == 0:
    print("Anda Telah Keluar!")
