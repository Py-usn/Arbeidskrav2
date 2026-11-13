#%% Oppgave 1

alder = int(input('Hvilket år er du født?'))
alder = 2024 - alder

print ('person blir', alder,'i 2024')

#%% Oppgave 2

antall_elever = int(input('skriv inn antall elever'))
antall_pizza = antall_elever * 0.25

import numpy as np
helepizza = np.ceil(antall_pizza)

helepizza = int(helepizza)

print ('Det må handles inn ', helepizza, 'til festen')

#%% Oppgave 3

import numpy as np

v_grad = float(input('skriv inn gradtallet'))


def fun_v_grad2v_rad(v_grad):
    v_rad = v_grad*np.pi/180
    return v_rad

v_rad = fun_v_grad2v_rad(v_grad)

print(v_grad,'grader er', v_rad,'radianer')

#%% Oppgave 4 a)

data = {
     "Norge":["Oslo", 0.634],
     "England":["London", 8.982],
     "Frankrike":["Paris", 2.161],
     "Italia":["Roma", 2.873]
     } 

#%% Oppgave 4 b)

print (f"{data['England'][0]} er hovedstaden i England og det er {data['England'][1]} millioner innbyggere i London.")

#%% Oppgave 4 c)

nytt_land = input ("skriv inn navnet på nytt land:").strip().capitalize()

#sjekker om landet allerede finnes i dictionary
if nytt_land in data:
    print(f"{nytt_land} finnes allerede i oversikten.")
else:
    #ber om hovedstaden og innbyggertall
    hovedstad = input (f" Hva er hovedstaden i {nytt_land}?").strip().capitalize()
    innbyggere = int(input (f" hvor mange innbyggere har {nytt_land}?"))
    
data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}

print ("\nOppdateret dictionary:")
print(data)
    
#%% Oppgave 5

import numpy as np

Katet_a = float(input('lengde på katet a'))
Katet_b = float(input('lengde på katet b'))

def utregning_figur(a,b):
    r=a/2
    areal_halvsirkel = np.pi**r/2
    areal_trekant = a*b/2
    omkrets_halvsirkel = 2*np.pi*r/2
    hypotenus = np.sqrt(a**2 + b**2)
    omkrets_trekant = b + hypotenus
    totalt_areal = areal_halvsirkel + areal_trekant
    total_omkrets = omkrets_halvsirkel + omkrets_trekant
    return totalt_areal,total_omkrets

totalt_areal, total_omkrets = utregning_figur(Katet_a, Katet_b)

print ('Det totale arealet er',totalt_areal, 'og total ytre omkrets er', total_omkrets)


#%% Oppgave 6

import numpy as np

import matplotlib.pyplot as plt

def f(x):
    return -x**2 -5

x = np.linspace(-10,10,200)

y = f(x)

plt.plot(x,y, label= "f(x) = -x**2 - 5", color='lightskyblue', linewidth=2)
