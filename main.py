import pickle

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
clf = pickle.load(open("model.pickle", "rb"))

def predict(k):
    return clf.predict(tfidf_vectorizer.transform([k]))[0]

def process(k):
    x = k.lower()
    final = ""

    for i in x:
        if i.isalpha() == False and i != " ":
            if i == "'":
                continue
            else:

                final += " "
        else:
            final += i 

    return final 

def get_raw_text(k):
    final = ""
    for i in k.splitlines():
        final += process(i) + " "

    return final

consumer_key = "RTjvM8xCUEAgWAOmArVBKW3ft" 
consumer_secret = "NmsbCOgIpqGx2xbwgdx6hDmgh2y1ZBRLQ9ePF2YMzYbwa83ZGn" 
access_token = "1219575883775610880-TNM0MnMmd6vt7DjDDvIwy2U2fZwzAK" 
access_token_secret = "el070XmQcYYX2lo7h6fpD0XczWgnvhn1xizop0esuErGU"

import tweepy
import time 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

prev = 0 
while True:
    last_dms = api.list_direct_messages()
    m = []
    for messages in last_dms:
        m.append({"text":messages._json["message_create"]["message_data"]["text"], "sender":messages._json["message_create"]["sender_id"]})

    print(m)
    for i in m:
        print(predict(get_raw_text(i["text"])))
        if predict(get_raw_text(i["text"])) == 1:
            print("ye")
            api.send_direct_message(i["sender"], "Hey, we want to let you know that we're here for you, and that we along with many other people care about you.\n\nPlease don't hesitate to call 1-800-273-8255 for help because we are there to support you every step of the way.") 
    time.sleep(30)