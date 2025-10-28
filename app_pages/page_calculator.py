# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
    
import streamlit as st

def calculator_body():
    st.write('----')
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input('Enter first number', step=1)
    with col2:
        num2 = st.number_input('Enter second number', step=1)
    with col3:
        operation = st.selectbox(label='Select operation', 
                                 options=['Addition', 'Subtraction', 'Multiplication', 'Division'])
    if st.button('Click here for the maths'):
        if num2 == 0 and operation == 'Division':
            st.error('Cannot divide by zero, try again.')
        else:
            calculator_function(num1, num2, operation)

def calculator_function(num1, num2, operation):
    if operation == 'Addition':
            result = num1 + num2
    elif operation == 'Subtraction':
            result = num1 - num2
    elif operation == 'Multiplication':
            result = num1 * num2
    elif operation == 'Division':
            result = num1 / num2
    st.write(f'Result: **{result}**')