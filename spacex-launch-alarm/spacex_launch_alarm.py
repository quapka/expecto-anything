#!/usr/bin/env python

# builtins
import argparse
import time
# 3rd party
from bs4 import BeautifulSoup
import requests
import vlc

trigger_words = [
    'launch', 'lift-off', 'lift',
    'webcast', 'spacex.com/webcast',
    'liftoff',
]

forbidden_words = [
    'delay', 'delayed',
]

def get_page():
    page = requests.get('https://twitter.com/spacex')
    return page

def parse_page(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_tweets(parsed_page):
    tweets = parsed_page.find_all(attrs={'class': 'tweet', 'data-name': 'SpaceX'})
    return tweets

def alarm(song):
    print('Starting the alarm!')
    player = vlc.MediaPlayer(song)
    volume = 50
    now = time.time()
    while True:
        # boost the volume by 10dB each 30 seconds
        if time.time() - now >= 30:
            # reset what 'now' means
            now = time.time()
            volume += 10
            player.audio_set_volume(volume)
        player.play()


def get_tweet_time(tweet):
    val = tweet.find(attrs={'class':'tweet-timestamp'}).span.attrs['data-time']
    return int(val)

def get_tweet_text(tweet):
    return tweet.find(attrs={'class':'TweetTextSize'}).text

def wanted_tweet(tweet):
    text = get_tweet_text(text).lower()
    wanted = False
    # any trigger word is enough
    for word in trigger_words:
        if word in text:
            wanted = True
            break
    # any forbidden word prevents the alarm to start
    for word in forbidden_words:
        if word in text:
            wanted = False
            break

    return wanted


def process_tweets(args, tweets):
    time_window = args.time_window
    now = time.time()
    for tweet in tweets:
        tweet_time = get_tweet_time(tweet)
        # the tweet is too old
        if now - tweet_time > time_window:
            print('Tweet is too old! At least have fun reading it!')
            print(get_tweet_text(tweet))
            print()
            continue

        if wanted_tweet(tweet):
            print("We got a winner! Wake Up! Maybe there's a Starma!")
            alarm(args.mp3_file)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        'Start playing the provided [mp3-file] file when the one of the tweets\n'
        'since [time] from @SpaceX or @elonmusk contain predefined set of words.'
    )
    parser.add_argument(
        '-m', '--mp3-file',
        required=True,
        help='Path to the .mp3 file for the alarm'
    )

    parser.add_argument(
        '-t', '--time-window',
        default=300,
        type=int,
        help='Specify the size of the time-window to use for the tweets in seconds (e.g. last 300s).'
    )

    args = parser.parse_args()
    while True:
        print('Getting the HTML page with the tweets.')
        page = get_page()
        print('Parsing the HTML page.')
        soup = parse_page(page)
        tweets = get_tweets(soup)
        print('Checking the tweets for a trigger tweets.')
        process_tweets(args, tweets)

        to_wait = abs(args.time_window - 30)
        while to_wait:
            print(' ' * 100, end='\r')
            print(f'Waiting for {to_wait} seconds', end='\r')
            time.sleep(1)
            to_wait -= 1
        print()
