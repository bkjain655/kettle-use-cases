from streamlit_app import app
import geojson, json
from folium.plugins import HeatMap

@app.streamlit_app_builder(allow_reuse=True)
def build_heatmap():
    # Load and parse the GeoJSON data for rental car companies in US states
    with open('geojson_data/rental-car-companies.geojson', 'r') as f:
        geodata = json.load(f)

    # Extract relevant information from the GeoJSON data
    rentals = [feature['properties']['Rentals'] for feature in geodata['features']]
    reservations = [feature['properties']['Reservations'] for feature in geodata['features']]
    returns = [feature['properties']['Returns'] for feature in geodata['features']]

    # Create a list of states and their respective values (rentals, reservations, and returns)
    state_data = []
    for i in range(len(geodata['features'])):
        state = geodata['features'][i]['properties']['State']
        rentals_state = [rental] * len(rentals[i]) if rentals[i] else 0
        reservations_state = [reservation] * len(reservations[i]) if reservations[i] else 0
        returns_state = [returned] * len(returns[i]) if returns[i] else 0
        state_data.append([state, rentals_state + reservations_state + returns_state])

    # Create a GeoJSON object with the heatmap data for each state and its values (rentals, reservations, and returns)
    geojson_heatmap = {
        'type': 'FeatureCollection',
        'features': [
            {
                'geometry': feature['geometry'],
                'properties': {
                    'Rentals': state_data[i][1],
                    'Reservations': state_data[i][2],
                    'Returns': state_data[i][3]
                }
            } for i in range(len(state_data))
        ]
    }

    # Create a HeatMap object with the GeoJSON heatmap data and add it to the map layer
    m = folium.Map([40, -100], zoom_start=3)
    HeatMap(geojson_heatmap).add_to(m)

    # Render the streamlit application with the created map as a main component and sidebar filters for state and date ranges
    return app.st_chart(m, use_container_width=True), None