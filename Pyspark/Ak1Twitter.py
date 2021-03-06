import socket
import sys
import requests
import requests_oauthlib
import json

ACCESS_TOKEN = 'your access token'
ACCESS_SECRET = 'yours'
CONSUMER_KEY = 'yours'
CONSUMER_SECRET = 'yours'
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)



TCP_IP = "localhost"
TCP_PORT = 9993
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Waiting for TCP connection...")
conn, addr = s.accept()
print(conn)
print("Connected... Starting getting tweets.")
url = 'https://stream.twitter.com/1.1/statuses/filter.json'
query_data = [('locations', '-130,-20,100,50')]
query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
response = requests.get(query_url, auth=my_auth, stream=True)
print(query_url, response)
for line in response.iter_lines():
	full_tweet = json.loads(line.decode('utf-8'))
        tweet_text = full_tweet['text'].encode('utf-8')
        print("Tweet Text: " + tweet_text)
        print ("------------------------------------------")
        conn.send(tweet_text + '\n')
    	
        	







