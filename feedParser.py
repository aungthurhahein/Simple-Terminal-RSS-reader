#-------------------------------------------------------------------------#
#!/usr/bin/env python
# a simple terminal feed parser to checkout web and development sources
# usage: python feedparser.py -w websiteInitials(ph,hn,gh..)

# Date: 19.12.2014
# author: Aung
#-------------------------------------------------------------------------#
__author__ = 'aungthurhahein@aol.com'
__version__ = '0.1'


import sys,os
import time
import json, requests
import webbrowser
#Pocket api wrapper-Copyright 2014 Felipe Borges <felipe10borges@gmail.com>
import pocket

# these might need to install
import argparse
import feedparser


# get website from initial
# config this dictionary list as you wish
def main(website):

    website_list={
        'ph': 'http://www.producthunt.com/feed.atom',
        'hn': 'https://news.ycombinator.com/rss',
        'gh': 'http://www.growth-hacker.com/feed/',
        'ri': 'researchers.io/feed/',
        'dn': 'https://news.layervault.com/stories?format=atom',
        'sb': 'http://feeds.feedburner.com/SidebarFeed',
        'sd':  'http://rss.slashdot.org/Slashdot/slashdot'
    }
    website = website.lower() #chage initials to lowercase for consistency
    rss_url =website_list.get(website)
    try:
        rss_parse(rss_url)
    except:
        print 'website initials not recognised.'

#arguments parser
def ParseCommandLine():
    parser = argparse.ArgumentParser('simple rss feed parser from popular web development and design sources: '
                                     'Product Hunt, '
                                     'Hacker News, '
                                     'Growth Hackers, '
                                     'Researcher Io, '
                                     'Designer News, '
                                     'Side Bar, '
                                     'Slash Dot.'
                                    )
    parser.add_argument('-w','--website', help='add initial of the url (e.g. ph for ProductHunt)')
    theArgs = parser.parse_args()
    return theArgs

#needs to improve
#TODO: add to pocket by keyboard input
#TODO: print as list with pointer

# parse it
def rss_parse(urlfool):
    site = feedparser.parse(urlfool)
    print "Title: %s" %(site.feed.title)
    print "URL: %s" % (site.feed.link)
    print "-------------------------------------"

    for ent in range(0,len(site.entries)):
        print ""
        time.sleep(0.5)
        print(site.entries[ent].title)
        print(site.entries[ent].link),
        try:
             print "[pocket]"
        except:
            print""

# Pocket OAuth
def PocketAuth():
    # step1
    headers = {"content-type": "application/json"}
    params ={
        'consumer_key':'34863-11080497bbeded19744312c9',
        'redirect_uri':'pocketapp1234:authorizationFinished'
    }
    pocketOAuth = requests.get("https://getpocket.com/v3/oauth/request", data=json.dumps(params), headers=headers)
    code =pocketOAuth.text
    request_token= code.split("=")[1]

    # step2
    userparam ={
        'request_token': request_token,
        'redirect_uri':'http://aungthurhahein.me/pocket.html'
    }
    UserAuth=requests.get("https://getpocket.com/auth/authorize", params=userparam)

    print "Do you want to use pocket to save news?(y/n)"
    Pocket_User= raw_input("> ")

    #step3
    if Pocket_User == "y":
        print "pocket authorization page will open in your default browser. This is one time only.I swears..."
        time.sleep(1)
        webbrowser.open(UserAuth.url)
        print ""
        time.sleep(2)
        print "type 'ok' after you done:"
        ok = raw_input("> ")

        #step4
        if ok == "ok":
            finalparam={
                'consumer_key':'34863-11080497bbeded19744312c9',
                'code': request_token
            }

            accessToken = requests.get("https://getpocket.com/v3/oauth/authorize", data=json.dumps(finalparam), headers=headers)

            configfile = open('.rssparser', 'w+')
            configfile.write(accessToken.text)
            configfile.close()
    else:
            configfile = open('.rssparser', 'w+')
            configfile.close()

# read aToken from file
def readPocket():
    configfile = open('.rssparser', 'r')
    configContent = configfile.read()
    try:
        accesstoken= configContent.split("&")[0]
        accesstoken= accesstoken.split("=")[1]
    except:
        print 'No pocket configuration.'
    configfile.close()

    return accesstoken

# added to pocket
def addtoPocket(aToken,url):
    # sample rss parser conumerkey
    cKey = "34863-11080497bbeded19744312c9"
    api = pocket.Api(consumer_key=cKey,access_token=aToken)
    item = api.add(url)

if __name__ == "__main__":
    if os.path.isfile(".rssparser") is False:
        PocketAuth()
    else:
      accesstoken = readPocket()
    args = ParseCommandLine()
    main(args.website)
