import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
#uso del fuzzywuzzy
cadena1="hola mundo"
cadena2="hola mundo"

similitud= fuzz.ratio(cadena1,cadena2)

st.write(f"la similitud es {similitud}%")

#Buscamos una cancion usando fuzzywuzzy en una lista con dic
album = [{"track_id":1,
       "tittle":"yellow",
       "author":"coldplay",
       "duration":3.10 } ,

       {"track_id":2,
       "tittle":"thunder",
       "author":"inmagine dragons",
       "duration":3.12 } ,
       
       {"track_id":3,
       "tittle":"stained",
       "author":"linkin park",
       "duration":3.00 }]
         
       #pedimos el nombre de la cancion
buscar_cancion=st.text_input("que cancion buscas")
ratio=0
#hacemos la busqeuda de la cancion 
if buscar_cancion:
       for i in album:
              #usamos el fuzzy para verificar que cancion es similar
              simil=fuzz.ratio(i["tittle"].lower(),buscar_cancion.lower())
              if simil>ratio:
                     ratio=simil
                     cancion_cerca=i
       st.write(cancion_cerca)
    
#buscar cancion mas larga
x=[c["duration"]for c in album]
opcion=st.selectbox("Introduce una opcion:",
                    ["cancion mas corta","cancion mas larga"])
if opcion=="cancion mas larga":
       st.write(max(x))

elif opcion=="cancion mas corta":
       st.write(min(x))
#crea barras de datos
st.bar_chart(x)

dias_semana=[{"lunes":-5},{"martes":4},{"miercoles":8},{"jueves":-7}]

st.bar_chart(dias_semana,y_label="celsius")