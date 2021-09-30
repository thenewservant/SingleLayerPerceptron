import requests
from time import sleep
import  os,sys
import resizer



def main():

    urlHumans = "https://thispersondoesnotexist.com/image"
    urlCats = "https://thiscatdoesnotexist.com"

    base="HUMAINS/NORMAL/"
    startpoint=0

    n=10 #quantite de nouvelles images a telecharger, 10 par defaut
    if len(sys.argv)>1:
        n=int(sys.argv[1])

    startpoint=max([int(i[:-4]) for i in os.listdir(base)])+1

    print([int(i[:-4]) for i in os.listdir(base)])

    for loop in range(startpoint, startpoint+n):
        sleep(1)
        response = requests.get(urlHumans)
        if response.status_code == 200:
            with open(base+str(loop)+".jpg", 'wb') as f:
                f.write(response.content)


    base="CHATS/NORMAL/"

    startpoint=max([int(i[:-4]) for i in os.listdir(base)])+1
        
    print([int(i[:-4]) for i in os.listdir(base)])

    for loop in range(startpoint, startpoint+n):
        sleep(0.75)
        response = requests.get(urlCats)


        if response.status_code == 200:
            with open(base+str(loop)+".jpg", 'wb') as f:
                f.write(response.content)

if __name__=="__main__":
    main()

resizer.main()