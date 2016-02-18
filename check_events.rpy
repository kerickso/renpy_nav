init 2 python:
    def check_location(location):
        if(location.label == "location1" && been_to_a == 0):
            renpy.call("RoomA00")
        else if(location.label == "location1")
            renpy.call("RoomA")
	if(location.label == "Finish")
            renpy.jump("EndGame")

RoomA00:
    "This is the first time you've been in Room A."
    python:
        been_to_a ++;
    return

RoomA:
    "You've been here before. But that door sure wasn't."
    python:
        location1.del_top()
        location2.add_bottom(EndGame)
    return

EndGame:
    "It's the end, you know?"
    return
