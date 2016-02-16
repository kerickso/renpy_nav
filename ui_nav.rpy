screen ui_nav(location):
        showif location.can_move("right"):
            button:
                #action Return("right")
                xalign 0.95
                yalign 0.5
                action If(location.can_move("right"), true=Return("right"))         
                xfill False
                has hbox
                if location.can_move("right"):
                    text location.right.title
        showif location.can_move("left"):
            button:
                xalign 0.05
                yalign 0.5
                action If(location.can_move("left"), true=Return("left"))         
                xfill False
                has hbox
                if location.can_move("left"):
                    text location.left.title
        showif location.can_move("up"):
            button:
                xalign 0.5
                yalign 0.05
                action If(location.can_move("up"), true=Return("up"))         
                xfill False
                has hbox
                if location.can_move("up"):
                    text location.top.title
        showif location.can_move("down"):
            button:
                xalign 0.5
                yalign 0.95
                action If(location.can_move("down"), true=Return("down"))         
                xfill False
                has hbox
                if location.can_move("down"):
