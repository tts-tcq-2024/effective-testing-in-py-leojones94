def generate_color_combinations():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    combinations = [
        (i * len(minor_colors) + j, major, minor)
        for i, major in enumerate(major_colors)
        for j, minor in enumerate(minor_colors)
    ]
    return combinations
def format_color_map(combinations):
    formatted_lines = [f'{num:2} | {major:6} | {minor:6}' for num, major, minor in combinations]
    return "\n".join(formatted_lines) + "\n"
def print_color_map():
    combinations = generate_color_combinations()
    output = format_color_map(combinations)
    print(output)
    return len(combinations)
def test_generate_color_combinations():
    combinations = generate_color_combinations()
    assert len(combinations) == 25, "Number of combinations is incorrect"
    assert combinations[0] == (0, "White", "Blue"), "First combination is incorrect"
    assert combinations[-1] == (24, "Violet", "Slate"), "Last combination is incorrect"
    print("generate_color_combinations() test passed!")

test_generate_color_combinations()
def test_format_color_map():
    combinations = generate_color_combinations()
    formatted = format_color_map(combinations)
    expected_output = "\n".join(
        f'{num:2} | {major:6} | {minor:6}'
        for num, major, minor in combinations
    ) + "\n"
    assert formatted == expected_output, "Formatted output is incorrect"
    print("format_color_map() test passed!")

test_format_color_map()
import io
import sys

def test_print_color_map():
    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    result = print_color_map()

    sys.stdout = sys.__stdout__

    # Get the expected output
    expected_output = format_color_map(generate_color_combinations())
    assert captured_output.getvalue() == expected_output, "Printed output is incorrect"
    assert result == 25, "Result is incorrect"

    print("print_color_map() test passed!")

test_print_color_map()
