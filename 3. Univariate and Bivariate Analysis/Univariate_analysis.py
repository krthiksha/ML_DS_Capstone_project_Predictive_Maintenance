import pandas as pd
import numpy as np

class Univariate():
    
    def __init__(self,dataset):
        self.dataset = dataset

    # Method to separate the Quantitative and Qualitative Data
    def quanQual(self):  
        quan=[]
        qual=[]
        for columnName in self.dataset.columns:
            if (self.dataset[columnName].dtypes == "O"):   # "O" - Object Data type
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual

    # frequency table 
    def freqTable(self,columnName):
        frequency_table = pd.DataFrame(columns=["Unique_values","Frequency","Relative_frequency","Cumsum"])
        frequency_table["Unique_values"]=self.dataset[columnName].value_counts().index
        frequency_table["Frequency"]=self.dataset[columnName].value_counts().values
        frequency_table["Relative_frequency"]=frequency_table["Frequency"] / len(frequency_table["Frequency"])
        frequency_table["Cumsum"]=frequency_table["Relative_frequency"].cumsum()
        return frequency_table


    # univariate continuous calculation - measure of central tendency & measure of location of data 
    def univariate_continuous(self, quan):
        descriptive_analysis = pd.DataFrame(index=["Mean","Median","Mode", "Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR", "1.5_rule", "lower_bound", "upper_bound","min","max"],columns=quan)
        for columnName in quan:
            descriptive_analysis.loc["Mean",columnName]=self.dataset[columnName].mean()
            descriptive_analysis.loc["Median",columnName]=self.dataset[columnName].median()
            descriptive_analysis.loc["Mode",columnName]=self.dataset[columnName].mode()[0]
            descriptive_analysis.loc["Q1:25%",columnName]= self.dataset.describe()[columnName]["25%"]   # this code handles missing values by default
            descriptive_analysis.loc["Q2:50%",columnName]= self.dataset.describe()[columnName]["50%"] 
            descriptive_analysis.loc["Q3:75%",columnName]= self.dataset.describe()[columnName]["75%"] 
            descriptive_analysis.loc["99%",columnName]= np.percentile(self.dataset[columnName],99)   
            descriptive_analysis.loc["Q4:100%",columnName]= self.dataset.describe()[columnName]["max"] 
            descriptive_analysis.loc["IQR",columnName]= descriptive_analysis.loc["Q3:75%"][columnName] - descriptive_analysis.loc["Q1:25%"][columnName]
            descriptive_analysis.loc["1.5_rule",columnName]= 1.5 * descriptive_analysis.loc["IQR",columnName]
            descriptive_analysis.loc["lower_bound",columnName]= descriptive_analysis.loc["Q1:25%"][columnName] - descriptive_analysis.loc["1.5_rule",columnName]
            descriptive_analysis.loc["upper_bound",columnName] = descriptive_analysis.loc["Q3:75%"][columnName] + descriptive_analysis.loc["1.5_rule",columnName]
            descriptive_analysis.loc["min",columnName] = self.dataset[columnName].min()
            descriptive_analysis.loc["max",columnName] = self.dataset[columnName].max()
            descriptive_analysis.loc["skew",columnName] = self.dataset[columnName].skew()
            descriptive_analysis.loc["kurtosis",columnName] = self.dataset[columnName].kurtosis()
            descriptive_analysis.loc["Var",columnName] = self.dataset[columnName].var()
            descriptive_analysis.loc["Std_dev",columnName] = self.dataset[columnName].std()
        return descriptive_analysis

    # finding outliers
    def find_outlier(self,descriptive_analysis,quan):
        # check outliers
        least_outlier_cols = [ columnName for columnName in quan if descriptive_analysis.loc["min",columnName]<descriptive_analysis.loc["lower_bound",columnName]]
        greater_outlier_cols = [ columnName for columnName in quan if descriptive_analysis.loc["max",columnName]>descriptive_analysis.loc["upper_bound",columnName]]
        return least_outlier_cols, greater_outlier_cols


    # replacing outliers
    def replace_outlier(self,descriptive_analysis,quan):
        for columnName in quan:
            dataset.loc[dataset[columnName]<descriptive_analysis.loc["lower_bound",columnName],columnName]=descriptive_analysis.loc["lower_bound",columnName]
            dataset.loc[dataset[columnName]>descriptive_analysis.loc["upper_bound",columnName], columnName]=descriptive_analysis.loc["upper_bound",columnName]
        return 'replaced outliers', descriptive_analysis


        