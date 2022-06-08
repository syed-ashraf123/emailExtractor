import pandas as pd
from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import validators
df = pd.read_csv("xxx.csv")
for c, web in enumerate(tqdm(df["website"])):
    if validators.url(web):
        email = ""
        if web[-1:] == "/":
            website2 = web+"contact"
            website3 = web+"about"
            website4 = web+"contact-us"
            website5 = web+"about-us"
            website6 = web+"contactus"
            website7 = web+"aboutus"
        else:
            website2 = web+"/contact"
            website3 = web+"/about"
            website4 = web+"/contact-us"
            website5 = web+"/about-us"
            website6 = web+"/contactus"
            website7 = web+"/aboutus"
        ee = []
        for i in [web, website2, website3, website4, website5, website6, website7]:
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
                response.close()
                session.close()
            except:
                pass
        email = ""
        if len(ee) > 0:
            for i in ee:
                email += i+", "
        df.at[c, "email"] = email
df.to_csv("xxxEmail.csv", index=False)
