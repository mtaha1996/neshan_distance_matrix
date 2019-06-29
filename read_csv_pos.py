from excel_export import excel
import requests

import pandas as pd


class DistanceMatrix:
    def __init__(self, path_raw_csv, header=None):
        # path to .csv file that contains the data
        path = path_raw_csv

        # read the csv file from the
        self.df = pd.read_csv(path, header=header)
        self.origins = []
        self.destinations = []

    def get_origins(self):
        org_df = pd.DataFrame(self.df)

        org_df["originLat"].dropna(inplace=True)
        org_df["originLong"].dropna(inplace=True)

        org_lat = list(org_df["originLat"])
        org_long = list(org_df["originLong"])

        org = []

        for i in range(len(org_lat)):
            lat, long = org_lat[i], org_long[i]

            org.append("{},{}".format(lat, long))

        self.origins = org

    def get_destinations(self):

        des_df = pd.DataFrame(self.df)

        des_df["destinationLat"].dropna(inplace=True)
        des_df["destinationLong"].dropna(inplace=True)

        dest_lat = list(des_df["destinationLat"])
        dest_long = list(des_df["destinationLong"])

        dest = []

        for i in range(len(dest_lat)):
            lat, long = dest_lat[i], dest_long[i]

            dest.append("{},{}".format(lat, long))

        self.destinations = dest

    def calc_distance_matrix(self):
        self.get_origins()
        self.get_destinations()

        url = "https://api.neshan.org/v1/distance-matrix"

        params = self.create_params_for_url()
        headers = {"Api-Key": "service.aYJyb8rJYo8mePEBpNzhn3CnE1yR7jbhhVQt3ic1"}

        resp = requests.get(url, params=params, headers=headers)

        if resp.status_code == 200:
            self.save_to_excel("", resp.json())
            return resp.json()
        else:
            return resp.json()

    def create_params_for_url(self):
        tmp = "|"

        org = tmp.join(self.origins)
        dest = tmp.join(self.destinations)

        params = {"origins": org, "destinations": dest}

        return params

    def save_to_excel(self, path, response):

        res = []

        for row_idx in range(len(response["rows"])):
            res.append([])
            res[row_idx].append(response["origin_addresses"][row_idx])
            for elm in response["rows"][row_idx]["elements"]:
                res[row_idx].append("{} sec, {} meters".format(
                    elm["duration"]["value"],
                    elm["distance"]["value"]))

        res.insert(0, ["origins \\ destinations"] + response["destination_addresses"])

        excel(res, path)
