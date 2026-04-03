pip install numpy google-generativeai
from google import genai
import os
import re
#import torch
import numpy as np
# Replace with your Gemini API key from Google AI Studio
client = genai.Client(api_key="YOUR_API_KEY_HERE")

file = client.files.upload(file=input("enter the pdf path of the specific topic you want to discuss about"))
def clean_output(text):
  clean_text = re.sub(r'\*+', '', text)
  clean_text = re.sub(r' {2,}', ' ', clean_text)
  return clean_text


def student_dashboard():

  s=int(input("enter total no of student"))
  names = []
  engagements = []
  marks_list = []
  attendances = []
  seriousness_list = []

  for i in range(s):
    name = input(f"enter student's name for student {i+1}:-")
    engagement = input(f"enter {name}'s engagement:-")
    marks = input(f"enter {name}'s marks in percentage:-")
    attendance = int(input(f"enter attendance % of {name}:-"))
    seriousness = input(f"how much serious is {name}:-")

    names.append(name)
    engagements.append(engagement)
    marks_list.append(marks)
    attendances.append(attendance)
    seriousness_list.append(seriousness)

  for i in range(s):
    response = client.models.generate_content(
      model="models/gemini-2.0-flash",
      contents=[
          f"arrange {names[i]},{engagements[i]},{marks_list[i]},{attendances[i]},{seriousness_list[i]} in a table format and make one improvement/warning colums for each student and display output in table format",
          ]
    )
    data=clean_output(response.text)
    print(data)

def AI_grading_assistance():
  image=input("enter image of question answer ")
  ask=input("ask anything")
  response = client.models.generate_content(
    model="models/gemini-2.0-flash",
    contents=[
        f"please check the ansers of each question and try to grade them accordingly by putting marks onto them",
        image  # pass the uploaded file object
      ]
    )
  answers=clean_output(response.text)
  print(answers)
def AI_library():
   response = client.models.generate_content(
     model="models/gemini-2.0-flash",
     contents=[
        f"please refer some learning resourses, recommend books or youtube resources according to the topic of this pdf file",
        file  # pass the uploaded file object
      ]
    )
   resources=clean_output(response.text)
   print(resources)
def Smart_Session_Planar():
   response = client.models.generate_content(
     model="models/gemini-2.0-flash",
     contents=[
        f"suggest important slides/pages from this pdf and generate class notes along too",
        file  # pass the uploaded file object
      ]
    )
   resources=clean_output(response.text)
   print(resources)
def Teacher_chatbot():
   response = client.models.generate_content(
     model="models/gemini-2.0-flash",
     contents=[
        f"generate some quizes to test students from this topic and after asking all questions give remarks for them by providing specified notes from this areas of asking ",
        file  # pass the uploaded file object
      ]
    )
   resources=clean_output(response.text)
   print(resources)
def AI_Magic():
  response = client.models.generate_content(
     model="models/gemini-2.0-flash",
     contents=[
        f"converts lessons and quizes into games",
        file  # pass the uploaded file object
      ]
    )
  game=clean_output(response.text)
  print(game)
def Parent_connect():
  response = client.models.generate_content(
     model="models/gemini-2.0-flash",
     contents=[
        f"check the {student_dashboard()} data and decide and schedule whose parents are needed to be called and what kind of guidance should be given to them"
     ]
  )
  request=clean_output(response.text)
  print(request)
while(True):
 n=int(input("right now what do you want\n1.Student DashBoard\n2.AI Grading assistance\n3.Smart Sessio Planar\n4.AI Library\n5.Teacher chatbot\n6.Parent connect\n7.AI Magic\n press any key to leave\n"))
 if n==1:
   student_dashboard()
 elif n==2:
   AI_grading_assistance()
 elif n==3:
   Smart_Session_Planar()
 elif n==4:
   AI_library()
 elif n==5:
   Teacher_chatbot()
 elif n==6:
   Parent_connect()
 elif n==7:
   AI_Magic()
 else:
   break

