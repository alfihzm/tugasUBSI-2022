list_nim = []
list_uts = []
list_uas = []
list_total = []
list_grade = []

ulang = 2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan NIM anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS anda : ")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))

#proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)
    if (int(list_total[i]) < 60) :
        list_grade.append("C")
    elif (int(list_total[i]) < 80) :
        list_grade.append("B")
    elif (int(list_total[i]) < 100) :
        list_grade.append("A")
    else :
        list_grade.append("-")

print("================================================================");
print("Nim \t\t Nilai Uts \t Nilai UAS \t Total \t Grade");
print("================================================================");
for i in range(ulang):
    print ("%s \t %i \t\t %i \t\t %i \t %s" % (list_nim[i], list_uts[i], list_uas[i], list_total[i], list_grade[i]));
print("================================================================");