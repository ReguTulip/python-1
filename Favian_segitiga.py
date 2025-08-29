n = int(input("Masukkan angka: "))
a = 0
while a <= n:
    print("*" * (a))
    a+=1

n = 5
a = 0
while a <= n:
    print("*" * (n))
    n-=1

n = 5
a = 0
while a <= n:
    print((n-a) * " " + (2*a-1) * "*")
    a+=1