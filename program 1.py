n = 100000000
sum = 0
y = 0
laba = [int(0), int(0), int(n) * .1, int (n) * .1, int(n) * .5, int(n) * .5, int(n) * .5, int(n) * .2]
print("modal awal seorang pengusaha: ",n)
for i in laba :
    sum = sum+i
    y+=1
    print("laba bulan ke - ",y,"sebesar :", i)
print("total laba adalah : ", sum)
