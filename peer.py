

class Peer():
    """ 
    A class for each node (i.e. phone). 
    
    Attributes:  
        areas_visited = []: A high level description (ie. sthlm,gbg)
        saved_locations = {time: location}: A  record of locations.
        hashed_events = Set(): A hash representation of all events. 

    """

    def receive_test_result(self, confirmed_ill):
        """ Called from the hospital / test center super node """
        if confirmed_ill:
            print("You have tested positive")
            hashed_contact_trace = self.compute_hashed_contact_trace()
            self.distribute_data(hashed_contact_trace)
        else:
            print("You have tested negative")

    def compute_hashed_contact_trace(self):
        """ 
        Use all saved locations/times to get hashed event for distribution. 
        Preferably this function reduces the events to the most relevant ones. 
        """
        pass

    def distribute_data(self, data):
        """ Distribute contace trace to the network """
        pass

    def receive_traces(self, area, traces):
        """ 
        Receive a block of hashed events from people confirmed ill. 
        Check if you were exposed to any of the events. 
        """
        if area in self.areas_visited:
            for hashed_event in traces:
                if self.exposed_to_event(hashed_event):
                    print("Go and get tested!")

    def exposed_to_event(self, hashed_event):
        """ Check using the set 'self.hashed_events' if you have been exposed. """ 
        pass

    def record_event(self):
        """ 
        Periodically record event (time, place) from phone data and save 
        to self.saved_locations. Hash, then save to self.hashed_events. 
        Also adds the current area to areas visited.
        """
        pass


### Other functionality
# REGISTER - register (personnummer, node_id) with test center
#          - Get encryption key from center such that results can be verified
#          - must also connect to pace maker
# LOGIN - verify that it is you through mobilt bank id
# DELETE - delete account, data on phone, and de-register from super node

