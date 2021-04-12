import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

test_data = False

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Veiw readable format
if test_data:
    readable_file = 'data/readable_eq_data_2-5.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)

# Take all data in stored in features.
all_eq_dicts = all_eq_data['features']
if test_data:
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

# Check the first 10 items.
if test_data:
    print(mags[:10])
    print(lons[:10])
    print(lats[:10])

if test_data:
    data = [Scattergeo(lon=lons, lat = lats)]
else:
    # Print data: type, lon, lat (first example)
    # Print data: mags - format magnitude to show earthquake size.
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        },
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
    
