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
        for index, row in df.iterrows():
            jsonData["requests"].append({
                "Order ID": int(row["OrderID"]),
                "Collection Postcode": row["CollectionPostcode"],
                "Depot": row["Depot"],
                "Collection From (HH:MM)": str(row["CollectionFrom"]),  
                "Collection To (HH:MM)": str(row["CollectionTo"]),     
                "Stop Postcode": row["StopPostcode"]
            })
        return jsonData
