import json

class JsonProcessor:
    """
    The JsonProcessor is used to read the JSON file provided by CBS.
    During the read, it filters data based on a given city/town.

    Properties:
    - source_file           stores the path to the original CBS data.
    - data                  stores the data, starts as None until data is read.

    Methods:
    - read_data             reads the data from the source file, filters it and stores the result.
    - write_data            writes the filtered data into a file called "filtered_neighborhoods.json".
    """

    def __init__(self, path):
        """
        Create an instance of the JsonProcessor.

        Arguments:
        - path (str): the path to the file containing the original data.
        """

        self.source_file = path
        self.data = None

    def read_data(self, city):
        """
        Read the data from the source file and filter it.
        The result is stored in the data property.

        Arguments:
        - city (str): the city_code to filter.
        """

        # Open the file
        with open(self.source_file) as json_file:
            # Get the data from the file
            self.data = json.load(json_file)

            # Filter the data to get only the neighborhoods (areas) from the given town
            self.data["features"] = [area for area in self.data["features"] if area["properties"]["gm_code"] == city]

    def write_data(self):
        """
        Write the data gathered to a file.
        The file will be called "filtered_neighborhoods.json".

        Raises:
        - Error when data has not yet been read.
        """

        # Check whether the data has been read
        if self.data is None:
            # If not, raise an error
            raise Error("Data has not been read yet...")
        
        # Open the output file with write privileges
        with open("./filtered_neighborhoods.json", "w") as output_file:
            # Convert the json data into a string and write it to the file
            json_data = json.dumps(self.data, indent=4)
            output_file.write(json_data)
