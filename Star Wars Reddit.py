"""
 --------------------------------------------------------------------------------
 File:    StrWrsbot.py
 Description: Finds references to star wars based on a specific set of words
              and replies with “May the force be with you”
 Author:  William Mabia
 --------------------------------------------------------------------------------
 """
import praw
import time


def login():
    #Reddit API login
    reddit = praw.Reddit(client_id='T8RWGMnizf2xVQ',
                         
                client_secret='Ggko7kxvgxe7Wt1wXz1FNeVq-l_c2g',
                username='notapythonbotforsure',
                password='{Sikethisabot124',
                user_agent='star wars bot by notWill')
    return reddit


#Subreddit I want my bot to work in
subreddit = reddit.subreddit('HIMYM')

#Array of keywords(Search Parameters)
Keywords = ["Luke", "Leia", "Darth Vader", "Star Wars", "Yoda"]

#Response
reply = "May the Force be with you"


def findncomment(Reddit):
    #Look for keywords and reply
    for comment in subreddit.stream.comments:
        if keywords in comment.body:
            try:
                print ("Instance Found")
                comment.reply(reply)
            except:
                #Error Handling
                print("somewhere else")




            
