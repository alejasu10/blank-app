import streamlit as st
import pandas as pd

def prueba():

    y= pd.DataFrame(
        {
            "Nombre": ["felipe", "juan", "carlos", "david"],
            "Apellido": ["suarez", "aaaa", "sssss", "dddd"],
        }
    )
    return y

if __name__ == "__main__":
    pages = {
    "Your account": [
        st.Page("pages/CUENTAS.py", title="Create your account"),
        st.Page("pages/INICIO.py", title="Manage your account")
    ]
       
}

    pg = st.navigation(pages)
    pg.run()

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

    if st.button("hola"):
        st.write(prueba())

    
    st.page_link("pages/INICIO.py")

    if st.button("Page 2"):
        st.switch_page("pages/CUENTAS.py")

    number=st.number_input("insert a number")
    numb1=st.number_input("insert a number1")
    numb2=st.number_input("insert a number2")
    suma=int(numb1)+int(numb2)
    if suma:
        st.write(f"la suma es: {suma}")
    if number:
         st.write(f"el doble del numero es {number*2}")

