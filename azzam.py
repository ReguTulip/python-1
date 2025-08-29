#var = 1
#var2 = "brot"
#print(str(var)*100)

#print(1+2)
#print(1-2)
#print(1/2)
#print(1*2)
#print(1**2)
#print(12%7)

#a = 6
#b = "asusususu&^&&#^&**#&&#sussu"
#print(a+len(b))

# a = input('masukkan password : ')
# if len(a)>=8:
#     print("berhasil")
#     if len(a)%2==1:
#         print(b*3)
#     elif len(b) >=10:
#         print("minimal 8 character")

# nilai = input("masukkan nilai")
# nilai_int = int(nilai)
# if nilai_int > 100:
#     print("Nilai Invaldi")
# elif nilai_int in range(90, 101):
#     print("Mantap")
# else:
#     print("gagal")

# a = "hello world"
# b = a.index('l')

# print(type(b))

# nilai = int(input("masukkan nilai"))
# if nilai > 100:
#     print("Nilai Invaldi")
# elif nilai >=90:
#     print("Mantap")
# else:
#     print("gagal")

# arr = ["apel" , "jeruk" , "kelapa" , "pisang"]
# for i in arr:
#     print("saya",i)

# arr = ["apel" , 2 , True , None , 9.90]
# for i in arr:
#     print("saya",i)

# for i in range(0,3):
#     print('apel')
#     for j in range(0,3):
#         print('p')

#FUNCTION
# def tambah (a,b):
#     print(a+b)
# def kurang (a,b):
#     print (a-b)
# def kali (a):
#     print(a * 10)

# tambah(10, 20)
# kurang(9, 19)
# kali ("Azzam")

# for i in range(0,5):
#     print("*" * (i+1))

# a = 0
# while a <= 5:
#     print("*" * (a))
#     a += 1
    
# a = 5
# while a >= 1:
#     print("*" * (a))
#     a -= 1

a = 0
n = int (input("masukkan nilai n : "))
while a <= n:
    print((n-a) * " " + (2*a-1) * "*")
    a += 1