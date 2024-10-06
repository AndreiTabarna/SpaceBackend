import requests
from django.http import JsonResponse
from django.views import View
from datetime import datetime, timedelta
import os
import pandas as pd

'''
class AsteroidFeedView(View):
    def get(self, request, days_since_epoch):
        # Set your API key here
        api_key = 'AMvTGeTbBACkgqeav4K83Lw9lAVjwUFy6TpRLn1T'  # Replace with your actual API key if you have one

        # Year 0 date
        year_zero_date = datetime(1, 1, 1)  # January 1, 0001
        start_date = year_zero_date + timedelta(days=days_since_epoch)  # Compute the start date
        end_date = start_date + timedelta(days=1)  # End date is one more day

        # Format dates as strings
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        # Prepare the API URL
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date_str}&end_date={end_date_str}&api_key={api_key}'

        # Make the API request
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Preprocess the response to keep only estimated diameters in meters and add size field
            self.preprocess_asteroids(data)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)

    def preprocess_asteroids(self, data):
        # Process the near_earth_objects section
        near_earth_objects = data.get('near_earth_objects', {})
        for date, asteroids in near_earth_objects.items():
            for asteroid in asteroids:
                # Keep only the estimated diameter in meters
                if 'estimated_diameter' in asteroid:
                    estimated_diameter = asteroid['estimated_diameter']
                    # Replace the estimated_diameter with only meters
                    asteroid['estimated_diameter'] = {
                        'meters': {
                            'estimated_diameter_min': estimated_diameter['meters']['estimated_diameter_min'],
                            'estimated_diameter_max': estimated_diameter['meters']['estimated_diameter_max'],
                        }
                    }
                    # Add size field based on estimated_diameter_max
                    max_diameter = estimated_diameter['meters']['estimated_diameter_max']
                    asteroid['size'] = self.categorize_size(max_diameter)

    def categorize_size(self, max_diameter):
        """Categorizes the size of the asteroid based on its maximum diameter."""
        if max_diameter < 100:
            return 'small'
        elif max_diameter < 500:
            return 'medium'
        elif max_diameter < 1000:
            return 'large'
        else:
            return 'extra_large'
'''

class PlanetDataView(View):
    def get(self, request, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), 'space/planets.csv')

        # Read CSV file
        data = pd.read_csv(csv_file_path)

        # Replace NaN values with 0
        data = data.fillna(0)

        # Convert to JSON
        json_data = data.to_dict(orient='records')

        return JsonResponse(json_data, safe=False)


class CometDataView(View):
    def get(self, request, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), 'space/comets.csv')

        # Read CSV file
        data = pd.read_csv(csv_file_path)

        # Replace NaN values with 0
        data = data.fillna(0)

        # Convert to JSON
        json_data = data.to_dict(orient='records')

        return JsonResponse(json_data, safe=False)


class MoonDataView(View):
    def get(self, request, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), 'space/moons.csv')

        # Read CSV file
        data = pd.read_csv(csv_file_path)

        # Replace NaN values with 0
        data = data.fillna(0)

        # Convert to JSON
        json_data = data.to_dict(orient='records')

        return JsonResponse(json_data, safe=False)

class AsteroidDataView(View):
    def get(self, request, *args, **kwargs):
        # Paths to your CSV files
        csv_file_path1 = os.path.join(os.path.dirname(__file__), 'space/asteroids.csv')
        csv_file_path2 = os.path.join(os.path.dirname(__file__), 'space/asteroids2.csv')

        # Read both CSV files
        data1 = pd.read_csv(csv_file_path1)
        data2 = pd.read_csv(csv_file_path2)

        # Append data from asteroids2.csv to asteroids.csv
        combined_data = pd.concat([data1, data2], ignore_index=True)

        # Replace NaN values with 0
        combined_data = combined_data.fillna(0)

        # Convert to JSON
        json_data = combined_data.to_dict(orient='records')

        return JsonResponse(json_data, safe=False)
