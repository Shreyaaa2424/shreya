import streamlit as st
st.title("some basic command  like slider button etc")

age =st.slider("enter your age",1,100,)
city =st.selectbox("choose your city",["Delhi", "mumbai","pune","banglore"])
if st.button("shoe details"):
    st.write("your age is", age)
    st.write("your city is", city)

