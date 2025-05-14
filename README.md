Robotic Package Sorting System
This Python function determines where packages should be dispatched in a robotic automation factory based on their dimensions and mass.

Functionality
The sort(width, height, length, mass) function classifies packages into three stacks:

STANDARD: Neither bulky nor heavy

SPECIAL: Either bulky or heavy (but not both)

REJECTED: Both bulky and heavy

Classification Rules
Bulky if:

Volume (width × height × length) ≥ 1,000,000 cm³, or

Any dimension (width, height, or length) ≥ 150 cm

Heavy if:

Mass ≥ 20 kg

Usage
python
from package_sorter import sort

# Example usage
print(sort(50, 50, 50, 19))   # STANDARD
print(sort(100, 150, 100, 15)) # SPECIAL (bulky)
print(sort(50, 50, 50, 25))    # SPECIAL (heavy)
print(sort(200, 200, 200, 25)) # REJECTED
Installation
No dependencies required. Simply copy the solution.py file into your project.

Testing
Run the included test cases:

python
python solution.py
Or test manually:

python
print(sort(50, 50, 50, 19))    # Expected: STANDARD
print(sort(50, 50, 50, 20))    # Expected: SPECIAL
print(sort(150, 50, 50, 10))   # Expected: SPECIAL
print(sort(150, 150, 150, 25)) # Expected: REJECTED

Edge Cases
The function handles:
All dimensions exactly at threshold values

Mass exactly at 20kg threshold

Non-integer values (if passed)
