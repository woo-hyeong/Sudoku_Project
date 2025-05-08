def solve_sudoku(board):
    # 빈 칸 찾기
    def find_empty_cell(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    # 숫자가 해당 위치에 놓일 수 있는지 검사
    def is_valid_move(board, row, col, num):
        # 행 검사
        if num in board[row]:
            return False
        # 열 검사
        if num in [board[i][col] for i in range(9)]:
            return False
        # 3x3 박스 검사
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False
        return True

    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return board  # 모든 칸이 채워지면 스도쿠 해결 완료

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num  # 유효한 숫자를 놓음
            if solve_sudoku(board):  # 재귀적으로 다음 빈 칸을 해결 시도
                return board
            board[row][col] = 0  # 백트래킹

    return None  # 해결 불가 시 None 반환