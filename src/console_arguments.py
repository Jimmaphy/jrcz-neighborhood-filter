import argparse
import os.path
import re

class ConsoleArguments:
    """
    ConsoleArguments is a custom implementation around the python ArgumentParser.
    It allows to quickly retrieve the arguments necessary for the application.
    The data is validated during initialization for:
        -   Syntax of city
        -   File is a json file
        -   File exists

    The arguments that will be setup are:
    - "path"                  positional argument for the file to be converted.
    - "-c", "--citycode"      option to define the city to be extracted from the document.

    Properties:
    - arguments             the variable containing the arguments if parsing was succesful.

    Methods:
    - get_path              Get the path from the arguments
    - get_city              Get the city from the arguments
    """

    def __init__(self):
        """Create an instance of the ConsoleArguments class."""

        # Create a parser
        parser = argparse.ArgumentParser(
            prog='app.py',
            description='Take in the list of neighborhoods provided by CBS and filter them by city code'
        )

        # Add the arguments to the parser
        parser.add_argument('path',
                            help='The path to the JSON file containing the neighborhood data from CBS',
                            type=str)
        parser.add_argument('-c', '--city',
                            help='The city code the neighborhoods should be retrieved from (GM0664)',
                            required=True,
                            type=str)

        # Save the arguments into a variable
        self.arguments = parser.parse_args()

        # Validate the arguments
        self.__validate_path(self.arguments.path, parser)
        self.__validate_city(self.arguments.city, parser)

    def __validate_path(self, path, parser):
        # Check whether the file is json and whether it exists
        if not (path.endswith('.json') and os.path.isfile(path)):
            parser.error("The path provided is not a JSON file or doesn't exist!")

    def __validate_city(self, city, parser):
        # Check whether the code matches the format: GM0000
        # Where 0 can be replaced with any number
        if re.search("(GM)([0-9]{4})", city) is None:
            parser.error("The city provided is not a correctly formatted code! example: GM0664!")

    def get_path(self):
        """
        Get the path from the arguments object
        Returns (str): the path to the json file
        """

        return self.arguments.path

    def get_city(self):
        """
        Get the city from the arguments object
        Returns (str): the city code (GW0664)
        """
        return self.arguments.city
