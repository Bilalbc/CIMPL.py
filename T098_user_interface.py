# T098 User Interface helper functions
# Author: Bilal Chaudhry 101141634
# 30/03/20

from T098_image_filters import *


def load_img():
    """
    function used to load an image selected by the user
    
    >>> load_img()
    """
    img = load_image(choose_file())
    return img


def get_thresh():
    """
    function used to get a threshold value from the user.
    
    >>> get_thresh()
    
    Please enter a threshold value:
    15
    """
    return float(input("Please enter a threshold value:"))


def apply_filter(img: Image, filter_name: str) -> Image:
    """
    function used to apply the desired filter to an image. takes an image for 
    the filter to be applied to, and a character, which specifies the filter
    to be applied. returns the filtered image.
    
    >>> apply_filter("miss_sullivan.jpg", "S")
    
    """
    if filter_name == "2":
        img = two_tone(img, "yellow", "cyan")

    elif filter_name == "3":
        img = three_tone(img, "yellow", "magenta", "cyan")

    elif filter_name == "X":
        img = extreme_contrast(img)

    elif filter_name == "T":
        img = sepia(img)

    elif filter_name == "P":
        img = posterize(img)

    elif filter_name == "E":
        thresh = get_thresh()
        img = detect_edges(img, thresh)

    elif filter_name == "I":
        thresh = get_thresh()
        img = detect_edges_better(img, thresh)

    elif filter_name == "V":
        img = flip_vertical(img)

    elif filter_name == "H":
        img = flip_horizontal(img)

    return img
