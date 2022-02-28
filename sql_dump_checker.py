import re

def sql_dump_checker(file_location):
    file = open(file_location, r)
    lines = file.readLines()

    for line in lines: