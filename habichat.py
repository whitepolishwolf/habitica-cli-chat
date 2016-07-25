import requests
# Place your user and key here
USER = 'userid'
KEY = 'userkey'

HEADERS = {'Content-Type' : 'application/json', 'x-api-user' : USER, 'x-api-key' : KEY}
print('[1] Chat drużynowy')
print('[2] Karczma (jeszcze bugniete ;<)')
print('[3] Runner\'s Edge')
print('[4] Linux')
print('[5] Polska')

GROUPNAME = input('Podaj numer grupy ')
if GROUPNAME == '1':
    GROUPNAME = 'party'
elif GROUPNAME == '2':
    GROUPNAME = 'tavern'
elif GROUPNAME == '3':
    GROUPNAME = 'a35aa006-b42d-4b27-ab0c-8864b087c6f2'
elif GROUPNAME == '4':
    GROUPNAME = '1df40f0f-b758-45b3-8ed8-8916f85577eb'
elif GROUPNAME == '5':
    GROUPNAME = '006c7f68-e07a-4a56-9dcf-fd64c90e3ef4'
else:
    print('Nie podałeś dobrego numeru grupy!')
    quit()

URL = 'https://habitica.com/api/v3/groups/' + GROUPNAME + '/chat'

print('[1] Odczytaj wiadomości')
print('[2] Wyślij wiadomość')
confirmation = input('Co chcesz zrobić? ')

if confirmation == '1':
    GETMSG = requests.get(URL, headers=HEADERS).json()
    for i in range(20, -1, -1):
        if 'user' in GETMSG['data'][i]:
            print('\033[92m' + GETMSG['data'][i]['user'] + '\033[0m', end=": ")
            print(GETMSG['data'][i]['text'])
        else:
            print('\033[93m' + GETMSG['data'][i]['text'] + '\033[0m')
elif confirmation == '2':
    MSGTEXT = input('Co chciałbyś napisać? ')
    MSGDICT = {'message' : msgtext}
    MSGSEND = requests.post(URL, headers=HEADERS, json=msgdict)
    MSGSEND
    print('Wiadomość została wysłana!')
    GETMSG = requests.get(url, headers=HEADERS).json()
    print('\033[92m' + GETMSG['data'][0]['user'] + '\033[0m', end=": ")
    print(GETMSG['data'][0]['text'])
else:
    print('You shall not pass!')
                            


