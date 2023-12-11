import streamlit as st

st.title('Find the Largest Numbers')

st.header('Enter numbers : ')

num1 = st.number_input('Input first number')
num2 = st.number_input('Input second number')
num3 = st.number_input('Input third number')

def maximum(num1,num2,num3):
    return max(num1, num2, num3)
    

if st.button("Find Largest"):
    largest=maximum(num1,num2,num3)
    st.success(f'The largest number is :{largest}')
