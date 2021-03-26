







image agano laugh = "images/sp/aga/agano_laugn.png"
image agano plain:
    "images/sp/aga/agano_plain.png"


    choice:
        3.5
    choice:
        1.5
    "images/sp/aga/agano_plain_blink.png"
    .10
    repeat

image agano happy:
    "images/sp/aga/agano_smile.png"


    choice:
        3.5
    choice:
        1.5
    "images/sp/aga/agano_smile_blink.png"
    .10
    repeat

image agano shock:
    "images/sp/aga/agano_shock.png"


    choice:
        3.5
    choice:
        1.5
    "images/sp/aga/agano_shock_blink.png"
    .10
    repeat

image yama angry = "images/sp/yam/yama angry.png"
image yama shock = "images/sp/yam/yama shock.png"
image yama frozen = "images/sp/yam/yama frozen.png"

image bob normal = "images/sp/bob/bob smile.png"
image bob think = "images/sp/bob/bob think.png"


image bg sky afternoon = "images/bg/Evening_clouds_C_01.png"
image bg sky night = "images/bg/nightsky.png"
image bg sky dusk = "images/bg/dusk.png"

image bg dungeon = "images/bg/cave1.jpg"
image bg dungeon blur = "images/bg/cave1_blur30.jpg"

image bg keep = "images/bg/castle_inside1.jpg"
image bg keep blur = "images/bg/castle_inside1_blur30.jpg"

image bg classroom = "images/bg/classroom.jpg"
image bg classroom blur = "images/bg/classroom_blur.jpg"

image bg hallway = "images/bg/hallway_school.jpg"
image bg hallway blur = "images/bg/hallway_school_blur.jpg"

image bg street afternoon = "images/bg/street2.jpg"
image bg street afternoon blur = "images/bg/street2_blur.jpg"

image bg apartment hallway = "images/bg/apartment building corridor_final.jpg"
image bg apartment hallway blur = "images/bg/apartment building corridor_final_blur.jpg"

image bg livingroom = "images/bg/living_room.jpg"
image bg livingroom blur = "images/bg/living_room_blur.jpg"

image bg livingroom rekt = "images/bg/living_room_destroyed.jpg"
image bg livingroom rekt blur = "images/bg/living_room_destroyed_blur.jpg"

image bg bedroom afternoon = "images/bg/bedroom_final.jpg"
image bg bedroom afternoon blur = "images/bg/bedroom_blur.jpg"

image bg bedroom night = "images/bg/bedroom_night.jpg"
image bg bedroom night blur = "images/bg/bedroom_night_blur.jpg"

image bg bedroom morning = "images/bg/bedroom_morning_final.jpg"
image bg bedroom morning blur = "images/bg/bedroom_morning_final_blur.jpg"

image bg bedroom gray = "images/bg/bedroom_gray.jpg"

image bg mall = "images/bg/mall.jpg"
image bg mall blur = "images/bg/mall_blur.jpg"

image bg convention = "images/bg/convention.jpg"
image bg convention blur = "images/bg/convention_blur.jpg"

image bg door = "images/bg/warp.png"

image overlay endof c1 = "images/assets/endscreen.png"
image overlay credits = "images/assets/Reel_long.png"
image overlay black = "images/assets/black.jpg"


init:
    image cg knife = "images/cg/morroniifen.png"
    image cg undress = "images/cg/undressZ.png"
    image cg romantic = "images/cg/romantic.png"
    image cg closeup = "images/cg/closeup.png"
    image cg bus full = "images/cg/bus_full.png"
    image cg bus close = "images/cg/bus_close.png"
    image cg bus noNerith = "images/cg/bus_noNer.png"

image splash1 = "images/assets/white.png"
image splash2 = "images/assets/logo.png"


define G = Character(' ', color="#666", what_color="#ffffff", window_background="FrameC.png", window_left_padding=100, window_right_padding=400, window_top_padding=105, window_yminimum=300, window_ypos=0.5, window_yanchor=-0.5)

define ner = Character('Нерит', color="#92b3b2")
define Gner = Character('Нерит', color="#9cd7d5", what_color="#ffffff", window_background="FrameC.png", window_left_padding=100, window_right_padding=400, window_top_padding=140, window_yminimum=300, window_ypos=0.5, window_yanchor=-0.5)

define hik = Character('Хикару', color="#d9cd7b")
define Ghik = Character('Хикару', color="#d9cd7b", what_color="#ffffff", window_background="FrameC.png", window_left_padding=100, window_right_padding=400, window_top_padding=140, window_yminimum=300, window_ypos=0.5, window_yanchor=-0.5)

define aga = Character('Агано-сенсей', color="#eccdff")

define mik = Character('Мика', color="#f87496")

define boy = Character('Yamaguchi-san', color="#e87575")
define dev = Character('Game developer', color="#ba95dd")


screen esc_menu:
    modal True

    frame background None:
        has vbox



        window:




            xalign 0.0
            yalign 0
            xpos -6
            ypos -6
            xmargin 0
            ymargin 0

            background "images/ol/fade.png"

            has vbox:
                at Position(xpos = 0.5, xanchor=0.5, ypos=1.2, yanchor=0.5)
            imagebutton auto "images/assets/main_%s.png" action MainMenu()
            imagebutton auto "images/assets/save_%s.png" action ShowMenu("save")
            imagebutton auto "images/assets/load_%s.png" action ShowMenu("load")
            imagebutton auto "images/assets/preferences_%s.png" action ShowMenu("preferences")
            imagebutton auto "images/assets/return_%s.png" action Hide("esc_menu", dissolve)
            key "game_menu" action Hide("esc_menu", dissolve)

init python:
    config.game_menu_action = [ FileTakeScreenshot(), Show("esc_menu", transition=dissolve) ]

    def bravery_count(amount):
        global count
        stamina += amount

label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .30
        achievement.Sync()



    $ overriding_on=True
    scene splash1
    $ renpy.pause(1.0, hard='True')
    scene splash2 with dissolve
    $ renpy.pause(3.0, hard='True')

    scene splash1 with dissolve
    $ renpy.pause(1.0, hard='True')
    $ overriding_on=False
    return



label start:
    $ count = 0


    jump ready
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
