import tweepy 
from bs4 import BeautifulSoup #pip3 install lxml
import requests
import re
  

consumer_key = "XXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXX"
  

 
def Tweets(username): 
          

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  

        auth.set_access_token(access_key, access_secret) 
  

        api = tweepy.API(auth) 
  

        number_of_tweets=10
        tweets = api.user_timeline(screen_name=username, count=number_of_tweets) 



  
        sum=""
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # sum tweets in a variable to count their words later
            sum=sum+j
  
        # counting words
        count = len(re.findall(r'\w+', sum))
        print (count)
        

        #followers count
        temp = requests.get('https://twitter.com/'+username)
        bs = BeautifulSoup(temp.text,'lxml')
        try:
         follow_box = bs.find('li',{'class':'ProfileNav-item ProfileNav-item--followers'})
         followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
         followers=int(format(followers.get('data-count')))
         print(followers)
         Tweets.multi=int(followers*count)  #creating number(followers X words)
        except:
         print('Account name not found...')
        
        
        
        
#first profile 
if __name__ == '__main__': 
    username=input("Όνομα 1ου χρήστη: ")
    username1=username
    Tweets(username) 
    multi1=Tweets.multi


#second profile
if __name__ == '__main__': 
    username=input("Όνομα 2ου χρήστη: ")
    Tweets(username)
    username2=username  
    multi2=Tweets.multi

#Final result
if multi1>multi2:
    diafora=multi1-multi2
    print("Ο",username1,"έχει το μεγαλύτερο γινόμενο με ",diafora," διαφορά") 
elif multi1<multi2:
    diafora=(multi2-multi1)
    print("Ο",username2,"έχει το μεγαλύτερο γινόμενο με ",diafora," διαφορά")  
else:
    print("το γινόμενο των followers ΕΠΙ τον αριθμό λέξεων των 10 τελευταίων tweets των δυο χρηστών είναι ίσα")    
