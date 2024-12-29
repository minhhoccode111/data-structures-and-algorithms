# python 3


# given 25 square pieces with colored edges, arrange them in a 5x5 grid such
# that touching edges share the same color and outer edges are black


from math import sqrt
from itertools import permutations


class PuzzleAssembly:
    def __init__(self, squares):
        self.squares = squares
        self.color_map, self.id_map = self.create_color_map(self.squares)
        self.internal_squares = self.convert_to_internal(self.squares, self.color_map)

    @staticmethod
    def create_color_map(squares):
        color_to_id = {}
        id_to_color = []
        color_to_id["black"] = 0
        id_to_color.append("black")
        index = 1
        for square in squares:
            for color in square:
                if color not in color_to_id:
                    color_to_id[color] = index
                    id_to_color.append(color)
                    index += 1
        return color_to_id, id_to_color

    @staticmethod
    def convert_to_internal(squares, color_to_id):
        internal = []
        for square in squares:
            internal_square = tuple(color_to_id[color] for color in square)
            internal.append(internal_square)
        return tuple(internal)

    @classmethod
    def read_input(cls, n):
        squares = []
        for _ in range(n):
            raw = input().strip()
            formatted = raw[1:-1]
            square = tuple(formatted.split(","))
            squares.append(square)
        return cls(tuple(squares))

    @staticmethod
    def print_result(grid):
        for row in grid:
            row_strings = ["(" + ",".join(square) + ")" for square in row]
            print(";".join(row_strings))

    def solve(self):
        n = int(sqrt(len(self.internal_squares)))
        pos = [[-1] * n for _ in range(n)]
        edges = {"up": [], "left": [], "down": [], "right": []}
        inner_squares = []

        for idx, (top, left, bottom, right) in enumerate(self.internal_squares):
            if top == left == 0:
                pos[0][0] = idx
                continue
            elif top == right == 0:
                pos[0][n - 1] = idx
                continue
            elif left == bottom == 0:
                pos[n - 1][0] = idx
                continue
            elif bottom == right == 0:
                pos[n - 1][n - 1] = idx
                continue

            if top == 0 and left != 0 and right != 0:
                edges["up"].append(idx)
                continue
            elif left == 0 and top != 0 and bottom != 0:
                edges["left"].append(idx)
                continue
            elif bottom == 0 and left != 0 and right != 0:
                edges["down"].append(idx)
                continue
            elif right == 0 and top != 0 and bottom != 0:
                edges["right"].append(idx)
                continue

            inner_squares.append(idx)

        solution = self.arrange(pos, edges, inner_squares)
        result = [[""] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                result[r][c] = self.squares[solution[r][c]]
        return result

    def arrange(self, pos, edges, inner_squares):
        n = len(edges["up"]) + 2
        inner_dim = len(edges["up"])
        for up_order in permutations(edges["up"]):
            for i, idx in enumerate(up_order):
                pos[0][i + 1] = idx
            if not self.validate_edges(pos[0], 3, 1):
                continue
            for left_order in permutations(edges["left"]):
                for i, idx in enumerate(left_order):
                    pos[i + 1][0] = idx
                if not self.validate_edges([row[0] for row in pos], 2, 0):
                    continue
                for down_order in permutations(edges["down"]):
                    for i, idx in enumerate(down_order):
                        pos[n - 1][i + 1] = idx
                    if not self.validate_edges(pos[n - 1], 3, 1):
                        continue
                    for right_order in permutations(edges["right"]):
                        for i, idx in enumerate(right_order):
                            pos[i + 1][n - 1] = idx
                        if not self.validate_edges([row[n - 1] for row in pos], 2, 0):
                            continue
                        for inner_order in permutations(inner_squares):
                            for k, idx in enumerate(inner_order):
                                r = k // inner_dim
                                c = k % inner_dim
                                pos[r + 1][c + 1] = idx
                            if self.verify(pos):
                                return pos
        return None

    def validate_edges(self, line, side1, side2):
        for i in range(1, len(line)):
            if (
                self.internal_squares[line[i - 1]][side1]
                != self.internal_squares[line[i]][side2]
            ):
                return False
        return True

    def verify(self, pos):
        n = len(pos)
        for r in range(1, n):
            for c in range(1, n):
                if (
                    self.internal_squares[pos[r][c - 1]][3]
                    != self.internal_squares[pos[r][c]][1]
                ):
                    return False
                if (
                    self.internal_squares[pos[r - 1][c]][2]
                    != self.internal_squares[pos[r][c]][0]
                ):
                    return False
        return True


def main():
    n = 25
    puzzle = PuzzleAssembly.read_input(n)
    result = puzzle.solve()
    puzzle.print_result(result)


if __name__ == "__main__":
    main()
