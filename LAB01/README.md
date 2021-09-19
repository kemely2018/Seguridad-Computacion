# LABORATORIO 01 : FUNCIONES ELEMENTALES DE CRIPTOGRAFÍA

Sobre el texto claro mostrado a continuación:
```
Hay golpes en la vida, tan fuertes... ¡Yo no sé!
Golpes como del odio de Dios; como si ante ellos,
          la resaca de todo lo sufrido
      se empozara en el alma... ¡Yo no sé!

 Son pocos; pero son... Abren zanjas oscuras
en el rostro más fiero y en el lomo más fuerte.
 Serán tal vez los potros de bárbaros Atilas;
o los heraldos negros que nos manda la Muerte.

  Son las caídas hondas de los Cristos del alma
  de alguna fe adorable que el Destino blasfema.
  Esos golpes sangrientos son las crepitaciones
de algún pan que en la puerta del horno se nos quema.

Y el hombre... Pobre... ¡pobre! Vuelve los ojos, como
  cuando por sobre el hombro nos llama una palmada;
      vuelve los ojos locos, y todo lo vivido
  se empoza, como charco de culpa, en la mirada.

  Hay golpes en la vida, tan fuertes... ¡Yo no sé!
```
 	

### 1. Reeemplazar j->i  h->i  ñ->n  k->l  u->v w->v  y->z (Minusculas)
```
def reemplazar():
    global linea
    for i,j in letras_reemplazar:
        linea= linea.replace(i,j)
```

```
Haz golpes en la vida, tan fvertes... ¡Yo no sé!
Golpes como del odio de Dios; como si ante ellos,
          la resaca de todo lo svfrido
      se empozara en el alma... ¡Yo no sé!

 Son pocos; pero son... Abren zanias oscvras
en el rostro más fiero z en el lomo más fverte.
 Serán tal vez los potros de bárbaros Atilas;
o los ieraldos negros qve nos manda la Mverte.

  Son las caídas iondas de los Cristos del alma
  de algvna fe adorable qve el Destino blasfema.
  Esos golpes sangrientos son las crepitaciones
de algún pan qve en la pverta del iorno se nos qvema.

Y el iombre... Pobre... ¡pobre! Vvelve los oios, como
  cvando por sobre el iombro nos llama vna palmada;
      vvelve los oios locos, z todo lo vivido
  se empoza, como ciarco de cvlpa, en la mirada.

  Haz golpes en la vida, tan fvertes... ¡Yo no sé!
```


### 2. Eliminar las tildes de las vocales
```
def tilde():
    global linea
    for i,j in tildes:
        linea= linea.replace(i,j)
```

```
Haz golpes en la vida, tan fvertes... ¡Yo no se!
Golpes como del odio de Dios; como si ante ellos,
          la resaca de todo lo svfrido
      se empozara en el alma... ¡Yo no se!

 Son pocos; pero son... Abren zanias oscvras
en el rostro mas fiero z en el lomo mas fverte.
 Seran tal vez los potros de barbaros Atilas;
o los ieraldos negros qve nos manda la Mverte.

  Son las caidas iondas de los Cristos del alma
  de algvna fe adorable qve el Destino blasfema.
  Esos golpes sangrientos son las crepitaciones
de algun pan qve en la pverta del iorno se nos qvema.

Y el iombre... Pobre... ¡pobre! Vvelve los oios, como
  cvando por sobre el iombro nos llama vna palmada;
      vvelve los oios locos, z todo lo vivido
  se empoza, como ciarco de cvlpa, en la mirada.

  Haz golpes en la vida, tan fvertes... ¡Yo no se!
```

### 3. Todas las letras a Mayusculas
```
def mayuscula():
    global linea
    for letra in linea :
            linea= linea.replace(letra,letra.upper())
```

```
HAZ GOLPES EN LA VIDA, TAN FVERTES... ¡YO NO SE!
GOLPES COMO DEL ODIO DE DIOS; COMO SI ANTE ELLOS,
          LA RESACA DE TODO LO SVFRIDO
      SE EMPOZARA EN EL ALMA... ¡YO NO SE!

 SON POCOS; PERO SON... ABREN ZANIAS OSCVRAS
EN EL ROSTRO MAS FIERO Z EN EL LOMO MAS FVERTE.
 SERAN TAL VEZ LOS POTROS DE BARBAROS ATILAS;
O LOS IERALDOS NEGROS QVE NOS MANDA LA MVERTE.

  SON LAS CAIDAS IONDAS DE LOS CRISTOS DEL ALMA
  DE ALGVNA FE ADORABLE QVE EL DESTINO BLASFEMA.
  ESOS GOLPES SANGRIENTOS SON LAS CREPITACIONES
DE ALGUN PAN QVE EN LA PVERTA DEL IORNO SE NOS QVEMA.

Y EL IOMBRE... POBRE... ¡POBRE! VVELVE LOS OIOS, COMO
  CVANDO POR SOBRE EL IOMBRO NOS LLAMA VNA PALMADA;
      VVELVE LOS OIOS LOCOS, Z TODO LO VIVIDO
  SE EMPOZA, COMO CIARCO DE CVLPA, EN LA MIRADA.

  HAZ GOLPES EN LA VIDA, TAN FVERTES... ¡YO NO SE!
```

### 4. Elimine los espacios en blanco y signos de puntuacion
```
def signos():
    global linea
    for s in signo:
            linea= linea.replace(s,"")
```

```
HAZGOLPESENLAVIDATANFVERTESYONOSEGOLPESCOMODELODIODEDIOSCOMOSIANTEELLOSLARESACADETODOLOSVFRIDOSEEMPOZARAENELALMAYONOSESONPOCOSPEROSONABRENZANIASOSCVRASENELROSTROMASFIEROZENELLOMOMASFVERTESERANTALVEZLOSPOTROSDEBARBAROSATILASOLOSIERALDOSNEGROSQVENOSMANDALAMVERTESONLASCAIDASIONDASDELOSCRISTOSDELALMADEALGVNAFEADORABLEQVEELDESTINOBLASFEMAESOSGOLPESSANGRIENTOSSONLASCREPITACIONESDEALGUNPANQVEENLAPVERTADELIORNOSENOSQVEMAYELIOMBREPOBREPOBREVVELVELOSOIOSCOMOCVANDOPORSOBREELIOMBRONOSLLAMAVNAPALMADAVVELVELOSOIOSLOCOSZTODOLOVIVIDOSEEMPOZACOMOCIARCODECVLPAENLAMIRADAHAZGOLPESENLAVIDATANFVERTESYONOSE
```

### 5.Tabla de frecuencias (diccionario ) - 5 mayor frecuencia
```
def frecuencias(archivo):
    global lineaP,s2
    texto = open(archivo+".txt")
    lineaP = texto.read()
    texto.close()
    #Diccionario de frecuencias
    DiccFrecuencias ={}
    for i in lineaP:
        DiccFrecuencias[i]=DiccFrecuencias.get(i,0)+1
    print('*Frecuencias : '+str(DiccFrecuencias))
    #Ordenar    
    s1= sorted(DiccFrecuencias.values())
    s1.reverse()
    D ={}
    for i in s1:
        for j in DiccFrecuencias.keys():
            if DiccFrecuencias[j]==i:
                D[j]=DiccFrecuencias[j]   
    s2=list(D.keys())
    s3 =s2[:5]
```

```
*Frecuencias : {'H': 2, 'A': 65, 'Z': 8, 'G': 8, 'O': 83, 'L': 47, 'P': 17, 'E': 74, 'S': 59, 'N': 36, 'V': 26, 'I': 26, 'D': 27, 'T': 18, 'F': 7, 'R': 33, 'Y': 4, 'C': 16, 'M': 20, 'B': 10, 'Q': 4, 'U': 1}
*Mayor frecuencia:['O', 'E', 'A', 'S', 'L']
```

### 6. Aplicar el método Kasiski
```
def kasiski():
    C=[]
    dic={}
    txt = lineaP
    for i in range(len(txt)-2):
        C.append(txt[i:i+3])
    for k in C:
        a = C.count(k)
        if a > 1:
            dic[k]=a
```

```
{'HAZ': 2, 'AZG': 2, 'ZGO': 2, 'GOL': 4, 'OLP': 4, 'LPE': 4, 'PES': 4, 'ESE': 3, 'SEN': 4, 'ENL': 4, 'NLA': 6, 'LAV': 2, 'AVI': 2, 'VID': 3, 'IDA': 3, 'DAT': 2, 'ATA': 2, 'TAN': 2, 'ANF': 2, 'NFV': 2, 'FVE': 3, 'VER': 5, 'ERT': 5, 'RTE': 4, 'TES': 4, 'ESY': 2, 'SYO': 2, 'YON': 3, 'ONO': 4, 'NOS': 7, 'OSE': 6, 'SCO': 3, 'COM': 4, 'OMO': 5, 'ODE': 3, 'DEL': 4, 'ELO': 4, 'DIO': 2, 'IOS': 3, 'OSC': 4, 'OSI': 2, 'ANT': 2, 'EEL': 3, 'ELL': 2, 'LLO': 2, 'LOS': 7, 'OSL': 3, 'ADE': 3, 'TOD': 2, 'ODO': 2, 'DOL': 2, 'OLO': 3, 'IDO': 2, 'DOS': 3, 'SEE': 2, 'EEM': 2, 'EMP': 2, 'MPO': 2, 'POZ': 2, 'OZA': 2, 'AEN': 2, 'ENE': 3, 'NEL': 3, 'ELA': 2, 'LAL': 2, 'ALM': 3, 'LMA': 3, 'MAY': 2, 'ESO': 3, 'SON': 4, 'OCO': 2, 'COS': 2, 'OSP': 2, 'ERO': 2, 'ROS': 5, 'OSO': 3, 'BRE': 5, 'ASO': 2, 'SOS': 2, 'TRO': 2, 'OMA': 2, 'MAS': 2, 'ASF': 3, 'IER': 2, 'ERA': 2, 'LVE': 3, 'OSD': 2, 'SDE': 4, 'BAR': 2, 'LAS': 4, 'OSQ': 2, 'SQV': 2, 'QVE': 4, 'ENO': 2, 'AND': 2, 'NDA': 2, 'LAM': 3, 'ONL': 2, 'ASC': 2, 'DAS': 2, 'ION': 2, 'SCR': 2, 'TOS': 2, 'MAD': 2, 'DEA': 2, 'EAL': 2, 'ALG': 2, 'VNA': 2, 'VEE': 2, 'EMA': 2, 'REP': 3, 'ELI': 3, 'LIO': 3, 'IOM': 2, 'OMB': 2, 'MBR': 2, 'EPO': 2, 'POB': 2, 'OBR': 3, 'VVE': 2, 'VEL': 4, 'ELV': 2, 'SOI': 2, 'OIO': 2, 'MOC': 2, 'ADA': 2}
```

### 7. UNICODE-8
```
def utf8():
    l = lineaP
    for i,j in UTF_8:
        l= l.replace(i,j)
```

```
48415a474f4c504553454e4c415649444154414e46564552544553594f4e4f5345474f4c504553434f4d4f44454c4f44494f444544494f53434f4d4f5349414e5445454c4c4f534c415245534143414445544f444f4c4f5356465249444f5345454d504f5a415241454e454c414c4d41594f4e4f5345534f4e504f434f535045524f534f4e414252454e5a414e4941534f534356524153454e454c524f5354524f4d4153464945524f5a454e454c4c4f4d4f4d4153465645525445534552414e54414c56455a4c4f53504f54524f5344454241524241524f534154494c41534f4c4f53494552414c444f534e4547524f535156454e4f534d414e44414c414d5645525445534f4e4c4153434149444153494f4e44415344454c4f5343524953544f5344454c414c4d414445414c47564e41464541444f5241424c45515645454c44455354494e4f424c415346454d4145534f53474f4c50455353414e475249454e544f53534f4e4c41534352455049544143494f4e45534445414c47554e50414e515645454e4c4150564552544144454c494f524e4f53454e4f535156454d4159454c494f4d425245504f425245504f4252455656454c56454c4f534f494f53434f4d4f4356414e444f504f52534f425245454c494f4d42524f4e4f534c4c414d41564e4150414c4d4144415656454c56454c4f534f494f534c4f434f535a544f444f4c4f56495649444f5345454d504f5a41434f4d4f43494152434f444543564c5041454e4c414d495241444148415a474f4c504553454e4c415649444154414e46564552544553594f4e4f5345
```

### 9. AQUÍ cada 20 caracteres
```
def aqui():
    global lineaP
    n=len(lineaP)
    d=20
    r=n//d
    l1=""
    for i in range(d, n+1, d):
        l1 = l1+lineaP[i-20:i]+'HOY'
    l1 = l1+lineaP[r*d:]
    n1=len(l1)
    if (n1%4 != 0):
        rr=(n1//4+1)*4
        for i in range(rr-n1):
            l1=l1+'X'
```

```
HAZGOLPESENLAVIDATANHOYFVERTESYONOSEGOLPESCHOYOMODELODIODEDIOSCOMOHOYSIANTEELLOSLARESACADHOYETODOLOSVFRIDOSEEMPOHOYZARAENELALMAYONOSESOHOYNPOCOSPEROSONABRENZAHOYNIASOSCVRASENELROSTRHOYOMASFIEROZENELLOMOMAHOYSFVERTESERANTALVEZLOHOYSPOTROSDEBARBAROSATIHOYLASOLOSIERALDOSNEGROHOYSQVENOSMANDALAMVERTEHOYSONLASCAIDASIONDASDEHOYLOSCRISTOSDELALMADEAHOYLGVNAFEADORABLEQVEELHOYDESTINOBLASFEMAESOSGHOYOLPESSANGRIENTOSSONLHOYASCREPITACIONESDEALGHOYUNPANQVEENLAPVERTADEHOYLIORNOSENOSQVEMAYELIHOYOMBREPOBREPOBREVVELVHOYELOSOIOSCOMOCVANDOPOHOYRSOBREELIOMBRONOSLLAHOYMAVNAPALMADAVVELVELOHOYSOIOSLOCOSZTODOLOVIVHOYIDOSEEMPOZACOMOCIARCHOYODECVLPAENLAMIRADAHAHOYZGOLPESENLAVIDATANFVHOYERTESYONOSEXX
```
