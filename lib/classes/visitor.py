class Visitor:

    def __init__(self, name):
        self.name = name
        
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
        all_trips = [trip for trip in Trip.all if trip.visitor is self]
        if isinstance(new_trip, Trip):
            all_trips.append(new_trip)
        return all_trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        return list(set([trip.national_park for trip in self.trips()]))