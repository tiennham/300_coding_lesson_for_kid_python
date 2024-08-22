from typing import List


class LearnSolution:
    def myfloodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        replacement_color = color
        target_color = image[sr][sc]
        if replacement_color == target_color:
            return image

        def func(r, c):
            queue = [(r, c)]
            while queue:
                i, j = queue.pop()
                cell_color = image[i][j]
                if 0 <= i < num_rows and 0 <= j < num_cols and cell_color == target_color:
                    image[i][j] = replacement_color
                    queue.append((i + 1, j)) if i + 1 < num_rows else None
                    queue.append((i - 1, j)) if i - 1 >= 0 else None
                    queue.append((i, j + 1)) if j + 1 < num_cols else None
                    queue.append((i, j - 1)) if j - 1 >= 0 else None

        func(sr, sc)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tmp = image[sr][sc]
        m = len(image)
        n = len(image[0])
        if tmp == color:
            return image
        def fun(i,j):
            queue = [(i,j)]
            while queue:
                i,j = queue.pop(0)
                if i>=0 and i < m and j >= 0 and j < n and image[i][j] == tmp:
                    image[i][j] = color
                    queue.append((i+1,j))
                    queue.append((i-1,j))
                    queue.append((i,j+1))
                    queue.append((i,j-1))
        fun(sr, sc)
        return image


class MyHeadSolution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_target = image[sr][sc]
        if color_target == color:
            return image
        image[sr][sc] = color
        return self.floodFillHelper(image, sr, sc, color_target, color)

    def floodFillHelper(self, image: List[List[int]], sr: int, sc: int, color_target: int, color_replacement) -> List[List[int]]:
        top_r = sr - 1
        if top_r >= 0 and image[top_r][sc] == color_target:
            image[top_r][sc] = color_replacement
            self.floodFillHelper(image, top_r, sc, color_target, color_replacement)

        right_c = sc + 1
        if right_c < len(image[0]) and image[sr][right_c] == color_target:
            image[sr][right_c] = color_replacement
            self.floodFillHelper(image, sr, right_c, color_target, color_replacement)

        bottom_r = sr + 1
        if bottom_r < len(image) and image[bottom_r][sc] == color_target:
            image[bottom_r][sc] = color_replacement
            self.floodFillHelper(image, bottom_r, sc, color_target, color_replacement)

        left_c = sc - 1
        if left_c >= 0 and image[sr][left_c] == color_target:
            image[sr][left_c] = color_replacement
            self.floodFillHelper(image, sr, left_c, color_target, color_replacement)

        return image


# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
# image = [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# color = 0
image = [[0,0,0],[1,0,0]]
sr = 1
sc = 1
color = 2

solution = LearnSolution()
print(solution.myfloodFill(image, sr, sc, color))




