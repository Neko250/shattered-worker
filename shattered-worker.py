#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytumblr


def hyperworker():
  config = get_config()
  if not config:
    print('config.json error')
    return
  
  tumblr = pytumblr.TumblrRestClient(
    config['consumer_key'],
    config['consumer_secret'],
    config['oauth_token'],
    config['oauth_secret']
  )
  
  print('{0!s} drafts'.format(len(tumblr.drafts('shatteredcontinuum')['posts'])))
  print('{0!s} enqueued'.format(len(tumblr.queue('shatteredcontinuum')['posts'])))


def get_config():
  conf = None
  with open('config.json') as f:
    conf = json.load(f)
  return conf


if __name__ == '__main__':
  hyperworker()
