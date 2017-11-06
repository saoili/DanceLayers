import sys
import json
from random import choice

START_WITH_FEET = True


def part_and_move(dance_parts, part=None):
    if not part:
        part = choice(list(dance_parts.keys()))
    move = choice(dance_parts.pop(part))
    return part, move


def get_parts(dance_parts, start_with_feet=None):
    first_part = "feet" if start_with_feet else None
    first_part, first_move = part_and_move(dance_parts, first_part)
    second_part, second_move = part_and_move(dance_parts)
    third_part, third_move = part_and_move(dance_parts)
    return (
        (first_part, first_move),
        (second_part, second_move),
        (third_part, third_move)
    )


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as inputs:
        file_contents = inputs.read()
        dance_parts = json.loads(file_contents)
        first, second, third = get_parts(dance_parts, START_WITH_FEET)
        first_part, first_move = first
        second_part, second_move = second
        third_part, third_move = third

        print (
            "Start with {}: {},\nAdd {}: {},\nThen add {}: {}".format(
                first_part, first_move, second_part, second_move,
                third_part, third_move
            )
        )
