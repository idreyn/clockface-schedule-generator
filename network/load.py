import csv
from os.path import dirname, join

PATH_TO_GTFS_DATA = dirname(__file__) + "/../data/MBTA_GTFS-1"


def loader_by_file_name(file_name):
    file_path = join(PATH_TO_GTFS_DATA, file_name + ".txt")

    def load():
        res = []
        with open(file_path, "r") as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                res.append(row)
        return res

    return load


load_services = loader_by_file_name("calendar")
load_stop_times = loader_by_file_name("relevant_stop_times")
load_stops = loader_by_file_name("stops")
load_transfers = loader_by_file_name("transfers")
load_trips = loader_by_file_name("trips")