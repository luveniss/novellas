








init -1 python hide:





    config.developer = False



    config.screen_width = 1920
    config.screen_height = 1080




    config.window_title = u"Celestial Crossing"



    config.name = "Celestial Crossing"
    config.version = "1.8.3"










    theme.roundrect(
        
        

        
        widget = "#7fa1b3",

        
        widget_hover = "#b38698",

        
        widget_text = "#ffffff",

        
        
        widget_selected = "#fffeed",

        
        disabled = "#dbe4dd",

        
        disabled_text = "#bd9ca9",

        
        
        label = "#fffeed",

        
        frame = "#fffeed",
        
        
        
        mm_root = "images/assets/MainBG.png",

        
        
        
        gm_root = "images/assets/menu.png",
        

        
        
        rounded_window = False,

        
        
        
        )










    style.window.background = Frame("images/textbox3.png", 0, 00)


    style.pref_button.background = Frame("images/assets/button_black.png",10,10)
    style.pref_button.hover_background = Frame("images/assets/button_hover_black.png",10,10)
    style.pref_button.yminimum = 40

    style.pref_label_text.outlines = [(0, "#000", 0, 0)]
    style.pref_label_text.size = 26
    style.pref_label_text.font = "images/assets/YanoneTagesschrift.ttf"

    style.pref_slider.left_bar = "images/assets/slider_full.png"
    style.pref_slider.right_bar = "images/assets/slider_empty.png"
    style.pref_slider.hover_left_bar = "images/assets/slider_hover.png"
    style.pref_slider.ymaximum = 30
    style.pref_slider.xmaximum = 200
    style.pref_slider.thumb = "images/assets/slider_thumb.png"

    style.quick_button_text.font = "images/assets/YanoneTagesschrift.ttf"
    style.pref_button_text.color = "#fff"
    style.pref_button_text.size = 14
    style.pref_button_text.font = "images/assets/YanoneTagesschrift.ttf"
    style.pref_button_text.outlines = [(0, "#fff", 0, 0)]
    style.pref_button_text.hover_outlines = [(0, "#fff", 0, 0)]
    style.pref_button_text.selected_outlines = [(2, "#49518f", 0, 0)]
    style.pref_button_text.selected_hover_outlines = [(2, "#49518f", 0, 0)]





    style.file_picker_nav_button_text.font = "images/assets/YanoneTagesschrift.ttf"
    style.file_picker_nav_button_text.outlines = [(0, "#fff", 0, 0)]

    style.file_picker_nav_button.background = Frame("images/assets/button_black.png",10,10)
    style.file_picker_nav_button.hover_background = Frame("images/assets/button_hover_black.png",10,10)


    style.menu_choice_button.background = Frame("images/assets/button_black.png",28,9)
    style.menu_choice_button.hover_background = Frame("images/assets/button_hover_black.png",28,9)
    style.menu_choice_button.top_padding = 20
    style.menu_choice_button.bottom_padding = 20
    style.pref_slider.thumb_offset = 10

    style.pref_frame.background = Frame("images/assets/button_black.png",28,9)
    style.pref_frame.left_padding = 40
    style.pref_frame.right_padding = 40
    style.pref_frame.top_padding = 20
    style.pref_frame.bottom_padding = 20

    style.pref_frame.left_margin = 20
    style.pref_frame.right_margin = 20

    style.yesno_prompt.background = Frame("images/assets/button_black.png",28,9)














    style.window.left_padding = 300
    style.window.right_padding = 300
    style.window.top_padding = 30
    style.window.bottom_padding = 12



































    style.default.size = 25


    style.default.outlines = [(2, "#222", 0, 0)]

    style.say_label.font = "images/assets/YanoneTagesschrift.ttf"
    style.say_label.bold = False




    style.menu_choice.font = "images/assets/YanoneTagesschrift.ttf"
    style.menu_choice_button.font = "images/assets/YanoneTagesschrift.ttf"
    style.menu_choice.outlines = [(0, "#222", 0, 0)]








    config.has_sound = False



    config.has_music = True



    config.has_voice = True

















    config.main_menu_music = "audio/music/Crowd Hammer.mp3"












    config.help = "README.html"






    config.enter_transition = fade


    config.exit_transition = fade


    config.intra_transition = dissolve


    config.main_game_transition = dissolve


    config.game_main_transition = dissolve


    config.end_splash_transition = None


    config.end_game_transition = fade


    config.after_load_transition = fade


    config.window_show_transition = dissolve


    config.window_hide_transition = dissolve


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = dissolve


    config.exit_yesno_transition = dissolve


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None





python early:
    config.save_directory = "CelestialCrossingSave-1-8-3"

init -1 python hide:









    config.default_fullscreen = True



    config.default_text_cps = 50



    config.default_afm_time = 10







init python:




    build.directory_name = "Celestial-Crossing-1.8.3"




    build.executable_name = "CelestialCrossing"



    build.include_update = False





























    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
