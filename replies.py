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

raccoongirls = ['https://cdn.discordapp.com/attachments/403050477840760832/726040871061159947/15931720134606432984084757995522.jpg',
								'https://cdn.discordapp.com/attachments/403050477840760832/726041020114010132/15931720639413141832262686302986.jpg',
								'https://cdn.discordapp.com/attachments/403050477840760832/726041071607480380/15931720773152536483211048539783.jpg',
								'https://cdn.discordapp.com/attachments/403050477840760832/726043365535252491/15931726181814064672364166463579.jpg',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049710527479808/cf158b93347530c3235c73f90754cf584df85fee.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049726931271710/96bd7b662a7e04a4bcec9d6ecef81d8b7d56e1d1.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049787710930944/f7ac14e54b5dccf25e9669df4d531690dacdbb3a.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049838940028948/6b9d99edb9888dd9ef33a0a81586c32c67b0d13d.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049869059325993/3867e212bc3aa0883e46be83b9c088db44c80f86.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726049961854369802/ec32ffdc91ed11f1d2b362ea2aa7d925eaabd50f.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054032958816356/286acddd6170573a0173018b5c03c02dd6258d17.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054050642001962/3b64b337cce0b9493c7007099550b2e6cbed3d77.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054113934311556/7a78315c3ec554c132bc99bb2ef59709aa346dbc.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054323334938634/5c83b5fea2f6b42e8c6a80f85befda0b2b5e9356.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054351247769710/sample_a8401aeb5fcabf52eff514a71b286cf8e30ab6a8.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726054675735904266/d7589c8641de85226cade8f87122c689e1f640aa.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726055050962665494/90057ce32ee5280b4576e48db734ab02b076bb7b.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726055249168564274/27f3c0902faf744ef1fe6a42fbe50c711e67c1e9.png',
								'https://cdn.discordapp.com/attachments/403050477840760832/726176393125429378/15932043202107317362254804076500.jpg',
								'https://i.imgur.com/IkqHdFD.jpg',
								'https://i.imgur.com/B11yWex.jpg',
								'https://i.imgur.com/zcPyQRs.jpg',
								'https://i.imgur.com/hEXtXhH.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214252477808651/be2520a4a3dd43a599dcca20ca20ac9f.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214253236846612/3f8c6038eaf3d6334e9202dffeb48cf6.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214253467664485/5586ae02fc85da21d98bdd7b9b74b441.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214253782106193/1e445267f648dad8d8c677ce42ab7c98.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214254197342208/f57547d3ac60da03bc8255070608e893.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214254440742912/c67bb7502c41610ad2602e4e18ffc0b4.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214254679818270/e50af791f55520228d236b5ef4585b01.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214255040528464/sample_9b39601a4fe3e94ed2aae88e3f86b643.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214255300313189/b1102d79797c0c644934a4d1b5da87c1.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214285893828680/e2f10ffdd1d284174ea0014b7f5dfcc7.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214286120190003/34606165f9782e5842438ac60c7fc52f.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214286120190003/34606165f9782e5842438ac60c7fc52f.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214286392950834/0df44d598f166f8980a1c5977bb0d8a0.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214286740815872/013f2ca7b1cb0de880c555b5bf434508.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214287202451526/16accefeadf5d088033c00f6bf047dcc.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214287735128154/7bcea9ec1d06ad7e4563646bcb772d39.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214288036855848/a27c521d56899df5d45c7b95cc24723a.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214288372531220/sample_b68f5021cea0a81cd572d6ec9a42c70f.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726214288695492698/8097fc219827228b53bc78edbaac2b5f.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215042160263198/c73c0c8c2629e821ceda2e379129f413.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215042600534026/7aa3c394e3d6e9a4c630e7157dc3103f.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215042944466954/ff5cc6172a7583eb331af20234acf151.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215043208970400/4235d0eb6eb97c9c17c278d0edb1d60a.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215043590520912/5aaae2c4b30866102f34e1460da0bee0.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215043963944970/09217b428245227b8c1c5e331a165fdc.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215044601348123/eaeba7f93630cd9355b70317daffa82f.png',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215044916052119/f7c37dcd4a8d21d47ee628a4086d60c9.jpg',
								'https://cdn.discordapp.com/attachments/406363854633828353/726215045180162109/6eef7e0817bcc4ad908ca9b609153b6c.jpg']

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
											'picture of an usagimimi! Pyon! Hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a catgirl, doggirl, foxgirl, horsegirl, raccoongirl, or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

catgirl_reply = ('[Here](' + random.choice(catgirls) + ') is a '
											'picture of a nekomimi! Nya! Hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, doggirl, foxgirl, horsegirl, raccoongirl, or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

doggirl_reply = ('[Here](' + random.choice(doggirls) + ') is a '
											'picture of an inumimi! Wan Wan! Hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, catgirl, foxgirl, horsegirl, raccoongirl, or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

foxgirl_reply = ('[Here](' + random.choice(foxgirls) + ') is a '
											'picture of a kitsunemimi! Kon Kon! Hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, catgirl, doggirl, horsegirl, raccoongirl, or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

horsegirl_reply = ('[Here](' + random.choice(horsegirls) + ') is a '
											'picture of an umamimi! Hihin! hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, catgirl, doggirl, foxgirl, raccoongirl, or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

raccoongirl_reply = ('[Here](' + random.choice(raccoongirls) + ') is a '
											'picture of a tanukimimi! Dokodon! hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, catgirl, doggirl, foxgirl, horsegirl or wolfgirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

wolfgirl_reply = ('[Here](' + random.choice(wolfgirls) + ') is a '
											'picture of an ookamimi! Awoo! Hopefully this will cheer you up!'
											'\n\n'
											'---'
											'\n\n'
											'Did you want a bunnygirl, catgirl, doggirl, or foxgirl, horsegirl, or raccoongirl? Just reply saying so. '
											'I am a bot. For more info on me and how to use me, see r/KemonomimiCheerUpBot')

replies = [bunnygirl_reply, catgirl_reply, doggirl_reply, foxgirl_reply, horsegirl_reply, wolfgirl_reply]

all_reply = ('Here is an [usagimimi](' + random.choice(bunnygirls) + 
											'), a [nekomimi](' + random.choice(catgirls) +
											'), an [inumimi](' + random.choice(doggirls) +
											'), a [kitsunemimi](' + random.choice(foxgirls) +
											'), an [umamimi](' + random.choice(horsegirls) +
											'), a [tanukimimi](' + random.choice(raccoongirls) + '), **AND** '
											'an [ookamimi](' + random.choice(wolfgirls) + ')!! '
											'Hopefully this will cheer you up more!')