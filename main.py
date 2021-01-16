from scrape import *
from FileIOAndMail import *

options_list = ['react', 'python', 'android', 'compiler', 'javascript', 'postgresql', 'django', 'dart', 'flutter', 'java', 'coq', 'ocaml', 'rust', 'c/c++', 'c++', 'vulkan', 'opengl', 'python 3', 'golang']

# print options
print("OPTIONS:")
i = 0
while i < len(options_list):
    print(', '.join(options_list[i:i + int((len(options_list) / 5))]))
    i = i + int((len(options_list) / 5))

mail_id = input("Enter your e-mail(gmail) id here: ")
password = input("Enter your password: ")
tech_need = input("Enter what you want from the above stack: ")
tech_need_list = []

# take all technologies user wants
while tech_need.lower() != 'exit':
    tech_need_list.append(tech_need.lower())
    tech_need = input("Enter what you want from the above stack: ")

# call to scrape function which return rows with required data
site_data = scrape(tech_need_list)

# if we get no matching data don't do anything else write to file and send mail
if len(site_data) != 0:
    writeFile(site_data)
    sendMail(mail_id, password)
    print("DONE!! :)")
else:
    print('NO matching data found for you :(')

