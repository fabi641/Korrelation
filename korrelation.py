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
    website = ""

#gibt die aktuell maximale id zurueck
#dise steht auf jeder Korrelationsseite
#daher immer auf der mit ID=1 nachschauen
def max_id():

    url = "https://tylervigen.com/view_correlation?id=1"
    ReOb = re.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"})

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
    #max_id is no longer looked up from the page, because the website changed in a way, that this inforamtion is no longer available. 92688 is the last correlation, in which the picture is not broken.
    max_cor_id = 92688  #max_id()

    #Zahl fue dir id generieren. Diese ist der unique identifier 
    #fuer eine Korrelation. Aktuell sind es 86816 erzeugte Korrelationsgrafiken.
    cor_id = str(random.randint(1, max_cor_id))

    #/debug
    #print(cor_id)

    #GET Request fuer die erzeugte korrelation
    #ReOb ist jetzt die HTML Antwort
    url = "https://tylervigen.com/view_correlation?id="+cor_id
    ReOb = re.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"})
   
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
    Korri.website = url

    return Korri

Korrelation = parsen()

#/debug
#print(Korrelation.url)
#print(Korrelation.title)
