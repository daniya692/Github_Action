import pandas as pd


#Create a Python class that enables data loading from CSV/XLSX files and provides functionalities
class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        
#a. Load the CSV/XLSX file.
    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format")
            
#b. Print summaries of all numeric variables in the dataset.
    def summarize_numeric_variables(self):
        if self.data is None:
            raise ValueError("Data not loaded yet")
        
        numeric_columns = self.data.select_dtypes(include=['number']).columns
        numeric_summary = self.data[numeric_columns].describe()
        print(numeric_summary)
    

# Example
data_analyzer = DataAnalyzer('train.csv')
data_analyzer.load_data()

data_analyzer.summarize_numeric_variables()