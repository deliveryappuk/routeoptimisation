import os
import pandas as pd

class OptimizeRoutes:
    
    def get_json_data(self):
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        excel_file_path = os.path.join(static_dir, 'locations.xlsx')

        if not os.path.exists(excel_file_path):
            raise FileNotFoundError("locations.xlsx not found in static directory")

        jsonData = {"requests": []}
        df = pd.read_excel(excel_file_path, sheet_name='locations')

        column_names = df.columns.tolist()

        for index, row in df.iterrows():
            request_data = {}
            for column in column_names:
                request_data[column] = row[column]
            jsonData["requests"].append(request_data)

        return jsonData
    
    def optimize_stops(self, json_data):
        optimized_data = {"routes": []}
        # Write your code here to optimise the route, please feel free to create seprated classes, modules and etc as you need.

        return optimized_data
    
