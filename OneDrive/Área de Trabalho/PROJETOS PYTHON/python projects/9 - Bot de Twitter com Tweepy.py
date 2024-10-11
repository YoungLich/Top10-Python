import tweepy

auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')

api = tweepy.API(auth)

mensagem = "Tweet automático via Tweepy"
api.update_status(mensagem)