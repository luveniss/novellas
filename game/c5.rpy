

label main5:
    scene bg sky afternoon with fade
    "Getting Nerith's badge in time for the convention is a hassle-and-a-half, but we manage it somehow."
    scene bg convention with fade
    play music "audio/music/Thinking Music.mp3"
    "The look of utter amazement on her face when we walk in is even worth the exorbitant price... almost."
    scene bg convention blur
    show nerith huh
    with dissolve
    voice "audio/voices/ner/146.ogg"
    ner "Holy shit, is that the Demogorgon just walking around?"
    "Her eyes actually, physically bug out of her head slightly."
    voice "audio/voices/ner/147.ogg"
    ner "... And what is a Knight of Sparrowkeep doing, calmly chatting him up?! Those goody-goody, shield-wearing twats give ME a hard time!"
    show nerith spell with dissolve
    hik "What are you {i}doing{/i}?!"
    "Nerith pauses with her fingers halfway through a spell-weaving and curses loud enough to attract attention when the magic fizzles."
    "She turns to glare at me before faltering at the expression on my face. Her angry retort comes out sounding more like a question."
    show nerith pissed with dissolve
    voice "audio/voices/ner/148.ogg"
    ner "Killing and looting?"
    hik "You can't-- Just... {i}no{/i}!"
    hik "Look, these are people in costumes. Remember when I explained what 'cosplayers' were?"
    show nerith huh with dissolve
    voice "audio/voices/ner/149.ogg"
    ner "Oh... so these are real ones?"
    hik "Yes."
    voice "audio/voices/ner/150.ogg"
    ner "So that means I won't get any XP for slaying them?"
    hik "You will not gain any XP from going on a mass-murdering spree, no."
    show nerith meh with dissolve
    voice "audio/voices/ner/151.ogg"
    ner "Oh."
    "Her look of disappointment says it all, really."
    "I take the homicidal elf with me toward the nearest information kiosk to pick up a map of the convention center."
    "On the way, we're stopped several times by desperate {i}Celestial Crossing{/i} fanboys who want to pose in pictures with Nerith."
    "They fall all over themselves complimenting her amazingly accurate and... resourceful cosplay."
    voice "audio/voices/ner/152.ogg"
    ner "The next fool that comes up to us wanting to flash some bright-ass light in my eyes gets punched in the face, Useless."
    voice "audio/voices/ner/153.ogg"
    ner "Fair warning."
    "I note the tense set of her shoulders and how her glower has evolved into something that looks worryingly unstable."
    "It's a complete turn-around from the wide-eyed awe she expressed earlier, and I try to phrase my concern carefully."
    hik "I didn't think it would bother you so much... You've had to deal with worse at school, haven't you?"
    voice "audio/voices/ner/154.ogg"
    ner "That was nothing like this..."
    "She mutters her answer sourly, but before I can answer, a girl dressed as a dark-elf comes barreling toward us and gushes over how natural Nerith's body-paint looks compared to hers."
    "It isn't until she asks what the warlock used to make her ears that the pieces click together in my head."
    show nerith pissed with dissolve
    "The muscles in Nerith's arms suddenly flex, as if she means to take a swing at the shorter girl..."
    "... who, by some miracle, realizes that she might be in danger, and stops talking abruptly."
    "The girl shoots me a nervous look, especially when the real-life elf in front of her begins to tremble slightly."
    hik "Haha... I think my friend here is just thirsty. We're going to go hunt down a vending machine. Excuse us!"
    scene bg convention with dissolve
    "I take Nerith's arm and guide her toward the section of the building where I know the game's panel is being held."
    "I'm breathing slightly harder than usual by the time we reach the room and turn to face her, fully expecting to have my head bitten off."
    "Instead, I'm greeted by the most shocking thing I've seen since..."
    stop music fadeout 3.0
    "Well, since a half-naked elven warlock dropped in my lap."
    scene bg convention blur
    show nerith huh
    with dissolve
    "Nerith looks... upset, and not in her usual rage-fueled way."
    "Her eyes are shut tight, as if to desperately block everyone and everything else out."
    "Her hands are even clutching over her ears in a gesture so disturbingly vulnerable that I hear myself talking to her in a low voice, the way one might speak to a cornered animal."
    hik "Nerith? Are you okay?"
    hik "This isn't just about the crowds, is it?"
    "Her eyes pop open and find mine immediately, looking angry and just a little bit frightened."
    play music "audio/music/Heartbreaking.mp3"
    show nerith pissed with dissolve
    voice "audio/voices/ner/155.ogg"
    ner "What the hell do you want me to say?"
    show nerith meh with dissolve
    voice "audio/voices/ner/156.ogg"
    ner "That you were right, and my world has always been a..."
    show nerith huh with dissolve
    voice "audio/voices/ner/157.ogg"
    ner "... A stupid fucking illusion created by other Useless people like {i}you{/i}?"
    "She spits the word 'you' out like it's a curse, but her gaze isn't on me any more. Instead, she's scowling up at a decorative banner from the game taking up most of the wall behind us."
    "Moodily, she crosses her arms in front of her and keeps staring over my shoulder."
    voice "audio/voices/ner/158.ogg"
    ner "I know that I don't fit into your world very well, and you've always been really aware of the fact that I don't belong here because of it..."
    voice "audio/voices/ner/159.ogg"
    ner "... But to me, this just felt like another raid."
    show nerith disapointed with dissolve
    voice "audio/voices/ner/160.ogg"
    ner "A weird, mostly boring one, but seeing these idiots dressed up like archdemons and mages, like it's nothing..."
    "She shakes her head despondently, facial features turning sad."
    show nerith pissed with dissolve
    voice "audio/voices/ner/161.ogg"
    ner "Those clothes MEAN something in my world..."
    scene overlay black with fade
    "Her eyes turn upward and she stares hard at the ceiling tiles over her head."
    "It takes me a long minute to realize that Nerith - tough, bad-ass Nerith - is trying not to cry..."
    scene cg closeup with fade
    voice "audio/voices/ner/162.ogg"
    ner "Hikaru, am I real?"
    "Her voice is small; smaller than I've ever heard it, and for a moment, I'm not sure what to say."
    "I have a feeling that this is a very important question to Nerith, and I have to take my time thinking of an answer..."

menu:
    "Tell her that she is not real.":
        $ nerithReal = False
        jump notreal
    "Explain that she is real.":

        $ nerithReal = True
        jump arereal

label notreal:
    "As much as it pains me to admit it, there really is only one correct answer."
    "Nerith might not want to hear the truth, but it doesn't feel right to try and sugar-coat or lie, either."
    hik "You aren't real, Nerith... but that's okay, right?"
    hik "We'll be getting you back to your world soon, and it won't matter what you mean to a bunch of idiot humans like me..."
    "Her lip gives a half-hearted twitch, and I take that as a victory."

    jump main5_1

label arereal:
    "I hesitate, because the truth is... I honestly don't know, and I don't feel at all qualified to be helping her through this existential crisis of hers."
    "There's no straight-forward answer, so I decide to go with pure gut instinct."
    hik "You're living and breathing and standing right next to me, so as far as I'm concerned..."
    hik "You're definitely real, Nerith. Screw what anyone else says."
    "I offer her a weak smile, hoping that my words didn't make an already bad situation worse."
    "Nerith looks at me with a mixture of annoyance and affection that only {i}she{/i} could ever pull off."

    jump main5_1

label main5_1:
    scene bg convention with fade
    "She's spared having to voice a reply as the line finally starts moving ahead of us and we're let into the panel room."
    "We take seats as far up front as we can manage, which isn't all that far, honestly."
    "The panel turns out to be more of an extended Q and A session than anything else."
    "I wait for my chance, and when the game devs open up the discussion to their audience, my hand shoots into the air before anyone else's."
    "Naturally, I'm ignored in favor of a cute blonde cosplaying as a succubus..."
    "The rest of the panel goes by like this."
    "I raise my hand, but I'm still just one person out of a hundred."
    "I shoot a pointed look over at Nerith, hoping she can throw a little bit of her magic around, but she isn't paying much attention."
    "She's slouched in her chair, staring at the back of the head of the guy in front of her and looking pretty perturbed."
    "Her concerns from earlier are clearly still bothering her."

menu:
    "Try and comfort your friend.":
        jump attemptedcomfort
    "Continue to try getting your question answered.":

        jump didnotcomfort

label attemptedcomfort:
    "I lower my arm and gently poke her in the side."
    hik "You okay?"
    "Her face immediately twists into a snarl and she opens her mouth to unleash a torrent of verbal abuse..."
    "... before pausing, obviously thinking better of it."
    "She looks up at the ceiling again for a moment and I feel like shit for saying anything at all."
    "She's clearly NOT okay."
    voice "audio/voices/ner/163.ogg"
    ner "I'll be fine once we talk to these idiots and get out of here."
    "Her voice is strained, but quiet."
    "I rack my brain for something else to say, but she shoots me a look out of the corner of her eye that says something along the lines of, \"drop it, or else.\""
    "I nod silently, waiting until the next call for questions before raising my hand again."
    "I probably should have known better, anyway..."
    "Nerith has only ever interacted with me on her own terms, now that I think about it."
    "She's fine with me comforting her when it's {i}her{/i} turning to {i}me{/i}, but apparently my offering it is a step too far."
    "As much as we've been through together, the fact that we've only known each other for a few weeks has never been more clear."
    "With that in mind, I realize that the best way to support her at this point is to just focus on getting the job we came here for, done."
    jump main5_2

label didnotcomfort:
    "I sigh, deciding to keep my hand in the air."
    "Because let's be honest: I suck at talking to people, and Nerith is an insanely difficult person to talk to on a {i}good{/i} day."
    "I don't have a clue how to comfort a depressed, angst-filled version of her."
    "The odds of me screwing up and saying something to make the situation worse are high."
    "It's much more productive of me to stay focused on the task at hand, anyway..."
    "... Or so I tell myself as I try to ignore the visibly upset elf sitting beside me for the next hour."
    jump main5_2

label main5_2:
    stop music fadeout 3.0
    "Sixty agonizing minutes later, the Q and A comes to an end."
    "Fuck."
    "I lower my arm in defeat, trying to shake some life back into my numb fingers."
    hik "What the hell do we do now?"
    "I fully expect Nerith to make some sassy comment on how I can't get anything done, but instead she simply scrunches her nose in irritation before getting out of her seat and making a beeline for the backstage exit."
    "It's all I can do to scramble after her."
    "We reach the edge of the stage, fighting our way through a crowd of people moving in the opposite direction, before we're stopped by security."
    "So close!"
    "We're literally only a few feet away from the developers..."
    "But Nerith is evidently done with all of the tomfoolery."
    scene bg convention blur
    show nerith spell
    with dissolve
    "Her hands fly through the motions of a now-familiar spell. She murmurs a low incantation, and this time, I can actually {i}taste{/i} the electricity in the air."
    "It's like licking a battery... Not that I've ever done that."
    "The developers and security guards all freeze what they're doing, eyes glazed over."
    "We're able to walk right up to them without further trouble and I glance around nervously to make sure everyone else is out of earshot."
    play music "audio/music/Thinking Music.mp3"
    hik "Er... hello. We... uh. Had a question for you that--"
    show nerith disapointed with dissolve
    voice "audio/voices/ner/164.ogg"
    ner "Is it possible for a gateway to open between this world and the world of the--"
    "She cuts herself off, struggling to say the word, and I take pity on her."
    hik "Game?"
    "The devs are obviously not so far out of it that they don't immediately start laughing at us."
    show bob normal at left with moveinleft
    voice "audio/voices/dev/1.ogg"
    dev "What are you guys talking about? There's no such... Ahahaha... I mean, you guys know this shit isn't real, right?"
    show nerith huh with dissolve
    "Nerith stiffens and even I flinch at the harsh words."
    show nerith pissed with dissolve
    "As if the elf wasn't already questioning her existence... This was the verbal equivalent of pushing a burn victim into a hot bath."
    "A very hot bath."
    hide nerith with moveoutright
    "Nerith turns on her heel and marches away, leaving me to deal with the brainwashed devs on my own."
    "Luckily, the spell doesn't wear off immediately."
    show bob normal at center with moveinleft
    "Sadly, however, I now have to worry about finishing up this discussion quickly, since there's no telling what kind of trouble a distressed elven warlock can get up to at a gaming convention."
    hik "Uh, there's magic within the game itself that opens doors to different dimensions, so is it really such a dumb question?"
    hik "Get a high enough level magic user and they can even get to different planes of existence, right?"
    hik "So... in actuality... did one of you... er... stumble onto a gap in time and space...? And turn it into a game?"
    hik "Maybe?"
    "My voice fades out at how stupid I sound."
    "This was the king of idiotic ideas..."
    "The grand poo-bah of embarrassing moments."
    hik "And please answer without laughing."
    "Obediently, the developing team holds in its mirth and they shake their heads, one-by-one."
    voice "audio/voices/dev/2.ogg"
    dev "No way, kid. {i}Celestial Crossing{/i} is just something we made up. It's completely fictional."
    "My shoulders slump, and I play my riskiest card out of desperation."
    "Hopefully they don't remember this conversation when the spell wears off."
    hik "Okay, well is there anything else you can think of that might explain how a character from the game could, theoretically!, get over into the real world?"
    "With amused expressions, the devs look at each other and shrug."
    "I wilt in disappointment until one of them appears to entertain the idea for a second longer than the others."
    show bob think with dissolve
    voice "audio/voices/dev/3.ogg"
    dev "Well, if we're talking about keeping this within the realm of fantasy..."
    hik "Yes...?"
    voice "audio/voices/dev/4.ogg"
    dev "And fiction..."
    hik "Right...?"
    "I impatiently try to draw the words out of him faster, wanting to go check on Nerith, but also needing something, ANYTHING, to show for our efforts today."
    voice "audio/voices/dev/5.ogg"
    dev "Well, our magic system in the game is pretty complex, but {i}in theory{/i} any spell can be reversed under similar conditions."
    show bob smile with dissolve
    voice "audio/voices/dev/6.ogg"
    dev "That's why shield spells and spell-breaches take the same number of turns, and are learned under the same school of magic."
    "The lead developer shrugs and smiles, and I realize he's making all of this up on the spot."
    "Still, it does makes sense... and it's more information than we had."
    hik "Got it. And, uh, thanks for answering my question."
    hik "Big fan, by the way."
    voice "audio/voices/dev/7.ogg"
    dev "Yeah, we kind of figured."
    "I turn to go, feeling hopeful that maybe this whole enterprise wasn't a {i}complete{/i} waste of time."
    "I'm in such a hurry to find Nerith that I almost miss their parting words as I duck toward the exit."
    show bob think with dissolve
    voice "audio/voices/dev/8.ogg"
    dev "If you think of the portal between worlds as a door, then it probably opens both ways, kid! That's the best answer I can come up with without a fresh coffee!"
    scene bg convention with dissolve
    "I mull over this imagery with more seriousness than it probably deserves before mentally storing it away for later."
    "First, I need to make sure Nerith didn't go on some kind of rampage."
    "I scan the hallways outside the panel room, but the area is thick with gamers and nerds as far as the eye can see."
    stop music fadeout 3.0
    "Finally, I decide to make my way over to the information kiosk, hoping that Nerith might remember it and return if she gets lost."
    "I only make it about halfway when I nearly collide with the woman herself."
    scene bg convention blur
    show nerith laugh
    with dissolve
    play music "audio/music/Marty Gots a Plan.mp3"
    voice "audio/voices/ner/165.ogg"
    ner "Oh good, I found you. Look what I got!"
    "She proceeds to shove several large convenience store bags full of yakisoba bread into my arms."
    "... the hell?"
    voice "audio/voices/ner/166.ogg"
    ner "Yeah, there was this stupid contest or something, and they really loved my armor, because really, who wouldn't?"
    show nerith smirk with dissolve
    voice "audio/voices/ner/167.ogg"
    ner "And then they offered me some useless prize."
    "I repeat her words dumbly, a bad feeling rising in the back of my mind."
    hik "A \"useless\" prize, you said?"
    show nerith meh with dissolve
    voice "audio/voices/ner/168.ogg"
    ner "It was some of that flimsy paper currency you're always whining about. 60,000 yen, or something like that?"
    hik "{i}60,000 yen?{/i} You walked away from..."
    show nerith laugh with dissolve
    voice "audio/voices/ner/169.ogg"
    ner "Of course not! I just waved my fingers, threw a little magic at them, and convinced them to award me something USEFUL instead."
    "She waves one of the bags in front of my face in a tempting manner, smirking with victory."
    show nerith smirk with dissolve
    voice "audio/voices/ner/170.ogg"
    ner "You're welcome."
    "Nerith spends the next few minutes trying to get a response out of me... I think."
    "I'm not sure what happens next, to be honest, as I more or less pass out at the thought of Nerith {i}turning down{/i} free money."
    "Free money that I could have used to fix all the shit she broke in my house..."
    "Still... at least she doesn't seem depressed anymore, triumphantly nibbling on one of her prizes."
    scene overlay black with fade
    "Once I'm finally recovered enough to re-join the world of the living, I lead us out of the crowded convention center and toward the bus stop where we catch the last one heading back to the apartments."
    "We pay our fare and share a seat toward the back."
    stop music fadeout 3.0
    scene bg sky dusk with fade
    "I spend the ride home thinking about what the developers said."
    "It was all just random stuff that they made up on the spot, but I try to consider it from the viewpoint that EVERYTHING about the past few weeks has been batshit insane."
    "Why stop suspending my disbelief now?"
    play music "audio/music/Montauk Point.mp3"
    "So with that in mind..."
    "A door... The doorway in-between Nerith's world and mine was a dream the first time, wasn't it?"
    "I mean, I was asleep at the time and woke up with her suddenly there..."
    "But I had slept every single night {i}since{/i} then, and nothing had happened."
    "Maybe I have to dream her away for it to actually work?"
    "Maybe... but who can control what they dream about?"
    "I glance over at Nerith, who is already fast asleep, leaning her head against the window."
    "Would she laugh in my face if I told her what I was thinking about, or just smack the back of my head and tell me to stop wasting my time thinking of nonsense?"
    "Hell, what if it all WAS just nonsense?"
    "And if it was, would having Nerith around for the foreseeable future really be that awful?"


    if brave == True:
        "I'm almost surprised to realize that... no, it really wouldn't be that bad."
        "Nerith's a pain in the ass, sure."
        "But I've always wanted to change things around in my life, be tougher; stronger as a person, and she's been the only one who could FORCE me to do that."
        "Mostly because she's a hard-ass, but also because I think of her as a friend... crazy as it sounds, even in my head."
        "And as much as she's helped me, I feel like I've helped her too."
        "A week ago it wouldn't have been possible for her to show any kind of weakness around me."
        "Today though, she reached out."
        "She asked me if she was real... and my answer actually {i}mattered{/i} to her."
        "I can't help wanting more of that. To watch her become more grounded and able to rely on me."
        "To see that I'm someone she can trust to have her back the way she's had mine."
        "So, no..."
        "It wouldn't be horrible to have my friend hang around a while longer."
        jump main5_3


    if brave == False:
        "... Yes... yes, it would."
        "Aside from the obvious complication of her being an unapologetic {i}bitch{/i}, there's also the logistics of the situation to consider."
        "How the hell am I going to explain her to my dad?"
        "Is she going to be able to make it on her own in the world, or will I be stuck living with her for the rest of my life...?"
        "I feel my blood pressure rise at the thought of the future looming ahead of me..."
        "A future filled with yakisoba bread, violent wake-up calls, and no dates, {i}ever{/i}, because what sane girl would date a guy living with a super-tall cosplayer who refuses to wear pants?"
        "Feeling more drained than ever, I push all of those thoughts aside for now..."
        "They aren't helping anything but my potential for going prematurely bald."
        jump main5_3

label main5_3:
    stop music fadeout 3.0
    "A yawn rises up out of my chest, suddenly."
    scene overlay black with fade
    "All of this thinking reminds me that we've had a long day. I'm pretty exhausted, physically and mentally."
    "I settle in for a short nap until we reach the apartment, resting my head against the back of my seat."
    "The bus lists to one side as we make a sharp turn and my head lolls onto Nerith's shoulder."
    "She grunts, but doesn't wake up to punch me in the face, so I stay there."
    "It's a much comfier position to sleep in than trying to keep my neck craned upward."
    "As I drift off, I reason that I'll be able to process the day's events much more easily when I wake up, anyway."


    play music "audio/music/Thunder Dreams.mp3"
    "Something feels off about this..."
    "I'm very obviously dreaming, but I've never been {i}aware{/i} that I'm dreaming without waking up before."
    "There's nothing but darkness around me."
    "Darkness and a dim outline of... something... in the distance."
    "When no other choice presents itself, I make my way toward the shape ahead."
    "As I get closer, it split into two, and I can soon make out the form of a woman standing next to..."
    scene bg door with dissolve
    hik "A door..."
    voice "audio/voices/ner/171.ogg"
    ner "About time you showed up, Useless!"
    "I'd recognize that voice in my sleep..."
    "I mean obviously."
    "Because I just recognized it..."
    "I finally reach the door, and the person standing next to it is, indeed, Nerith."



    if nerithReal == True:
        if brave == True:
            show nerith smirk at right with dissolve
            "She grins."
            voice "audio/voices/ner/172.ogg"
            ner "Well, I didn't think you'd be able to un-fuck yourself long enough to do it, but you managed to impress me, Hero."
            voice "audio/voices/ner/173.ogg"
            ner "You found the doorway."
            "I look at her with my brow furrowed and realize... I don't want her to go..."
            "Still, it's not like she'd leave her entire world behind to hang out in mine."
            "I'd rather chew sand than ask her to do that."
            "Instead I shoot for nonchalance."
            hik "So you're heading back home, then?"
            "She laughs loudly. Her whole face brightens up and it's the happiest I've ever seen the elf."
            voice "audio/voices/ner/174.ogg"
            ner "No need to give me that kicked-puppy look!"
            "Her expression settles into it's usual arrogant smirk and she even gives me a playful punch in the shoulder."
            show nerith smile with dissolve
            voice "audio/voices/ner/175.ogg"
            ner "If I leave, who's going to keep your head out of your ass?"
            voice "audio/voices/ner/176.ogg"
            ner "You think I'd let all of that self-confidence I drilled into you just disintegrate the minute I'm gone?"
            show nerith smirk with dissolve
            voice "audio/voices/ner/177.ogg"
            ner "Fuck that."
            voice "audio/voices/ner/178.ogg"
            ner "I'm just here to make sure we close this stupid door for good so nothing else can get through."
            hik "But... What about your life? Your whole world...?"
            voice "audio/voices/ner/179.ogg"
            ner "You mean my fake life in a pretend world?"
            voice "audio/voices/ner/180.ogg"
            ner "Why go back when I'm a real person here?"
            "I'm dumbfounded that my words had such an impact on her."
            "I gape for a minute before she snaps her fingers in front of my eyes impatiently."
            show nerith smile with dissolve
            voice "audio/voices/ner/181.ogg"
            ner "Since you're here, care to do the honors?"
            hide nerith with dissolve
            "She gestures toward the door, which is starting to glow around the edges, almost like it's beckoning us through."
            "Creeped out, I shut it tight and throw the latch that appears on the outside."
            scene overlay black with fade
            "The moment it locks..."
            stop music fadeout 3.0
            "... I feel a light smack on the top of my head and jolt awake."
            scene bg sky dusk with fade
            voice "audio/voices/ner/182.ogg"
            ner "We're home, Useless. Get your fat head off me."
            "Despite her less than gentle wake-up, she's smiling. I grin back and we make our way off the bus."
            play music "audio/music/Luminous Rain.mp3"
            "The bus-stop is otherwise pretty much deserted, except for a figure making its way toward us in the dark."
            "I lead the way forward only to bump, almost literally, into Mika."
            scene cg bus full with fade
            voice "audio/voices/mik/88.ogg"
            mik "Hikaru! Nerith-chan! Fancy meeting you two here."
            "She laughs a bit, giving Nerith a small wave before looking up at me."
            "I might be imagining it, but she seems to be fidgeting more than usual, playing with the hem of her skirt and pushing strands of hair out of her face as she talks."
            voice "audio/voices/mik/89.ogg"
            mik "Since you're here, I was wondering if you could grab the dishes I lent you guys the other day when I brought food...?"
            "I open my mouth, but Nerith abruptly speaks over me."
            voice "audio/voices/ner/183.ogg"
            ner "No problem, I'll run ahead and grab them."
            "She gives me a very pointed look as I dig in my pocket for the key to give her."
            "The look clearly says: \"Don't fuck this up.\""
            "I try to nod my understanding at her discreetly and she smirks, punching my shoulder once before turning toward the apartment in the dark."
            scene cg bus noNerith with dissolve
            voice "audio/voices/mik/90.ogg"
            mik "Does she always do that?"
            hik "Pretty much."
            "Mika and I walk toward the building a few steps, before my hand shoots out, almost of its own accord, to stop her."
            hik "Mika-chan, wait."
            "She turns to face me, and her face is illuminated in the light of a nearby streetlamp."
            "She's beautiful."
            "Her eyes are wide and warm and there's definitely affection there."
            "Is there also a glimmer, of attraction?"
            "It's hard to tell, and I'm no expert on women... but after everything else I've been through, this finally feels like something I can take a chance on."
            "I take a deep breath and call on all of the self-confidence I've gathered from going through such a life-changing ordeal..."
            hik "Mika-chan, there's something I need to tell you."
            "She says nothing."
            scene cg bus close with dissolve
            "Instead, her cheeks light up softly with a blush and her smile turns shy and hopeful."
            python:
                achievement.grant("Home")
            scene overlay black with fade
            $ overriding_on=True
            show text "{font=images/assets/YanoneTagesschrift.ttf}{size=+12}Ending number 1: Home{/size}{/font}" at truecenter


            with dissolve
            $ renpy.pause(6.0, hard='True')
            hide text
            jump the_end


        if brave == False:
            show nerith smirk at right with dissolve
            "She grins."
            show nerith smirk at right with dissolve
            voice "audio/voices/ner/184.ogg"
            ner "Well, I didn't think you'd be able to un-fuck yourself long enough to do it, but you managed to impress me, Hero."
            voice "audio/voices/ner/185.ogg"
            ner "You found the doorway."
            "I guess I did, since we're presumably in my dream, but I don't really feel like I've accomplished anything."
            "All I did was fall asleep."
            hik "Why do you think it worked THIS time and not any other time I've fallen asleep?"
            "Nerith gives a careless shrug."
            voice "audio/voices/ner/186.ogg"
            ner "It could be that the spell had a time limit, or maybe it's because we fell asleep together for the first time?"
            show nerith meh with dissolve
            voice "audio/voices/ner/187.ogg"
            ner "It could even be the simple fact that you fell asleep touching me."
            show nerith smirk with dissolve
            voice "audio/voices/ner/188.ogg"
            ner "You have a really heavy, fat head by the way."
            "I want to argue that it can't be that easy... but the evidence is staring us right in the face."
            "As if sensing that our conversation is over, the doorway starts to glow with light around it's edges, almost as if--"
            show nerith disapointed with dissolve
            voice "audio/voices/ner/189.ogg"
            ner "It's calling me home."
            "She doesn't say it with hesitance or excitement, just... acceptance."
            hik "You don't have to go if you don't want."
            "Her snort is comforting and familiar enough that I relax, despite the setting."
            show nerith smirk with dissolve
            "I even feel a small smile form on my lips, in answer to hers."
            voice "audio/voices/ner/190.ogg"
            ner "I DO have to go. At least in my world, I have a purpose."
            voice "audio/voices/ner/191.ogg"
            ner "Besides, I miss being able to raid, loot, and maim anytime I want."
            "Her grin stretches wide and she offers one last, uncharacteristically gentle slap to the back of my head."
            voice "audio/voices/ner/192.ogg"
            ner "Do yourself a favor and man the fuck up."
            voice "audio/voices/ner/193.ogg"
            ner "Tell that cute girl how you feel and stop wasting her time."
            hide nerith with dissolve
            "With those parting words, she opens the door, letting out a flood of golden light, and, without looking back, steps through."
            "I shut the door and lock it behind her to make sure nothing else can get out."
            scene overlay black with fade
            "The instant I let the latch drop..."
            stop music fadeout 3.0

            "I wake with a loud snort."
            scene bg sky dusk with fade
            "I'm alone, sitting on the bus where Nerith had been only minutes before."
            play music "audio/music/Heartbreaking.mp3"
            "The bus is parked right at my stop and I scramble to get off before the driver leaves."
            "He gives me an extremely odd look as I step down, and I wonder if he remembers the girl I got on with."
            "Outside, the air feels chilly."
            "Or at least... I notice it more, now that I'm alone."
            "I simply stand there for a time, wondering if the events of the past couple weeks really even happened."
            stop music fadeout 3.0
            "I stand there so long, it's a surprise when someone touches me gently on the arm."
            voice "audio/voices/mik/91.ogg"
            mik "Hikaru? Are you all right?"
            scene cg bus noNerith with dissolve
            play music "audio/music/Montauk Point.mp3"
            "I turn and see a concerned Mika holding my sleeve uncertainly."
            "It takes me a second to realize she's waiting on my response."
            hik "I'm fine."
            voice "audio/voices/mik/92.ogg"
            mik "Are you sure?"
            "She bites her lip."
            voice "audio/voices/mik/93.ogg"
            mik "Where's Nerith-chan?"
            "I'm a little surprised to hear the name said so easily... Was it all real after all?"
            hik "She... ah, had to go back home. I'm sorry, Mika-chan, but you just missed her."
            voice "audio/voices/mik/94.ogg"
            mik "Oh..."
            "She looks genuinely disappointed."
            voice "audio/voices/mik/95.ogg"
            mik "That's a shame. She seemed really cool and interesting..."
            voice "audio/voices/mik/95b.ogg"
            mik "I would've liked to get to know her better."
            "Speaking about Nerith to Mika makes me wonder..."
            "If everything about her was real, should I take her final parting words to heart?"
            "Tell her how I feel..."
            "I gather my courage and open my mouth."
            hik "Mika-chan, I--"
            "-- And then she looks directly into my eyes."
            "There's nothing aggressive about it, only curious, and I {i}still{/i} shrink away... all of my old insecurities falling back into place at such a familiar scenario."
            stop music fadeout 3.0
            "Stomach flooded with butterflies, I spout the first bit of nonsense that pops into my head."
            hik "I wanted to wash those dishes you lent me before giving them back. Just give me a few minutes, and I'll bring them by your apartment."
            voice "audio/voices/mik/96.ogg"
            mik "Oh... sure, that's fine."
            "If she looked disappointed before, it doesn't hold a candle to the expression she's wearing now..."
            scene overlay black with fade
            play music "audio/music/Heartbreaking.mp3"
            "I turn my back on those big, sad eyes of hers and practically run toward the apartment building."
            "I curse myself the whole way up the stairs, through the living room, and into my bedroom where I immediately jump on the computer."
            scene bg bedroom afternoon with fade
            "The log in screen of {i}Celestial Crossing{/i} beams at me with Nerith's character rendered in all its three-dimensional glory."
            "I click on her inventory menu and try not to imagine the scowl of disapproval she'd be wearing right now."
            "Her digital face blinks at me accusingly, and I find myself reassuring her."
            scene overlay black with fade
            hik "Next time... I promise I'll do it next time."
            python:
                achievement.grant("NextTime")
            $ overriding_on=True
            show text "{font=images/assets/YanoneTagesschrift.ttf}{size=+12}Ending number 2: Next time{/size}{/font}" at truecenter
            with dissolve
            $ renpy.pause(6.0, hard='True')
            hide text
            jump the_end


    if nerithReal == False:
        if brave == True:
            show nerith smirk at right with dissolve
            "She grins."
            voice "audio/voices/ner/194.ogg"
            ner "Well, I didn't think you'd be able to un-fuck yourself long enough to do it, but you managed to impress me, Hero."
            voice "audio/voices/ner/195.ogg"
            ner "You found the doorway."
            "I look at her with my brow furrowed and realize... I don't want her to go..."
            "Still, it's not like she'd leave her entire world behind to hang out in mine."
            "I'd rather chew sand than ask her to do that."
            "Instead I shoot for nonchalance."
            hik "So you're heading back home, then?"
            "She smiles, and it's kind of sad."
            show nerith smile with dissolve
            voice "audio/voices/ner/196.ogg"
            ner "Yeah, I think it's time."
            voice "audio/voices/ner/197.ogg"
            ner "At least in my world, I have a purpose."
            "Her grin stretches wider."
            show nerith smirk with dissolve
            voice "audio/voices/ner/198.ogg"
            ner "Besides, I miss being able to raid, loot, and maim anytime I want."
            "She steps forward and offers one last, uncharacteristically gentle slap to the back of my head."
            voice "audio/voices/ner/199.ogg"
            ner "Do yourself a favor and man the fuck up."
            voice "audio/voices/ner/200.ogg"
            ner "Tell that cute girl how you feel and stop wasting her time."
            hide nerith with dissolve
            "With those parting words, she opens the door, letting out a flood of golden light, and, without looking back, steps through."
            "I shut the door and lock it behind her to make sure nothing else can get out."
            scene overlay black with fade
            "The instant I let the latch drop..."
            stop music fadeout 3.0

            scene bg sky dusk with fade
            "I wake with a loud snort."
            play music "audio/music/Heartbreaking.mp3"
            "I'm alone, sitting on the bus where Nerith had been only minutes before."
            "The bus is parked right at my stop and I scramble to get off before the driver leaves."
            "Some impulse stops me right before I step down, and I turn to him."
            hik "Did you see the tall, dark-skinned girl that got on the bus with me, sir?"
            "The driver just looks at me blankly until I'm obliged to get off the bus or stand there staring at him until hell freezes over."
            "As the door closes behind me, I hear the man grumble that I ought to go home and sleep off whatever I drank."
            "..."
            "So that's it, then?"
            "Nerith was never really there at all?"
            "She was just a figment of my imagination that somehow built me up, made me stand up for myself, and told me to...?"
            stop music fadeout 3.0
            voice "audio/voices/mik/97.ogg"
            mik "Hikaru? What are you doing out here?"
            scene cg bus noNerith with dissolve
            play music "audio/music/Luminous Rain.mp3"
            "As if she was called by my thoughts, Mika turns up, her face scrunched up cutely in concern."
            "She glances left and right, as if searching for someone."
            voice "audio/voices/mik/98.ogg"
            mik "Nerith-chan isn't with you?"
            "At this confirmation that I'm not as crazy as I feared, I feel my lungs fully inflate with oxygen again."
            hik "She... ah, had to go back home to Sweden. I'm sorry, Mika-chan, but you just missed her."
            voice "audio/voices/mik/99.ogg"
            mik "Oh..."
            "She looks genuinely disappointed."
            voice "audio/voices/mik/100.ogg"
            mik "That's a shame. She seemed really cool and interesting..."
            voice "audio/voices/mik/101.ogg"
            mik "I would've liked to get to know her better."
            hik "I'm sure she probably wanted to get to know you better too."
            "I'm happy to see that this brings a little smile to her face as she looks up at me."
            "I think on Nerith's final parting words as I watch Mika fidget with the hem of her skirt a bit."
            "She's beautiful."
            "Her eyes are wide and warm and there's definitely affection there."
            "Is there also a glimmer of attraction?"
            "It's hard to tell, and I'm no expert on women... but after everything else I've been through, this finally feels like something I can take a chance on."
            "I take a deep breath and call on all of the self-confidence I've gathered from going through such a life-changing ordeal..."
            scene cg bus close with dissolve
            hik "Mika-chan, there's something I need to tell you."
            "She says nothing."
            "Instead, her cheeks light up softly with a blush and her smile turns shy and hopeful."
            python:
                achievement.grant("Hopeful")
            scene overlay black with fade
            $ overriding_on=True
            show text "{font=images/assets/YanoneTagesschrift.ttf}{size=+12}Ending number 3: Hopeful{/size}{/font}" at truecenter
            with dissolve
            $ renpy.pause(6.0, hard='True')
            hide text
            jump the_end


        if brave == False:
            show nerith disapointed at right with dissolve
            voice "audio/voices/ner/201.ogg"
            ner "You found the doorway."
            "I guess I did, since we're presumably in my dream, but I don't really feel like I've accomplished anything."
            "All I did was fall asleep."
            hik "Why do you think it worked THIS time and not any other time I've fallen asleep?"
            "Nerith gives a careless shrug."
            voice "audio/voices/ner/202.ogg"
            ner "It could be that the spell had a time limit, or maybe it's because we fell asleep together for the first time?"
            voice "audio/voices/ner/203.ogg"
            ner "It could even be the simple fact that you fell asleep touching me."
            show nerith smirk with dissolve
            voice "audio/voices/ner/204.ogg"
            ner "You have a really heavy, fat head by the way."
            "I want to argue that it can't be that easy... but the evidence is staring us right in the face."
            "As if sensing that our conversation is over, the doorway starts to glow with light around it's edges, almost as if--"
            show nerith disapointed with dissolve
            voice "audio/voices/ner/205.ogg"
            ner "It's calling me home."
            "She doesn't say it with hesitance or excitement, just... acceptance."
            hik "Well... I guess this is goodbye then."
            "Her familiar snort grates on my nerves, but I reassure myself that at least this will be the last time I ever have to hear it."
            voice "audio/voices/ner/206.ogg"
            ner "Yeah, I guess so. It was fun while it lasted."
            "I would have to disagree on that count, but I keep my mouth shut."
            "As if sensing my dissent regardless, Nerith shoots me one of her usual scowls and offers one last, hard punch in the shoulder."
            "I try not to flinch, but I can't really help it. Even in a dream, she's way stronger than me."
            voice "audio/voices/ner/207.ogg"
            ner "Do yourself a favor and man the fuck up."
            voice "audio/voices/ner/208.ogg"
            ner "Tell that cute girl how you feel and stop wasting her fucking time."
            "The implicit threat of \"or else,\" hangs over her sentence and I feel my throat move in a nervous swallow."
            hide nerith with dissolve
            "With those parting words, she opens the door, letting out a flood of golden light, and, without looking back, steps through."
            scene overlay black with fade
            "I shut the door and lock it behind her to make sure nothing else can get out."
            stop music fadeout 3.0
            "The instant I let the latch drop..."

            scene bg sky dusk with fade
            "I wake with a loud snort."
            play music "audio/music/Heartbreaking.mp3"
            "I'm alone, sitting on the bus where Nerith had been only minutes before."
            "The bus is parked right at my stop and I scramble to get off before the driver leaves."
            "Some impulse stops me right before I step down, and I turn to him."
            hik "Did you see the tall, dark-skinned girl that got on the bus with me, sir?"
            "The driver just looks at me blankly until I'm obliged to get off the bus or stand there staring at him until hell freezes over."
            "As the door closes behind me, I hear the man grumble that I ought to go home and sleep off whatever I drank."
            "..."
            "So that's it, then?"
            "Nerith was never really there at all?"
            "As much of a pain as she was... I feel a weird sort of... loneliness, thinking that she was a figment of my imagination the whole time."
            voice "audio/voices/mik/102.ogg"
            mik "Hikaru? What are you doing out here?"
            scene cg bus noNerith with dissolve
            "As if she was called by my thoughts, Mika turns up, her face scrunched up cutely in concern."
            hik "Nerith is gone, Mika-chan. I'm sorry she didn't say goodbye--"
            voice "audio/voices/mik/103.ogg"
            mik "Nerith?"
            voice "audio/voices/mik/104.ogg"
            mik "Is that a friend of yours?"
            "Her look of confusion is too genuine for there to be any doubt, now."
            "I choke back the urge to laugh bitterly."
            "I would only come across sounding even crazier to her than I already do."
            "Nerith's final parting words cross my mind, but the thought of listening to them is inconceivable... insane, even."
            "Am I insane now?"
            "I'm having full-blown delusions, so that's a pretty good indicator, right?"
            "I need to get away, and so I run."
            scene overlay black with fade
            "I turn on my heel and sprint for the apartment buildings, away from Mika."
            "She shouts something at my retreating back, but I don't hear it."
            "I don't want to."
            "I just want to escape this awful reality for a little while."
            scene bg bedroom gray with fade
            "My key won't turn the lock on the front door quickly enough, and it seems like an eternity before I find myself sitting in front of a familiar log in screen."
            "The {i}Celestial Crossing{/i} logo blinks at me and I finally feel myself relax."
            "Escape..."
            scene overlay black with fade
            "I just want to escape for a little while..."
            python:
                achievement.grant("Escape")
            $ overriding_on=True
            show text "{font=images/assets/YanoneTagesschrift.ttf}{size=+12}Ending number 4: All a dream{/size}{/font}" at truecenter
            with dissolve
            $ renpy.pause(6.0, hard='True')
            hide text
            jump the_end

label the_end:

    if achievement.has("Home") and achievement.has("Hopeful") and achievement.has("NextTime") and achievement.has("Escape"):
        $ achievement.grant("Completionist")

    scene bg sky night with dissolve
    $ overriding_on=True

    show text "{font=images/assets/YanoneTagesschrift.ttf}{size=+12}Thank you for playing{/size}{/font}" at truecenter
    with dissolve
    $ renpy.pause(6.0, hard='True')
    hide text

    show overlay credits at Move((0.4, 3.0), (0.4, -5.0), 60.0, xanchor="center", yanchor="center")
    with dissolve
    $ renpy.pause(35.0, hard='True')
    $ overriding_on=False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
