from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup
# url = r"https://aarsrecovery.org/contact"
# pattern = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
# session = HTMLSession()
# response = session.get(url)
# response.html.render(timeout=30)
# body = response.html.find("body")[0]
# emails = re.findall(
#     r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", body.text)
# for index, email in enumerate(emails):
#     print(email)
# print("nkk"[-1:])
website = "https://experiencethereprieve.com/contact/"
website1 = "https://experiencethereprieve.com/contact/"
if website[-1:] == "/":
    website2 = website+"contact"
    website3 = website+"about"
    website4 = website+"contact-us"
    website5 = website+"about-us"
    website6 = website+"contactus"
    website7 = website+"aboutus"
else:
    website2 = website+"/contact"
    website3 = website+"/about"
    website4 = website+"/contact-us"
    website5 = website+"/about-us"
    website6 = website+"/contactus"
    website7 = website+"/aboutus"
ee = []
for i in [website, website1, website2, website3, website4, website5, website6, website7]:
    try:
        url = i
        pattern = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        session = HTMLSession()
        response = session.get(url)
        response.html.render(timeout=15)
        body = response.html.find("body")[0]
        emails = re.findall(
            r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", body.text)
        for e in emails:
            if e not in ee:
                ee.append(e)
    except:
        pass
email = ""
if len(ee) > 0:
    for i in ee:
        email += i+", "
print(email)
