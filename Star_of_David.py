def print_v_shape(width_v, size_x, star_position_x):
    # Go through the lines
    for i in range(width_v):
        # to match the V to the X's it has to be odd
        if size_x % 2 == 0:
            size_x += 1
        # prints an exact amount of spaces for the V that will be in the middle of the Star of David
        print(" " * (size_x + 1), end="")
        # Prints an amount of star_position_x spaces to place the Star of David in the middle of the flag
        print(" " * star_position_x, end="")
        # go over columns
        for j in range(2 * width_v - 1):
            if j == i or j == 2 * width_v - 2 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def print_up_side_down_v_shape(width_v, size_x, star_position):
    # The same way as the V shape only in reverse
    for i in range(width_v):
        if size_x % 2 == 0:
            size_x += 1
        print(" " * (size_x + 1), end="")
        print(" " * star_position, end="")
        for j in range(2 * width_v - 1):
            if j == width_v - 1 - i or j == width_v - 1 + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def print_two_x_shapes_with_border(width_x, height_x, star_position):
    # to match the X's to the V it has to be odd
    if height_x % 2 == 0:
        height_x += 1

    # Width of the entire line including both X shapes and the space in between
    width_top_border = height_x*3

    # Print the top border and the amount of star_position_x spaces
    # to place the Star of David in the middle of the flag
    print(" " * star_position, end="")
    print("*" * width_top_border)

    # Print the X shapes with the space in between
    for i in range(height_x):
        # Prints an amount of star_position_x spaces to place the Star of David in the middle of the flag
        print(" " * star_position, end="")
        for j in range(width_x):
            if j == i or j == height_x - 1 - i or j == height_x + i + height_x or j == 3 * height_x - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Print the top border and the amount of star_position_x spaces
    # to place the Star of David in the middle of the flag
    print(" " * star_position, end="")
    print("*" * width_top_border)


def print_two_lines(width_lines, height_lines):
    print("*" * width_lines)
    for i in range(height_lines-2):
        print()
    print("*" * width_lines)


def print_star_of_david(width_of_star, height_of_star):

    # check which is smaller and divide it by 4 to get the quarter of the smallest dimension
    if width_of_star < height_of_star:
        height_star = width // 4
    else:
        height_star = height_of_star//4

    # In general, the method of construction of the Star of David, I divided it into several parts
    # 1. the horizontal stripes
    # 2. inverted V shape
    # 3. the shape of two parallel x's plus two stripes that close them from above and below
    # 4. V shape
    # 5. more horizontal stripes

    # the size of the Star of David is a quarter of the total size
    # the height of the X's is half the height of the Star of David
    # and each V is a quarter of the height of the Star of David
    # and the height of the rows of the horizontal stripes is one tenth of the total height

    height_x = height_star // 2         # the height of the X's
    width_v = height_x // 2             # the height of the V's
    height_lines = height_of_star//10   # the horizontal stripes

    # calculation of the position (x,y) of the Star of David inside the flag
    star_position_x = width_of_star // 3
    # Calculating the Y axis - take the general height and subtract the height of the horizontal
    # stripes minus the horizontal stripes themselves minus the height of the Star of David
    # and divide all this by 2 to give the flag the missing height from above and below
    star_position_y = (height_of_star - height_lines*2 - 4 - height_star) // 2

    # print the flag:
    for i in range(star_position_y):
        print()
    print_two_lines(width_of_star, height_lines)

    print_up_side_down_v_shape(width_v, height_x, star_position_x)
    print_two_x_shapes_with_border(width_of_star, height_x, star_position_x)
    print_v_shape(width_v, height_x, star_position_x)

    print_two_lines(width_of_star, height_lines)
    for i in range(star_position_y):
        print()


if __name__ == '__main__':
    height = 0
    width = 0
    # need to be greater the 15 to get a proper star of david... smaller than 15 will print just a square
    # if one of them is smaller than 15, enter number again
    while height < 15 or width < 15:
        height = int(input("pls enter the height of the star greater than 15: "))
        width = int(input("pls enter the  width of the star greater than 15: "))
    print_star_of_david(width, height)

