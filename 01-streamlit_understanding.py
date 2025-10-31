#running the streamlit file in python cmd: "streamlit run python_file.py"
import streamlit as st
from traitlets import default
from PIL import Image
import time

st.markdown("## Header: ")
#header
st.title("This is 'Title' of streamlit")
st.header("_Streamlit_ is :blue[cool] and this is :red[header]")
st.subheader("This line is  :orange[subheader]")
# st.divider()



st.markdown("## text(). ")
# To display text on screen
st.text("This is some text")        



st.markdown("## Taking input from user by test_input().")
# read input from the user
text_input=st.text_input("Enter the you input in below box", "Something type here")

#display on screen.
st.text(text_input)

#Display multi-line text input widget
st.text_area("This is multi-line taking input by user")

#Display single-line text input widget
st.text_input("This is single line taking user input")

#read your password
user_password = st.text_input("this is the text area", type='password')




st.markdown("## Markdown")
#markdown
st.markdown("this information is very __important__.")  #underscore using for bold
st.markdown("*Streamlit* is **really** ***cool***.")    #* is using for tilt, bold and tilt
st.markdown("###### This is Heading:")                    # "####" using for headding.

#multi items markdonw.
st.markdown("""This is multi-item markdown             
            1. first item 
            2. second item
            3. third item
            4. fourth item""")



st.markdown("# Buttons:")
# Display a button widget.
button = st.button("Click Here")

if button:
    st.text("This is the tutorial for understanding of streamlit app.")
    st.info("Hey, You clicked me!")         #Display an informational message.
    st.toast("Hii, I'm going to disappear in 4 sec")  #Display a short message on top right corner, in 4sec it will disappear.
    st.warning("This is warning for you. dont waste your time.",icon='⚠️') #Display warning message.
    
    st.error("This is error from your side. thats not my fault.", icon=":material/error:")
    
    
 
    
st.markdown("# Checkbox ")

#Display a checkbox widget and True/False given.
agree=st.checkbox('Please agree terms and condi.')
if agree:
    st.write("✅ You agreed!")
else:
    st.write("❌ You didn’t agree.")

# st.markdown("### this is checkbox") 

#multiple checkbox example  
option_a = st.checkbox("Option A")
option_b = st.checkbox("Option B")
option_c = st.checkbox("Option C")
option_d = st.checkbox("Option D")

if option_a:
    st.write("You selected A")
if option_b:
    st.write("You selected B")
if option_c:
    st.write("You selected C")
if option_d:
    st.write("You selected D")



st.markdown("# Colum wise seperation")

# using column divide vertically.
col1, col2 = st.columns(2)

with col1:
    # st.text() — plain text only
    # Displays raw text (no formatting, no markdown, no variables interpreted).
    # Everything is shown exactly as it is.
    st.text("*This is text() function*")  
    st.text("Result: 5 + 2 = {7}")  # shows literally {7}, not computed
    st.text("Text Display simple text")
    
with col2:    
    # st.write() — smart display
    # It’s versatile — can show text, numbers, DataFrames, Markdown, Matplotlib charts, and more.
    # It automatically detects the data type and displays it appropriately.
    x = 7
    st.write("*This is write() function*")
    st.write("Result:", 5 + 2)       # shows: Result: 7
    st.write({"a": 1, "b": 2})       # shows a table
    st.write("##### This is a Markdown heading")
    
 
    
st.markdown("## Radio button, select box, multi select:")

col1, col2, col3 = st.columns(3)

with col1:
    st.text("1. Radio Button")
    movie_name=st.radio("What is your favorite movie.", ['Horror', 'Thrilled', 'comedy', 'Action'])
    st.write("you selected: ", movie_name)
    
with col2:
    st.text("2. Select box")
    movie_name=st.selectbox("What is your favorite movie.", ['Horror', 'Thrilled', 'comedy', 'Action'])
    st.write("you selected: ", movie_name)
    
with col3:
    st.text("2. Multiselect.")
    movie_name=st.multiselect("What is your favorite movie.", ['Horror', 'Thrilled', 'comedy', 'Action'])
    st.write("you selected: ", movie_name) 
 
    
    
st.markdown("## Slidder: ")

col1, col2 = st.columns(2)
with col1:
    st.text("2. Slidder")
    threshold=st.slider("Select the Threshold.", min_value=0, max_value=100, step=5)
    st.write("Hey, You selected threshold value is : ", threshold)
    
with col2:
    st.text("2. Slidder")
    color=st.select_slider("Select a color of the rainbow",
     options=[
         "red",
         "orange",
         "yellow",
         "green",
         "blue",
         "indigo",
         "violet"])
     #value=['red', 'blue'])
    st.write("You selected:", color)



st.markdown("## Spinner:")
with st.spinner("Wait for it...."):
    time.sleep(10)
    st.success("Operation has been completed.")





