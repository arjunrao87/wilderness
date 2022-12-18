import os
import csv
import osmnx as ox
import matplotlib.pyplot as plt
import hashlib
from algoliasearch.search_client import SearchClient
from dotenv import load_dotenv

load_dotenv()

ALGOLIA_API_KEY = os.getenv('ALGOLIA_API_KEY')
ALGOLIA_APPLICATION_ID = os.getenv('ALGOLIA_APPLICATION_ID')


def get_park_names():
    parks = {}
    with open('../../data/parks/india.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            parks[row[0]] = None
    return parks


def get_geojson_for_parks(parks):
    for park in parks:
        try:
            geo = ox.geocode_to_gdf(park)
        except ValueError as v:
            print(v)
        parks[park] = geo.to_json()
    return parks


def write_to_algolia(parks):
    client = SearchClient.create(
        ALGOLIA_APPLICATION_ID, ALGOLIA_API_KEY)
    records = []
    for park in parks:
        id = hashlib.sha256(park.encode('utf-8')).hexdigest()
        record = {
            "park_name": park,
            "objectID": id,
            "geojson": parks[park]
        }
        records.append(record)

    index = client.init_index("wilderness")
    index.save_objects(records)


parks = get_park_names()
parks = get_geojson_for_parks(parks)
write_to_algolia(parks)
