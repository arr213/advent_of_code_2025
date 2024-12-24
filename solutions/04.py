def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
    return lines


def word_search(haystack: list[str], needle: str) -> int:
    needle_len = len(needle)
    match_count = 0
    num_rows = len(haystack)
    num_cols = len(haystack[0])  # Assuming all rows have the same length

    # Loop through all positions in the grid
    for y in range(num_rows):
        for x in range(num_cols):
            # horizontal check
            if (x + needle_len <= num_cols and
                    haystack[y][x:x + needle_len] == needle):
                match_count += 1
            if (x + needle_len <= num_cols and
                    haystack[y][x:x + needle_len][::-1] == needle):
                match_count += 1

            # vertical check 
            # (check if there are enough rows below to fit the needle)
            if y + needle_len <= num_rows:
                vertical_str = ''.join(
                    haystack[y + i][x] for i in range(needle_len)
                )
                if vertical_str == needle:
                    match_count += 1
                if vertical_str[::-1] == needle:
                    match_count += 1

            # diagonal check 
            # (down-right, check if there are enough rows and columns)
            if x + needle_len <= num_cols and y + needle_len <= num_rows:
                # Only attempt to build the diagonal string 
                # if there is enough space
                diagonal_str = ''.join(
                    haystack[y + i][x + i] for i in range(needle_len)
                )
                if len(diagonal_str) == needle_len:  
                    # Ensure we have a complete diagonal
                    if diagonal_str == needle:
                        match_count += 1
                    if diagonal_str[::-1] == needle:
                        match_count += 1

            # diagonal check 
            # (down-left, check if there are enough rows and columns)
            if x - needle_len + 1 >= 0 and y + needle_len <= num_rows:
                # Only attempt to build the diagonal string 
                # if there is enough space
                diagonal_str = ''.join(
                    haystack[y + i][x - i] for i in range(needle_len)
                )
                if len(diagonal_str) == needle_len:  
                    # Ensure we have a complete diagonal
                    if diagonal_str == needle:
                        match_count += 1
                    if diagonal_str[::-1] == needle:
                        match_count += 1

    return match_count


def search_for_cross(haystack, needle):
    """Search for the needle in a cross pattern."""
    match_count = 0
    num_rows = len(haystack)
    num_cols = len(haystack[0])  # Assuming all rows have the same length

    # Loop through all positions in the grid
    for y in range(num_rows):
        for x in range(num_cols):
            # Check if the needle can fit in the cross pattern
            if x + 2 < num_cols and y + 2 < num_rows:
                partial_match_count = 0
                # Check if the needle is in the cross pattern
                if (haystack[y][x] == needle[0] and
                        haystack[y + 1][x + 1] == needle[1] and
                        haystack[y + 2][x + 2] == needle[2]):
                    partial_match_count += 1
                if (haystack[y][x + 2] == needle[0] and
                        haystack[y + 1][x + 1] == needle[1] and
                        haystack[y + 2][x] == needle[2]):
                    partial_match_count += 1
                if (haystack[y][x] == needle[2] and
                        haystack[y + 1][x + 1] == needle[1] and
                        haystack[y + 2][x + 2] == needle[0]):
                    partial_match_count += 1
                if (haystack[y][x + 2] == needle[2] and
                        haystack[y + 1][x + 1] == needle[1] and
                        haystack[y + 2][x] == needle[0]):
                    partial_match_count += 1
                if partial_match_count == 2:
                    match_count += 1

    return match_count


if __name__ == '__main__':
    lines = read_input('solutions/04.txt')
    print(word_search(lines, 'XMAS') == 2406)
    print(search_for_cross(lines, 'MAS') == 1807)
