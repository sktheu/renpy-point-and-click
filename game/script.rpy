
define e = Character("Eileen")


label start:
    scene bg start

    show eileen happy

    e "Hello! What direction do you want to go?"

    # Testing
    menu:
        "{b}Choose a direction:{/b}"

        "Right":
            $ go_to_next(possibilities_right)
        "Left":
            $ go_to_next(possibilities_left)
        "Up":
            $ go_to_next(possibilities_up)
        "Down":
            $ go_to_next(possibilities_down)

    return


label room_right:
    scene bg room_right

    e "Now you are in the right room!"

    menu:
        "{b}You want to go back?{/b}"

        "Yes":
            $ go_to_next(possibilities_right)
        "No":
            return

    return

label room_left:
    scene bg room_left

    e "Now you are in the left room!"

    menu:
        "{b}You want to go back?{/b}"

        "Yes":
            $ go_to_next(possibilities_left)
        "No":
            return

    return

label room_up:
    scene bg room_up

    e "Now you are in the up room!"

    menu:
        "{b}You want to go back?{/b}"

        "Yes":
            $ go_to_next(possibilities_up)
        "No":
            return

    return

label room_down:
    scene bg room_down

    e "Now you are in the down room!"

    menu:
        "{b}You want to go back?{/b}"

        "Yes":
            $ go_to_next(possibilities_down)
        "No":
            return

    return
