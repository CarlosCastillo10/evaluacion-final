from credenciales import *
import tweepy
import codecs
<<<<<<< HEAD

=======
>>>>>>> upstream/master
# https://tweepy.readthedocs.io/en/v3.5.0/

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# For loop to iterate over tweets with #ocean, limit to 10
<<<<<<< HEAD
lista = ['CarlosC62169047', 'djosuejj', 'pedrojsalinas', 'fernandogdo1']
for l in lista:
    archivo = codecs.open('%s.csv' %l, 'w', encoding='utf-8')
    archivo.write('%s|%s|%s|%s|%s|%s\n'%('name','screen_name','followers_count','friends_count', 'listed_count', 'favourites_count'))
    informacion = api.followers(l)
    for x in informacion['users']:
    	datos = {'followers_count': x['followers_count'], 'listed_count': x['listed_count'], 'friends_count': x['friends_count'],
    	'screen_name': x['screen_name'], 'favourites_count': x['favourites_count'], 'name': x['name'], 'created_at': x['created_at'] }
    	archivo.write('{name}|{screen_name}|{followers_count}|{friends_count}|{listed_count}|{favourites_count}|\n'.format(** datos))
    archivo.close()
    




=======

'followers_count', 
'listed_count', 
'friends_count', 
'screen_name', 
'favourites_count',
'name',
'created_at'

lista = ["CarlosC62169047", "djosuejj", "pedrojsalinas", "fernandogdo1"]
for l in lista:
    archivo = codecs.open("%s.csv" % l, "w", encoding="utf8")
    informacion = api.followers(l)
    for u in informacion['users']:
        data = {'followers_count': u['followers_count'], 
                'listed_count': u['listed_count'], 
                'friends_count':u['friends_count'], 
                'screen_name':u['screen_name'], 
                'favourites_count':u['favourites_count'],
                'name':u['name'],
                'created_at':u['created_at']
                }
        archivo.write(u"{screen_name}|{name}|{created_at}|{followers_count}|{listed_count}|\
                {friends_count}|{favourites_count}\n".format(**data))
    archivo.close()
>>>>>>> upstream/master



