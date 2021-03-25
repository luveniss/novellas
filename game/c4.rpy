


label main4:

    if (wingman == False):
        "I don't get to enjoy deep, dreamless sleep very often..."
        "Which is why Nerith's wake-up call the next day is so unwelcome--"


        scene bg bedroom night blur
        show nerith uniform pissed
        with fade
        voice "audio/voices/ner/86.ogg"
        ner "{i}GET UP,{/i} USELESS!"
        with vpunch
        "THUD."
        play music "audio/music/Thinking Music.mp3"
        "--Part of the reason, anyway."
        "The other part could be the sharp pain radiating out from where my skull meets the floor..."
        "I don't bother to point out to her that the shout alone would have been enough to jolt me awake."
        "It's my suspicion that flipping my entire body off the couch is just Nerith's preferred method of starting the day."
        "Although it hardly even looks as if the day HAS started."
        "Once the stars fade from my vision, I catch a glimpse of the still-dark living room window. The sun hasn't even risen yet."
        "Before Nerith's appearance in my life, I'd typically find myself climbing into bed around this time of night, not waking up."
        show nerith uniform dissapoint with dissolve
        voice "audio/voices/ner/87.ogg"
        ner "First day of training, moron. And fair warning: I {i}don't{/i} feel like going easy on you after that embarrassing shit you pulled the other day."
        "I feel my face blanch."
        hik "You mean you were serious about that? What training?"
        "The elf doesn't even grace me with a response, instead crossing her arms and narrowing her eyes venomously. I note that she's already wearing her school uniform for the day."
        "I dare to feel a little relieved at that... Surely she isn't planning to use \"training\" as an excuse to pummel me if she's dressed for class? The blood would be troublesome to explain, after all, magic or no-magic."
        show nerith uniform pissed with dissolve
        voice "audio/voices/ner/88.ogg"
        ner "Where do you think you're going?"
        "I pause in my trek toward the bedroom."
        hik "Er... To change clothes?"
        show nerith uniform dissapoint with dissolve
        voice "audio/voices/ner/89.ogg"
        ner "Those will work. Follow me."
        scene bg bedroom night with dissolve
        "She spins on her heel and marches to the front door, clearly intending to train me away from the apartment."

        scene bg apartment hallway with fade
        "This is  fine by me. The further away I am, the less likely we are to destroy what few pieces of unbroken furniture I have left..."
        "Sadly, however, she doesn't move toward the main stairwell the way I expect. Instead, she heads out into the hallway and pads further down."
        "I don't typically come down this way, so I feel a flutter of sudden anxiety when she pauses in front of a door."
        hik "What're you...?"
        "She raps her knuckles smartly against it and it takes me another minute to realize what's happening."
        "There is a long moment of complete silence, and when no one answers her knock, Nerith pounds on the door even harder."
        "Automatically seeking to stop her from making such a racket, I reach out and grab her fist."
        hik "{i}Are you crazy? What are you doing?{/i}"
        "I don't know why I even bother whispering."
        "A sudden fumbling noise from the other side of the door catches our attention, and I realize that the damage has already been done..."
        scene bg apartment hallway blur with dissolve
        show yama angry with moveinleft

        voice "audio/voices/boy/5.ogg"
        boy "Who the hell is...?"
        "I stare in horrified surprise as I come face-to-face with none other than Yamaguchi..."
        "I'd had no idea he even lived in this building, let alone my own floor."

        "It's clear from the way he looks at us blearily that we woke him out of a sound sleep, and it takes a minute for the expressions of startled surprise and then intense dislike to chase across his features."
        show yama shock with dissolve
        voice "audio/voices/boy/6.ogg"
        boy "YOU!"
        "His voice lowers to an enraged hiss and he grabs the collar of my pajamas. "
        voice "audio/voices/boy/7.ogg"
        boy "I don't know how the hell you did it, but everyone in class thinks my friends and I beat each other up!"
        "He shakes me, and even though he's only a few inches taller than me, his fury is enough that he actually manages to lift my heels off the ground."
        "I think I make a noise."
        "I can only pray it isn't a pathetic-sounding one."
        voice "audio/voices/boy/8.ogg"
        boy "You know what? I don't even care."
        "True to his word, he lets go of me so suddenly that I wobble, trying to regain my balance."
        "I'm relieved until I see him winding his fist back for a one-punch knock-out."
        voice "audio/voices/boy/9.ogg"
        boy "I think I just want to beat the shit out of you now."
        "His angry snarl promises violence, and I have mere moments to decide what to do."

        menu:
            "Try to talk him down.":
                jump timeforwords
            "Raise your fists.":

                jump timeforaction

        label timeforwords:
            hik "Look, Yamaguchi--"
            "-- But he isn't interested in anything I have to say."
            "Time slows to a crawl, and I see his fist come flying at me with such perfect clarity that I can spot a tiny white scar running across one of his knuckles."
            stop music fadeout 3.0
            scene overlay black with fade
            "My eyes squeeze tight shut and I brace myself for impact."
            "Fuck. I really liked having a full set of teeth."
            jump main4_1

        label timeforaction:
            "All I can think about is the fact that I can't just stand here and wait to be slaughtered by this guy."
            "My fists shake a bit as I raise them in front of my face, poised to at least {i}attempt{/i} some kind of block should it become necessary."
            "It's too late to wonder if I'm doing it wrong."
            "The furious punch is already in full swing, and on reflex, my eyes flinch closed."
            stop music fadeout 3.0
            scene overlay black with fade
            "It's stupid, and I have just enough time to recognize that I'm sabotaging myself, before I expect the blow to land."
            jump main4_1

        label main4_1:
            "..."
            "The painful impact I expect never comes."
            voice "audio/voices/ner/90.ogg"
            ner "You can open your eyes now..."
            scene bg apartment hallway blur
            show yama frozen
            show nerith uniform smirk at right
            with dissolve

            play music "audio/music/Thinking Music.mp3"
            "Shocked, I oblige and immediately jump back from the fist clenched just a few centimeters from my face."
            hik "You froze him?"
            voice "audio/voices/ner/91.ogg"
            ner "That's right."
            show nerith uniform spell with dissolve
            "She strides to Yamaguchi's side and whispers something to him – possibly the incantation to yet another spell."
            show yama angry with dissolve
            "His arm quickly snaps back to his side and without a word, he shuffles back into his apartment, closing the door behind him."
            hide yama with moveoutleft
            voice "audio/voices/ner/92.ogg"
            show nerith uniform smirk at center with moveinright
            ner "He won't remember this, don't worry. I was just using him to prove a point."
            "She looks entirely too pleased with herself, placing her hands smugly on her hips."
            "I'm too deflated with relief at the moment to be upset with her, so I save the emotional outburst she deserves for another day."
            hik "What point were you proving, exactly?"
            voice "audio/voices/ner/93.ogg"
            ner "A very simple one."
            "She lifts a finger and points it directly at my nose, so close, I almost go cross-eyed."
            show nerith uniform dissapoint with dissolve
            voice "audio/voices/ner/94.ogg"
            ner "Listen up, Useless, because this is lesson one:"
            voice "audio/voices/ner/95.ogg"
            ner "There's a time for words, and times when trying to talk just gives your enemy the opportunity they need to cave your head in."
            show nerith uniform pissed with dissolve
            voice "audio/voices/ner/96.ogg"
            ner "Your main problem is that you either don't know when to take action, or you try to take action and HESITATE."
            "This sounds like nonsense to me. How the heck are you supposed to know which situations are which in a split second?"
            "I think back to the beginning of the confrontation, and even before that – to the fight in class with Yamaguchi's friends..."
            hik "It's hard think about taking action when you're naturally a passive person..."
            "She rolls her eyes, but doesn't argue. At least she recognizes that we're fundamentally different people."
            show nerith uniform dissapoint with dissolve
            voice "audio/voices/ner/97.ogg"
            ner "It's all about attitude, Useless. Attitude, and knowing what your own capabilities are."
            hik "Pft. What capabilities?"
            "I half expect her to smack me for my pessimism, or at least throw a derisive snort my way. Instead, she gives me a wide grin."
            show nerith uniform smirk with dissolve
            voice "audio/voices/ner/98.ogg"
            ner "Don't worry about it, idiot. That's what I'm here for."
            "An expectant silence grows between us for a moment."
            show nerith uniform smile with dissolve
            voice "audio/voices/ner/99.ogg"
            ner "For now though, I just want breakfast. Go get me some of that yaki-bread-stuff we had the other day."
            "I blame the small smile I give her on a combination of fatigue and relief."
            "It's easy to tell myself that I hate her for putting me through such a ridiculous test, but when all's said and done, I still hurry through my morning routine and purchase a few extra yakisoba breads on the way to school..."
            jump main4_3


    if (wingman == True):
        "I don't sleep very well the next night."
        scene bg sky night with fade
        "My jaw is so sore and bruised that it gives me a migraine. I toss and turn on the couch, trying to find a comfortable position, drifting in and out of sleep until finally at 4:00 in the morning, I can't do it anymore."
        scene bg bedroom night with fade
        "I get up and make for the bathroom. Soaking in the warm water eases the headache slightly, but I'm still not feeling completely alert when I open the door and find Nerith waiting for me in the hall."

        scene bg bedroom night blur with dissolve
        show nerith uniform smirk with moveinleft
        "She's already dressed in her school uniform, which is odd, but not alarming enough to fully distract me from the throbbing pain behind my eyeballs."
        hik "Nerith! Er... You're up early..."
        voice "audio/voices/ner/100.ogg"
        ner "Did you expect me to forget my promise?"
        play music "audio/music/Hidden Agenda.mp3"
        "It takes my foggy brain a minute to catch up, but eventually I remember her words from the previous day."
        hik "You want to start right now? Today?"
        "She takes a second to stretch out her shoulders and motions that I should do the same. Her answer doesn't come until she's satisfied that I'm copying her to the best of my ability."
        voice "audio/voices/ner/101.ogg"
        ner "Why NOT start today?"
        "Gee, Nerith. Maybe because my skull feels as if it might be splitting in half the more we do these stupid stretches?"
        "I glower at her silently instead of voicing my thoughts out loud. I'm in a bad mood, but I'm not quite suicidal... yet."
        "She either doesn't notice the strain or doesn't find it worth commenting on."
        voice "audio/voices/ner/102.ogg"
        ner "I figure since you showed you actually had some guts the other day, we could start by working on your form."
        hik "My form?"
        voice "audio/voices/ner/103.ogg"
        ner "Don't make me repeat myself, Useless. Now copy my stance."
        show nerith uniform fight with dissolve
        "Nerith bends her knees and lowers her center of gravity before raising her fists in front of her. One is slightly higher than the other."
        "Clumsily, I mimic her."
        voice "audio/voices/ner/104.ogg"
        ner "You want to turn your hips to the side a bit and bend your knees even more."
        voice "audio/voices/ner/105.ogg"
        ner "Good. Now hit me."
        "I gasp, straightening in surprise."
        hik "Hit you? You mean throw a punch? Just-- I mean... Right now?"
        hik "I'm not even sure how I should--"
        "Her utterly implacable expression silences me."
        voice "audio/voices/ner/106.ogg"
        ner "Hit me with everything you've got, Useless. Now."

        menu:
            "Ask her to show the proper technique first.":
                jump properform
            "Make a fist and swing.":

                jump heregoesnothing

        label properform:
            hik "Damn it. Can you at least show me a technique first? I have no idea what I'm doing here!"
            "She raises a thin eyebrow at my petulant tone, but doesn't seem upset by it."
            voice "audio/voices/ner/107.ogg"
            ner "All right then."
            "Without warning, she launches a vicious right hook straight into my solar plexus."
            hik "HURK!" with hpunch
            "It hurts. A LOT."
            "For a second I'm thankful that she roped me into this training session {i}before{/i} I had anything to eat. Cleaning vomit off the floor is not the way I typically like to start the day."
            "As it is, I fall to my knees, dry-heaving. Nerith looks at me without sympathy."
            show nerith uniform dissapoint with dissolve
            voice "audio/voices/ner/108.ogg"
            ner "When you're done being dramatic, you can tell me if you still think demonstrations are a good idea."
            "I glare up at her, but can't do much until the pain subsides enough to stand."
            show nerith uniform fight with dissolve
            voice "audio/voices/ner/109.ogg"
            ner "Good. Now, because you asked, I'll let you punch at me slowly and break down the steps..."
            jump main4_2

        label heregoesnothing:
            "I'm over-thinking this, I realize."
            "My pounding headache resurfaces and further convinces me that following Nerith's instructions without argument or analysis seems like the best way to go."
            "Mind made up, I screw up my courage and tap my fist against the elf's shoulder, which is the safest-looking target I see."
            "She stares at me in disbelief."
            show nerith uniform meh with dissolve
            voice "audio/voices/ner/110.ogg"
            ner "What the fuck was that?"
            hik "A... punch?"
            "She mutters something in Elvish, but obligingly comes around to show me what I'm doing wrong."
            "I get the sense that she's giving me credit for attempting the exercise, at the very least."
            jump main4_2

        label main4_2:
            scene bg sky night with fade
            "We practice for the better part of an hour before I finally have to beg for a break."
            "Nerith nods briskly, to my pleasant surprise."
            scene bg bedroom night blur
            show nerith uniform smile
            with fade
            voice "audio/voices/ner/111.ogg"
            ner "Yeah, you should probably hop in the bath if we want to make it to school on time."
            "I can't help noticing that she obviously hasn't broken a sweat at all. It's a little insulting how completely unruffled she is, given the amount of effort I put into our session."
            "Still, I can't deny that the workout has made me feel a little better about myself."
            scene bg sky night with fade
            "I rush through my morning routine, and in a show of gratitude, I buy some extra yakisoba bread for Nerith on the way to school..."
            jump main4_3

    label main4_3:
        stop music fadeout 3.0
        scene overlay black with fade
        "..."

        scene bg sky afternoon with fade
        play music "audio/music/Montauk Point.mp3"
        "A week passes, and the two of us fall into an uneasy routine."
        "We go to school together, eat together, and in the mornings before the sun is up, Nerith tosses me out of bed for training."
        "It's getting almost frighteningly comfortable."
        "I have to remind myself that things can't stay this way forever."
        "For one, casting such extensive spells in school everyday is obviously beginning to strain her magic."
        "She spends longer and longer amounts of time meditating to keep her mana levels high, and I can't help worrying that she's reached the limits of what a max-level warlock can do in the real world..."
        "She doesn't complain. Ever. Nerith is many things, but not a whiner."
        "Instead, she gets frustrated more often when she runs into things she's unfamiliar with."
        "I barely manage to save my father's expensive espresso machine from her wrath when she tries to makes herself tea with it and spits out the bitter, black beverage instead."
        "All of the tantrums I translate to her simply wanting to get back home, and I can't entirely blame her."
        "I'd love to send her back into the game, but the truth I'm confronted with is that I don't have the murkiest idea how to do it."
        "I don't even know where to start {i}looking{/i} for an answer."
        "The looming failure makes me feel so guilty that I find myself keeping a steady supply of yakisoba bread on hand."
        "That, and focusing all of my energy into our training, is basically all I'm able to do to keep Nerith from going on a destructive rampage."
        scene bg livingroom with fade
        "The training itself isn't fun, per se, but it does satisfy me in a weird way."
        "At this stage, it mostly consists of Nerith picking fights with muscular strangers on the street and goading them into fights with me."
        "It kind of works... In the sense that I'm a lot more comfortable getting pissed off at her now. She even lets me argue with her sometimes without threatening to lop my head off..."
        scene bg livingroom blur
        show nerith sporty fight
        with dissolve
        voice "audio/voices/ner/112.ogg"
        ner "Good! Now come at me like you actually fucking mean it!"
        "I rush forward, taking advantage of the space we've cleared in the center of the living room, and aim a jab at her face."
        "I get about a hand's length away before she spins to the side, grabbing my wrist and squeezing hard."
        "My eyes water as pain shoots up my arm."
        "With a harsh chuckle, she twists the limb at an angle and takes a short step back."
        "Before I can wrap my mind further around the mechanics, she has me flat on the floor."
        show nerith sporty laugh with dissolve
        voice "audio/voices/ner/113.ogg"
        ner "How does it feel getting thrown – what is this, even? – the twentieth time today?"
        "She gives a jeering scoff."
        show nerith sporty smirk with dissolve
        voice "audio/voices/ner/114.ogg"
        ner "And you call yourself a man... You don't even have the balls to talk to that little girl you like next door!"
        "I lunge to my feet, infuriated, but with barely an effort, Nerith uses my forward momentum to sweep my legs. I go down on my front this time, and the elf wastes no time wrestling me into a headlock."
        voice "audio/voices/ner/115.ogg"
        ner "It's even more pathetic considering how much {i}she{/i} wants {i}you{/i}."
        "I stop struggling immediately."
        "Perhaps worried that she might have accidentally killed me, Nerith jumps off, looking at me quizzically."
        hik "H-How do you know? You've never even talked to her!"
        "She rolls her eyes before pointing at her own ears."
        show nerith sporty smile with dissolve
        voice "audio/voices/ner/116.ogg"
        ner "Elf, idiot."
        voice "audio/voices/ner/117.ogg"
        ner "My natural senses are enhanced enough that I can pick up the pheromones of anyone around me."
        "She wrinkles her nose a bit."
        voice "audio/voices/ner/118.ogg"
        ner "And you two put out enough that I gag a little every time you're in the same room."
        "I sit down on the arm of the couch, trying to digest this new information."
        "It's no surprise to hear what my body does around Mika, but her...?"
        hik "I don't think I believe you."
        "Nerith snorts, affronted."
        show nerith sporty dissapoint with dissolve
        voice "audio/voices/ner/119.ogg"
        ner "I don't care if you do or not! I CAN detect pheromones, and that's how I know you secretly liked it the whole time I ran around this apartment with no pants on!"
        "My face goes scarlet with humiliation. I'm only human, goddamnit!"
        "I open my mouth to say something in my own defense, but a quick knock at the front door interrupts me."
        voice "audio/voices/ner/120.ogg"
        ner "I'm getting some water."
        scene bg livingroom with dissolve

        "Nerith flounces away toward the kitchen as I unlock and open the door."
        scene bg apartment hallway blur
        show mika smile blush
        with fade

        "I gulp, suddenly shy and flustered to see that it's none other than Mika-chan. She smiles warmly, holding a tray of what appears to be all my favorite foods."
        "It's impossible to open my mouth. Speaking is unfathomable."
        "What can I possibly say to her, now that I know...?"
        scene bg livingroom blur
        show mika smile blush
        with dissolve
        "Something in the air between us shifts, and I can't help thinking that she notices it too."
        "Her smile turns almost bashful and she drops her gaze self-consciously to the tray in her hands."
        voice "audio/voices/mik/30.ogg"
        mik "It occurred to me earlier while I was cooking that I haven't seen you in a few days."
        show mika laugh blush with dissolve
        voice "audio/voices/mik/31.ogg"
        mik "I got worried that you might not be eating well, so I brought this, hoping I might tempt you."
        show mika shock with dissolve
        voice "audio/voices/mik/32.ogg"
        mik "Um! To – to {i}eat{/i}, of course! The food."
        "Her cheeks get visibly rosier and I can't help finding this role-reversal completely adorable."
        show mika smile blush with dissolve
        voice "audio/voices/mik/33.ogg"
        mik "Right, so this is--"
        show nerith sporty smirk at right with moveinright
        voice "audio/voices/ner/121.ogg"
        ner "Ready for round two, yet?"
        "Nerith comes strolling around the kitchen corner, sipping a glass of water casually."

        show nerith sporty huh with dissolve
        "She pauses, taking in the scene before her with widened eyes for a second before glancing my way."
        show mika shock with dissolve
        "For my part, I watch Mika with a rising sense of panic as she slowly mouths the words, \"round two.\""
        "My gut clenches. I can see her forming the wrong idea about my relationship with Nerith as she takes in how sweaty and disheveled we both are."
        "Shit, this looks bad."
        "There's a moment where I'm almost sure Mika might cry, and I open my mouth to loudly deny everything... when she surprises us all by giggling instead."
        "Still balancing her tray, she playfully nudges me with her elbow the way she always does. I realize suddenly that I'm starting to hate when she does that."
        "The action screams of artificially-created distance, like she's keeping me from getting too close... like she's trying too hard to convince both of us that we're friends and nothing more."
        show mika laugh blush with dissolve
        voice "audio/voices/mik/34.ogg"
        mik "Finally got a girlfriend, huh? Congratulations, I thought it was never going to happen! Heehee..."
        stop music fadeout 3.0
        "As she and Nerith formally introduce themselves to each other, I try to calm myself enough to decide what to do."

        menu:
            "Assure her that there's nothing between you and Nerith.":

                $ count += 1
                jump nothingtoseehere
            "Try to make her jealous.":

                $ count -= 1
                jump sillyrabbit

        label nothingtoseehere:
            hik "She's my cousin!"
            play music "audio/music/Marty Gots a Plan.mp3"
            "I blurt out the words so suddenly that they both turn to stare at me."
            hik "She came from out of town to visit me and I've been busy showing her around... She's, uh... really into cosplay, as you can see. Heh..."
            show mika shock with dissolve
            "Mika's eyebrows rise so high on her forehead that they come dangerously close to jumping off her face completely."
            "Her expression goes beyond disbelief."
            "It looks like she's actually questioning my level of sanity."

            voice "audio/voices/mik/35.ogg"
            mik "Your cousin."
            "Her voice is deadpan. I gulp and nod frantically."
            voice "audio/voices/mik/36.ogg"
            mik "Your cousin, who I've never met or heard about in all the years we've known each other."
            show nerith sporty laugh with dissolve
            voice "audio/voices/ner/122.ogg"
            ner "It's true! I'm from his mother's side, so we don't see each other much."
            "No one looks more surprised to hear Nerith speak than she does, herself."
            "I find that I'm gaping openly, so I shut my mouth before anyone notices."

            show nerith sporty smirk with dissolve
            voice "audio/voices/ner/123.ogg"
            ner "Yeah, clearly I got all the looks – and height – in the family."
            "She caps this off with a forced chuckle, and Mika-chan finally cracks a friendly grin."
            voice "audio/voices/mik/37.ogg"
            mik "Oh, well luckily I made way too much food. It's nice to meet you...?"
            voice "audio/voices/ner/124.ogg"
            ner "Nerith."
            voice "audio/voices/mik/103b.ogg"

            mik "\"Nerith\"?"
            hik "She's from Sweden!"
            "I find myself blurting out the lie in desperate hope that she won't ask any awkward questions."
            "Mika looks confused, but seems content to hand the tray over without fuss. She gives Nerith a suddenly bright look."

            show mika smile with dissolve
            voice "audio/voices/mik/39.ogg"
            mik "That's such a pretty shirt! I have the same one hiding in my closet somewhere."
            show nerith sporty huh with dissolve
            voice "audio/voices/ner/125.ogg"
            ner "Er... I'll just take this into the kitchen, okay? Bye."
            hide nerith with moveoutright
            "Taking the food in hand, the elf practically sprints out of the room, leaving me to deal with the remaining conversation on my own."
            hik "Thanks for the food, Mika-chan. Sorry about my cousin's... uh lack of--"
            "I trail off, distracted at how closely she's watching me. She seems to realize the same thing, and her cheeks redden once more."
            "Her hand reaches out to close the front door on herself as she turns to go. As it creaks shut, she looks me directly in the eye."

            show mika smile blush with dissolve
            voice "audio/voices/mik/40.ogg"
            mik "I guess you don't have a girlfriend after all. That's too bad..."

            "It's almost impossible to tell with the stupid door blocking half her face, but I'm almost positive I see her lips tilted up in a little smile."
            scene bg livingroom with dissolve
            stop music fadeout 3.0
            "The door closes and I hear her steps retreat in the hall outside."
            "I know I'm smiling like the biggest idiot in the world... and I can't bring myself to care, even when I enter the kitchen later to find that Nerith's already demolished most of Mika's cooking."
            jump main4_4

        label sillyrabbit:
            "I can't fully shrug off the irritation from earlier, and my smile comes across a little forced."
            "Tired of her games, I reach out as if to put an arm around Nerith's waist."
            hik "Nerith is just a friend. A very {i}close{/i} friend... We--"
            show nerith sporty pissed
            show mika shock
            with dissolve
            play music "audio/music/Thinking Music.mp3"
            "Before I can touch her, however, Nerith halts me with a hard glare."
            "She then very decisively slaps the back of my head."
            with vpunch
            voice "audio/voices/ner/126.ogg"
            ner "Liar. As if you'd ever have a shot with me."
            "Then, with more friendliness than I even knew she was capable of, the warlock grins at Mika and introduces herself properly."
            show nerith sporty smirk with dissolve
            voice "audio/voices/ner/127.ogg"
            ner "Useless over here is letting me stay for a few days, until I figure out my... living situation."
            show nerith sporty dissapoint with dissolve
            voice "audio/voices/ner/128.ogg"
            ner "He's not a bad guy when he's not trying to be macho and show off."
            "The two laugh, and I feel my face burn with embarrassment. This situation couldn't possibly get any worse, could it?"
            show mika smile with dissolve
            voice "audio/voices/mik/41.ogg"
            mik "Well, I suppose we can forgive him. He's just a dumb kid, after all..."
            "Ouch."
            "Feeling my chances with Mika-chan fly out the window, I'm tremendously relieved when she turns to go."
            "Shutting the front door on herself, she throws her parting words over my head to Nerith, as if I'm not even standing there."
            show mika normal with dissolve
            voice "audio/voices/mik/42.ogg"
            mik "That's a cute shirt, by the way. I have one just like it hiding in my closet somewhere!"
            hide mika with dissolve
            "She leaves."
            "The instant her footsteps retreat, Nerith punches me in the shoulder, hard."
            with vpunch
            hik "OW! What the hell?!"
            show nerith sporty pissed with dissolve
            voice "audio/voices/ner/129.ogg"
            ner "Being manly isn't the same as being an ass, Useless."
            scene bg livingroom with dissolve
            "With that, she gives a haughty sniff and stomps off toward the kitchen, likely to partake in Mika's home cooking."
            scene overlay black with fade
            stop music fadeout 3.0
            "With the feeling that I've been kicked repeatedly while down, I spend the rest of the day in moody silence."
            jump main4_4

        label main4_4:
            scene bg bedroom afternoon with fade
            "I log in to {i}Celestial Crossing{/i} that night on a whim. I haven't played since Nerith's arrival – for obvious reasons – so I'm not quite sure what to expect as the logo flashes briefly."
            "Nerith's character doesn't appear on the login screen, I note with only mild surprise."
            "With no trace of her left in the game, the question of how to get her back to her world seems even more daunting than before..."
            "Then there's also the depressing fact that – assuming she's stuck out here – I'll have to spend months building a new character up from scratch."
            "I lament briefly over all the gear I spent so many months raiding for..."
            hik "I wonder if the developers would credit me all the gold I had in her inventory if I tell them the character somehow magically got out of their game?"
            "I snort at my own dry humor."
            "Inspiration strikes me suddenly."
            play music "audio/music/Hidden Agenda.mp3"
            "Quickly, I dig out the badge I got for the upcoming convention and stare at it. I'd have to get Nerith one as well, but that shouldn't be too hard."
            "A one-day pass for the day of the \"Celestial Crossing\"panel should be enough."
            "I remember how excited I was to hear that that the developers of the game itself would be there."
            "Now my pulse is pounding with the knowledge that we might finally have a shot at getting some answers!"
            "After all, who could know better about the lore of the game than the developers themselves?"
            scene bg livingroom with fade
            "I surge out of my seat and rush into the living room where Nerith is busy putting the finishing touches on her armor."
            scene bg livingroom blur
            show nerith sporty meh
            with dissolve
            hik "Great news!"
            hik "We're going to go see the developers of your game. They should have some answers on how to get you home."
            show nerith sporty dissapoint with dissolve
            voice "audio/voices/ner/130.ogg"
            ner "Developers?"
            hik "Yeah! Think of them as the high authority on magic from your world. If anyone should know anything, it's them."
            "I'm liking the sound of this plan more and more."
            "After weeks of nothing, it feels like I'm finally doing something to help our situation."
            "Nerith, on the other hand, looks less than enthused."
            show nerith sporty meh with dissolve
            voice "audio/voices/ner/131.ogg"
            ner "If you say so, I guess. Better than nothing..."
            "I realize that I've neglected to tell her the best part."
            hik "Did I mention that you can wear your armor?"
            show nerith sporty huh with dissolve
            "The elf 's ear twitches, and her face breaks into an broad grin. She almost looks like her in-game self again."
            stop music fadeout 3.0
            show nerith sporty smirk with dissolve
            voice "audio/voices/ner/132.ogg"
            ner "Fuck yeah. Let's do it!"

            if count >= 3:
                $ brave = True

                if count >= 4:
                    jump mika1

            if count < 3:
                $ brave = False

            jump main5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
