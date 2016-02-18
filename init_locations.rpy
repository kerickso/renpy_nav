##### Step 1: SET UP ALL THE LOCATION OBJECTS #####
init 1 python:
    # Just in case the UI nav has been popped up....
    renpy.hide_screen("ui_nav")

    location1 = Location("location1", "Room A")
    location2 = Location("location2", "Room B")
    location1.add_top(location2)
    location2.add_bottom(location1)

    location3 = Location("location3", "Room C")
    location2.add_left(location3)    



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
    "Feel free to go back whenever you want to."
    python:
        renpy.hide_screen("ui_nav")
        check_location(location2)
    python:
        renpy.show_screen("ui_nav", location2)
        location2.screen_loop()
    return

label location3:
    scene location3
    "Or not. Let's keep moving forward."
    python:
        renpy.hide_screen("ui_nav")
        check_location(location3)
    python:
        renpy.show_screen("ui_nav", location3)
        location3.screen_loop()
    return

 



