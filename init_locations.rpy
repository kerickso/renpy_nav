##### Step 1: SET UP ALL THE LOCATION OBJECTS #####
init 1 python:
    # Just in case the UI nav has been popped up....
    renpy.hide_screen("ui_nav")

    location1 = Location("location1", "Room A")
    location2 = Location("location2", "Room B")
    location1.add_bottom(location2)
    location2.add_left(location1)



###### Step 2: SET UP ALL THE REN'PY TAGS: #####
label location1:
    scene location1
    python:
        renpy.hide_screen("ui_nav")
        check_location(location1)
    python:
        renpy.show_screen("ui_nav", location1)
        location1.screen_loop()
    return

label location2:
    scene location2
    python:
        renpy.hide_screen("ui_nav")
        check_location(location2)
    python:
        renpy.show_screen("ui_nav", location2)
        location2.screen_loop()
    return





