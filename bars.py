import json
import os
from geopy.distance import vincenty
import win_unicode_console
win_unicode_console.enable()


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as json_file:
        return json.load(json_file)


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


def get_coordinates_from_user():
    try:
        latitude = float(input("Введите вашу широту: "))
    except ValueError:
        latitude = None

    try:
        longitude = float(input("Введите вашу долготу: "))
    except ValueError:
        longitude = None

    if longitude is None or latitude is None:
        print("Некорректные координаты")
    else:
        return longitude, latitude


if __name__ == '__main__':
    filepath = input("Введите путь до файла: ")
    data_from_json = load_data(filepath)
    if data_from_json is None:
        print("Некорректный путь до файла")
    else:
        biggest_bar = get_biggest_bar(data_from_json)
        smallest_bar = get_smallest_bar(data_from_json)
        print("самый большрй бар '{}' и в нем {} мест".format(
            biggest_bar["Name"], biggest_bar["SeatsCount"]))
        print("самый маленький бар '{}' и в нем {} мест".format(
            smallest_bar["Name"], smallest_bar["SeatsCount"]))
        longitude, latitude = get_coordinates_from_user()
        closest_bar = get_closest_bar(data_from_json, longitude, latitude)
        print("К вам ближе всего бар '{}'".format(closest_bar["Name"]))
