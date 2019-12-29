#!/usr/bin/env python3
from bs4 import BeautifulSoup
# mutool merge 1.pdf >> ./1_mutool.txt
file='/tmp/1_mutool.txt'
f=open(file)
soup=BeautifulSoup(f,'html.parser')
# start index 11

# easy to parse company  index 18 
l1=soup.find_all('span',{'font':'DFNTPM+direkt'})[18].find_all('g')
l2=soup.find_all('span',{'font':'DFNTPM+direkt'})[19].find_all('g')
l3=soup.find_all('span',{'font':'DFNTPM+direkt'})[20].find_all('g')
l4_0=soup.find_all('span',{'font':'DFNTPM+direkt'})[21].find_all('g')
l4_1=soup.find_all('span',{'font':'DFNTPM+direkt'})[22].find_all('g')
l4_2=soup.find_all('span',{'font':'DFNTPM+direkt'})[23].find_all('g')
l5=soup.find_all('span',{'font':'DFNTPM+direkt'})[24].find_all('g')

company_name=''
for i in l1:
    company_name+=i['unicode']
# main_product symbol '^'
main_product=''
for i in l2[1:]:
    main_product+=i['unicode']
# person_engaged symbol ';'
person_engaged=''
for i in l3[1:]:
    person_engaged+=i['unicode']

# aoe symbol '`'
# adress of establishment
aoe=''
for i in l4_0[1:]:
    aoe+=i['unicode']
aoe+='\n'
for i in l4_1[0:]:
    aoe+=i['unicode']
aoe+='\n'
for i in l4_2[0:]:
    aoe+=i['unicode']

# telefon symbol '%'
telephon=''
for i in l5[1:]:
    telephon+=i['unicode']
print('{0},\n{1}\n{2}\n{3}'.format(company_name,main_product,aoe,telephon))
