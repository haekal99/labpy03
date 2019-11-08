print (" program menampilkan bilangan terbesar dari n bilangan ")

n = 1
max = 0
while n != 0 :
    if n > max :
        max = n
    n = int(input(" masukan bilangan : "))
    if n == 0:
        break
print ("bilangan terbesar adalah : ", max)
