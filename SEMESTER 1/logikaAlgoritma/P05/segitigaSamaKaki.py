n = 0;
symbol = ["*", "@", "#", "$", "!"];
char = symbol;

while n >= n :
    n = int(input("Masukkan nilai n : "));
    if n > 100 :
        print("Melebihi Limit!, input ulang");
        continue;
    
    while char == char :
        char = input("Masukkan (@, #, $, %, !) : ");
        if char not in symbol :
            print("Symbol Salah!, input ulang");
            continue;
    
        for i in range(n) :
            print((str(char)*(1+2*i)).center(1+2*20));
        break;
    break;