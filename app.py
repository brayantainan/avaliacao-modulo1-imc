import streamlit as st

st.title("Calculadora IMC ")
st.subheader("Feito com Streamlit 💓")

altura = st.number_input("Digite sua altura", min_value = 0.0)
peso = st.number_input("Digite seu peso", min_value = 0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.info(f"Seu imc é {imc:.2f}")
    
    if imc < 18.5:
        st.error("Abaixo do peso")
        st.image("https://static.wikia.nocookie.net/liberproeliis/images/2/27/Seu_Madruga_.jpeg/revision/latest?cb=20191021194541&path-prefix=pt-br")
    elif imc < 24.9:
        st.success("Peso normal")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/047/830/014/small/smiling-man-giving-a-thumbs-up-wearing-a-striped-shirt-isolated-on-white-background-showing-positive-gesture-and-confidence-png.png")
    elif imc < 29.9:
        st.error("Sobrepeso")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL6cuwlAVm3EazGDVqWl2e5TPNht4DdMNTcg&s")
    elif imc < 34.9:
        st.error("Obesidade Grau 1")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL6cuwlAVm3EazGDVqWl2e5TPNht4DdMNTcg&s")
    elif imc < 39.9:
        st.error("Obesidade Grau 2")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL6cuwlAVm3EazGDVqWl2e5TPNht4DdMNTcg&s")
    else:
        st.error("Obesidade Grau 3 (mórbida)")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL6cuwlAVm3EazGDVqWl2e5TPNht4DdMNTcg&s")