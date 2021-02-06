#totally offline libraary
#can change to male as well as female voice
# link - 
# https://pypi.org/project/pyttsx3/

#for speech to text
import pyttsx3
# text simmilarity
import spacy
import speech_recognition as sr
from small_files.preprocessing_of_file import doPreprocessing,doPreprocessingOfText
from small_files.visualization import visualize,visualize2



engine = pyttsx3.init()

#python -m spacy download en_core_web_lg
nlp = spacy.load("en_core_web_md")
question = "Which are the features of the object oriented language ?"


#preprocessing of the predefined answer.txt
# sending answer.text file for preprocesseing 
individual_items_list = doPreprocessing('answer.txt')


#again adding the processed predefined answer to answer.txt
with open('answer.txt', 'w') as f:
    for item in individual_items_list:
        f.write("%s\n" % item)

#reading predefined answer       
pred_ans = open("answer.txt","r")
answer = pred_ans.read()



#in future we will wait here for 30 seconds

#one popup will be there to show 1) repeate or 2) Ready

#to speak a question 
r = sr.Recognizer()
engine.say(question)
engine.runAndWait()
engine.stop()

lst1 = []
lst2 = []

with sr.Microphone() as source:
    print("Hey, Give me your Answer, i am Listening.....")
    audio = r.listen(source,timeout=3)

    try:
        givenAns = r.recognize_google(audio)

        preProcessedAnsList = doPreprocessingOfText(givenAns)

        #storing answer to givenAnswer txt file
        ans_file = open("givenAnswer.txt","w")
        for item in preProcessedAnsList:
            ans_file.write("%s\n" % item)

        givenAns2 = ""

        for s in preProcessedAnsList:
            givenAns2 = givenAns2 + " " + s

        

        ex1 = nlp(givenAns2)
        ex2 = nlp(answer)

        # inserting words which are commen as per given condition 
        for token1 in ex1:
            for token2 in ex2:
                if(token1.similarity(token2) == 1.0):
                    {
                        lst1.append(token1.text)
                        

                    }
                elif(token1.similarity(token2) >= 0.80):
                    {
                        lst2.append(token1.text)
                        
                    }

        print(len(lst1))
        print(len(lst2))

        # simmilarData = [(token1.text,token2.text,token1.similarity(token2)) for token1 in ex1 for token2 in ex2]

        
    except:
        #or i can simply speak the message
        
        print("Sorry could not listen your voice.")


if(len(lst1) == 0):
    print("Say Something please.......")

    

if(len(lst2) == 0):
    {
    visualize(lst1)
    }

else:
    {
    visualize2(lst1,lst2)
    }

















