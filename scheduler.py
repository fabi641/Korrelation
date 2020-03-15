import schedule
import time
import tweet
import korrelation

i = 0
Zeit = "15:00"

#tweetet einen korrelations tweet und schreibt ihn auch nochmal in die shell
def korrelieren():
    #holt sich ein objekt mit der URL und dem namen der Korrelation
    Korrelation = korrelation.parsen()
    print("Tweet this:\n")
    print("-------------------------------------")
    tweet.tweet(Korrelation.url, Korrelation.title, Korrelation.website)
    print(Korrelation.url)
    print("-------------------------------------")


#Jeden Tag um 15:00 Uhr wird 'korrelieren' ausgeführt
schedule.every().day.at(Zeit).do(korrelieren)

#Hat das Twitter-API-Gedöns geklappt?
print("Twitter Api Kram:")
print(tweet.api.VerifyCredentials())
print("---------------------------------------------\n")

#Am Anfang was ausgeben
print("Jeden Tag um "+ Zeit +" Uhr gibt's Korrelationen!")
print("Starting Korrelation...")
print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))


#Dauerschleife
while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
    #Immer mal schreiben, dass das skript noch lebt
    i += 1
    if i == 10:
	#um die Connection zur twitter API aufrecht zu erhalten
        try:
            tweet.api.VerifyCredentials()
            print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))
            i = 0
        except:
            print("Beim Aufrechterhalten der Verbindung ist ein Fehler aufgetreten.\n In einer Minute wird es nochmal probiert")
