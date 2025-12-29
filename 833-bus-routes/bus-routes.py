from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        station_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for station in route:
                station_to_buses[station].append(i)

        visited_buses = set()
        visited_stations = set([source])
        q = deque()

        # start with all buses that contain source
        for bus in station_to_buses[source]:
            q.append(bus)
            visited_buses.add(bus)

        buses_taken = 1

        while q:
            for _ in range(len(q)):
                bus = q.popleft()
                for station in routes[bus]:
                    if station == target:
                        return buses_taken
                    if station in visited_stations:
                        continue
                    visited_stations.add(station)
                    for next_bus in station_to_buses[station]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            q.append(next_bus)
            buses_taken += 1

        return -1
