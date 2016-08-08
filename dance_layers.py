import sys
import json
from random import choice

START_WITH_FEET = True


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as inputs:
        file_contents = inputs.read()
        as_dict = json.loads(file_contents)
        first_part = "feet" if START_WITH_FEET else choice(as_dict.keys())
        first = choice(as_dict.pop(first_part))
        second_part = choice(as_dict.keys())
        second = choice(as_dict.pop(second_part))
        third_part = choice(as_dict.keys())
        third = choice(as_dict.pop(third_part))
        print "Start with {}: {},\nAdd {}: {},\nThen add {}: {}".format(
            first_part, first, second_part, second, third_part, third)

