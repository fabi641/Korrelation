import requests
re = requests
import random
from lxml import html
from bs4 import BeautifulSoup

def parsen():
    #Zahl fue dir id generieren. Diese ist der unique identifier 
    #fuer eine Korrelation. Aktuell sind es 86816 erzeugte Korrelationsgrafiken.
    cor_id = str(random.randint(1, 86816))
    print(cor_id)

    #GET Request fuer die erzeugte korrelation
    #ReOb ist jetzt die HTML Antwort
    url = "https://tylervigen.com/view_correlation?id="+cor_id
    ReOb = re.get(url)
    print(ReOb)

    #Ueberpruefen, ob Status Code 200
    if(ReOb.status_code != 200):
        print("Irgendetwas hat nicht geklappt. HTML-Status-Code: "+str(ReOb.status_code))
        return 0

    #Wenn GET Request erfolgreich html Seite mit BeautifulSoup bearbeiten    
    soup = BeautifulSoup(ReOb.content, 'html.parser')

    #Name der Korrelation
    KorrName = soup.meta.get('content')

    #Bild-URL bekommen
    #Ist immer das zweite Bild auf der Seite
    Bild = soup.find_all('img')
    print(Bild[1].get('src'))

parsen()