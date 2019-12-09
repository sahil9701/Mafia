from gtts import gTTS
import os
import random
import time
players=['Sahil', 'Sam','Meet', 'Pooja', 'Deep','Pranav','Pratik','Krunal','Nisarg']
characters={1:'Mafia',2:'Mafia',3:'Mafia',4:'Police_1',5:'Police_2',6:'Doctor',7:'Villagers',8:'Villagers',9:'Villagers'}
ranks=[i for i in range(1,10)]
random.shuffle(ranks)

final_assignments={}
for idx, ch in enumerate(players):
    final_assignments[ch]=characters[ranks[idx]]
print(final_assignments)

for i in players:
    tts = gTTS(text=i+'wake up.', lang='en', slow=False)
    tts.save("good.mp3")
    os.startfile('good.mp3')

    print('You are ' + final_assignments[i])
    time.sleep(4)
    os.remove('good.mp3')
    print('\n' * 40)
    time.sleep(1)

tts = gTTS(text='Mafia it is your turn to wake up. Whom do you want to kill?', lang='en', slow=False)
tts.save("good.mp3")
os.startfile('good.mp3')
time.sleep(5)
os.remove('good.mp3')
for idx, i in enumerate(players):
    print(str(idx) +"."+ i)
dead=input("Whom do you want to kill?")
print('\n' * 40)

#print(final_assignments)
tts = gTTS(text='Police 1 it is your turn to wake up. Whom do you suspect?', lang='en', slow=False)
tts.save("good.mp3")
os.startfile('good.mp3')
time.sleep(5)
os.remove('good.mp3')
for idx, i in enumerate(players):
    print(str(idx) +"."+ i)

suspect_1=input("Whom do you suspect?")
if final_assignments[players[int(suspect_1)]]=='Mafia':
    print("Yes")
else:
    print("No")
time.sleep(2)
print('\n' * 40)

tts = gTTS(text='Police 2 it is your turn to wake up. Whom do you suspect?', lang='en', slow=False)
tts.save("good.mp3")
os.startfile('good.mp3')
time.sleep(5)
os.remove('good.mp3')
for idx, i in enumerate(players):
    print(str(idx) +"."+ i)

suspect_2=input("Whom do you suspect?")
if final_assignments[players[int(suspect_2)]]=='Mafia':
    print("Yes")
else:
    print("No")
time.sleep(2)
print('\n' * 40)

tts = gTTS(text='Doctor it is your turn to wake up. Whom do you want to heal?', lang='en', slow=False)
tts.save("good.mp3")
os.startfile('good.mp3')
time.sleep(5)
os.remove('good.mp3')
for idx, i in enumerate(players):
    print(str(idx) +"."+ i)
heal=input('Whom do you want to heal?')
print('\n' * 40)
if dead==heal:
    tts = gTTS(text="City wakes up with no one dead!!!!", lang='en', slow=False)
    tts.save("good.mp3")
    os.startfile('good.mp3')
    time.sleep(5)
    os.remove('good.mp3')
    print("City wakes up with no one dead!!!!")
else:
    tts = gTTS(text="City wakes up with "+players[int(dead)]+' dead!!!!', lang='en', slow=False)
    tts.save("good.mp3")
    os.startfile('good.mp3')
    time.sleep(5)
    os.remove('good.mp3')
    print("City wakes up with "+players[int(dead)]+' dead!!!!')