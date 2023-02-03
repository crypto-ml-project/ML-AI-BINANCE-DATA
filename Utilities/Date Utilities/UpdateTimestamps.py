def add_time_to_timestamp(timestamp, endtime, price):
    while timestamp < endtime:
        timestamp += 300_000
        if (timestamp != endtime):
            print(f"{timestamp}, {price}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0")


price = 4605.50000000
add_time_to_timestamp(1504713300000, 1504738800000, price)
