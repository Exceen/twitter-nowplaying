#!/usr/bin/python
from ScriptingBridge import *
import twitter

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
curTrack = iTunes.currentTrack()

api = twitter.Api(consumer_key='consumer_key',
  				consumer_secret='consumer_secret',
					access_token_key='access_token_key',
					access_token_secret='access_token_secret')
user = api.VerifyCredentials().GetScreenName()

tweet = '#nowplaying ' + curTrack.artist() + ' - ' + curTrack.name() #+ ' - ' + curTrack.album()
statuses = api.GetUserTimeline(user)

if iTunes.isRunning() and iTunes.playerState() == 1800426320: # == 1800426352 when paused

	retry = True
	loop_count = 0
	
	while retry:
		try:
			api.PostUpdate(tweet)
			print user + ": " + tweet
			retry = False
		except twitter.TwitterError, err:
			print err
			retry = False
		except:
			retry = False

		loop_count += 1
		if loop_count > 9:
			retry = False
