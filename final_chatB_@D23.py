import subprocess
import wolframalpha
import pyttsx3
import tkinter
import speech_recognition as sr
import datetime
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
from tkinter import*
from tkinter import simpledialog
parent=Tk()
parent.geometry("1400x700")
parent.title("Admission_cell")
parent.configure(background="pink")
font1=('Times',30,'normal')
el = Label(parent,text= 'Admission Cell DYPCET',fg='blue',font=font1).place(x=480,y=0)

#photo =PhotoImage(file="newlogo.png")
#lp = Label(image=photo).grid()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

global name
global font00
font00=('Times',15,'normal')
uname=Label(parent,text="Enter Name",font=font00).place(x=10,y=60)
name = Entry(parent,width=15,font=font00)
name.place(x=120,y=60)


def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir...!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir...!")

    else:
        speak("Good Evening ...!")

    speak("I am your D Y P C E T Assistant")
    speak("Enter your name")

global font2
font2=("Times",20,'bold')

global font3
font3=("Times",7,'normal')

global font4
font4=("Times",6,'underline')

global query
def query():
    choice = choices.get()
    ls = Label(parent,text="Answer To Query : ",fg='dark green',font=font4).place(x=120,y=400)
    if choice == '1':
        a1 = Label(parent,text="- D Y Patil College of Engineering and Technology Kolhapur. Is an autonomous\t\n engineering institute in Kolhapur, Established in 1984.\n\n\n\n\n",fg='green',font='font4').place(x=400,y=390)
        speak("D Y Patil College of Engineering and Technology Kolhapur. Is an autonomous engineering institute in Kolhapur, Established in 1984.")
        
    elif choice == '2':
        l8 = Label(parent,text='To become a leading institute in producing high quality technical professionals for   \nNation Building.\n\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak('To become a leading institute in producing high quality technical professionals for Nation Building.')
    
    elif choice == '3':
        l9 = Label(parent,text='- WIFI enable campus\n- Excellent placement record\n- 10000+ worldwide alumni record\n- All Govt. Scholarships available to student\n\t\t\t     - Bus facility available\t\t\t\n',fg='green',font='font4').place(x=400,y=390)
        speak("Following are the features of D Y Patil College of Engineering")
    
    elif choice == '4':
        l10= Label(parent,text='- Industry based curriculum under Autonomy\n- Highest placement record in the region\n- Mandatory Soft skills training for job enhancement\n\t- 42 Gold Medals  and 252 Ranks in Shivaji University Exam\n- Highly Qualified and experienced teaching faculty\n- State of Art Infrastructures & modern Laboratories',fg='green',font='font4').place(x=400,y=390)
        speak("Following are the reasons behind why you must choose D Y P C E T")
    
    elif choice == '5':
        l11= Label(parent,text='   1)Chemical Engineering\n2)Civil Engineering\n    3)Computer Science and Engineering\n\t\t\t   4)CSE(Data Science)\t\t\t\t\n\t5)CSE(Artificial Inteligence and Machine Learning)\n\t6)Electronics and Telecommunication Engineering\n7)Mechanical Engineering',fg='green',font='font4').place(x=400,y=390)
        speak("Following Under graduate Programs are offered by college")

    elif choice == '6':
        l12= Label(parent,text='- Industry visits\n- Live projects\n\t\t\t\t- Seminars\t\t\t\t\n- Internship\n- Development programmes\n- Research Based Projects.',fg='green',font='font4').place(x=400,y=390)
        speak("Following are extra carricular activities conducted by college")
            
    elif choice == '7':
        l13= Label(parent,text='\t\t\t- Assignments \t\t\t\t\n- Field study reports\n- Periodic tests\n-  Discussion forums\n-  Case analysis\n-  Group discussions\n',fg='green',font='font4').place(x=400,y=390)
        speak("College Usage Following assessment Methods")
            
    elif choice == '8':
        l7= Label(parent,text='- Software Developer\n- Data Analyst / Scientist\n- Project Manager\n- Automobile Sector\n- Communication  Engineer\n- ML Engineer\n\t\t\t\t- Govt. Jobs\t\t\t\t',fg='green',font='font4').place(x=400,y=390)
        speak("Career Opportunities at Our College")

    elif choice == '9':
        l7= Label(parent,text='- Capgemini, Cognizant, TCS, Infosys, Wipro, Adobe, HCL, JustDial, Accenture,\t\n IBM, TechMahindra.\n\n\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Following Companies visit for Campus Placement")

    elif choice == '10':
        l7= Label(parent,text='\t\t- Intake : 180\t\t\t\nThe department has the state of art laboratories, latest computer systems, \nopen source software, licensed software and modern digital teaching aids.\n      The teaching faculty is a blend of highly qualified, experienced, dynamic and\t\n young professionals.\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department of Computer Science and Engineering")

    elif choice == '11':
        l7= Label(parent,text='- Intake : 120\nMechanical engineering focuses on the  manufacturing, testing, design and improvement of\nmechanical system which are used in every industry. Most of the innovations which are very\nimportant to our future development will have their root in world of mechanical engineers.\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department Of Mechanical Engineering")

    elif choice == '12':
        l7= Label(parent,text='- Intake : 120 \nCivil engineering is the oldest branch of the engineering. The foundation of our \nsociety is build by civil engineers. Civil engineers design, build, monitor, operate and maintain\n infrastructure, transportation and public works project.\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department Of Civil Engineering")

    elif choice == '13':
        l7= Label(parent,text='- Intake : 60\n\t\tChemical engineering deals with application of physical science \t\t\nand mathematics to the process of converting raw material into more useful and valuable products.\n Chemical engineering serve as backbone for the entire spectrum of the process \t\nindustry.\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department of Chemical Engineering")

    elif choice == '14':
        l7= Label(parent,text='- Intake : 60\n\tElectronics & Telecommunication Engineering is rapidly advancing profession\t\t \nand it is driving force behind the development of worlds information technology. \nProvide career opportunities by producing new innovation and development in the\t\n field of telecommunication and robotics.',fg='green',font='font4').place(x=400,y=390)
        speak("Department of Electronics and telecommunication Engineering")

    elif choice == '15':
        l7= Label(parent,text='- Intake : 120\nDYPCET has new course data science from academic year 2020-2021. Data Science is\t \nhigh in demand that combines scientific methods math and statistics, specialized \nprogramming, advance analytics, AI, visualization to get insights buried in data.\t\t\t\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department of Data Science Engineering")

    elif choice == '16':
        l7= Label(parent,text='- Intake : 60\nDepartment of CSE has designed unique B.Tech program in AI &  ML giving sufficient\t\n emphasis on lifeskill development. \n\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("Department of Artificial Inteligence and Machine Learning Engineering")

    elif choice == '17':
        l7= Label(parent,text='\t\tadmission.dypcet@dypgroup.edu.in\t\t\t\t\n\n\n\n\n',fg='green',font='font4').place(x=400,y=390)
        speak("You can contact with us At following e mail")

    elif choice == '18':
        speak("Thank You Sir")
        parent.destroy()

    else:
        l7=  Label(parent,text='Enter correct option\t\t\t\t\t\t\t\n\n\n\n\n',fg='red',font='font4').place(x=400,y=390)
   
def entry():
    v = name.get()
    wel = Label(parent,text= f"Welcome {v}",font=font2).place(x=570,y=70)
    l2= Label(parent,text="Options\n\n\t1.About College\t\t\t2.Vission of DYPCET\t3.Features of College\t\t4.Why DYPCET Kolhapur?\t\n  5.UG programs\t\t\t  6.Activities Conducted ?\t 7.Assessment Methods\t\t 8.Career Opportunities\n9.Companies for Campus Placement\t10.CSE Department\t\t11.Mechanical Department\t\t12.Civil Department\n13.Chemical department\t\t14.E&TC Department\t15.Data Science Department \t\t16.AIML Department\n17.Contact e-mail\t\t 18.Exit",font="font3").place(x=150,y=150)     
    global choices
    speak("How can i help you")
    uchoice=Label(parent,text='Enter Choice',font=font00).place(x=600,y=310)
    choices = Entry(parent,width=5,font=font00)
    choices.place(x=730,y=310)
    

    choiceButton=Button(parent,text="Submit",command=query)
    choiceButton.place(x=680,y=350)

    speak("Choose following option")
   
       
nameButton=Button(parent,text="Submit",command=entry)
nameButton.place(x=100,y=100)

#choiceButton=Button(parent,text="SUBMIT",command=query)
#choiceButton.place(x=280,y=370)
   
wishMe()
parent.mainloop()