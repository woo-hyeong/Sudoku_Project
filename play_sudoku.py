def play_sudoku():
    # generate_sudoku 함수로 초기 보드를 생성합니다.
    board = generate_sudoku()
    solved_board = [row[:] for row in board]  # 정답 보드 복사
    solve_sudoku(solved_board)  # 정답을 구함

    print("스도쿠 게임을 시작합니다!")
    while True:
        print_board(board)
        try:
            row = int(input("행을 입력하세요 (1-9): ")) - 1
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            # 입력이 유효한지 확인
            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue

            # 이미 숫자가 있는 칸인지 확인
            if board[row][col] != 0:
                print("이미 숫자가 있는 칸입니다. 다시 시도하세요.")
                continue

            # 이동이 유효한지 확인
            if not (board[row][col] == 0 and solved_board[row][col] == num):
                print("잘못된 이동입니다. 다시 시도하세요.")
                continue

            # 올바른 이동 시 숫자 채우기
            board[row][col] = num

            # 스도쿠가 완성되었는지 확인
            if all(all(cell != 0 for cell in row) for row in board):
                print("축하합니다! 스도쿠를 완료했습니다!")
                print_board(board)
                break

        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해야 합니다. 다시 시도하세요.")