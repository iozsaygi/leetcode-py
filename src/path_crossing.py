# https://leetcode.com/problems/path-crossing/

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Utilities:

    # Linear search to determine if the point is already visited.
    @staticmethod
    def is_point_visited(point: Point, visited_points: list) -> bool:
        for visited_point in visited_points:
            if visited_point.x == point.x and visited_point.y == point.y:
                return True

        return False


class Solution:

    @staticmethod
    def path_crossing_iteration_0(path: str) -> bool:
        origin = Point(0, 0)
        current = origin

        visited_points = [current]

        for character in path:
            if character == 'N':
                change = Point(0, 1)
            elif character == 'S':
                change = Point(0, -1)
            elif character == 'W':
                change = Point(-1, 0)
                visited_points.append(current)
            elif character == 'E':
                change = Point(1, 0)
            else:
                change = Point(0, 0)

            destination = current + change
            if Utilities.is_point_visited(destination, visited_points):
                return True
            else:
                current = destination
                visited_points.append(destination)

        return False
