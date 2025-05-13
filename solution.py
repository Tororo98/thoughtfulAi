def sort(width, height, length, mass):
    # Calculate the volume of the box
    volume = width * height * length
    # Check if package is bulky
    is_bulky = (volume > 1000000) or (width >= 150 or height >= 150 or length >= 150)
    # Check if package is heavy
    is_heavy = mass >= 20

    # Determine the stack using the conditions
    stack = "REJECTED" if (is_bulky and is_heavy) else (
        "SPECIAL" if (is_bulky or is_heavy) else "STANDARD")
    return stack

# Test cases
def test():
    assert sort(100, 100, 100, 10) == "STANDARD"
    assert sort(200, 200, 200, 10) == "SPECIAL"
    assert sort(200, 200, 200, 30) == "REJECTED"
    assert sort(150, 150, 150, 10) == "SPECIAL"
    assert sort(150, 150, 150, 30) == "REJECTED"
    assert sort(50, 50, 50, 30) == "SPECIAL"
    assert sort(50, 50, 50, 20) == "SPECIAL"
    assert sort(50, 50, 50, 19) == "STANDARD"


if __name__ == "__main__":
    # Run the test cases
    test()
    print("All test cases passed!")

    # print(sort(50, 50, 50, 30))  # Expected output: "STANDARD"
    

    
