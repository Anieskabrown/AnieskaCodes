"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""


class HandshakeError(20):
    pass

def count_handshakes(num_people):
    # this should be able to check if the input is an integer and at least 2 people
    if not isinstance(num_people, int) or num_people < 2:
        raise HandshakeError(2)

    # Ive put this formula to calculate the number of handshakes
    handshakes = (num_people * (num_people - 1)) // 2
    return handshakes
# Testing the function with different inputs
try:
    print(count_handshakes(2))  # I think this should print 1 (1 handshake)
    print(count_handshakes(3))  # i think this should print 3 (3 handshakes)
    print(count_handshakes(1))  # I think should raise an error (invalid input)
except HandshakeError as e:
    print(e)

try:
    print(count_handshakes(-5))  # should raise an error (invalid input)
except HandshakeError as e:
    print(e)

try:
    print(count_handshakes(5)  # should raise an error (invalid input)
except HandshakeError as e:
    print(e)
