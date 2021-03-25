


init python:
    gallery_cg_items = ["cg knife", "cg undress", "cg romantic", "cg closeup", "cg bus full", "cg bus close", "cg bus noNerith"]
    gal_rows = 2
    gal_cols = 3
    thumbnail_x = 480
    thumbnail_y = 270
    gal_cells = gal_rows * gal_cols
    g_cg = Gallery()

    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

init 1 python:
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))

screen gallery:
    tag menu
    use navigation
    frame background None xpos 200:
        grid gal_rows gal_cols:
            ypos 70
            $ i = 0
            $ next_cg_page = cg_page + 1
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("images/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells):
                null
        frame:
            background None yalign 0.97
            has vbox
            if len(gallery_cg_items)>gal_cells:
                imagebutton auto "images/assets/next_%s.png" xalign 503 yalign 0.5 action [SetVariable('cg_page', next_cg_page), ShowMenu("gallery")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
