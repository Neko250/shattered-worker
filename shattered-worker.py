#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


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
  
  client.info()


def get_config():
  conf = None
  with open('config.json') as f:
    conf = json.load(f)
  return conf


if __name__ == '__main__':
  hyperworker()
