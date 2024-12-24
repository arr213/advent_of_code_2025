def read_input(file_path):
    col1 = []
    col2 = []
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()
        for line in lines:
            i1, i2 = line.split('   ')
            col1.append(i1)
            col2.append(i2)

    return col1, col2


def get_total_distance(col1, col2) -> int:
    total_distance = 0
    col1, col2 = sorted(col1), sorted(col2)
    # loop through sorted col1 and col2 in one loop
    # convert col1 and col2 to integers
    for i in range(len(col1)):
        total_distance += abs(int(col1[i]) - int(col2[i]))
    return total_distance


def get_similarity_score(col1, col2) -> int:
    similarity_score = 0
    # create a map that has the count of the number of occurence of each number in col2
    col2_count = {i: col2.count(i) for i in col2}
    for i in range(len(col1)):
        try: 
            count = col2_count[col1[i]]
        except KeyError:
            count = 0
        similarity_score += int(col1[i]) * count
    return similarity_score 


if __name__ == '__main__':
    c1, c2 = read_input('solutions/01.txt')
    total = get_total_distance(c1, c2)
    print(total == 1830467)
    similarity = get_similarity_score(c1, c2)
    print(similarity == 26674158)

