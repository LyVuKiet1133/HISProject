from datetime import datetime


def get_random_last_10digits():
    current_datetime = datetime.now()
    current_millis = int(current_datetime.timestamp() * 1000)
    return str(current_millis % (10 ** 10))


def convert_datetime_string(input_datetime_str):
    dt_object = datetime.strptime(input_datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date_str = dt_object.strftime("%d%m%Y")
    return formatted_date_str


def convert_datetime_string_medical(input_datetime_str):
    dt_object = datetime.fromisoformat(input_datetime_str)
    formatted_date_str = dt_object.strftime("%Y-%m-%dT%H:%M:%S")
#   print(formatted_date_str)
    return formatted_date_str


# 20240511125645
def convert_server_time_string(input_datetime_str):
    dt_object = datetime.fromisoformat(input_datetime_str.replace('Z', '+00:00'))
    formatted_time = dt_object.strftime("%Y%m%d%H%M%S")
#   print(formatted_time)
    return formatted_time


# 11/05/2024 12:56
def convert_server_time_ddmmyyyhhmm(input_datetime_str):
    dt_object = datetime.fromisoformat(input_datetime_str.replace('Z', '+00:00'))
    formatted_time = dt_object.strftime("%d/%m/%Y %H:%M")
#   print(formatted_time)
    return formatted_time


if __name__ == "__main__":
    convert_datetime_string_medical("2024-05-19T21:49:59.6681242+07:00")
