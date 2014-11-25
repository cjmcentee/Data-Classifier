__author__ = 'coltonmcentee'

def parse_as_floats(tabbed_file_name):
    tabbed_file = open(tabbed_file_name, 'r')

    values = []
    for line in tabbed_file:
        if not line.startswith('#') and line != "":

            columns = line.split("\t");

            columns_number = tuple([float(c) for c in columns]) # list of tuples, not list of lists
            values.append(columns_number)

    return values