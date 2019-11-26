from connections.peer import Peer
from connections.simulation import Simulation, BINS
from connections.histogram import compute_histogram_bins, plot_histogram


class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2: implement this method
        """

        return self.peer_pool


class SimulationQ2(Simulation):

    def generate_network(self):
        self.network = [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):

        """
            Question 2: implement this method
        """
        # collecting connections' durations of each peer:
        data = []
        for i in range(self.number_of_peers):
            for p in self.backend_database[i]:
                data.append(self.backend_database[i][p])

        result = compute_histogram_bins(data, BINS)
        # Dividing a number of each connection by 2 to avoid repetitions:
        result[0] = [int(count / 2) for count in result[0]]
        return result


if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=100000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000000, max_peer_pool_size=10)
    s.run()
    s.report_result()
