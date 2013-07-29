#!/usr/bin/python
from ScriptingBridge import SBApplication
import tweepy

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
curTrack = iTunes.currentTrack()

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token_key', 'access_token_secret')
api = tweepy.API(auth)

if iTunes.isRunning() and iTunes.playerState() == 1800426320: # == 1800426352 when paused
	try:
		tweet = '#nowplaying ' + curTrack.artist() + ' - ' + curTrack.name() #+ ' - ' + curTrack.album()
		api.update_status(tweet)
		print api.me().name + ": " + tweet
	except tweepy.error.TweepError, err:
		print err



