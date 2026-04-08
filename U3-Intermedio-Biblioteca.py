
filoNum = 1
ficcNum = 2
CienNum = 1

prestamos = 4

while prestamos > 0:
    categoria = input()
    
    if categoria == "Filosofía" and filoNum > 0: 
            filoNum = filoNum - 1
            prestamos = prestamos -1
            print("Préstamo correcto")
        
    elif categoria == "Filosofía" and filoNum == 0:
             print ("No hay préstamos disponibles para Filosofía")
            
    elif categoria == "Ciencia" and CienNum > 0:
            CienNum = CienNum - 1
            prestamos -= 1
            print("Préstamo correcto")
            
    elif categoria == "Ciencia" and CienNum == 0:
            print("No hay préstamos disponibles para Ciencia")
            
    elif categoria == "Ficción" and ficcNum > 0:
            ficcNum -=1
            prestamos-=1
            print ("Préstamo correcto")
            
    elif categoria == "Ficción" and ficcnum == 0:
            print ("No hay préstamos disponibles para Ficción")
            
    else: 
        print ("Debe ingresar una categoría válida")
        
print("Préstamos completados")
