import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '809972565:AAHkGT-DhPJZW8YzkZAudssQ65VND3FjDEA'
    bot_chatID = '694453858'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    
import datetime
now = datetime.datetime.now()
day = (now.strftime("%A"))
a = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
b=['EEE','C_PROG','CHEM','LUNCH','MATHS','FREE','CUL','Hope u will enjoy ur day']
c=['MATHS','ESSENTIALS','EEE_LAB','LUNCH','CHEM','EEE','Hope u will enjoy ur day']
d=['CHEM_LAB','ESSENTIALS','C_PROG','MATHS','CUL','Hope u will enjoy ur day']
e=['C_LAB','ESSENTIALS','LUNCH','C_PROG','EEE','Hope u will enjoy ur day']
f=['CHEM','EEE','MATHS','FREE','LUNCH','SAH','FREE','Hope u will enjoy ur day']
if(day=='Monday'):
	for i in range(0,len(b)):
    	test = telegram_bot_sendtext(b[i])
		
if(day=='Tuesday'):
	for i in range(0,len(c)):
    	    test = telegram_bot_sendtext(c[i])
if(day=='Wednesday'):
	for i in range(0,len(d)):
    	    test = telegram_bot_sendtext(d[i])
if(day=='Thursday'):
	for i in range(0,len(e)):
    	    test = telegram_bot_sendtext(e[i])
if(day=='Friday'):
	for i in range(0,len(f)):
    	    test = telegram_bot_sendtext(f[i])
                                  
