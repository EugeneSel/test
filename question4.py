"""
    addition
"""
import random

from connections.peer import Peer
from connections.simulation import Simulation, BINS
from connections.histogram import compute_histogram_bins, plot_histogram


class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        return self.id, self.peer_pool


class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        # creating a temporary database, from which we are going delete the twins:
        temporary_database = {}
        for i in range(self.number_of_peers):
            temporary_database[self.backend_database[i][0]] = self.backend_database[i][1]

        # collecting connections' durations of each peer:
        data = []
        for p in temporary_database:
            for connected_to in temporary_database[p]:
                data.append(temporary_database[p][connected_to])
                del temporary_database[connected_to][p] # deleting twin

        return compute_histogram_bins(data, BINS)


if __name__ == "__main__":
    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=100000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000000, max_peer_pool_size=10)
    s.run()
    s.report_result()
