anakAyam = 0;

while anakAyam >= anakAyam :
    anakAyam = int(input("Masukkan Jumlah Anak Ayam 1 - 100 : "));

    if anakAyam < 0 or anakAyam > 100 :
        print("Jumlah salah, input lagi");
        continue;

    if anakAyam >= 2 :
        while anakAyam > 1 :
            print("Tekotek kotek kotek, anak ayam turun berkotek");
            print("Anak ayam turunlah %s mati satu tinggallah %d" % (anakAyam, anakAyam - 1));
            anakAyam = anakAyam - 1;

        if anakAyam <= 1 :
            print("Tekotek kotek kotek, anak ayam turun berkotek");
            print("Anak ayam turunlah %d mati satu tinggalah induknya" % (anakAyam));
            print("");
        else :
            print("Anak Ayam turunlah %s mati satu tinggal induknya" % (anakAyam))
        break;     