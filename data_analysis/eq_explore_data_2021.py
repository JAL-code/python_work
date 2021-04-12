import json

test_data = False

# Explore the structure of the data.
filename = 'data/2-5_day.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

# Veiw readable format
if test_data:
    readable_file = 'data/readable_eq_data_2-5.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)

# Take all data in stored in features.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extract the magnitude of earthquakes
mags = []
lons, lats = [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])
    
