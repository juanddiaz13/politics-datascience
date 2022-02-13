from googlesearch import search
from urllib.parse import urlparse
import pandas as pd

#Carga de de los datos
df=pd.read_excel("20220131_candidatos-congreso_18012022.xlsx", sheet_name="Candidatos")
division=pd.read_excel("20220131_candidatos-congreso_18012022.xlsx", sheet_name="Sheet1")

#Funcion made by Semillero to search a twitter account given the full name of the politician
def identify_twitter (nombre):
    query= nombre +" twitter"
    #print(query)
    count=0
    username=None
    while username is None:
        response = search(query, tld="co.in", num=1, stop=1, pause=2)
        count+=1
        for result in response:
            parsed_url=urlparse(result)
            if "twitter" in parsed_url.hostname:
                if "status" not in parsed_url.path:
                    username=parsed_url.path
        if count>=10:
            break
    return username
    print(username,count)
    
#given the Semillero's member, returns the range of politicians he's to take care of
def buscar_nombre(numero):
    print("Bienvenido,", division["Semillero "][numero])
    num1=division["empezar"][numero]
    num2=division["terminar"][numero] 
    print("Su rango de consulta es",num1,"hasta",num2)
    return [num1,num2]

#given a number in the range of politician, returns the full name stored in Candidatos sheet
def extraer_nombre(numero):
    i=numero
    nombre=""
    nombre+=df["NOMBRE1"][i-1]+" "
    nombre+=df["NOMBRE2"][i-1]+" "
    nombre+=df["APELLIDO1"][i-1]+" "
    nombre+=df["APELLIDO2"][i-1]
    return nombre


    
#print("Ingrese su nombre completo, por favor: ")

print("-----------***********************-----------")
print("-----------Bienvenido al semillero-----------")
print("-----------***********************-----------")
print("Digite el numero correspondiente a su nombre:")

numero_input = int(input())
numeros=buscar_nombre(numero_input)

print(extraer_nombre(numeros[0]))





