from datetime import datetime


def get_random_last_10digits():
    current_datetime = datetime.now()
    current_millis = int(current_datetime.timestamp() * 1000)
    return str(current_millis % (10 ** 10))


def convert_datetime_string(input_datetime_str):
    dt_object = datetime.strptime(input_datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date_str = dt_object.strftime("%d%m%Y")
    return formatted_date_str
