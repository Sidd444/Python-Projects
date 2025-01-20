#CONTENT EXTRACTION

# import urllib.request as url_request
# import urllib.parse as url_parse
# import urllib.error as url_error
import requests as req
#from bs4 import BeautifulSoup
#import csv
import re

# url=url_request.urlopen('file:///C:/Users/blazo/Documents/projects/MERN%20practice/temp/index.html')

# for line in url:
#     print(line.decode().strip())


# IMAGE EXTRACTION

# url='https://img.freepik.com/premium-photo/fire-flames-isolated-black-background_246836-2250.jpg'

# res=req.get(url=url)
# pic=res.content
# o=open('fire-flames-isolated-black-background_246836-2250.jpg','wb')
# o.write(pic)


# POSTING DATA

# url='http://127.0.0.1:8000/post/'

# payload={
#     'title':'web posting',
#     'content':'server content'
# }

# response = req.post(url=url,data=payload)
# print(response.text)

# RETRIEVING DATA USING OFFSET

# url='http://127.0.0.1:8000/post/'

# param={
#     'offset':'3'
# }

# response=req.get(url=url,params=param)

# print(response.text)


# RETRIEVING DATA FROM A WEB PAGE AND FILTERING

# def Extract(url):
#     response=req.get(url=url).content
#     soup=BeautifulSoup(response,'lxml')
#     tag=soup.find('div',{'id':'mp-upper'})
#     div=tag.find_all('div')
#     content=[span.text for span in div]
#     #print(content)

#     with open('wiki.csv','w') as csv_file:
#         csv_write=csv.writer(csv_file)
#         csv_write.writerow(content)

# Extract(url='https://en.wikipedia.org/wiki/Main_Page')


# RETRIEVING IMAGES

item=input('Enter the content you want to search:')
url='https://www.google.com/search?q={item}&sca_esv=e2ae8c4310a8b420&rlz=1C1CHBF_enIN1139IN1140&udm=2&biw=1366&bih=633&sxsrf=ADLYWIJjx-ln71fHHrQ_1YM5Y3QlBY32nA%3A1737303706179&ei=miaNZ6PNCp-Z4-EPvZmR4A0&ved=0ahUKEwijgpjSmIKLAxWfzDgGHb1MBNwQ4dUDCBE&uact=5&oq=moon&gs_lp=EgNpbWciBG1vb24yDRAAGIAEGLEDGEMYigUyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5I2ghQAFjHBXABeACQAQGYAcECoAGiBqoBBTItMi4xuAEDyAEA-AEBmAIDoAKABMICBBAjGCfCAgoQABiABBhDGIoFwgIOEAAYgAQYsQMYgwEYigXCAgsQABiABBixAxiDAZgDAIgGAZIHBTEuMC4yoAfyEQ&sclient=img'
user_agent={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
pattern="\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"

response=req.get(url=url,headers=user_agent).text
# images=re.findall(pattern,response)
# for image in images:
#     print(list(image)[0])

print(response)

