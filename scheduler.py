import time
import tweet
import korrelation

Zeit = "15:00"

#tweetet einen korrelations tweet und schreibt ihn auch nochmal in die shell
def korrelieren():
    #holt sich ein objekt mit der URL und dem namen der Korrelation
    Korrelation = korrelation.parsen()
    print("Tweet this:\n")
    print("-------------------------------------")
    tweet.tweet(Korrelation.url, Korrelation.title, Korrelation.website)
    print(Korrelation.url + "\n" + Korrelation.title)
    print("-------------------------------------")

#Hat das Twitter-API-Gedöns geklappt?
print("Twitter Api Kram:")
print(tweet.api.VerifyCredentials())
print("---------------------------------------------\n")

#Am Anfang was ausgeben
print("Jeden Tag um "+ Zeit +" Uhr gibt's Korrelationen!")
print("Starting Korrelation...")
print("Es ist: "+ time.strftime("%d.%m.%Y %H:%M:%S"))


korrelieren()
