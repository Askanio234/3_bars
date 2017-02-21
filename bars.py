import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, "r") as json_file:
        data = json.load(json_file)
    return data


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda bar: bar["SeatsCount"])
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda bar: bar["SeatsCount"])
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    user_coordinates = [longitude, latitude]
    return min(data, key=lambda data: vincenty(user_coordinates,
                data["geoData"]["coordinates"]).km)


if __name__ == '__main__':
    filepath = input("Введите путь до файла: ")
    data = load_data(filepath)
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    print("самый большрй бар '{}' и в нем {} мест".format(
        biggest_bar["Name"], biggest_bar["SeatsCount"]))
    print("самый маленький бар '{}' и в нем {} мест".format(
        smallest_bar["Name"], smallest_bar["SeatsCount"]))
    latitude = float(input("Введите вашу широту: "))
    longitude = float(input("Введите вашу долготу: "))
    closest_bar = get_closest_bar(data, longitude, latitude)
    print("К вам ближе всего бар '{}'".format(closest_bar["Name"]))
