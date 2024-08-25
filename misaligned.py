
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


# result = print_color_map()
# assert(result == 25)
# print("All is well (maybe!)\n")

import io
import sys

def test_print_color_map():
    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Run the function
    result = print_color_map()

    # Reset redirect.
    sys.stdout = sys.__stdout__

    # Expected output
    expected_output = "\n".join(
        f'{i * 5 + j} | {major} | {minor}'
        for i, major in enumerate(["White", "Red", "Black", "Yellow", "Violet"])
        for j, minor in enumerate(["Blue", "Orange", "Green", "Brown", "Slate"])
    ) + "\n"

    # Check if the printed output is as expected
    assert captured_output.getvalue() == expected_output, "Printed output is not as expected"
    assert result == 25, "Result is not as expected"

    print("All tests passed!")

# Run the enhanced test
test_print_color_map()
