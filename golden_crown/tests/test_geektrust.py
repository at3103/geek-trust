import pytest
from geektrust import find_ruler
#from geektrust import find_ruler


@pytest.mark.parametrize("input_fname, output_fname", [
	("tests/input/sample1.txt","tests/output/sample1.txt"),
	("tests/input/sample2.txt","tests/output/sample2.txt"),
	("tests/input/sample3.txt","tests/output/sample3.txt"),
	("tests/input/multiple_msgs.txt","tests/output/multiple_msgs.txt"),
	("tests/input/only_space.txt","tests/output/only_space.txt"),
	("tests/input/with_space_kingdom.txt","tests/output/with_space_kingdom.txt"),
	("tests/input/empty_message.txt","tests/output/empty_message.txt")
])
def test_find_ruler(input_fname, output_fname):
	expected_output = ""
	with open(output_fname,"r") as file:
		expected_output = file.read().strip()

	assert find_ruler(input_fname) == expected_output

