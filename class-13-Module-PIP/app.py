# Module PIP
# Install PIP https://pypi.org/project/pip

import tools

print(tools.PI)
print(tools.GRAVITY)

print(tools.get_extension("text.txt"))
print(tools.highest_number([4, 6, 1, 4, 2]))
import sys

this_python = sys.version_info[:2]
min_version = (3, 7)
if this_python < min_version:
    message_parts = [
        "This script does not work on Python {}.{}".format(*this_python),
        "The minimum supported Python version is {}.{}.".format(*min_version),
        "Please use https://bootstrap.pypa.io/pip/{}.{}/get-pip.py instead.".format(*this_python),
    ]
    print("ERROR: " + " ".join(message_parts))
    sys.exit(1)