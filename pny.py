import requests
from  bs4 import BeautifulSoup
import pandas as pd
url='https://www.pnytrainings.com/'
r=requests.get('https://www.pnytrainings.com/')
contentview= BeautifulSoup(r.content,'html5lib')
data=[]
courses = contentview.find_all('h1', class_='text-black font-bold dark:text-white')


# Loop through each course and extract details
for course in courses:
    course_info = {}
    
    # Extracting short courses in lahore
    course_name = course.find('a', class_='hover:text-blue-500') 
    course_info['Course Name'] = course_name.text.strip() if course_name else 'N/A'

   

    # Extract duration (fee structure)
    fee_structure=course.find('a',class_='py-5 px-1 hover:underline')
if 'lahore' in fee_structure:
    duration = course.find('a', class_='block py-2 px-4 text-sm hover:bg-gray-700') 
    course_info['Duration'] = duration.text.strip() if duration else 'N/A'

    data.append(course_info)

# Creating DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('pny_trainings_courses.csv', index=False)
print("Data written to pny_trainings_courses.csv")


