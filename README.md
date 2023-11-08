# JRCZ Neighborhood Filter

During a project in collaboration with the Municipality of Goes,
the need to be able to filter out neighborhoods from a nation-wide dataset arised.

## Getting the Data Set

The CBS (Centraal Bureau voor de Statistiek) in the Netherlands provide data on all neighborhoods.
The entire dataset (a little under 500MB) can be downloaded from the link below.
The data is provided as GeoPackages (.GPKG files) per year.
Only a small portion from the data is required, so the dataset will be filtered after downloading.

[Download the data from CBS](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/cbs-gebiedsindelingen)

In order to filter the data to just neighborhoods, 
a tool called [GeoPackage Viewer](https://ngageoint.github.io/geopackage-viewer-js/) will be used.
The steps to get the required data are:

1. Load the most recent file and scroll down to either "buurt_gegeneraliseerd" or "buurt_niet_gegeneraliseerd".
The second provides the neighborhoods exactly, while the first has more smoothened borders.
2. Click begin the prefered option on "Download Layer as GeoJSON".
3. In order to make the file compatibile with the tool, rename the downloaded file.
For example: "buurt_niet_gegeneraliseerd.geojson" becomes "buurt_niet_gegeneraliseerd.json".

## Installation

The project is made using Python 3.11. Other versions of Python have not been tested.
Clone the repository or download the code to your computer.
No additional pip packages are required.

## Usage

It may be easy to move the datafile downloaded earlier into the ```src``` folder inside the project.
Open a terminal inside the ```src``` folder and run app.py.
The arguments for the application are ```-c``` or ```--city``` for the manucipality code,
followed by the path to the sourcefile. 
For example: ```python3 app.py -c "GM0664 ./buurt_niet_gegeneraliseerd.json```

For a list of municipality codes, visit
[Gemeenten Nederland op OpenDataSoft](https://public.opendatasoft.com/explore/dataset/georef-netherlands-gemeente/table/?disjunctive.prov_code&disjunctive.prov_name&disjunctive.gem_code&disjunctive.gem_name&sort=gem_name).
The code used by the application is ```Gemeente code (with prefix)```.
