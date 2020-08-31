
a=random.randint(1, 100)
b=0
p=0
Print(a)
while a!=b:
    b=int(input("Ваше число->"))
    p+=1
    if a>b:
        print("Мое число больше")
    if a<b:
        print("Мое число меньше")

print("Вы угадали за",p,"попыток")