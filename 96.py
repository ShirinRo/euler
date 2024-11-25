import numpy as np
import time

inputfile = open('p096_sudoku.txt', 'r')
lines = inputfile.readlines()


def verify_set_adheres_sudoku(nums: np.matrix):
    no_zeros = np.asarray(nums[np.nonzero(nums)]).reshape(-1)
    if len(no_zeros) == 9:
        return set(no_zeros) == {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return len(set(no_zeros)) == len(no_zeros)


def verify_num(sudoku_mat, row, col):
    arr = []
    for i in range(3 * (row // 3), 3 * (row // 3) + 3):
        for j in range(3 * (col // 3), 3 * (col // 3) + 3):
            arr += [sudoku_mat[i, j]]
    return verify_set_adheres_sudoku(sudoku_mat[row]) and \
        verify_set_adheres_sudoku(np.transpose(sudoku_mat)[col]) and \
        verify_set_adheres_sudoku(np.asmatrix(arr))


def quick_verify_set_adheres_sudoku(nums: np.matrix):
    list_nums: list = nums.tolist()[0]
    while list_nums:
        num = list_nums.pop()
        if num and num in list_nums:
            return False
    return True


def quick_verify_num(sudoku_mat, row, col):
    if quick_verify_set_adheres_sudoku(sudoku_mat[row]) and \
            quick_verify_set_adheres_sudoku(np.transpose(sudoku_mat)[col]):
        three_by_three = sudoku_mat[3 * (row // 3): 3 * (row // 3) + 3, 3 * (col // 3): 3 * (col // 3) + 3]
        return quick_verify_set_adheres_sudoku(three_by_three.reshape(-1))
    return False

def solve_sudoku(sudoku_mat: np.matrix):
    iterated_mat = sudoku_mat
    appearances = {0: (), 1: (), 2: (), 3: (), 4: (), 5: (), 6: (), 7: (), 8: (), 9: ()}
    count_filled = 0
    for value in range(1, 10):
        appearances_of_val = np.count_nonzero(sudoku_mat == value)
        count_filled += appearances_of_val
        cur_tuple = list(appearances[appearances_of_val])
        appearances[appearances_of_val] = tuple(cur_tuple + [value])
    # print(f"count_filled: {count_filled}")
    # solved, stam = quick_solve_sudoku_helper(iterated_mat, appearances, count_filled)
    solved, stam = solve_sudoku_helper(iterated_mat)
    return three_digits(solved)

# not really quicker
def quick_solve_sudoku_helper(unsolved_sudoku_mat: np.matrix, histogram: dict, count_filled):
    if unsolved_sudoku_mat.min() > 0:
        return unsolved_sudoku_mat, False
    unfilled = np.where(unsolved_sudoku_mat == 0)
    row, col = unfilled[0][0], unfilled[1][0]
    for appearances in range(8, -1, -1):
        values_with_count: tuple = histogram[appearances]
        for i, value in enumerate(values_with_count):
            copy_of_mat = unsolved_sudoku_mat.copy()
            copy_of_mat[row, col] = value
            if quick_verify_num(copy_of_mat, row, col):
                histogram_copy = histogram.copy()

                appearances_of_value = list(histogram_copy[appearances])
                appearances_of_value.remove(value)
                histogram_copy[appearances] = tuple(appearances_of_value)

                appearances_of_value_plus = list(histogram_copy[appearances + 1])
                appearances_of_value_plus.append(value)
                histogram_copy[appearances + 1] = tuple(appearances_of_value_plus)

                solved, stuck = quick_solve_sudoku_helper(copy_of_mat, histogram_copy, count_filled+1)
                if not stuck:
                    return solved, False
        if appearances == 0:
            return unsolved_sudoku_mat, True

    print("oops!!!")
    assert "not here"



def solve_sudoku_helper(unsolved_sudoku_mat: np.matrix):
    if unsolved_sudoku_mat.min() > 0:
        return unsolved_sudoku_mat, False
    unfilled = np.where(unsolved_sudoku_mat == 0)
    row, col = unfilled[0][0], unfilled[1][0]
    for i in range(1, 10):
        copy_of_mat = unsolved_sudoku_mat.copy()
        copy_of_mat[row, col] = i
        if quick_verify_num(copy_of_mat, row, col):
            solved, stuck = solve_sudoku_helper(copy_of_mat)
            if not stuck:
                return solved, False
            elif i == 9:
                return unsolved_sudoku_mat, True
        elif i == 9:
            return unsolved_sudoku_mat, True

    print("oops!!!")
    assert "not here"


def three_digits(solved_sudoku_mat):
    first_line = np.asarray(solved_sudoku_mat[0])
    return first_line[0][0] * 100 + first_line[0][1] * 10 + first_line[0][2]


new_mat = []
all_mats = []
for line in lines:
    if line.startswith("Grid"):
        if new_mat:
            all_mats += [new_mat]
        new_mat = []
    else:
        new_mat += [[int(x) for x in [x for x in str(line.split())][2:-2]]]

all_mats += [new_mat]
grid_num = 1
mats = []
sum_mats = 0
timer = time.perf_counter()
for mat in all_mats:
    npmat = np.asmatrix(mat)
    mats += [npmat]
    solution_three_numbers = solve_sudoku(npmat)
    # print(grid_num)
    print(f"grid num {grid_num}, solution: {solution_three_numbers}, time: {time.perf_counter() - timer}")
    timer = time.perf_counter()
    sum_mats += solution_three_numbers
    # print(three_digits(npmat))
    # print(npmat)
    grid_num += 1

print(sum_mats)
print(f"total time: {timer}")
