import string
letras_reemplazar = [('j','i'),('h','i'),('ñ','n'),('k','l'),('u','v'),('w','v'),('y','z')]
tildes =[('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u')]
signo = ['?', '¿','¡','!',' ',',','.',';',':','\n']
texto = open("heraldos.txt",encoding='utf-8')
linea = texto.read()
texto.close()
resultado= open("HERALDOSNEGROS_pre.txt", 'w')

#1 Reeemplazar j->i  h->i  ñ->n  k->l  u->v w->v  y->z
def reemplazar():
    global linea
    for i,j in letras_reemplazar:
        linea= linea.replace(i,j)
          
#2 Eliminar las tildes de las vocales
def tilde():
    global linea
    for i,j in tildes:
        linea= linea.replace(i,j)
        
#3 Todas las letras a Mayusculas
def mayuscula():
    global linea
    for letra in linea :
            linea= linea.replace(letra,letra.upper())
            
#4 Elimine los espacios en blanco y segnos de puntuacion

def signos():
    global linea
    for s in signo:
            linea= linea.replace(s,"")

# Guardar en "HERALDOSNEGROS_pre.txt"
def guardar():
    resultado.write(linea)
    resultado.close()

#5 Tabla de frecuencias (diccionario ) - 5 mayor frecuencia

def frecuencias(archivo):
    global lineaP,s2
    texto = open(archivo+".txt")
    lineaP = texto.read()
    texto.close()
    #Diccionario de frecuencias
    DiccFrecuencias ={}
    for i in lineaP:
        DiccFrecuencias[i]=DiccFrecuencias.get(i,0)+1
    print('Frecuencias : '+str(DiccFrecuencias))
    #Ordenar    
    s1= sorted(DiccFrecuencias)
    #Mayores 5
    s2 =s1[:5]
    print('Mayor frecuencias : '+ str(s2))

#6 Aplicar el método Kasiski


    
def main():
    #1era Parte
    reemplazar()
    tilde()
    mayuscula()
    signos()
    guardar()
    #2da Parte
    frecuencias("HERALDOSNEGROS_pre")
    

    
if __name__ == '__main__':
    main()

