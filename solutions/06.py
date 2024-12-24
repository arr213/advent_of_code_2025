def read_input(file_path):
    with open(file_path, 'r') as file:
        maze = file.read().strip()

    return maze


def walk_the_maze(maze):
    # You start by making a map (your puzzle input) of the situation. For example:
    # ....#.....
    # .........#
    # ..........
    # ..#.......
    # .......#..
    # ..........
    # .#..^.....
    # ........#.
    # #.........
    # ......#...
    # The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

    # The guard can move in any of the four cardinal directions (up, down, left, right), but cannot move through obstructions. The guard can also rotate 90 degrees to the right. The guard can rotate in place or move in the direction they are facing.
    # The guard will always walk straight until they hit an obstruction or the edge of the map. The guard will always rotate 90 degrees to the right when they hit an obstruction.
    # The guard will keep walking until they walk off of the map in the direction they are facing.
    # The guard starts by facing up.
    # We do not know the dimensions of the map in advance, but we know that the map is a rectangle.

    directions = ['up', 'right', 'down', 'left']
    direction = 'up'
    maze_rows = maze.splitlines()
    x, y = 0, 0
    for row in maze_rows:
        if '^' in row:
            x = row.index('^')
            y = maze_rows.index(row)
            break

    while 0 <= x < len(maze_rows[0]) and 0 <= y < len(maze_rows):
        if maze_rows[y][x] == '#':
            direction = directions[(directions.index(direction) + 1) % 4]
        elif direction == 'up':
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1  


if __name__ == '__main__':
    lines = read_input('solutions/06.txt')
    print(lines)