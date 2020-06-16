import random

##list of images to be used in the replies
bunnygirls = ['https://cdn.discordapp.com/attachments/403050477840760832/413458140458385408/ru_Sou_Desu_yo_340247.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413457856801538054/1_latest.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413457877689171971/2_latest.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413457914691321856/6gzfvdbqb2hs7kjbrq_hq.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413457917090725890/8ttyFKd91qdwdrto1_500.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458000569958401/69093ba1c9c1d7ab99_hq.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458031003828234/D4c94xF.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458048498008065/e8877996b05cd6e5d8436.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458071176740864/iji_tachi_bunny_girls.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458087199113228/Konachan.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413458140458385408/ru_Sou_Desu_yo_340247.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/491832290486386728/IMG_20180918_234543.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/491447094218063883/image0.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/491100453640339456/drawn_by_citemer__sample-60807551b6ce813e66c8c2f249662cad.jpg',
              'https://imgur.com/ckPNxx1',
              'https://imgur.com/RWBmr6v',
              'https://imgur.com/GXjtsas',
              'https://imgur.com/VjpeXyt',
              'https://imgur.com/PzYkyTS']

catgirls = ['https://imgur.com/RGHKirG',
              'https://imgur.com/4A8CrDC',
              'https://imgur.com/G2Gyey2',
              'https://imgur.com/qs2AsLP',
              'https://imgur.com/V7GvM1z',
              'https://imgur.com/qfKMtrJ',
              'https://imgur.com/N3ALJOP',
              'https://imgur.com/uYg52N9',
              'https://imgur.com/u08q7Ku',
              'https://imgur.com/nZpL1pS',
              'https://imgur.com/jERVdaS',
              'https://imgur.com/Juqb6Nn',
              'https://imgur.com/AWQtq0A',
              'https://imgur.com/6yWLbfW',
              'https://imgur.com/FUZR8jq',
              'https://imgur.com/Zvv6Rsl',
              'https://imgur.com/T2hlBUm',
              'https://imgur.com/aA4eh60',
              'https://imgur.com/wtEzFLu',
              'https://imgur.com/E9xp31c',
              'https://imgur.com/RcrLkpe',
              'https://imgur.com/xjJHi0B',
              'https://imgur.com/HCJZnpi',
              'https://cdn.discordapp.com/attachments/403050507310202881/429057255028031500/61573291_p0.jpg',
              'https://cdn.discordapp.com/attachments/403050507310202881/432228224416743434/qtnb.png',
              'https://cdn.discordapp.com/attachments/403050507310202881/438638109249241108/28616770_2134594886752623_5299159988306267350_o.jpg',
              'https://cdn.discordapp.com/attachments/403050507310202881/446312004026892289/C3IkNvKXAAEpc1G.png',
              'https://cdn.discordapp.com/attachments/403050507310202881/471843681712996352/image.jpg',
              'https://i.imgur.com/uWQiXcE.jpg',
              'https://i.redd.it/gughqaz7h5a11.png',
              'https://cdn.discordapp.com/attachments/403050507310202881/468025754958168064/131jr.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/492380917948481537/images_4.jpeg',
              'https://i.imgur.com/DC7ZuRK.png',
              'https://cdn.awwni.me/13zas.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/491203612555345950/67902372_p0_master1200.png']

doggirls = ['https://cdn.discordapp.com/attachments/403050477840760832/413456405190803457/10emo.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456419652894732/10e73.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456444956868610/3226c591b6027a3c11f7d.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456472106860567/50387458_p0.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456484035330058/50635124_p0.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456485876760577/50725896_p0.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456493644480522/50776026_p0.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456534690070540/bece86c30fbb7e1b2ab7f.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456546555625492/by_envysmercy_d4jbj5j.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456568261279746/gffs5AFK1r4vymlo1_500.gif',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456578126282782/inu___yudachi.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456582798475274/Koya.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456631544938506/ulmJGGj.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/413456637907566592/unknown.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/491293016179474443/Coyote.png',
              'https://imgur.com/AUAWMqb',
              'https://imgur.com/jGxRM4T',
              'https://imgur.com/2h13izO',
              'https://imgur.com/DYI95CK',
              'https://imgur.com/2VSdPJU',
              'https://cdn.discordapp.com/attachments/403050497898184707/464642758909624320/66651189_p0_master1200.png',]

horsegirls = ['https://imgur.com/1CqzgSv',
                'https://imgur.com/3QH5jrf',
                'https://imgur.com/Oo5wr5A',
                'https://imgur.com/QCkGuEd',
                'https://imgur.com/Zo7ajyb',
                'https://imgur.com/MDl4h79',
                'https://imgur.com/ohgI6Hp',
                'https://imgur.com/BNItYCx',
                'https://imgur.com/OYsMnzO',
                'https://imgur.com/JdEVtoF',
                'https://imgur.com/pfQSfZo',
                'https://imgur.com/TmG43mJ',
                'https://imgur.com/htzSkKt',
                'https://imgur.com/xQecv9u',
                'https://imgur.com/fJytgLU']

nanachis = ['https://imgur.com/IN98eXb',
              'https://imgur.com/aO5TuhD',
              'https://imgur.com/TiMzW1y',
              'https://imgur.com/sxcGpBv',
              'https://imgur.com/MlDXYgS',
              'https://imgur.com/jdZfTaH',
              'https://imgur.com/cRVqWuI',
              'https://imgur.com/H9YyFfE',
              'https://imgur.com/sxcGpBv']

foxgirls = ['https://imgur.com/H4mguan',
              'https://imgur.com/lhjxG60',
              'https://imgur.com/hau9PTd',
              'https://imgur.com/rgLbadq',
              'https://imgur.com/sUocz2T',
              'https://imgur.com/2643a1Y',
              'https://imgur.com/9FxgRTT',
              'https://imgur.com/UEqXI5X',
              'https://imgur.com/WuFNzjy',
              'https://imgur.com/J0ZHuja',
              'https://cdn.discordapp.com/attachments/403050532740005891/412624561226514432/g41_girls_frontline_drawn_by_marmoset_marmoset0__598c2fc6dddaf5d0358314f5aea30bce.jpg',
              'https://cdn.discordapp.com/attachments/403050532740005891/417119208128643082/eaa3b8ea85328ff4458211f9e620ed50.png',
              'https://cdn.discordapp.com/attachments/403050532740005891/417187924119912448/VxGXzkMuD.png',
              'https://cdn.discordapp.com/attachments/403050532740005891/425442989637107722/c92aab218a5e4eec2c618c8f4d045a3a.png',
              'https://i.imgur.com/mYjHNYp.png',
              'https://cdn.discordapp.com/attachments/403050532740005891/462705692986310671/IMG_20180630_203717.jpg',
              'https://cdn.discordapp.com/attachments/403050532740005891/462978096409083915/69490327_p0.jpg',
              'https://cdn.discordapp.com/attachments/403050532740005891/470318680987926530/Kiyomi20Bed.png',
              'https://cdn.discordapp.com/attachments/403050532740005891/467585759315099658/59529325_p0.jpg',
              'https://cdn.discordapp.com/attachments/403050532740005891/467547897718636544/d2177023719f3a9c27fd6dc13737832698588098.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/491211966040506378/59529325_p0.png',
              'https://cdn.discordapp.com/attachments/403050477840760832/492840953850101790/68392672_-_06.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/492840797104898071/68392672_-_09.jpg',
              'https://i.imgur.com/HR3PeJo.png',
              'http://cdn.awwni.me/1409o.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/491800635457667073/image2_1.jpg']

wolfgirls = ['https://imgur.com/Ve9anbO',
              'https://imgur.com/ny8Npgt',
              'https://imgur.com/dWxMXOU',
              'https://imgur.com/xWAFh3X',
              'https://cdn.discordapp.com/attachments/403050497898184707/418157616750133259/1510929002.jpg',
              'https://cdn.discordapp.com/attachments/403050497898184707/423199511532404736/inubashiri_momiji_touhou_and_yozakura_quartet__57af3ff4d792d19659e154c28f47cc17.gif',
              'https://cdn.discordapp.com/attachments/403050497898184707/423380534501048320/15388ca18d359286250c5452ab33a317.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/422061141590540299/0aB3OUH.jpg',
              'https://cdn.discordapp.com/attachments/403050497898184707/471318562624241675/doomguy_and_imaizumi_kagerou_doom_game_and_touhou_drawn_by_majormilk__923f473b2a5bbb3de17cb45b31deb4.png',
              'https://i.imgur.com/rT4ekQf.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/469958736753197057/IOpSwSE.jpg',
              'https://i.imgur.com/cyGMoSc.png',
              'https://cdn.weeb.sh/images/B1yvBbLYW.gif',
              'https://cdn.discordapp.com/attachments/403050497898184707/466991639664263178/8edabc40082239adbb5d9cfa772ec028c6f4fb45.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/466981292442124288/4c8b8c1a4f905d241ab4188fa37599d20963c864.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/466276068693770251/41419802_p0_master1200.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/466136173283115009/XEFeVIm5JZc-1.jpg',
              'https://cdn.discordapp.com/attachments/403050497898184707/464430222675148800/geqkmuw600o01.png',
              'https://cdn.discordapp.com/attachments/403050497898184707/403318691225141248/03c07b6ac5cc7a8e5a52ac2452d33abf.jpg',
              'https://cdn.discordapp.com/attachments/403050497898184707/403319821934133248/ookami_-_holo_takeover.jpg',
              'https://cdn.discordapp.com/attachments/403050497898184707/403319872345473044/sample_9b210b968c6abb53e90d842f3152cd40.jpg',
              'https://cdn.discordapp.com/attachments/403050477840760832/491159472501293056/58fef20c66c70f8d872183dce500f9bc.png']

##the replies themselves
bunnygirl_reply = ('[Here](' + random.choice(bunnygirls) + ') is a '
                      'picture of a bunnygirl! Pyon! Hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a catgirl, doggirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

catgirl_reply = ('[Here](' + random.choice(catgirls) + ') is a '
                      'picture of a catgirl! Nya! Hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a bunnygirl, doggirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

doggirl_reply = ('[Here](' + random.choice(doggirls) + ') is a '
                      'picture of a doggirl! Wan Wan! Hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a bunnygirl, catgirl, foxgirl, horsegirl, or wolfgirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

foxgirl_reply = ('[Here](' + random.choice(foxgirls) + ') is a '
                      'picture of a foxgirl! Kon Kon! Hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a bunnygirl, catgirl, doggirl, horsegirl, or wolfgirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

horsegirl_reply = ('[Here](' + random.choice(horsegirls) + ') is a '
                      'picture of a horsegirl! Hihin! hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a bunnygirl, catgirl, doggirl, foxgirl, or wolfgirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

humangirl_reply = ('What kind of heretic are you? Kemonomimi are clearly superior to humans!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want an actual kemonomimi girl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

wolfgirl_reply = ('[Here](' + random.choice(wolfgirls) + ') is a '
                      'picture of a wolfgirl! Awoo! Hopefully this will cheer you up!'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Want an endless supply of kemonomimi girls? '
                      'We have them [here](https://discord.gg/GtETtcW)'
                      '\n\n'
                      '---'
                      '\n\n'
                      'Did you want a bunnygirl, catgirl, doggirl, or foxgirl, or horsegirl? Just reply saying so. '
                      'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

replies = [bunnygirl_reply, catgirl_reply, doggirl_reply, foxgirl_reply, horsegirl_reply, wolfgirl_reply]

all_reply = ('Here is a [bunnygirl](' + random.choice(bunnygirls) + 
                      '), a [catgirl](' + random.choice(catgirls) +
                      '), a [doggirl](' + random.choice(doggirls) +
                      '), a [foxgirl](' + random.choice(foxgirls) +
                      '), a [horsegirl](' + random.choice(horsegirls) + '), **AND** '
                      'a [wolfgirl](' + random.choice(wolfgirls) + ')!! '
                      'Hopefully this will cheer you up more!')