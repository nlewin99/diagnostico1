import json

tweets = []
for line in open('tweets.json', 'r'):
    tweets.append(json.loads(line))


def top_retweet(tweets):
    all = []
    top = []
    actual = []
    count = 0
    for i in range(10):
        for t in tweets:
            if t['retweetCount'] > actual:
                actual[0] = t['retweetCount']
                actual[1] = count
            
            count += 1
        top.append(tweets[actual[1]])
        tweets.pop(actual[1])
    return top


def top_user(tweets):
    return



