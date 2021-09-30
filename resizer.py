from PIL import Image 
import os
def main():
    for i in os.listdir("CHATS/NORMAL"):
        image=Image.open("CHATS/NORMAL/"+i)
        new=image.resize((150,150)).convert("L") # --> en nuances de gris
        new.save("CHATS/GRAYSCALE/"+i[:-4]+"RGS.jpg")
    for i in os.listdir("HUMAINS/NORMAL"):
        image=Image.open("HUMAINS/NORMAL/"+i)
        new=image.resize((150,150)).convert("L") # --> en nuances de gris
        new.save("HUMAINS/GRAYSCALE/"+i[:-4]+"RGS.jpg")

if __name__=="__main__":
    main()