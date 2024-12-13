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