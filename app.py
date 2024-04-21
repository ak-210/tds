import streamlit as st
st.write("""
# Largest number 

This app predicts the largest of the given 3 numbers
""")
st.header('User input numbers')
num1 = st.number_input('FIRST NUMBER')
num2 = st.number_input('SECOND NUMBER')
num3 = st.number_input('THIRD NUMBER')

  # data = {'FIRST NUMBER' : num1,
  #         'SECOND NUMBER' : num2,
  #         'THIRD NUMBER' : num3
  #         }
ans = 0
if(num1>num2 and num1>num3) :
  ans = num1
elif(num2 > num1 and num2 > num3) :
  ans = num2
elif(num3>num1 and num3>num2):
  ans = num3
elif(num1==num2):
  if(num1 > num3):
    ans = num1
  else:
    ans = num3
elif(num2==num3):
  if(num2 > num1):
    ans = num2
  else:
    ans = num1
elif(num1==num3):
  if(num1 > num2):
    ans = num1
  else:
    ans = num2
elif(num1==num2==num3):
  ans = num1
st.subheader("The largest number")
st.write(ans)
