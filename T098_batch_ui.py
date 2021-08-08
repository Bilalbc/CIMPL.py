# T098 Batch file interpreter
# Author: Bilal Chaudhry 101141634
# 30/03/20

from Cimpl import choose_file, load_image, show, save_as
from T098_user_interface import apply_filter

batch_file = choose_file()
batch = open(batch_file, "r")

for line in batch:
    temp = line.split()
    image = load_image(temp[0])
    save_location = temp[1]

    for i in range(2, len(temp)):
        image = apply_filter(image, temp[i])
    show(image)
    save_as(image, save_location)

batch.close()
