import re


def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
    return lines


def multiply_lines(lines):
    # use regex to match the line to 'mul(\d+, \d+)'
    # except the numbers can only be integers between 1 and 3 digits long.
    # It should grab as many matches as there are in the line.
    # Then, split the matches by ', ' and multiply them together.
    # Finally, sum all the results.
    # For example, consider the following section of corrupted memory:
    # xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    # Only the four highlighted sections are real mul instructions.
    # Adding up the result of each instruction produces 161
    # (2*4 + 5*5 + 11*8 + 8*5).

    return sum(
        sum(
            int(x) * int(y)
            for x, y, in [
                match.split(',')
                for match in re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
            ]

        )
        for line in lines
    )


def multiply_if_commanded(lines):
    usable_text = get_usable_text('\n'.join(lines), 'do', '')
    return sum(
        sum(
            int(x) * int(y)
            for x, y, in [
                match.split(',')
                for match in re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
            ]

        )
        for line in usable_text.split('\n')
    )


def get_usable_text(haystack, last_command, usable_text):
    # If the haystack is empty, return the usable_text.
    if not haystack:
        return usable_text

    # If the haystack is not empty, process the first part.
    # Check for a 'do()' or 'don't()' command and adjust accordingly.
    else:
        # If last_command was 'do', look for 'don't()'
        if last_command == 'do':
            match = re.search(r"don\'t\(\)", haystack)
            # Look for don't() in haystack
            if not match:
                return usable_text + '\n' + haystack
                # No 'don't()', append whole haystack
            i = match.start()  # Find the starting index of 'don't()'
            return get_usable_text(
                haystack[i + len("don\'t()"):],  # Skip past the 'don't()' part
                'do_not',  # Update last_command to 'do_not'
                usable_text + '\n' + haystack[:i]
                # Append up to 'don't()' to usable_text
            )
        # If last_command was 'do_not', look for 'do()'
        else:
            match = re.search(r"do\(\)", haystack)  # Look for do() in haystack
            if not match:
                return usable_text
                # No 'do()', return the usable_text as it is
            i = match.start()  # Find the starting index of 'do()'
            return get_usable_text(
                haystack[i + len("do()"):],  # Skip past the 'do()' part
                'do',  # Update last_command to 'do'
                usable_text  # No changes to usable_text in this case
            )


if __name__ == '__main__':
    lines = read_input('solutions/03.txt')
    print(multiply_lines(lines) == 166357705)
    print(multiply_if_commanded(lines) == 88811886)
