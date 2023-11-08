# Import the right libraries
from console_arguments import ConsoleArguments 
from json_processor import JsonProcessor

# Initialize the argument parser, parsing the arguments
argument_parser = ConsoleArguments()

# Load the json data, filter it, and write it to another file
json = JsonProcessor(argument_parser.get_path())
json.read_data(argument_parser.get_city())
json.write_data()
