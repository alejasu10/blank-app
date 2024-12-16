import streamlit as st
import pandas as pd
import time
#crea una funcion de la misma manera que en python
def prueba():

    y= pd.DataFrame(
        {
            "Nombre": ["felipe", "juan", "carlos", "david"],
            "Apellido": ["suarez", "aaaa", "sssss", "dddd"],
        }
    )
    return y
#la funcion llamada se instancia de la misma manera
if __name__ == "__main__":
    #le damos nombre a las pagianas creadas
    pages = {
         #nombre si quiero colcoar las paginas dentro de una clasificion
    "Your account": [
          st.Page("pages/INICIO.py", title="Inicio"),
        st.Page("pages/pagina2.py", title="")
       
    ]
       
}
#iniciamos las paginas creadas con los nombres
    pg = st.navigation(pages)
    pg.run()
#side bar con las pigans creadas
    with st.sidebar:
            if st.button("HOLA"):
                st.write("hola")

    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    st.write("hola mundo")
    x=10
    st.write(f"mi numero es: {x}")
    st.title("mundo")
#boton que llama a la funcion anterior
    if st.button("hola"):
        st.write(prueba())

    #hacemos un cambio de pag con el metodo link
    st.page_link("pages/INICIO.py")
#creamos un boton que cambie de pagia al presionar
    if st.button("Page 2"):
        st.switch_page("pages/pagina2.py")
# creamos una operacion donde pedimos numeros y sumamos y multiplicamos en este caso
    number=st.number_input("insert a number")
    numb1=st.number_input("insert a number1")
    numb2=st.number_input("insert a number2")
    suma=int(numb1)+int(numb2)
    if suma:
        st.write(f"la suma es: {suma}")
    if number:
         st.write(f"el doble del numero es {number*2}")
#creamos columnas, e identificamos
col1,col2=st.columns(2)

with col1:
     st.write("columna 1")

with col2:
     st.write("columna 2")

#fotos

"""foto=st.camera_input("sacar una foto")
if foto:
     st.image(foto)"""

#para subir un archivo

f=st.file_uploader("subir un archivio")

if f:
     x=f.read()
     st.write(x)
     st.success("tu archivo se ha subido")
     st.error("tu archivo no se ha subido")
     #barra metrica
st.metric(label="temperatura",value=40,delta=-5)
# barra de progreso
pb= st.progress(0)
for i in range(100):
    time.sleep(0.5)
    pb.progress(i)

with st.expander("leer mas"):
     st.write("jsjsjs")