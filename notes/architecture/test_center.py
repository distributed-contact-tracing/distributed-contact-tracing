

class TestCenter():
    """
    A class for the test centers / hospitals

    Distributes information regarding who is infected. 

    Make node id so long and sparse it becomes impossible to guess
    to increase the security in case there is unauthorized access. 

    Attributes:
        registered_patients = {test_id: node_id}

    """

    def deliver_test_results(self, test_id, results):
        """ 
        Send the results of a test to a specific patient. 
        Use encryption to proove you are the real sender. 
        """
        pass

    def receive_registration(self, patient_id, node_id):
        """ Save a new user of the app. """
        pass


### Other functionality: 
# LOGIN - perferably using 2FA, since unauthorized access to 
#       - this system will be catastrophic. 

