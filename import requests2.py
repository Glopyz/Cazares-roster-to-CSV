import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

r = requests.get ('https://www.myeform4.net/cazares/Admin/Reports/ReportCrRoster.aspx?ClassRoomID=3960')

soup= BeautifulSoup(r.text,'html.parser')

i=1
StudentsNameArr = []
StudentsAdressArr= []
StudentsEmailArr = []
StudentsCellphoneArr = []
StudentsDOBArr = []

while i !=4:
    i+=1
    StudentsName = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str (i) + '_lblName'}).text
    StudentsAdress = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str (i) + '_lbladdress'}).text
    StudentsEmail = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblEmail'}).text
    StudentsCellphone = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblCP'}).text
    StudentsDOB = soup.find('span',attrs={'id':'ctl00_ContentPlaceHolder1_gvRoster_ctl0' + str(i) + '_lblDOB'}).text

    StudentsNameArr.append(StudentsName)
    StudentsAdressArr.append(StudentsAdress)
    StudentsEmailArr.append(StudentsEmail)
    StudentsCellphoneArr.append(StudentsCellphone)
    StudentsDOBArr.append(StudentsDOB)


    
    
print(StudentsNameArr,"\n",StudentsAdressArr,"\n",StudentsEmailArr,"\n",StudentsCellphoneArr,"\n",StudentsDOBArr)
 

#df = pd.DataFrame.from_dict(
        # { 
          #   'Name': [StudentsName],
          #   'DOB': [StudentsDOB],
           #  'Adress': [StudentsAdress],
           #  'Email' : [StudentsEmail],
            # 'Phone' : [StudentsCellphone]
        # }
    # )   
#print(df)
arrName = np.array ([StudentsNameArr,StudentsEmailArr,StudentsAdressArr,StudentsDOBArr,StudentsCellphoneArr])
#arrName= list(arrName)
#df = pd.DataFrame(arrName)

print(arrName)
np.savetxt("CazaresRoster.csv",arrName,fmt='%s', delimiter=",")

#df.to_csv('CazaresRoster.csv') 



# Loading a Sample Dataframe
#df = pd.DataFrame.from_dict(
   # {   'Name': ['Nik', 'Nik', 'Jane', 'Jane'],
   #     'Year': [2020, 2021, 2020, 2021],
   #     'Sales': [1000, 2300, 1900, 3400],
   # }
#)
print()

