import requests
re = requests
import random
from bs4 import BeautifulSoup

#Objekt, welches von parsen() zurueckgegeben wird und alle Infos
#ueber die random korrelation enthaelt, die fuer den tweet
#benoetigt werden
class KorrOb:
    url = ""
    title = ""

#gibt die aktuell maximale id zurueck
#dise steht auf jeder Korrelationsseite
#daher immer auf der mit ID=1 nachschauen
def max_id():

    url = "https://tylervigen.com/view_correlation?id=1"
    ReOb = re.get(url)

    #Ueberpruefen, ob Status Code 200
    if(ReOb.status_code != 200):
        print("Irgendetwas hat nicht geklappt. HTML-Status-Code: "+str(ReOb.status_code))
        return 0

    #Wenn GET Request erfolgreich html Seite mit BeautifulSoup bearbeiten    
    soup = BeautifulSoup(ReOb.content, 'html.parser')
    #Den String, in dem die Anzahl der Korrelationen steht bekomen
    MAX_ID = soup.find(href="http://tylervigen.com/").string
    #String splitten, sodass nur die Zahl uebrig bleibt
    MAX_ID = MAX_ID.split(" ")[0]
    #Wenn nich nur aus Zahlen bestehend, wird wahrscheinlich ein komme drin sein
    #Also Komma entfernen
    if(MAX_ID.isdecimal() == 0):
        MAX_ID = MAX_ID.split(",")[0]+MAX_ID.split(",")[1]
    
    return int(MAX_ID)


def parsen():

    Korri = KorrOb

    #Anzahl an vorhandenen Korrelationen abfragen
    max_cor_id = max_id()

    #Zahl fue dir id generieren. Diese ist der unique identifier 
    #fuer eine Korrelation. Aktuell sind es 86816 erzeugte Korrelationsgrafiken.
    cor_id = str(random.randint(1, max_cor_id))

    #/debug
    #print(cor_id)

    #GET Request fuer die erzeugte korrelation
    #ReOb ist jetzt die HTML Antwort
    url = "https://tylervigen.com/view_correlation?id="+cor_id
    ReOb = re.get(url)
   
    #/debug
    #print(ReOb)

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
    Bildurl = Bild[1].get('src')

    #Objekt zum zurueckgeben erstellen
    Korri.title = KorrName
    Korri.url = "https://tylervigen.com/"+Bildurl

    return Korri

Korrelation = parsen()

#/debug
#print(Korrelation.url)
#print(Korrelation.title)