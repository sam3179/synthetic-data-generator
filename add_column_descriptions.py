import pandas as pd


class AddColumnDescriptions():
    def __init__(self, sampled_data):
        self.sampled_data = sampled_data

    def add_column_descriptions(self):
        sampled_data_df = pd.DataFrame(self.sampled_data)
        print(sampled_data_df.info())
