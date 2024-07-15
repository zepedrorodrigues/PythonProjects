def check_homogeneous(n):
    copy_n = n; sum = 0
    while n>0:
        sum = (n%10)**(3) + sum 
        n = (n-n%10)/10
    if copy_n==sum:
        print("homogeneous")
    else:
        print("non-homogeneous")

def check_capicua(n):
    copy_n = n; 
    sum = 0
    while n!=0:
        sum = (sum*10) + n%10
        n= n//10
    if sum == copy_n:
        print("capicua")
    else:
        print("não capicua")

def turn_time(n):
    horas = int((n-(n%3600))/3600)
    minutos = int(((n-(horas*3600))-(n%60))/60)
    segundos = int(n-(horas*3600)-(minutos*60))
    print(f"{n} segundos são {horas} horas, {minutos} minutos e {segundos} segundos")

def check_prime(n):
    primo = n; copy_primo = primo
    if n ==1:
        print("Não Primo")
        return
    else:
        while primo>2:
            if copy_primo%(primo-1)==0:
              print("Não Primo")
              return
            primo -= 1
    print("Primo")

def div(d,d1):
    copy_d = d; divis = 0
    while d-d1>=0:
        divis +=1; d-=d1
    print(f"{copy_d}/{d1} = {divis} com resto {d}")

def binary_to_decimal(n):
    copy_n = n; place = 0; final_number = 0
    while n!=0:
        if n%2!=0:
            final_number+=2**place
        n=(n-(n%10))/10
        place+=1
    print(final_number)

def cifra(n):
    copy_n = n; numero_final = 0
    while n>1:
        numero_final=numero_final/10
        x = ((n%10)+8)%10
        numero_final +=x
        n=(n-n%10)/10
    return numero_final*10000