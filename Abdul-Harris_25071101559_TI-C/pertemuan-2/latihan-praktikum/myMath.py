#soal 1
def tambah(a, b):
    return a + b

hasil = tambah(5, 6)
print("hasil penjumlahan =",hasil)

#soal 2
def kurang(a, b):
    return a - b

hasil = kurang(10, 5)
print("hasil pengurangan =", hasil)

#soal 3
def perkalian(a, b):
    return a * b

hasil = perkalian(10, 5)
print("hasil perkalian =", hasil)

#soal 4
def pembagian(a, b):
    if b == 0:
        return("pesan error karena pembagi bernilai 0")
print(pembagian(10, 2))
print(pembagian(10, 0))

#soal 5
def modulus(a, b):
    return a % b
hasil = modulus(10, 3)
print("hasil modulus", hasil)

#soal 6
n = 8
deret = []
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)
    
for i in range (n):
    deret.append(fibonacci(n-i))
print (deret)

