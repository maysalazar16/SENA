'''los conjuntos son un tipo de conexion donde los elemententos se juntan de manera desordenada, que su principal caracteristica es que no pueden tener duplicados
 cuando se crea un conjunto vacio, simrpe ira de la siguiente manera

 conjunto = set()
 conjunto = {}

 de tal manera sabemos que es un conjunto

 NOOOOO se puede colocar

 conjunto = set{}  ya que de esta forma python lo toma como un diccionrio 


 dentro de los conjunto no podemos tenener otro tipo de colecciones como por ejemplo una lista, ya que no se puede tener colecciones

'''


# conjunto = set()
# conjunto ={1,2,3,"hola",4.56}
# # conjunto ={1,2,3,"hola",4.56,1,2,3}    # si duplicamos valores el conjunto iempre se va guardar como valor unicos, no pueden haber duplicados 
# # conjunto.add(5)                          # agrega el valor de 5 pero lo agrega en cualquier parte del conjunto, ya que el conjunto guarda los valores en forma desordenada
# # conjunto.add("adios")
# # conjunto.add("dias")


# # conjunto.discard(3)                     # conjuto.discard(3) elimina el valor que agregemos dentro del parentesis
# # conjunto.discard("adios")


# # conjunto.clear()                      # nos limpia y nos deja bacio el conjunto, imprime set() ya que set() es el nombre del conjuto

# print(4.53 in conjunto)                #   .in = se utiliza para preguntarle a la lista si el valor esta nos dira True o false

# print(conjunto)



'''//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
'''cuando creas un conjunto con elemento, sencillamente creas la variable con el nombre abres llaves{} y lo separas por comas,
python al ver que lo estas seprando por comas y no por dos puntos, entendera que es un conjunto y no un diccionario 


ejemplo '''


# a = {1,2,3}
# b = {3,4,5}
# print(a == b)    # nos indicara FALSE  porque los dos conjuntos no son iguales 

# a = {1,2,3}
# b = {2,3,1}
# print(a == b)    # nos indicara TRUE porque el conjunto asi esten en desorden el valida que teng los mismos numeros 


# print(len(a))     #len nos idncica cuantos elementos tenemos en el conjunto, en ese caso indicaria que tenemos 3


'''operaciones que podemos hacer en co junto'''

'''union de dos conjuntos'''

# a = {1,2,3} # esto es un ejemplo  de diccionariosgit 
# b = {3,4,5}

# c = a | b

# print(c)


'''la interseccion
recuerdaa que son aquellos elementos que estan en los dos conjuntos'........''

# a = {1,2,3}
# b = {3,4,5}

# c = a & b

# print(c)


'''la diferencia

es simplemente elementos que estan en el conjunto A y no esta en el conjunto B'''

# a = {1,2,3}
# b = {3,4,5}

# # c = a - b

# c = a ^ b                  # diferencia simetrica son elementos que estan en A y B pero que no estan en ambos 

# print(c)



'''para determinar si un conjunto es un subconjunto de otro'''

# a = {1,2,3}
# b = {3,4,5}
# c = {1,2,3,4,5}

# print(a.issubset(c))          # si a es un issubset es un subconjunto de c nos dira que es verdadero porque c tiene los mismos valores que a

# print(c.issuperset(a))         #para validar si c es super conjunto de a o de b

# print(a.isdisjoint(b))         #podemos tambien saber si ambos conjuntos son disconexos(no comparten numeros en comun)


''' de esta manera dejamos a nuestro conjunto inmutable, con lo cual ya no se puede egregar,modifica,o eliminar elementos '''
# a = frozenset({1,2,3})      
# b = {3,4,5}
# print(a)