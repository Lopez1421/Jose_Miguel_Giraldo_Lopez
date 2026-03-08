
print("Bienvenido a EduTech Solutions calculadora de Promedio de notas")

#se asginan una variaba a cada calificacion del estudiante 

C1 = int(input("Ingresa la calificacion numero 1:"))
C2 = int(input("Ingresa la calificacion numero 2:"))
C3 = int(input("Ingresa la calificacion numero 3:"))
C4 = int(input("Ingresa la calificacion numero 4:"))
C5 = int(input("Ingresa la calificacion numero 5:"))
#se suman todas las calificaciones y el resultado se asgina a la variable CT

CT= C1+C2+C3+C4+C5
# se calcula el promedio en base a la formula 
Promedio= CT/5

#se aplican los condicionales 

if Promedio >= 60:
    print("Felicitaciones usted esta aprobado")

elif  40 <= Promedio <= 59:
    print("Usted se encuentra en recuperacion")

else:
    print("Lo siento Usted se encuentra reprobado")

print("EL promedio acomulado suyo es:", Promedio)