

class TestCenter():
    """
    A class for the test centers / hospitals

    Distributes information regarding who is infected. 

    Attributes:
        registered_patients = {patient_id: node_id}

    """

    def deliver_test_results(self, patient_id, results):
        """ Send the results of a test to a specific patient. """
        pass

    def receive_registration(self, patient_id, node_id):
        """ Save a new user of the app. """
        pass


### Other functionality: 
# LOGIN - perferably using 2FA, since unauthorized access to 
#       - this system will be catastrophic. 

