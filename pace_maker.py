

class PaceMaker():
    """
    Class for a server that distributes the anonymized and 
    hashed contact traces. 

    Attributes: 
        connected_peers = []: List of peers to communicate with.
        trace_buffer = {area: hashed_events}: Temporarily stored hashed events.
    """

    def receive_hashed_trace(self, area, trace):
        """ 
        Receive sets of hashed events (a trace) from a confirmed ill peer.
        Save to the trace buffer. 
        """
        pass

    def distribute_traces(self):
        """ 
        Distribute the events from the trace buffer to all peers. 
        """
        trace_packets = self.shuffle_and_pack_traces()
        for peer in self.connected_peers():
            for packet in trace_packets:
                self.send_packet(peer, packet)

    def shuffle_and_pack_traces(self):
        """ 
        Shuffle the hashed events within the same area. 
        Put into packets for distribution. 
        """
        pass

    def send_packet(self, peer, packet):        
        """ Connect to peer and send packet of events. """
        pass

### Other functionality
# Connect to new peers

