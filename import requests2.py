import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

r = requests.get ('https://www.myeform4.net/cazares/Admin/Reports/ReportCrRoster.aspx?ClassRoomID=3920')
soup= BeautifulSoup(r.text,'html.parser')
student_count = soup.find_all('td', attrs={'class':'admin-content2'},align="left")
student_count = len(student_count)
student_count+=2
print(student_count)


i=2 # Setting this to 2 becuase it searches for number 2 on the HTML file
StudentsNameArr = []
StudentsAdressArr= []
StudentsEmailArr = []
StudentsCellphoneArr = []
StudentsDOBArr = []


while i != student_count and i<10 :  # Stripping the HTML file and making each array by appending to it

    StudentsName = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str (i) + '_lblName'}).text.replace("," , "  ")
    StudentsAdress = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str (i) + '_lbladdress'}).text
    StudentsEmail = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblEmail'}).text
    StudentsCellphone = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblCP'}).text
    StudentsDOB = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblDOB'}).text

    print(StudentsName,StudentsAdress,StudentsEmail,StudentsCellphone,StudentsDOB)

    StudentsNameArr.append(StudentsName)
    StudentsAdressArr.append(StudentsAdress)
    StudentsEmailArr.append(StudentsEmail)
    StudentsCellphoneArr.append(StudentsCellphone)
    StudentsDOBArr.append(StudentsDOB)

    i+=1
    print(i)

while student_count>= 10 and i!= student_count:
    StudentsName = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl' + str (i) + '_lblName'}).text.replace("," , "  ")
    StudentsAdress = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl' + str (i) + '_lbladdress'}).text
    StudentsEmail = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl' + str(i) + '_lblEmail'}).text
    StudentsCellphone = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl' + str(i) + '_lblCP'}).text
    StudentsDOB = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl' + str(i) + '_lblDOB'}).text

    print(StudentsName,StudentsAdress,StudentsEmail,StudentsCellphone,StudentsDOB)

    StudentsNameArr.append(StudentsName)
    StudentsAdressArr.append(StudentsAdress)
    StudentsEmailArr.append(StudentsEmail)
    StudentsCellphoneArr.append(StudentsCellphone)
    StudentsDOBArr.append(StudentsDOB)
    i+=1
    print(i)


  
class_date = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_lblCRNumber'}).text + str(" Roster.csv")
 
arrName = np.array ([StudentsNameArr,StudentsEmailArr,StudentsAdressArr,StudentsDOBArr,StudentsCellphoneArr]) # Making the Numpy Array structure
np.savetxt(class_date,arrName,fmt='%s', delimiter=",") # Saving the Array to the CSV file with some modifications
