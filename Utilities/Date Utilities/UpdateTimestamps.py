def add_time_to_timestamp(timestamp, endtime, price):
    while timestamp < endtime:
        timestamp += 300_000
        if (timestamp != endtime):
            print(f"{timestamp},{price},0,0,0,0,0,0,0,0,0,0")


price = 138.86000000
add_time_to_timestamp(1632898500000, 1632906000000, price)
