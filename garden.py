"""
Introduction
Given a diagram, determine which plants each child in the kindergarten class is responsible for.

The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.

They've chosen to grow grass, clover, radishes, and violets.

To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.

[window][window][window]
........................ # each dot represents a cup
........................
There are 12 children in the class:

Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.

The following diagram represents Alice's plants:

[window][window][window]
VR......................
RG......................
In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.

Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, it should be able to determine which plants belong to each student.

For example, if it's told that the garden looks like so:

[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
Then if asked for Alice's plants, it should provide:

Violets, radishes, violets, radishes
While asking for Bob's plants would yield:

Clover, grass, clover, clover
"""

students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

sample_row1 = ["V", "R", "C", "G", "V", "V", "R", "V", "C", "G", "G",
               "C", "C", "G", "V", "R", "G", "C", "V", "C", "G", "C", "G", "V"]
sample_row2 = ["V", "R", "C", "C", "C", "G", "C", "R", "R", "G", "V",
               "C", "G", "C", "R", "V", "V", "C", "V", "G", "C", "G", "C", "V"]

veggies = {
    "G": "Grass",
    "C": "Clovers",
    "R": "Raddishes",
    "V": "Violets"
}


def get_one_student(student, row1, row2):
    veggie_keys = []
    ret = []
    i = students.index(student)
    position = i * 2
    veggie_keys.append(row1[position])
    veggie_keys.append(row1[position + 1])
    veggie_keys.append(row2[position])
    veggie_keys.append(row2[position + 1])
    for key in veggie_keys:
        full_name = veggies[key]
        ret.append(full_name)
    print(ret)
    return ret


get_one_student("Alice", sample_row1, sample_row2)
get_one_student("Bob", sample_row1, sample_row2)
get_one_student("Charlie", sample_row1, sample_row2)
