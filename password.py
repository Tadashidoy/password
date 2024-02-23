import random
x="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
word = int(input("Esto es el credor de contraseñas, escribe la cantidad de símbolos que quieras en tu contraseña para crear la contraseña"))
IDK=""
for i in range(word):
    IDK +=random.choice(x)
print (IDK)