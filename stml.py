import streamlit as st
import pandas as pd
import numpy as np
import time
# Title of the webside
st.set_page_config(page_title=" My Website")

# Adding logo to sidebar
st.sidebar.image("log.png",use_column_width=True)

# Adding a sidebar with useful links
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to",["HOME","ABOUT","PROJECTS","WORK","VIDEO","CONTACT","MAP"])

# Home page
if page == "HOME":
    # Displaying an image
    st.title(("Welcome ot Code Dhirendra's Portfolio!"))
    st.image("2.png")
    st.write('### Welcome to Code Dhirendrea Steamlit Web App')
    #Text
    st.write("This is the home page of my Streamlit-powered website.Streamlit allows you to create highly interective web applications with Python.")

    # Displaying a header
    st.header("Introduction:")
    st.write("Hello,I am Dhirendra, a Python programmer with a passion for solving real-world problems through code. I am activley seeking opportunities in th IT files.where I can contribute my skills in Python programming, data analysis,and automation.")
    st.header("Skills:")
    st.markdown(""" 
    1. Proficient in Python programming
    2. Experienced in building voice assistants ,Bank management app, web scrappig tools,and automation scripts   
    3. Familiar with data analysis ,machine learning, and web application development and mysql 
    4. Knowledge of API developmet and web technologies """)
    st.header("Objectives:")
    st.write("I am currently seeking a challenging position in IT as a Python porgrammer, where I can contrinue ot grow my epertise, work on excitting projects, and contribute to innovative solutions.")
    st.header("Projects:")
    st.markdown("""
    1. Bank Management System
    2. File Management System
    3. Voice Assistants/ Speech Recognition """)

# About page
elif page == "ABOUT":
   st.title("Welcome to About Page")
   st.image("dhi.JPG",caption="Dhirendra",width=300)
   st.header("About Us:")
   st.write('''###### I am Dhirendra, and I hold a Master of Computer Applicatios(MCA) degree and Becholor of Education(B.Ed).I bring diverse experience form various roles, including working as a secretary at BBNL,teaching ,and serving as an operations officer in the cargo department.These roles have strengthened my skills in organization,problem-solving and communication,all of which are critical in the IT sector.''')
   st.write("###### I have a strong interest in software development and have gained proficiency in Python throuh self-study and academic projects.Although I don't have formal work experience in IT,I have worked on several Python projects,such as[ Bank Management System ],which demonstrate my codeing ability,understanding of algorithms,and software developmlent principle.")
   st.write("###### I am now seeking to transition into a Python Programming role,where I can apply my techniclal skills,leverage my diverse background,and coutinue growing professionally.")
   st.markdown("#### Check out my:[RESUME|CV](https://drive.google.com/file/d/1DcU5G6YWVJ_zWRgpRzuk9ahTVQRsQvna/view?usp=sharing)")

# Work page
elif page == "WORK":
    st.title("Welcome to Work Page")
    st.header("Work on Streamlit key fuuction ")
    st.write("###### On this page, I demostrate various Streamlit funtons I've implemanted in my projects. Streamlit is a powerful tool for crating interactive web application, and here are some of the key functions I've worked with:")
    # Adding title and header


    # Adding a radio button
    st.title("1.st.buttone()Purpse:")
    st.write("A simple yet powerful funtion that allows users to trigger an action when clicked.")
    st.header("Implementation:")
    st.write('''I used st.button ("Submit") on my contact form page to sumbit/send user information.It's also userful for triggering any event or function, such as running a script when the button is clicked.''' )
    st.write("#### Radio Button Example ")
    genre = st.radio("Choose your facorite programming language:",('Python','JavaScript','C++','Java'))
    st.write(f"You selected:{genre}")

    # Adding a button
    st.write('#### Button Example')
    if st.button('Click Me'):
      st.write('Button clicked!!')

    # Adding a checkbox
    st.write("### Checkbox Exapmple")
    if st.checkbox('Show/Hide Greeting'):
       st.write("Hello,Streamlit ")

    st.title("2. st.line_chart(),st.bar_chart(),and st.pyplot()Purpose:")
    st.write("These function allow for real-time data visualization. Streamlit provides simple charting functions like st.line_chart() and st.bar_chart() anf also allows for intefration of Matplotlib visualization with st.pyplot().")
    st.header("Implementation:")
    st.write("In our machine learning project, We used st.line_chart() to display the training and validation accuray of the model ober time, helping users visualize the model's perfomance.")    

    # Creating a simple line chart
    st.write("### Line Chart Example")
    data = pd.DataFrame(np.random.randn(10,3),columns=['A','B','C'])
    st.line_chart(data)  

    # Adding a selectbox
    st.write("### Selectbox Example")
    option = st.selectbox('Which is your favorite numbers?',[1,2,3,4,5,6,7,8,9])
    st.write("You selected:",option)

    # Addig a slider
    st.write("### Slider Example")
    slider_value = st.slider('Choose a value between 0 and 100:',0,100,25)
    st.write('Slider value:',slider_value)
    
    st.title("3. st.text_input() and st.text_area()Purpose:")
    st.write("These input function are essential for collecting text-based inputs form users, which I've utilized for creating interactive forms.")
    st.header("Implementation:")
    st.write("In one our web apps, We can used st.text_input('Enter your name:') to collect user names and st.text_area('Your feedback:') to allow users to provide feedback,which enhances the user interactivity of our apps.")
    # Adding a text input
    st.write('### Text Input Example')
    name = st.text_input("Enter Your name:")
    feedback =st.text_area("Your Feedback:")
    st.write(f"Hello,{name} your feedback {feedback}!!")


    st.title("4.st.dataframe () and st.table() Purpose:")
    st.write("These function are used to display data in a structured table or grid format,which is particularly useful for data analysis apps.")
    st.header("Implementation:")
    st.write("In data science project, We used st.dataframe() to dispplay large datasets in a scrollable and sortable format,making it easy for users to explore data.")
    st.write("### DataFrame Example")
    st.dataframe(data)

    # Adding a dataframe
    # Adding a radio button with condition content
    st.write('### Conditional Display with Radio Button')
    status =st.radio("What's your status?",('Active','Inactive'))
    if status == 'Active':
       st.success("You are active!!")
    else:
       st.warning("You are inactive.") 

   # Displaying progress bar
    st.write('### Progress Bar Example')
    progress_bar = st.progress(0)
    for i in range(100):
       time.sleep(0.01)
       progress_bar.progress(i+1)
    st.write("Task Completed!!") 

    
    st.title("5. st.file_uploader() Purpose:")
    st.write("This function allows users to upload files into the app, which can then be processed or analyzed.")
    st.header("Implementaion:")
    st.write("In one of my data analysis projects,I used st.file_uploaded('Upload Your CSV file') to allow users to upload their datasets for furher processing and visualization directly within the app.")
   # Adding a file uploader
    st.write('### File Uploader Example')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
       st.write("File uploaded successfully!!")    


# Projects page
elif page == "PROJECTS":
       
   st.title("Welcome to Our Projects Page")
   st.write("##### Here you will find an overview of the work we have done,showcsing our skills,creativity and dedication.")
   st.sidebar.subheader("Select a Project")
   project = st.sidebar.selectbox("##### Select a Projects From Here", [ "Please Select","Project 1:Bank Management System","Project 2:File Management System","Project 3: Voice Assistant"])
   
   if project == "Project 1:Bank Management System":
       st.write("### Bank Management System")
       st.image("bank.png")
       st.write("### Decriptions:")
       st.write('''##### This is a "Bank Management System " build in Python. It allows users to manage bank accounts through a simple menu- driven interface. Users can create new accounts with automatically generated account number that include a prefix and sufix, deposit and withdraw funds, and view account details. The system sensures that all transactions are valid and provides an easy way to interact with banking operations programmatically.''')
       st.write("### Technologies Used:")
       st.write("##### Python")
       # Add links of github project
       st.markdown("#### Check out my:[DGitHub Link | Live Demo](https://github.com/Dhirendra-Projects/bankmgtsystem)")
   
   elif project == "Project 2:File Management System":
       st.write("### Welcome to File Management System")
       st.image("fmgt.png")
       st.write("### Decriptions:")
       st.write('''##### This Python-based "File Management System" provides core file operations such as creating,viewing,deleting ,reading and editing files through a simple console interface.It efficiently handles files in the current directory,allowing users to manage their files interactively. The program continuously prompts for input,ensuring an intuitive user experience,and exits gracefully when needed.''')
       st.write("### Technologies Used:")
       st.write("##### Python")
       # Addd links of github project
       st.markdown("#### Check out my: [GitHub Link | Live Demo](https://github.com/Dhirendra-Projects/filemgtapp)")
   elif project == "Project 3: Voice Assistant":
      st.write("### Welcome to Voice Assistant")
      st.image("va.png")
      st.write("### Decriptions:")
      st.write("##### Build a basic voice assistant that listens to user commands,searching for information on Wikipedia, and opens Google search results if necessary. This project demonstrates my abillity to work with speech recognition and web scraping.")
      st.write("### Technologies Used:")
      st.markdown("""        
       ##### 1. Python
       ##### 2. SpeechRecognition
       ##### 3. Wikipedia API 
       ##### 4. Webbrowser       """)
      # Add links of github projects
      st.markdown("#### Check out my: [GitHub Link | Live Demo](https://github.com/Dhirendra-Projects/voiceassist)")

      

  
# Contact Page        
elif page == "CONTACT":
   st.title("Contact Us") 
   st.write(" Feel free to reach out via the from below.")  

   # Adding a data input
   st.write('### Data Input Example ')
   import datetime
   date = st.date_input("Pick a date:",datetime.date.today())
   st.write("You selected:",date)  

   # Adding input form clients
   name = st.text_input("Please write your Name: ")
   email = st.text_input("Please enter the your email:")

   # Addoing a text area
   #st.write('### Text Area Example')
   message = st.text_area("Enter your message:")
   #st.write(f" Your message:",message)
   if st.button("Send"):
      st.write(f"Thank you ,{name}. We have received your message.")

# Adding Map
elif page == "MAP":
    # Adding a map
   st.write('### World Map Example')
   map_data = pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])
   st.map(map_data)

# video page
elif page == "VIDEO":
   
  # Adding a video
   st.write('### MY YouTube Video Example')
   st.video("https://www.youtube.com/watch?v=VKrmUDk-kPc") 
   st.video("https://www.youtube.com/watch?v=f6BcO-LM8rY")

  


   
   


