











screen say(who, what, side_image=None, two_window=False):


    if not two_window:


        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu








screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:

                button:
                    action action
                    style "menu_choice_button"

                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.33)
        xmaximum int(config.screen_width * 0.33)








screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu():
    tag menu




    window:
        style "mm_root"



        style_group "mm"
        xalign .98
        yalign .98



        has vbox:
            at Position(xpos = 0.8, xanchor=0.5, ypos=0.74, yanchor=0.5)

        imagebutton auto "images/assets/start_%s.png" action Start()
        imagebutton auto "images/assets/load_%s.png" action ShowMenu("load")
        imagebutton auto "images/assets/gallery_%s.png" action ShowMenu("gallery")
        imagebutton auto "images/assets/preferences_%s.png" action ShowMenu("preferences")
        imagebutton auto "images/assets/help_%s.png" action Help()
        imagebutton auto "images/assets/quit_%s.png" action Quit(confirm=True)
















init -2:


    style mm_button:
        size_group "mm"









screen navigation():


    window:
        style "gm_root"

        xalign .98
        yalign .98

        has vbox:
            at Position(xpos = 0.8, xanchor=0.5, ypos=0.74, yanchor=0.5)

        imagebutton auto "images/assets/return_%s.png" action Return()
        imagebutton auto "images/assets/save_%s.png" action ShowMenu("save")
        imagebutton auto "images/assets/load_%s.png" action ShowMenu("load")
        imagebutton auto "images/assets/gallery_%s.png" action ShowMenu("gallery")
        imagebutton auto "images/assets/preferences_%s.png" action ShowMenu("preferences")
        imagebutton auto "images/assets/main_%s.png" action MainMenu()















init -2:


    style gm_nav_button:
        size_group "gm_nav"













screen file_picker():

    frame:
        style "file_picker_frame"
        background Frame("images/assets/button_black.png",28,9)
        top_padding 20
        bottom_padding 20
        left_padding 80
        right_padding 80

        top_margin 20
        bottom_margin 20
        left_margin 80
        right_margin 80

        has vbox



        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5


        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True
                    background Frame("images/assets/button_black.png",28,9)
                    hover_background Frame("images/assets/button_hover_black.png",28,9)
                    top_padding 20
                    bottom_padding 20
                    left_padding 20
                    right_padding 20


                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "   [file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():
    tag menu



    use navigation
    use file_picker

screen load():
    tag menu



    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text








screen preferences():
    tag menu



    use navigation


    grid 3 1:
        style_group "prefs"
        xfill True


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")













            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")


                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0








screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .3
        ypos .5
        yanchor 0.5
        ypadding .05
        background Frame("images/assets/button_black.png",28,9)

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action

init -2:

    style yesno_button:
        background Frame("images/assets/button_black.png",28,9)
        hover_background Frame("images/assets/button_hover_black.png",28,9)
        font "images/assets/YanoneTagesschrift.ttf"
        top_padding 20
        bottom_padding 20
        left_padding 80
        right_padding 80
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        outlines [(0, "#fff", 0, 0)]
        size 26
        font "images/assets/YanoneTagesschrift.ttf"
        layout "subtitle"

    style yesno_button_text:
        font "images/assets/YanoneTagesschrift.ttf"
        outlines [(0, "#fff", 0, 0)]
        size 26

    style file_picker_frame:
        left_margin 80
        outlines [(0, "#fff", 0, 0)]
        font "images/assets/YanoneTagesschrift.ttf"

    style file_picker:
        left_margin 80
        outlines [(0, "#fff", 0, 0)]
        font "images/assets/YanoneTagesschrift.ttf"

    style file_picker_text:
        left_margin 80
        outlines [(0, "#fff", 0, 0)]
        font "images/assets/YanoneTagesschrift.ttf"







screen quick_menu():


    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')



        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action Show("esc_menu", dissolve)

init -2:
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 20
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
