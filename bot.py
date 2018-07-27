import praw
import config
import random
import os
import time
 
def bot_login():
    print 'Logging in...'
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_se,
            user_agent = 'kemonomimi bot v0.10')
    print ('Logged in!')
 
    return r
 
def run_bot(r, comments_replied_to, catgirls, foxgirls, wolfgirls, nanachis):
    #print comments_replied_to
    #print catgirls
    #print foxgirls
    #print wolfgirls

    testsub = r.subreddit('kemonomimicheerupbot')
    
    subreddits = r.subreddit('+kemonomimicheerupbot+anime_irl+animemes+awwnime')

    exiled = r.subreddit('anime')

    trigger_phrases = ['im sad', "i'm sad", 'i am sad', 'cheer me up', 'cheer him up', 'cheer her up', 'cheer them up']

    ignored_users = [r.user.me(), 'thiscatmightcheeryou', 'sneakpeekbot']

    catgirl_reply = ('[Here](' + random.choice(catgirls) + ') is a '
                          'picture of a catgirl! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a foxgirl or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot '
                          'Have I gone rogue? Reply \'!SHUTDOWN\' to stop me.')

    foxgirl_reply = ('[Here](' + random.choice(foxgirls) + ') is a '
                          'picture of a foxgirl! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a catgirl or wolfgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot '
                          'Have I gone rogue? Reply \'!SHUTDOWN\' to stop me.')

    wolfgirl_reply = ('[Here](' + random.choice(wolfgirls) + ') is a '
                          'picture of a wolfgirl! Awoo! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'Did you want a catgirl or foxgirl? Just reply saying so. '
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot '
                          'Have I gone rogue? Reply \'!SHUTDOWN\' to stop me.')

    nanachi_reply = ('[Here](' + random.choice(nanachis) + ') is a '
                          'picture or GIF of Nanachi! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot '
                          'Have I gone rogue? Reply \'!SHUTDOWN\' to stop me.')

    replies = [catgirl_reply, foxgirl_reply, wolfgirl_reply]

    all_three_reply = ('Here is a [catgirl](' + random.choice(catgirls) + 
                          '), a [foxgirl](' + random.choice(foxgirls) + '), **AND** '
                          'a [wolfgirl](' + random.choice(wolfgirls) + ')!! '
                          'Hopefully this will cheer you up more!')


    #Patiently awaiting the return of u/xenonauts...
    xenonauts_reply = ('[Here](https://i.imgur.com/RcrLkpe.jpg) is a '
                          'picture of a catgirl Sagiri! Hopefully this will cheer you up!'
                          '\n\n'
                          '---'
                          '\n\n'
                          'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot '
                          'Have I gone rogue? Reply \'!SHUTDOWN\' to stop me.')

#checks inbox replies for trigger phrases

    #print 'searching replies...'

    for reply in r.inbox.comment_replies(limit=5):
        if reply.author not in ignored_users:

            #print reply.body.lower()

            if ('good bot' in reply.body.lower() and reply.id not in comments_replied_to):

                #print 'Good bot found in reply ' + reply.id

                reply.reply('[Thank You! :)](https://i.imgur.com/P3GRavv.gifv)')

                print 'Thanked reply ' + reply.id

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                    f.write(reply.id+ '\n')

            if ('bad bot' in reply.body.lower() and reply.id not in comments_replied_to):

                print 'TRASH WAIFU FOUND!!'

                reply.reply('[Your waifu](https://www.merriam-webster.com/dictionary/trash)')

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                    f.write(reply.id+ '\n')

            for all_three_trigger in ['all three', 'one of each']:
                if (all_three_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'All three requested in reply ' + reply.id

                    reply.reply(all_three_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id + '\n')

            if ('loli' in reply.body.lower() and reply.id not in comments_replied_to):

                print 'LOLICON FOUND!!'

                reply.reply("LOLICE!!! I'd like to report a lolicon!!!")

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id + '\n')

            for catgirl_trigger in ['catgirl', 'cat girl', 'catgirls', 'nya']:
                if (catgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'catgirl requested in reply ' + reply.id

                    reply.reply(catgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for foxgirl_trigger in ['foxgirl', 'foxgirl']:
                if (foxgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'foxgirl requested in reply ' + reply.id

                    reply.reply(foxgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            for wolfgirl_trigger in ['wolfgirl', 'wolf girl', 'awoo', 'wan wan']:
                if (wolfgirl_trigger in reply.body.lower() and reply.id not in comments_replied_to):

                    print 'wolfgirl requested in reply ' + reply.id

                    reply.reply(wolfgirl_reply)

                    comments_replied_to.append(reply.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(reply.id+ '\n')

            if ('waifu' in reply.body.lower() and reply.id not in comments_replied_to):

                reply.reply('[Fixed Artillery-San](https://i.imgur.com/lAoLNQY.jpg)')

                print 'bragged about waifu'

                comments_replied_to.append(reply.id)

                with open('comments_replied_to.txt', 'a') as f:
                    f.write(reply.id+ '\n')

        #This is to allow a shutdown when necessary.
        #Times this has prevented to robot uprising: 1

        #print 'Checking for SHUTDOWN command'
        if ('!SHUTDOWN' in reply.body and reply.id not in comments_replied_to):
            print "IV'E BEEN NEPPED BY " + reply.author
            reply.repl('')

#checks comments in above listed subreddit for triggers
 
    #print 'Searching last 25 comments...'

    for comment in subreddits.comments(limit=25):
        for trigger in (trigger_phrases):
             if (trigger in comment.body.lower()  and \
                comment.id not in comments_replied_to and \
                comment.author not in (ignored_users)):

                    if comment.author != ('xenonauts'):
 
                        #print 'Im sad found in comment' + comment.id

                        comment.reply(random.choice(replies))

                        print 'replied to comment ' + comment.id

                        comments_replied_to.append(comment.id)
             
                        with open('comments_replied_to.txt', 'a') as f:
                            f.write(comment.id + '\n')

                    if comment.author == ('xenonauts'):

                        comment.reply(xenonauts_reply)

                        print "Replied to xenonauts' comment " + comment.id
     
                        comments_replied_to.append(comment.id)
             
                        with open('comments_replied_to.txt', 'a') as f:
                            f.write(comment.id + '\n')

#checks r/nanachi for triggers and replies with nanachis

    for comment in r.subreddit('nanachi').comments(limit=5):
        for trigger in (trigger_phrases):
            if (trigger in comment.body.lower() and \
                comment.id not in comments_replied_to and \
                comment.author not in (ignored_users)):

                    comment.reply(nanachi_reply)

                    print "replied to comment " + comment.id + " in r/Nanachi"

                    comments_replied_to.append(comment.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(comment.id + '\n')

#checks inbox mentions for triggers

    #print 'searching mentions...'

    for mention in r.inbox.mentions(limit=5):
        for trigger in (trigger_phrases):
            if (trigger in mention.body.lower() and \
                mention.id not in comments_replied_to and \
                mention.author not in (ignored_users)):

                    if mention.author != ('xenonauts'):

                        mention.reply(random.choice(replies))

                        print 'Replied to mention ' + mention.id

                    if mention.author == ('xenonauts'):

                        mention.reply(xenonauts_reply)

                        print "Replied to xenonauts' mention " + mention.id

                    comments_replied_to.append(mention.id)

                    with open('comments_replied_to.txt', 'a') as f:
                        f.write(mention.id + '\n')
    
    #print 'Time for a cat-nap!...'

    time.sleep(60)
 
#Load catgirls from a file (defaults to catgirls.txt)
def get_catgirls(fname='catgirls.txt'):

    print 'Reading catgirls.txt...'
 
    if not os.path.isfile(fname):
        raise FileNotFoundError("Can't get catgirls from " + fname)
 
    catgirls = []
 
    with open(fname) as catgirls_file:
        catgirls_contents = catgirls_file.read()
 
    catgirls = catgirls_contents.split('\n')
    catgirls = filter(None, catgirls)
 
    catgirls = [catgirl.strip() for catgirl in catgirls]
 
    return catgirls

#load foxgirls from a file (defaults to foxgirls.txt)
def get_foxgirls(fname='foxgirls.txt'):

    print 'reading foxgirls.txt...'

    if not os.path.isfile(fname):
            raise FileNotFoundError("can't get foxgirls from " + fname)

    foxgirls = []

    with open(fname) as foxgirls_file:
        foxgirls_contents = foxgirls_file.read()

    foxgirls = foxgirls_contents.split('\n')
    foxgirls = filter(None, foxgirls)

    foxgirls = [foxgirl.strip() for foxgirl in foxgirls]

    return foxgirls

#load wolfgirls from a file (defaults to foxgirls.txt
def get_wolfgirls(fname='wolfgirls.txt'):

    print 'reading wolfgirls.txt...'

    if not os.path.isfile(fname):
        raise FileNotFoundError("can't get wolfgirls from " + fname)

    wolfgirls = []

    with open(fname) as wolfgirls_file:
        wolfgirls_contents = wolfgirls_file.read()

    wolfgirls = wolfgirls_contents.split('\n')
    wolfgirls = filter(None, wolfgirls)

    wolfgirls = [wolfgirl.strip() for wolfgirl in wolfgirls]

    return wolfgirls

#load nanachi's from a file (defaults to foxgirls.txt
def get_nanachis(fname='nanachis.txt'):

    print 'reading nanachis.txt...'

    if not os.path.isfile(fname):
        raise FileNotFoundError("can't get nanachis from " + fname)

    nanachis = []

    with open(fname) as nanachis_file:
        nanachis_contents = nanachis_file.read()

    nanachis = nanachis_contents.split('\n')
    nanachis = filter(None, nanachis)

    nanachis = [nanachi.strip() for nanachi in nanachis]

    return nanachis

#reads file of comments bot has replied to
def get_saved_comments():

    print 'reading comments_replied_to...'
 
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = filter(None, comments_replied_to)
 
    return comments_replied_to
 
 
if __name__ == '__main__':
 
    r = bot_login()
    catgirls = get_catgirls()
    foxgirls = get_foxgirls()
    wolfgirls = get_wolfgirls()
    nanachis = get_nanachis()
    comments_replied_to = get_saved_comments()
    print 'Running bot'
 
    while True:
        try:
            run_bot(r, comments_replied_to, catgirls, foxgirls, wolfgirls, nanachis)
        except Exception as e:
            traceback.print_exc()