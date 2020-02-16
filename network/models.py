from dataclasses import dataclass
from typing import List, Tuple, Dict
import functools
import datetime


class LocationType:
    STOP = "0"
    STATION = "1"


@dataclass
class Trip(object):
    id: str
    service_id: str
    route_id: str
    direction_id: str
    service_days: List[str]

    def __post_init__(self):
        self.stop_times = []

    def add_stop_time(self, stop_time):
        self.stop_times.append(stop_time)


@dataclass
class Station(object):
    id: str
    name: str
    location: Tuple[str, str]

    def __post_init__(self):
        self.child_stops = []

    def add_child_stop(self, stop):
        self.child_stops.append(stop)


@dataclass
class Stop(object):
    parent_station: Station
    id: str
    name: str

    def __post_init__(self):
        self.stop_times = []
        self.transfers = []

    def set_stop_times(self, stop_times):
        self.stop_times = stop_times

    def add_transfer(self, transfer):
        self.transfers.append(transfer)


@functools.total_ordering
@dataclass
class StopTime(object):
    stop: Stop
    trip: Trip
    time: datetime.timedelta

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __lt__(self, other):
        return self.time < other.time


@dataclass
class Transfer(object):
    from_stop: Stop
    to_stop: Stop
    min_walk_time: int


@dataclass
class Network(object):
    stations_by_name: Dict[str, Station]
    trips_by_id: Dict[str, Trip]