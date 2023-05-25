import pdb
class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15 and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("Names must be between 1 and 15 characters")
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        all_trips = [trip for trip in Trip.all if trip.national_park is self]
        if isinstance(new_trip, Trip):
            all_trips.append(new_trip)
        return all_trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        all_visitors = [trip.visitor for trip in self.trips()]
        return list(set(all_visitors))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visit_counts = dict()
        for visitor in self.visitors():
            visit_counts[visitor] = visit_counts.get(visitor, 0) + 1
        maximum = max(visit_counts, key=visit_counts.get)
        # pdb.set_trace()
        return maximum