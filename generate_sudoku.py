import random

def generate_sudoku():
    def fill_board(board):
        # 스도쿠의 각 3x3 블록을 무작위로 채움
        def fill_box(start_row, start_col):
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for i in range(3):
                for j in range(3):
                    board[start_row + i][start_col + j] = numbers.pop()

        # 주요 대각선 3x3 블록을 먼저 채움
        for i in range(0, 9, 3):
            fill_box(i, i)

        # 스도쿠 퍼즐을 해결하여 전체 보드를 채움
        solve_sudoku(board)

    def remove_numbers(board, difficulty=40):
        # 난이도에 따라 특정 개수의 숫자를 제거하여 빈 칸을 만듦
        attempts = difficulty
        while attempts > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                attempts -= 1

    # 빈 스도쿠 보드 초기화
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)          # 보드 채우기
    remove_numbers(board, 40)  # 난이도 설정 (여기선 40개의 숫자를 제거)

    return board