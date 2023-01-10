# 🐘 Wilderness

## Running the program

```sh
source src/backend/.venv/bin/activate
python3 src/backend/park_boundaries.py
```

## Ways to check whether the park is getting mapped

- List of parks by name -> [Link](https://wiki.openstreetmap.org/wiki/National_parks_in_India)
- Map geojson by name -> [Link](https://nominatim.openstreetmap.org/ui/search.html?country=India&q=Kaziranga%20National%20Park%20and%20Tiger%20Reserve)
- Check algolia to ensure the document got populated with geojson

## Tasks

- [ ] Create a shell frontend for wilderness
- [x] Figure out why there are errors for some parks in OSM (data/errors.txt) [unable to resolve Mukurthi :-()]
- [x] store all indian park geo boundaries in algolia
- [x] Connect to algolia as the indexing store
- [x] retrieve park geojson from OSM
- [x] Figure out how to get the park boundaries from OSM

## Resources

- https://osmnx.readthedocs.io/en/stable/
- https://github.com/openshift-roadshow/nationalparks-js
- https://wiki.openstreetmap.org/wiki/National_parks_in_India
- https://en.wikipedia.org/wiki/List_of_national_parks_of_India#Map
- https://tyrasd.github.io/osmtogeojson/
- https://jenningsanderson.com/geo
- https://geojson.io/
- how to potentially get boundaries for all parks by type - https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dnational_park
- https://nominatim.openstreetmap.org/ui/search.html?country=India&q=Anamudi%20Shola%20National%20Park
- https://www.geoapify.com/ways-to-get-openstreetmap-data
