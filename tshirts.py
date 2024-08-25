
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


# assert(size(37) == 'S')
# assert(size(40) == 'M')
# assert(size(43) == 'L')
# print("All is well (maybe!)\n")

def test_size():
    # Tests for 'S' category
    assert size(37) == 'S', "Expected 'S' for cms = 37"
    assert size(37.9) == 'S', "Expected 'S' for cms = 37.9"

    # Tests for 'M' category
    assert size(38.1) == 'M', "Expected 'M' for cms = 38.1"
    assert size(41.9) == 'M', "Expected 'M' for cms = 41.9"

    # Tests for 'L' category
    assert size(42) == 'L', "Expected 'L' for cms = 42"
    assert size(43) == 'L', "Expected 'L' for cms = 43"
    assert size(50) == 'L', "Expected 'L' for cms = 50"

    # print("All tests passed!")

# Run the enhanced test cases
test_size()
