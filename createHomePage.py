from sentence import *
from findTemperatureLive import *
# part C
def createHomePage(emailuser):
    firstname, lastname = emailuser.split('.')
    firstname = firstname.lower()
    lastname = lastname.lower()
    f = open(emailuser +".html", "wt", encoding="utf-8")
    f.write('<!DOCTYPE html>\n<html lang="en">\n')
    f.write(f"<head>\n<title>{firstname} {lastname}</title>\n</head>\n")
    f.write(f'<body>\n<h1 style="color: black;"> Introducing Myself <h1>\n<ul>\n')
    f.write(f'<h2>Index</h2>\n<ul>\n')
    f.write(f'<li>email address</li>\n<li>Seongju.Yi@gordon.edu</li>')
    f.write(f'<li>picture</li>\n')
    f.write(f'<img src="seongju.yi.jpeg" alt="My name is Seongju Yi" width="100" height="100">\n')
    f.write(f'</body>\n</head>\n</html>')

# part D
def createHomePage2(emailuser):
    firstname, lastname = emailuser.split('.')
    firstname = firstname.lower()
    lastname = lastname.lower()
    random_sentence = sentence()
    wenham = findTemperatureLive()
    f = open(emailuser +".html", "wt", encoding="utf-8")
    f.write('<!DOCTYPE html>\n<html lang="en">\n')
    f.write(f"<head>\n<title>{firstname} {lastname}</title>\n</head>\n")
    f.write(f'<body>\n<h1 style="color: black;"> Introducing Myself <h1>\n<ul>\n')
    f.write(f'<h2>Index</h2>\n<ul>\n')
    f.write(f'<li>email address</li>\n<li>Seongju.Yi@gordon.edu</li>')
    f.write(f'<li>picture</li>\n')
    f.write(f'<img src="seongju.yi.jpeg" alt="My name is Seongju Yi" width="100" height="100">\n')
    f.write(f'<li>The Temperature </li>\n<li> {wenham} </li>\n</ul>')
    f.write(f'<li>The random sentence </li>\n<li>{random_sentence} </li>\n</ul>')
    f.write(f'</body>\n</head>\n</html>')

emailuser = input('What is your email address:')
createHomePage(emailuser)
createHomePage2(emailuser)
print("Home page created successfully!")
