from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice


# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = 2


def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    dice_type = int(document.querySelector("#diceType").value)


def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    number_of_dice = int(document.querySelector("#diceNumber").value)
    for x in range(number_of_dice):
        result = dice.dice_roll(dice_type)
        document.querySelector("div#result").innerHTML += str(result) + "<br>"


def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#result").innerHTML = ""

