# Module PIP
# Install PIP https://pypi.org/project/pip
# install: pip install beautifulsoup4 # install in the same python installation directory
# install: pip install beautifulsoup4 -t ./lib # install within the project itself in the lib folder
# Remove:  pip uninstall beautifulsoup4
# pip install -r ./requirements.txt -t ./libs # instal all the libs that are inside the requirements.txt file

import tools

print(tools.PI)
print(tools.GRAVITY)

print(tools.get_extension("text.txt"))
print(tools.highest_number([4, 6, 1, 4, 2]))
