
class Trip:
    
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        visitor.trips(self)
        
        self.national_park = national_park
        national_park.trips(self)
        
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        
    @property
    def national_park(self):
        return self._national_park
        
    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark
        if value is not None and isinstance(value, NationalPark) and not hasattr(self, 'national_park'):
            self._national_park = value
        else:
            raise Exception("Nationalpark must be a NationalPark")
        
    @property
    def visitor(self):
        return self._visitor
        
    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor
        if value is not None and isinstance(value, Visitor) and not hasattr(self, 'visitor'):
            self._visitor = value
        else:
            raise Exception("Visitor must be a Visitor")
