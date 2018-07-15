import json
import random

players =["Ronaldo","Benzema","Bale","Luca","Ramos","Navas","Varane","Croos","Isco","kaka","Casilas","Marcelo","Raul","VNroy"]


'''
with open('/home/rohanbagwe/GoogleChrome/mongo/realFC.json', 'w') as outfile:  
    for w in range(len(players)):
        data = json.dumps({'_id': w, 'emp_code': 'player_'+str(w), 'salary': round(random.randint(6754,8989) * 1000), 'experience': round(random.randint(30,55)),})

        json.dump(data, outfile)
'''

with open('/home/rohanbagwe/GoogleChrome/mongo/realFC.json', 'w') as outfile:  
    for w in range(len(players)):
         outfile.write(str({'_id': w, 'emp_code': 'player_'+str(w), 'salary': round(random.randint(6754,8989) * 1000), 'experience': round(random.randint(30,55)),})+"\n")
         