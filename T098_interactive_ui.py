# T098 interactive UI
# Author: Bilal Chaudhry 101141634
# 30/03/20

from Cimpl import show, save
from T098_user_interface import apply_filter, load_img

filter_choice = ""
run = True
image = None
image_loaded = False
choices = ["L", "S", "2", "3", "X", "T", "P", "E", "I", "V", "H", "Q"]

while run:
    filter_choice = input(
        "L)oad image\tS)ave-as\n2)-tone\t3)-tone\tX)treme contrast\tT)int "
        "sepia\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical"
        "flip\tH)orizontal Flip\nQ)uit\n\n: ")

    # converts input to uppercase 
    filter_choice = filter_choice.upper()

    if filter_choice not in choices:  # Ensures user entered a valid command
        print("Please enter a valid selection.")

    # ensures the user has selected an image
    elif not image_loaded:
        if filter_choice == "L":
            image = load_img()
            show(image)

            image_loaded = True  # user has selected an image
        else:
            print("Please select an image.")

    else:
        if filter_choice == "S":
            save(image)
        elif filter_choice == "Q":
            print("Quitting program...")
            run = False
        else:
            image = apply_filter(image, filter_choice)
            show(image)


