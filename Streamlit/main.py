import streamlit as st
import time as t

st.image("rain.png")
#title - it is used to add the title of an app
st.title("Welcome to Streamlit")

#Header - 
st.header("Machine Learning")

# sub-header
st.subheader("Linear Regression")

# To give Information
st.info("Information details of a user")

# Warning message
st. warning("come on time or else you will marked as absent")
#Error message 
st.error("Wrong Password")

#Success message
st.success("Congrats you have get A grade")

# write 
st.write("Employee name")
st.write(range(50))

#Markdown
st.markdown("Shyam")
st.markdown("# Shyam")
st.markdown("## Shyam")

st.markdown(":moon:")

st.text("Hello Learners")

#To write a caption
st.caption("Caption is here")

# to display mathematical equation.
st.latex(r''' a+b x^2+c''')


# Widget

#checkbox
st.checkbox('Login')

#button
st.button("click")

#radio widget
st.radio("Pick you gender","Male", "Female", "Other")

#select box
st.selectbox("Pick your course", ["ML", "cloud", "cyber security"])

#multiselect
st.multiselect("choose the dept", ["Content", "Sales", "market"])

# selectslider
st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding"])

# slider
st.slider("enter your number", 0, 100)

#number input
st.number_input("pick a number",0,100)

#text_input
st.text_input("enter your email address")

#date input
st.date_input("Opening ceremony")

#time input
st.time_input("Hey whats the timing")

#text area
st.text_area("welcome to the streamlit for web app deployment")

#upload a file
st.file_uploader("upload your file/folder")

#choosing a color
st.color_picker("color")

#progress
st.progress(90)

#spinner
with st.spinner("just wait"):
    t.sleep(3)

#ballon
st.balloons()

#sidebar
st.sidebar.title("welcome to shyam")
st.sidebar.text_input("Mail address")
st.sidebar.text_input("Password")
st.sidebar.button("submit")
st.sidebar.radio("Professional Expert", ["Student", "Working", "Others"])

#data visualizaion
import pandas as pd
import numpy as np

st.title("Bar chart")
data=pd.DataFrame(np.random.randn(50, 2), columns=["x","y"])
st.bar_chart(data)

st.title("Line chart")
st.line_chart(data)

st.title("Area chart")
st.area_chart(data)