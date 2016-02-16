init 2 python:
    def check_location(location):
        if(location.label == "location1"):
            renpy.call("label1")

label1:
    "You've made it back to Room A."
    return
