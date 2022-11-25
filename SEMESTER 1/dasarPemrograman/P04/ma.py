import pandas as pd

c="============================================================="

ulang=int(input("Masukan Perulangan:"))
nama=[]
golongan=[]
tingkat=[]
jam=[]
total=[]

gaji=300000
print("============")
i = 0
for i in range(i + 1) :
    while i < ulang:
        print("Karyawan ke",str(i+1))
        golongan.append(input("Golongan :[GOL1,GOL2,GOL3]:"))
        tingkat.append(input("Tingkat:[SMA,D1,D3,S1]:"))
        jam.append(int(input("Jam:")))
    
        if golongan[i]=="GOL1" or golongan[i]=="gol1" or golongan[i]=="1":
            golongan.append(gaji*5/100)
            total.append(golongan[i]*gaji)
        
        elif golongan[i]=="gol2" or golongan[i]=="GOL2" or golongan[i]=="2":
            golongan.append(gaji*10/100)
            total.append(golongan[i]*gaji)

        elif golongan[i]=="gol3" or golongan[i]=="GOL3" or golongan[i]=="3":
            golongan.append(gaji*20/100)
            total.append(golongan[i]*gaji)
        else :
            golongan=0

        if tingkat[i]=="SMA":
            tingkat.append(gaji*2.5/100)
            total.append(golongan[i]*gaji)
        elif tingkat[i]=="D1":
            tingkat.append(gaji*5/100)
            total.append(golongan[i]*gaji)
        elif tingkat[i]=="D3":
            tingkat.append(gaji*20/100)
            total.append(golongan[i]*gaji)
        elif tingkat[i]=="S1":
            tingkat.append(gaji*30/100)
            total.append(golongan[i]*gaji)
        else :
            tingkat=0
    
    i += 1;

menu = {
    "golongan":golongan,
    "Tingkat":tingkat,
    "Jam": jam,
    "Total":total
};

daftarmenu=pd.DataFrame(menu)
print(c)

print("        Program hitung gaji karyawan            \n              PT Dingin damai")
print(c)
print(daftarmenu)
print(c)