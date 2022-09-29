
init python:


    #################################################################
    #                        DIR DICTIONARIES                       #
    ################################################################

    # Store the possibilities of each direction based on current location

    # Right
    possibilities_right = {
    "start" : "room_right",
    "room_right" : "start"
    }

    # Left
    possibilities_left = {
    "start" : "room_left",
    "room_left" : "start"
    }

    # Up
    possibilities_up = {
    "start" : "room_up",
    "room_up" : "start"
    }

    # Down
    possibilities_down = {
    "start" : "room_down",
    "room_down" : "start"
    }

    # Stores the label that is currently being on execution, in the variable current_label
    def label_callback(name, abnormal):
        store.current_label = name

    # Updates current_label
    config.label_callback = label_callback

    # Jumps to a specific Label
    def go_to_next(dictionary):
        renpy.jump(switch_next(dictionary))

    # Switching the next label, the parameter is the dir dictionary choosed
    def switch_next(dictionary):
        return dictionary.get(current_label, "start")
