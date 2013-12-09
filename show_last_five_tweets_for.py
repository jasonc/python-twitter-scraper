#!/usr/bin/env python

import sys
import lxml.html
import urllib2

def get_tweets(tweeter):
  """ get_tweets(tweeter) - Returns a list of the 5 most recent tweets for tweeter. """
  tweets = []
  tweets_url = 'https://twitter.com/' + tweeter

  try:
    html = urllib2.urlopen(tweets_url).read()
  except:
    return tweets

  parsed_html = lxml.html.fromstring(html)
  tweet_elements = parsed_html.cssselect('.tweet-text')

  for tweet_element in tweet_elements[:5]:
    tweets.append(tweet_element.text_content())
  return tweets


def print_tweets(tweeter, tweets):
  """ print_tweets(tweeter,tweets) - Display tweets for tweeter."""
  print '>>>', tweeter , '<<<'
  print '\n\n'.join(tweets)


def main():
  if len(sys.argv) < 2:
    print 'Usage: %s [twitter-username] [twitter-usernameN] ...' % sys.argv[0]
    sys.exit(1)

  for tweeter in sys.argv[1:]:
    print_tweets(tweeter, get_tweets(tweeter))


if __name__ == '__main__':
  main()
