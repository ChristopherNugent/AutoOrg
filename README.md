# Objective
The goal of this project is to provide a tool that can be used to automatically organize
files based on naming conventions that can be defined by regular expressions.

# Usage
`python3 autoorg.py [-o] pattern`
+ pattern is recognized in filenames in ~/Documents. The matched segment is used as the destination folder.
+ -o enables overwriting in the destination folder.
