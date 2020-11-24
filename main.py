import json
import random


def parse_comp1(data, str_value):
    commands = [row.copy() for row in data if 'function' in row and row['function'] == str_value]
    return commands


# doing this with list compression will not be more readable
def put_together_lists(commands):
    counter = 0
    for row in commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    return functional_commands


def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())


    parse_commands = parse_comp1(data,'parse')

    print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())

    copy_commands = parse_comp1(data, 'copy')
    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = put_together_lists(parse_commands)
    functional_commands1 = put_together_lists(copy_commands)

    print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
