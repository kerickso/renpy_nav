init -1 python:
    class Location(object):
        def __init__(self, label, name):
            self.label = label
            self.left = None
            self.right = None
            self.top = None
            self.bottom = None
            self.title = name

        def add_left(self, left):
            self.left = left

        def add_right(self, right):
            self.right = right

        def add_top(self, top):
            self.top = top

        def add_bottom(self, bottom):
            self.bottom = bottom

        def del_left(self, left):
            self.left = None

        def del_right(self, right):
            self.right = None

        def del_top(self, top):
            self.top = None

        def del_bottom(self, bottom):
            self.bottom = None

        def go_left(self):
            if self.left != None:
                return self.left.label
            else:
                return self.label

        def go_right(self):
            if self.right != None:
                return self.right.label
            else:
                return self.label

        def go_top(self):
            if self.top != None:
                return self.top.label
            else:
                return self.label

        def go_bottom(self):
            if self.bottom != None:
                return self.bottom.label
            else:
                return self.label

        def can_move(self, direction):
            if direction == "up":
                if self.go_top() != self.label:
                    return True
            if direction == "down":
                if self.go_bottom() != self.label:
                    return True
            if direction == "left":
                if self.go_left() != self.label:
                    return True
            if direction == "right":
                if self.go_right() != self.label:
                    return True

        def screen_loop(self):
            while True:
                result = ui.interact()                    
                
                if result == "right":
                    if self.can_move("right"):
                        renpy.jump(self.go_right())
                elif result == "left":
                    if self.can_move("left"):
                        renpy.jump(self.go_left())
                elif result == "up":
                    if self.can_move("up"):
                        renpy.jump(self.go_top())
                elif result == "down":
                    if self.can_move("down"):
                        renpy.jump(self.go_bottom())


    





