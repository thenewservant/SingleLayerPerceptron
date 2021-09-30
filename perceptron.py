"""
Premier essai d'un Réseau de neurones type perceptron à une couche. On essaie de différencier les chats des humains.

Les images sont en noir et blanc, idéalement de taille 150x150.

Le set d'entrée est un tenseur de n Matrices converties en listes successives"""

import numpy, random, os,sys, getopt
from PIL import Image
import pickle

EPOCHS=25
SAMPLES=39

NEUR=150*150 #nombre de neurones

PATH_HUMANS="HUMAINS/GRAYSCALE/"
PATH_CATS="CHATS/GRAYSCALE/"

global weights

bias=1
lr=1 #learning rate

acces1="HUMAINS/TEST_HUMAN.jpg"
acces2="CHATS/TEST_CAT.jpg"
modelPreConcu="Models/Model25x39.bin" #Si on modèle a déjà été entraîné, mettre son lien ici (syntaxe: Model{nb_epoques}x{nb_samples}.bin)


d=dict()
argA,argB=getopt.getopt(sys.argv[1:], 'f', ['model=','img1=', 'img2='])

for i in argA:
    d[i[0]]=i[1]

if len(d.keys())>0: #GESTION DES OPTIONS D'ENTREE
    if '--model' in d.keys():
        EPOCHS, SAMPLES= [int(i) for i in d["--model"].split("x") ]
        if (not "Model{}x{}.bin".format(EPOCHS,SAMPLES) in os.listdir("Models/")) or '-f' in d.keys():
            modelPreConcu=''
    if ("--img1" in d.keys() ) and ("--img2" in d.keys()):
        acces1=d['--img1']
        acces2=d['--img2']
    elif ("--img1" in d.keys() ) or ("--img2" in d.keys()):
        print("two images must be specified!")
        sys.exit(2)


def flatten(lst): #Matrice --> liste , et chaque valeur est multipliee par 1/255 pour la normalisation
    var=[[] for x in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(len(lst[i][j])):
                var[i].append(lst[i][j][k]/255)
    return var

def Perceptron(inputs, output):
    global weights
    outputP=0

    for i in range(NEUR):
        outputP+=inputs[i]*weights[i]
       
    outputP+=bias*weights[NEUR]
 
    outputP=outputP>0 #fonction d'activation (de heaviside, ici)

    error=output-outputP

    for i in range(NEUR):
        weights[i]+=error*inputs[i]*lr
        
    weights[NEUR]+=error*bias*lr #poids de la sommation

#TRAINING si le modele n'existe pas ou n'est pas specifie.

if not modelPreConcu:
    TENSOR_HUMANS=flatten([list(numpy.array(Image.open(PATH_HUMANS+i))) for i in os.listdir(PATH_HUMANS)])
    TENSOR_CATS=flatten([list(numpy.array(Image.open(PATH_CATS+i))) for i in os.listdir(PATH_CATS)])

    
    weights=[random.random() for i in range(NEUR+1)]#+1 correspond au poids de la sortie

    for epochs in range(EPOCHS):
        print("EPOQUE "+str(epochs) +"...",end="")
        for i in range(SAMPLES):
            #HUMAINS
            #print("HUMAIN: "+str(inp))
            Perceptron(TENSOR_HUMANS[i],1)
            #CHATS
            #print("CHATS: "+str(inp))
            Perceptron(TENSOR_CATS[i],0)
            
            #print("poids: "+str(weights[0:100]))
        print("OK!")

    with open("Models/Model{}x{}.bin".format(str(EPOCHS),str(SAMPLES)), "wb") as output:
        pickle.dump(weights,output)
else:
    with open(modelPreConcu, 'rb') as input:  
        weights=pickle.load(input)


##TEST

IMG_1=flatten([list(numpy.array(Image.open(acces1)))])[0]
IMG_2=flatten([list(numpy.array(Image.open(acces2)))])[0]


#score du premier

output1=0
for i in range(NEUR):
        
       output1+=IMG_1[i]*weights[i]

output1+=bias*weights[NEUR]


#score du second

output2=0
for i in range(NEUR):
        output2+=IMG_2[i]*weights[i]

output2+=bias*weights[NEUR]

print("l'image 1 est vraisemblablement un ", end="")

if output1>output2: #en theorie, l'humain possede un score positif et le chat un score negatif

    print("humain, et l'image 2 un chat.")
else:
    print("chat, et l'image 2 un humain.")
   
print("score 1: "+ str(output1)+" \nscore 2:"+ str(output2))