### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 5:
        #break
        continue
else:
    print("La condicion ya no se cumple") #esta mamada es cosa del diavlo, como vas a usar un else aqui nmms
    
    
# For

my_list = [18, 22, 54, 69, 78, 22]

for i in my_list:
    print(i)

my_tuple = (18, 1.77, "Steven", "Mejia")
for i in my_tuple:
    print(i)

my_set = {"Steven", "Mejia", 18}
for i in my_set:
    print(i)

my_dict = {"Nombre":"Steven", "Apellido":"Morgan","Edad":18, 1:"Python"}
for i in my_dict:
    print(i)