#!/usr/bin/python
import win32com.client
import tweepy
from os import system

iTunes = win32com.client.Dispatch("iTunes.Application")

if iTunes.PlayerState == 1:
    curTrack = iTunes.CurrentTrack
    if curTrack.Artist == '':
        song = curTrack.Name
    else:
        song = curTrack.Artist + ' - ' + curTrack.Name #+ ' - ' + curTrack.album()

    tweet = '#nowplaying ' + song

    try:
        auth = tweepy.OAuthHandler('consumer', 'consumer_secret')
        auth.set_access_token('access', 'access-secret')
        api = tweepy.API(auth)
        
        api.update_status(tweet)
        print(api.me().name + ': ' + tweet)
    except tweepy.error.TweepError as err:
        print(err)




