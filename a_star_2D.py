import heapq

# Define the 8 possible movement directions (horizontal, vertical, diagonal)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (-1, -1), (1, -1), (-1, 1)]


def heuristic(a, b):
    # Calculate the Manhattan distance as the heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, (0, start))
    g_score = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for dx, dy in directions:
            neighbor = current[0] + dx, current[1] + dy

            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, 0):
                continue

            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None  # No path found


# Define your grid with obstacles (0 = passable, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Define start and goal coordinates
start = (0, 0)
goal = (4, 4)

came_from = {}
path = astar(grid, start, goal)

if path:
    print("Path:", path)
else:
    print("No path found.")
