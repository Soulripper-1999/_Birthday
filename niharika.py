import streamlit as st
from PIL import Image
image = Image.open('hogwarts.jpg')
st.sidebar.image(image)


st.title("Happy Birthday Niharika " + ":gift_heart:")
st.subheader(" With Love \n The Witches and Wizards of Hogwarts School of Witchcraft and Wizardry")


#video_file = open("C:/Users/Lenovo/Videos/Captures/Grand Theft Auto V 2020-08-29 20-54-23.mp4" , "rb")
#video_bytes = video_file.read()
#st.video(video_bytes)
intro = st.sidebar.selectbox("Welcome to Hogwarts",("None", "McGonagall's Welcome Speech", "Proceed to Houses", "Artwork" , "Games"))

button = st.sidebar.button("Revelio")

def main(intro):
    if intro == "McGonagall's Welcome Speech":
        if button:
            video_file = open("puchu.mp4" , "rb")
            video_bytes = video_file.read()
            intro_speech = st.video(video_bytes)
            return intro_speech
    elif intro == "Proceed to Houses":
        choice= st.sidebar.selectbox("Select your House:",( "None" , "Gryffindor" , "Hufflepuff" , "Ravenclaw" , "Slytherin"))
        return choice

    elif intro == "Games":
        if button:
            st.write('''# Running Monkey
            https://shivaliaich.github.io/project-19-/
            
            ''')

            st.write('''# Quidditch
            https://studio.code.org/projects/gamelab/W7dsw9ScZaXyvNybPws6NRtq4YZbLMbcrB_4y5N6gSk
            ''')
    elif intro == "Artwork":
        if button:
            image = Image.open('photo1.jpg')
            st.image(image)
            image = Image.open('photo2.png')
            st.image(image)


        


choice = main(intro)






def House(choice):
    if choice == "Gryffindor":
        gryffindor = st.sidebar.selectbox("Choose the Witch/Wizard :" , ("None","Hermione Granger" , "Harry Potter", "Ronald Bilius Weasely","Rubeus Hagrid" , "Professor McGonagall" , "Ginny Weasely"))
        return gryffindor
    elif choice == "Hufflepuff":
        hufflepuff = st.sidebar.selectbox("Choose your Witch/Wizard :" , ("None" , "Nymphadora Tonks"))
    
        return hufflepuff
    elif choice == "Ravenclaw":
        ravenclaw = st.sidebar.selectbox("Choose your Witch/Wizard :" , ("None" , "Rowena Ravenclaw" , "Garrick Ollivander"))
        return ravenclaw
    elif choice == "Slytherin":
        slytherin = st.sidebar.selectbox("Choose your Witch/Wizard :" , ("None" , "Draco Malfoy" , "Bellatrix Lestrange" , "Severus Snape"))
        return slytherin




choice2 = House(choice)



def Video_Quotes(choice2):
    if choice2 == "Rubeus Hagrid":
        if button:
            video_file = open("debuda.mp4" , "rb")
            video_bytes = video_file.read()
            a= st.video(video_bytes)
            b = st.write(''' 23rd years old yeh? I have known you since you were 20 and a half, and I have seen you come a long way in these few years. 
            But could I be more proud of the way you have transformed yourself between your 22nd and 23rd birthday. 
            To me it still seems like yesterday. But if there is something that I can assure you is that life will only keep getting tougher, and you? You will be tougher than the challenges that life will bring to you. 
            What's comin' will come and you'll meet it when it does." And you will be better and brighter because yer a witch, nik! Yer a witch''')

        
            return a,b
    elif choice2 == "Severus Snape":
        if button:
            video_file = open("Reeves.mp4" , "rb")
            video_bytes = video_file.read()
            c= st.video(video_bytes)
            c_text = st.write(''' You're 23 now. I've seen you fly and crawl and over the years you've learnt to bewitch the mind and ensnare the senses, to bottle fame and brew glory and I've always advised you to control your emotions, discipline your mind but you still can't Stopper death? Not quite. 
            	You can't cross the road without almost dying. So take this advice from The Half Blood Prince, don't ask for much and don't take much for granted, for as you may have noticed, life isn't fair, but I bet it must feel great to be an insufferable know-it-all! Happy Birthday!''')


           
            return c,c_text
    elif choice2 == "Bellatrix Lestrange":
        if button:
            video_file = open("Meghamala.mp4" , "rb")
            video_bytes = video_file.read()
            d= st.video(video_bytes)

            return d

    elif choice2  == "Nymphadora Tonks":
        if button:
            video_file = open("shivali.mp4" , "rb")
            video_bytes = video_file.read()
            e= st.video(video_bytes)

            return e
    elif choice2 == "Harry Potter":
        if button:
            st.write(''' Niharika aka Niha for me.Lets listen to a story together.i am going to tell & u just listen.even if u get bored u hve no way out except listening to it🤣.
            There was a very mediokar boy who got into a college and there he suddenly met a bunch of people whom he strtd thinking as his own frst college mates but as time passed their true colors started to get revealed by opening their "GOOD" masks and the boy got startled suddnly as he never knew that there is such masks which exactly looks like a "GOOD" human face, because from childhood he only knew masks of batman Superman spiderman which is still sold.But at that time one girl among them held that boys hand and made him realise that neither evryone is masked nor evryone is selfish.There is still sme good hearted people around.She,He along with a couple of more true mad friends stayed together till the end off the cllge.Which started from many,ended into 4-5.and amng those 4-5,she was the only girl who never stopped caring whts good or bad for that boy.She used to criticise when the boy was wrong making the boy understand directly or indirectly thay he is doing wrong and used to praise too when he is doing good.She used to motivate him to the highest.The gril once told the boy pointing to the boys dream car sittng from a bus window -"life e do somethng big keeping motivation working very hard thle ekdin tuio oirm garite chrte prbi"-.These words struck the boy,coming from one of the most favourite and important person in his life.She is still that boys one of the best wisher,the boy has got till date and the boy has no words to say her that how gratefull he is to her that she cared such a hopeless boy,gave confidence to that boy and made him blve that if u want truely something,working hard u can achve ur dream.
            THE END
            The boy here is me and the girl is You Niharika aka My Niha.
            Happy Birthday my gem.Stay healthy safe.❤️
        
        "onnke onnk kichui ble glo toke niye amar kche, kintu prlona keu bhngte bondhutto amader"-if u knw what i mean.🙈❤️''')
    elif choice2 == "Hermione Granger":
        if button:
             video_file = open("anasua.mp4" , "rb")
             video_bytes = video_file.read()
             f= st.video(video_bytes)
             return f
    elif choice2 == "Ronald Bilius Weasely":
        if button:
             video_file = open("tuneer.mp4" , "rb")
             video_bytes = video_file.read()
             g= st.video(video_bytes)
             return g

    elif choice2 == "Draco Malfoy":
        if button:
             video_file = open("momo.mp4" , "rb")
             video_bytes = video_file.read()
             h= st.video(video_bytes)
             return h
    elif choice2 == "Ginny Weasely":
        if button:
             video_file = open("ananya.mp4" , "rb")
             video_bytes = video_file.read()
             i= st.video(video_bytes)
             return i

    elif choice2 == "Professor McGonagall":
        if button:
             video_file = open("puchu2.mp4" , "rb")
             video_bytes = video_file.read()
             j= st.video(video_bytes)
             return j
    elif choice2 == "Rowena Ravenclaw":
        if button:
             video_file = open("mamma.mp4" , "rb")
             video_bytes = video_file.read()
             k= st.video(video_bytes)
             return k
    elif choice2 == "Garrick Ollivander":
        if button:
             video_file = open("pappa.mp4" , "rb")
             video_bytes = video_file.read()
             l= st.video(video_bytes)
             return l
    
            






result = Video_Quotes(choice2)
        


    

