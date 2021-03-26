

label ready:
    play music "audio/music/Drums of the Deep.mp3"
    scene bg dungeon with fade
    G "ДЗЫНЬ!"
    G "БАМС!"
    G "Голос демона стонет от боли, а женщина зовет."
    voice "audio/voices/ner/1.ogg"
    Gner "Черт побери, Хикару! ЧТО ТЫ ДЕЛАЕШЬ?! Считаешь трещины в гребаном потолке?!"
    G "Я удивленно моргаю, рассматривая сцену передо мной."
    G "Нерит, эльфийскийская колдунья, противостоит двум рычащим минотаврам."
    G "Ее короткий меч выглядит довольно жалким, когда сталкивается с их тяжелыми широкими топорами, меня пронзает страх."
    G "Не задаваясь вопросом, как я оказался в этой ситуации, я чувствую, что мое тело двигается автоматически."

menu:
    "Использовать заклинание":
        jump hikusespell
    "Используй оружие":

        jump hikuseweapon

label hikusespell:
    G -"Мои руки непроизвольно совершают движения, и я бормочу заклинание. Я жду, когда тепло огня распространится от моих вытянутых пальцев..."
    G "Слабая струя пламени вырывается из моих рук, описывая дугу в воздухе, пока не ударяется о руку ближайшего минотавра.."
    G "Он хрюкает из-за дискомфорта."
    G "... Разочарование начинает накапливаться до тех пор, пока..."
    G "Какого черта? Что происходит с моей магией?"
    G "По крайней мере мне удалось отвлечь его внимание от Нерит."
    voice "audio/voices/ner/2.ogg"
    Gner "Не надоело быть бесполезным?"
    G "Она бросает вопрос через плечо, когда наносит удар мечом по глазам другого минотавра, ослепляя его."
    Ghik "Что - то не так с моей магией. Должно быть, у меня кончилась мана или что-то в этом роде!"
    jump main1_1

label hikuseweapon:
    G "Мои пальцы тянутся к рукояти тяжелой булавы, которая должна была висеть у меня на боку, но её там не оказалось.."
    G "Какого черта? Я хожу совершенно безоружный?!"
    G "Не находя чего-то стоящего, я хватаю с земли гость щебня и со всей силы швыряю его в ближайшего минотавра."
    G "*глухой удар*" with vpunch
    G "Она отскочил от его спины, но, по крайней мере, привлек внимание."
    voice "audio/voices/ner/3.ogg"
    Gner "Кидаться камнями? Ты серьезно?!"
    jump main1_1

label main1_1:
    G "Минотавр, кажется, решил, что я слишком раздражаю, чтобы оставлять меня в живых и, останавливая борьбу с Нерит, ковыляет ко мне."
    G "Вот дерьмо..."
    G "Ее руки выполняют сложные движения, и когда она выдыхает, облако ледяного пара окутывает двух монстров, превращая их в твердые статуи.."
    G "Прежде чем я успел запаниковать, Нерит начала действовать."
    G "Она с полным безразличием пинает одного из них, разбивая на несколько больших кусков."
    G "Вокруг... кусочки... повсюду, и рука мертвого минотавра скатывается к моей ноге."
    G "К горлу подкатывает тошнота, а я пытаюсь сосредоточиться на том, что говорит Нерит, чтобы отвлечься.."
    show bg dungeon blur with dissolve
    show nerith pissed with moveinleft
    voice "audio/voices/ner/4.ogg"
    Gner "Чертовское расточительство. Это был бы недурный лут... И все потому, что ТЫ решил ничего не делать, только попусту тратил воздух вокруг."
    show nerith fight with dissolve
    G "Опрокинув вторую статую и печально глядя на разбитые остатки своей добычи, она перевела взгляд на меня."
    show bg dungeon
    hide nerith
    with dissolve
    G "Я не мог оправдаться и немного вздрогнул. Она чертовски милая, когда злится."
    G "Я не знаю, что произошло. Я посмотрел вниз и ... --"
    G "Внезапно она прерывает меня абсолютно равнодушным тоном:."
    show bg dungeon blur
    show nerith disapointed
    with dissolve
    voice "audio/voices/ner/5.ogg"
    Gner "Ты в порядке?"
    G "Это покажется безумием, но я не заметил как прямо у моего живота медленно расползается кровавое пятно."
    G "Я смотрю вниз."
    G "Не чувствую боли... Это плохой знак, да?"
    G "Зрелище почти такое же тревожное, как и осознание того, что совсем не больно."
    Ghik "Что за--? Я даже не помню, как поранился!"
    show nerith pissed with dissolve
    voice "audio/voices/ner/6.ogg"
    Gner "А чего ты ожидал, явившись в таком виде? Идиот..."
    G "Все вдруг становится ясно."
    G "На мне надета школьная форма."
    G "Я не должен быть здесь. Я НЕ МОГУ быть здесь. Нерит-это я, в..."
    stop music fadeout 3.0
    G "...игре."


    scene bg classroom with fade


    hik "(SNORT) Wha...?"
    play music "audio/music/Hidden Agenda.mp3"
    voice "audio/voices/aga/1.ogg"
    aga "...And how was your nap, Izumi-san?"
    show bg classroom blur with dissolve
    show agano plain with moveinleft
    "The entire class is laughing so hard, I fantasize briefly about vanishing into the floor."
    "The worst part is embarrassing myself in front of Agano-sensei, though. This isn't quite as bad as the time I fell asleep and had a dirty dream about her in the middle of class, and at least there's no drool..."
    show agano happy with dissolve
    voice "audio/voices/aga/2.ogg"
    aga "Go stand in the hallway, Izumi. I'll deal with you in a minute."
    show bg classroom
    hide agano
    with dissolve
    show bg hallway with fade
    "I feel my face flush in humiliation as I make the walk of shame through the classroom, trying my best to ignore the snickers and giggles."
    "It's a small relief to shut the door behind me, but I hate that Agano-sensei is disappointed... again."
    "Especially since the nap really wasn't worth the embarrassment."
    hik "What a lame dream... Fighting beside my game character, and failing at it? Even in my imagination I'm a freaking loser."
    "Thinking back to battle, I can easily place the setting, now that I'm not asleep. It looked like the final level before the end of the Lich Lord quest."
    hik "Maybe I'm subconsciously trying to remind myself I need to max out her level before the expansion gets released..."
    "And as it always is, thinking about {i}Celestial Crossing{/i} is the metaphorical balm on my soul."
    hik "{i}Crossing-Con{/i} is coming up too... I need to at least grind through Lich Lord Keep and maybe the Forest to--"
    voice "audio/voices/aga/3.ogg"
    aga "--Keep falling asleep in my class, again?"
    show bg hallway blur with dissolve
    show agano happy with moveinleft
    "My automatic reaction is to squeak out her name, but it comes out sounding like..."
    hik "Ak!"
    show agano plain with dissolve
    voice "audio/voices/aga/4.ogg"
    aga "If you spent more time at home sleeping properly and less time playing games, maybe we wouldn't have to have this little chat once a week."
    hik "Y-yes, ma'am."
    "Her gaze is stern at first, but as she sighs, the wind seems to go out of her."
    voice "audio/voices/aga/5.ogg"
    aga "Honestly, Izumi-san... It's not as though you're a bad student when you apply yourself! I know your father isn't home... but I need you to try harder..."
    "My face heats up and I hang my head like an idiot."
    show bg hallway
    hide agano
    with dissolve
    "At eighteen years of age, I'm way too old to be falling asleep in class all the time, barely passing all my subjects."
    "I KNOW this."
    show bg sky afternoon with fade
    stop music fadeout 3.0
    "If only it was as easy to level up in real life as it is in a game..."

    "It's hard not to drift back into a daydream as she scolds me, but I manage not to."
    "The rest of the day passes by in a fog of sleepiness amid the judgmental stares of my classmates..."


    scene bg street afternoon with fade
    "...The walk home is peaceful by comparison."
    "I'm close to the apartment complex I live in, when I see a familiar head turn the adjacent corner."
    voice "audio/voices/mik/1.ogg"
    mik "Oh! Hey, Hikaru-kun. Heading home?"
    play music "audio/music/Montauk Point.mp3"
    show bg street afternoon blur
    show mika grocery smile
    with dissolve
    "Why? WHY do I blush every time she so much as looks as me?"
    show mika grocery with dissolve
    hik "Uh... yeah. I just got out of school."
    "Of course she knows that! The time of day and the uniform make it fairly obvious, idiot."
    "Time to deflect. DEFLECT."
    hik "You went grocery shopping?"
    "I motion lamely toward the plastic bags she's holding. They look a little heavy."
    "By some miracle, she actually smiles."
    show mika grocery smile with dissolve
    voice "audio/voices/mik/2.ogg"
    mik "Uh-huh! I got some ingredients to make dinner tonight."
    "She laughs lightly before giving me a mock-angry look."
    voice "audio/voices/mik/3.ogg"
    mik "It figures that we'd bump into each other when I have food. It seems like the only time you ever see me is when I'm trying to feed you!"
    hik "S-sorry, Mika-chan."
    "She throws her elbow playfully at my midsection."
    "It takes all of my willpower not to grunt like a little sissy."
    "She's completely wrong, of course. In the entire span of time we've known each other as next-door neighbors, I don't think I've sought her out once."
    "In fact, up until my mother passed away, I got the sense that she didn't even like me."
    "She stopped coming over to play when she entered junior high two years ahead of me. It wasn't hard to figure out that she probably didn't want a little kid hanging around with her older friends."
    "When Mom passed, though, she started showing up again. Mostly with food, but also sometimes just to make sure I was taking care of myself."
    show mika grocery sad with dissolve
    voice "audio/voices/mik/4.ogg"
    mik "Mou, Hikaru-kun... Can you please try to be a little more comfortable with me? We've known each other since we were practically in diapers!"
    show mika grocery with dissolve
    voice "audio/voices/mik/5.ogg"
    mik "Actually, do you think I could walk home with you? I wouldn't mind some company."
    "I feel the skin under my collar go hot."
    "I've always been in love with her, of course... but with her looks and the fact that she's already dating real men at her university, I have less than a snowball's chance in hell."
    "I'm pretty sure I nod or something, because Mika continues smiling and falls into step beside me."
    "The silence that falls between us is painfully awkward."
    "I feel myself start to sweat a little as we pass by the park and a couple houses."
    "There are still a good two or three blocks before we make it home and I have no idea how to entertain her."

menu:
    "Offer to carry her bags":

        $ count += 1
        jump carrybags
    "Make small talk":
        jump smalltalk

label carrybags:
    hik "Those look heavy... I could carry them for you if you want."
    show mika grocery smile with dissolve
    voice "audio/voices/mik/6.ogg"
    mik "Oh! Sure."
    "She looks pleasantly surprised at my offer and I feel an unfamiliar surge of self-confidence."
    hide mika
    show bg street afternoon
    with dissolve
    "I reach out and take hold of the groceries."
    "They're a little heavier than I anticipated, but I force my muscles to relax and not look like I'm straining too hard to carry them."
    show mika smile
    show bg street afternoon blur
    with dissolve
    "I ask the question before I really think about it."
    hik "What'd you get?"
    voice "audio/voices/mik/7.ogg"
    mik "You're being unusually assertive today."
    "She looks quietly amused for a minute – like she's laughing at some inner joke – before casually moving on."
    voice "audio/voices/mik/8.ogg"
    mik "I bought some extra things to make your favorite: beef stew."
    hik "MY favorite?"
    "Mika rolls her eyes."
    show mika normal with dissolve
    voice "audio/voices/mik/9.ogg"
    mik "Yes, YOUR favorite. It's been a while since I cooked for you last, hasn't it?"
    "A warm feeling rises in my chest and I look down at her. Cooking for a guy is a girlfriend thing, isn't it?"
    show mika smile with dissolve
    voice "audio/voices/mik/10.ogg"
    mik "...and let's face it, you could use the extra calories. When was the last time you ate something that didn't come out of a styrofoam cup?"
    "The warm feeling drops back down to my stomach where it belongs."
    "Snowball's chance in hell, remember?"
    show bg apartment hallway
    hide mika
    with fade
    "We reach the apartments and head up to the third floor where we live."
    "I start puffing by the second landing, but if she notices, she's kind enough to pretend not to."
    show bg apartment hallway blur
    show mika grocery smile
    with dissolve
    voice "audio/voices/mik/11.ogg"
    mik "Thanks for your help, Hikaru-kun. I'll come over later when the food's ready, okay?"
    "She takes the bags from me and her fingers accidentally brush against mine."
    show bg apartment hallway
    hide mika
    with dissolve
    "The innocent contact sends a shiver through me, and by the time she smiles sweetly in thanks, I'm ready to flee back to the lonely, quiet lair I call home."
    jump main1_2

label smalltalk:
    hik "H-how's school going?"
    show mika grocery smile with dissolve
    "Mika's smile is friendly and a little relieved, as if she was equally bothered by the tension."
    voice "audio/voices/mik/12.ogg"
    mik "Not too bad, but the workload is pretty intense. Industrial chemistry isn't a field to get into if you want to have any kind of social life."
    hik "You mean, you don't have much free time anymore?"
    show mika grocery sad with dissolve
    voice "audio/voices/mik/13.ogg"
    mik "Right. I can't remember the last time I went out with friends or on dates."
    "I try not to perk up too noticeably at the last part. Mika turns her attention back to me and her grin widens."
    show mika grocery smile with dissolve
    voice "audio/voices/mik/14.ogg"
    mik "This doesn't count as a free time activity, by the way. I ALWAYS have time to cook for you, Hikaru-kun."
    "My mouth gapes open a little at her casual admission. I feel my heart start to beat faster..."
    voice "audio/voices/mik/15.ogg"
    mik "You need all the home-cooked meals you can get! You'll have a much easier time getting a girlfriend once you've bulked up a bit."
    show bg street afternoon
    hide mika
    with dissolve
    "I shut my mouth with a grimace."
    "Snowball's chance in hell, Hikaru. Snowball's chance in hell."
    show bg apartment hallway with fade
    "We reach the apartments and head up to the third floor where we live."
    "Mika is puffing with exertion by the time we reach the second landing and I feel a little guilty for not offering to carry her groceries."
    "Still, her smile is genuinely sweet when she says goodbye at her front door."
    show bg apartment hallway blur
    show mika grocery smile
    with dissolve
    voice "audio/voices/mik/16.ogg"
    mik "I'll bring by some stew later, Hikaru-kun. Thanks for walking me home!"
    hide mika
    show bg apartment hallway
    with dissolve
    jump main1_2

label main1_2:

    "I unlock and enter the apartment, placing my shoes on the rack by the door."
    scene bg bedroom afternoon with fade
    hik "Home sweet home..."
    stop music fadeout 3.0
    "My voice sounds small and depressed."
    "Ugh... time to log some hours into {i}Celestial Crossing{/i} before anything else happens to remind me how pathetic I am."


    scene bg bedroom night with fade
    "Hours later, I'm feeling pretty good about myself."
    "Mika's beef stew is a distant memory now, and the empty dishes are stacked on top of the incomplete homework assignment I should really get started on."
    "I glance at the clock and realize it's already midnight."
    hik "Crap... I'm gonna fall asleep in class again."
    "It's hard to feel upset about it while staring at Nerith's character screen where the word MAX stares back at me in big green letters over the player level."
    "Happy that I've achieved my goals for the day, I save and log off."
    "I realize belatedly that I'm still wearing my uniform when I topple on top of the covers to get some shut-eye."
    hik "Screw it."
    show bg sky night with fade
    "Agano-sensei will overlook a wrinkled uniform if she can get me to stay awake the whole day for once."
    "With that final thought in mind, I feel myself drift peacefully into slumber."
    "My dreams decide to pick up right where they left off."


    play music "audio/music/Drums of the Deep.mp3"
    scene bg dungeon blur



    show nerith spell
    with fade
    voice "audio/voices/ner/7.ogg"
    Gner "You'd better be okay now, Useless."
    G "Instead of reacting to the new nickname – I'm pretty sure I've earned it by this point – I place a hand on the fully healed wound above my stomach."
    show nerith fight with dissolve
    voice "audio/voices/ner/8.ogg"
    Gner "That was my last healing spell, so if we get mortally injured by the Lich, we're shit out of luck."
    G "She delivers a quick, perfunctory smack to my shoulder and sneers."
    voice "audio/voices/ner/9.ogg"
    Gner "Don't make me regret it."
    show bg dungeon
    hide nerith
    with dissolve
    G "She shoulders her weapon and leads the way toward a set of stairs that spirals down to the lower level of the keep."
    show bg keep with dissolve

    G "I follow, wondering why the layout of the corridor feels so hauntingly familiar."
    G "It hits me that I'm dreaming."
    G "I'm lucid, but this is definitely a dream."

    G "As we continue to trek downward, the details come to me slowly as if I were dragging a waterlogged boat up from the bottom of a lake."
    G "We enter a short, dark corridor that ends in a portal of swirling purple energy."
    G "Nerith approaches it fearlessly, even as the final piece snaps into place within my memory."
    stop music fadeout 3.0
    G "Game."
    G "I'm in the game."
    G "This is the final level of the Lich Lord's Keep, right before the boss, which means... we're about to walk through the portal..."
    G "...right into a veritable mine field of magical traps."
    G "Nerith is almost within reach, and she gives me a strange look as the two of us pass through the portal."
    G "There's no turning back now, and if either of us takes another step, we're going to end up as a smear of charcoal on the floor."
    play music "audio/music/Mystic Force.mp3"


menu:
    "Call out a warning!":
        jump callwarning
    "Pull Nerith back!":

        jump pullherback

label callwarning:
    Ghik "WAIT, NERITH! I KNOW--"
    G "Horrified at my sudden outburst, Nerith lunges at me, slapping her hand painfully across my mouth. Her voice is somewhere between a shout and a whisper when she hisses in my ear."
    show bg keep blur
    show nerith pissed
    with dissolve
    voice "audio/voices/ner/10.ogg"
    Gner "Are you MENTALLY CHALLENGED?! You're going to get us both killed, you stupid piece of--"
    G "A dark, disembodied voice begins chanting from the opposite end of the corridor."
    G "Clearly, even without setting off the traps, we've been noticed."
    voice "audio/voices/ner/11.ogg"
    Gner "SHIT!"
    show bg keep
    hide nerith
    with dissolve
    G "She has time to shoot me a look of pure murder, before we are both engulfed with dark magic."
    G "Flames spurt down the halls, shooting toward us."
    G "Death seems absolutely certain."
    jump main1_3

label pullherback:
    G "I reach out in a blind panic and snatch at Nerith's arm, ready to yank her out of harm's way."
    G "Nerith, however, is having none of it."
    G "Not used to being manhandled, she fights against my grip, squawking in outrage."
    show bg keep blur
    show nerith pissed
    with dissolve
    voice "audio/voices/ner/12.ogg"
    Gner "Hands OFF, Useless!"
    G "I failed to take into account how much stronger than me she actually is."
    G "With a final triumphant jerk, she shakes me off and the momentum carries her that last fateful step into the hallway."
    show bg keep
    hide nerith
    with dissolve
    G "We both freeze at the ominous click of a trap triggering."
    G "Flames and dark magic shoot out from every conceivable surface, blinding us."
    G "Echoing laughter is the last thing we hear as the corridor goes black."
    G "We don't even have time to scream..."
    jump main1_3

label main1_3:


    scene bg bedroom night with fade


    "I wake up, gasping like a fish out of water."
    "I can still taste smoke in my mouth; FEEL magic tendrils crawling along my skin..."
    stop music fadeout 3.0
    "...and then I feel the unmistakable prick of a sharp metal edge against my throat."
    scene overlay black with dissolve
    voice "audio/voices/ner/13.ogg"
    ner "WHAT. HAVE. YOU. DONE?"
    "Attached to the blade is a shaky, purplish-gray arm."
    "Attached to that arm is one seriously pissed off Elven warlock."
    play music "audio/music/Echoes of Time v2.mp3"
    scene cg knife with dissolve
    "I want to shake my head in disbelief, but even my shocked mind realizes that I don't want to accidentally decapitate myself."
    "\"Impossible!\" My mind screams."
    "I'm still dreaming."
    "I have to be..."
    "...but I don't flatter myself that my imagination could come up with these kinds of details."
    "The way her badly singed clothes are hanging from her body in tatters, barely concealing the important bits, and still smoking from the fires in the dream..."
    "The way her eyes dart around the room like a cornered animal..."
    "I'm about to ask her how she – a character I created for a fictional video game – came to be standing in my bedroom when she suddenly speaks, beating me to the punch."
    voice "audio/voices/ner/14.ogg"
    ner "Send me back right now, or I swear... I will GUT you where you stand..."
    $ achievement.grant("Guest")
















    jump main2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
