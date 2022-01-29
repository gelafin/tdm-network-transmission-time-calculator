# Author: Mark Mendez
# Date: 01/29/2022


def calculate_circuit_switched_transmission_time(file_size_in_bytes: int, rate_in_Gbps: float,
                                                 setup_time_in_ms: float, total_users_sharing: int
                                                 ):
    """
    Calculates the network transmission time for one file in a circuit-switched network
    :param file_size_in_bytes: number of bytes to be transmitted, in bytes
    :param rate_in_Gbps: total connection speed / link transmission rate, in Gbps
    :param setup_time_in_ms: milliseconds of setup time for the connection
    :param total_users_sharing: if TDM with equal share, enter the number of users sharing bandwidth
    :return: transmission time of the file in the network
    """
    # convert units
    file_size_in_bits = file_size_in_bytes * 8
    rate_in_bps = rate_in_Gbps * 1000 * 1000 * 1000 / 15  # Gbps to bps shared by 15 users

    # calculate transmission time
    transmission_time_in_ms = file_size_in_bits / rate_in_bps * 1000 + setup_time_in_ms  # * 1000 to convert to ms

    return transmission_time_in_ms


if __name__ == '__main__':
    # test
    file_size_in_MiB = 9  # set to None if entering file_size_in_bytes
    file_size_in_bytes = None  # set to None if entering file_size_in_MiB
    file_size_in_bytes = file_size_in_MiB * 1024 * 1024 if file_size_in_MiB is not None else file_size_in_bytes
    result = calculate_circuit_switched_transmission_time(file_size_in_bytes, 47.7, 58.3, 15)
    print('\ntransmission time: ', result)
