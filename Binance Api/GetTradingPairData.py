import datetime
from CurlBinanceEndpoint import get_and_save_kline_data


def get_and_save_kline_data_range(symbol, interval, start_date, end_date, destination):
    # Parse the start and end dates
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    # Loop over the date range
    current_date = start_date
    while current_date <= end_date:
        # Get the kline data for the current date
        get_and_save_kline_data(
            symbol, interval, current_date.strftime("%Y-%m-%d"), destination)

        print(f"Queried: {current_date}")
        # Check the number of days in the current month
        month = current_date.month
        year = current_date.year
        if month in [1, 3, 5, 7, 8, 10, 12]:
            # These months have 31 days
            days_in_month = 31
        elif month in [4, 6, 9, 11]:
            # These months have 30 days
            days_in_month = 30
        elif month == 2:
            # Check if the current year is a leap year
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                # Leap year - February has 29 days
                days_in_month = 29
            else:
                # Non-leap year - February has 28 days
                days_in_month = 28

        # Increment the current date by one day
        current_date += datetime.timedelta(days=1)
        # Check if we have reached the


# Example usage:
symbol = "BTCUSDT"
interval = "5m"
start_date = "2021-03-01"
end_date = "2022-12-31"
destination = f"data/{symbol}/{interval}"

get_and_save_kline_data_range(
    symbol, interval, start_date, end_date, destination)
