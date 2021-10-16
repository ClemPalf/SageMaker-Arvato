import numpy as np
import pandas as pd
import os
import time
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def dataset_treatment(azdias, customers, cust=True):
    
    print("Deleting columns...")
    
    # Specific to customers
    if cust:
        del customers['PRODUCT_GROUP']
        del customers['CUSTOMER_GROUP']
        del customers['ONLINE_PURCHASE']
    
    # Just the person ID
    del azdias["LNR"]
    del customers["LNR"]
    
    
    # Replace 'X', 'XX' and 'nan' values with np.nan for 'CAMEO_DEUG_2015' and 'CAMEO_INTL_2015' columns
    cols = ["CAMEO_DEUG_2015", "CAMEO_INTL_2015"]

    azdias[cols] = azdias[cols].replace({"X": np.nan, "XX": np.nan})
    azdias[cols] = azdias[cols].astype(float) 
    customers[cols] = customers[cols].replace({"X": np.nan, "XX": np.nan})
    customers[cols] = customers[cols].astype(float) 
    
    # Create unkown attributes
    attributes_values = pd.read_csv('data/DIAS Attributes - Values 2017.csv', sep=';')
    attributes_values["Attribute"] = attributes_values["Attribute"].ffill() # To simply the visualisation
    unkown_attributes_values = attributes_values[attributes_values["Meaning"] == "unknown"].dropna().reset_index(drop=True)
    
    # Replace unkown attributes
    customers = unknown_to_NaN(customers, unkown_attributes_values)
    azdias = unknown_to_NaN(azdias, unkown_attributes_values)
    
    azdias["WOHNLAGE"] = azdias["WOHNLAGE"].replace({0: np.nan})
    customers["WOHNLAGE"] = customers["WOHNLAGE"].replace({0: np.nan})
    
    # Delete columns with too much missing values
    columns_to_delete = ["ALTER_KIND4", "ALTER_KIND3", "TITEL_KZ", "ALTER_KIND2", "ALTER_KIND1", "KK_KUNDENTYP", "KBA05_BAUMAX", "AGER_TYP", "EXTSEL992"]
    for column in columns_to_delete:
        del azdias[column]
        del customers[column]
    
    print("Deleting rows...")
    
    customers = remove_rows(customers, threshold=50)
    azdias = remove_rows(azdias, threshold=50)
    
    print("Encoding...")
    del customers["CAMEO_DEU_2015"]
    del customers["D19_LETZTER_KAUF_BRANCHE"]

    del azdias["CAMEO_DEU_2015"]
    del azdias["D19_LETZTER_KAUF_BRANCHE"]

    customers = date_to_year(customers)
    azdias = date_to_year(azdias)
    
    customers["OST_WEST_KZ"] = customers["OST_WEST_KZ"].replace({"W": 0, "O": 1})
    azdias["OST_WEST_KZ"] = azdias["OST_WEST_KZ"].replace({"W": 0, "O": 1})
    
    customers["ANREDE_KZ"] = customers["ANREDE_KZ"].replace({1: 0, 2: 1})
    azdias["ANREDE_KZ"] = azdias["ANREDE_KZ"].replace({1: 0, 2: 1})
    
    
    imputer = SimpleImputer(strategy="most_frequent") # With this parameter, we will replace the NaN values by the most frequent value for this parameter.
    imputer.fit(azdias) # We will fit the imputer on the azidias esclusively, as it contains the most data. 
    
    
    

    azdias = pd.DataFrame(imputer.transform(azdias), columns = azdias.columns)
    customers = pd.DataFrame(imputer.transform(customers), columns = customers.columns)
    
    scaler = StandardScaler()
    scaler.fit(azdias)
    azdias = pd.DataFrame(scaler.transform(azdias), columns = azdias.columns)
    customers = pd.DataFrame(scaler.transform(customers), columns = customers.columns)
    
    
    return azdias, customers

def dataset_treatment_test(azdias, customers):
    
    print("Deleting columns...")
    
    
    
    # Just the person ID
    del azdias["LNR"]
    del customers["LNR"]
    
    # Replace 'X', 'XX' and 'nan' values with np.nan for 'CAMEO_DEUG_2015' and 'CAMEO_INTL_2015' columns
    cols = ["CAMEO_DEUG_2015", "CAMEO_INTL_2015"]

    azdias[cols] = azdias[cols].replace({"X": np.nan, "XX": np.nan})
    azdias[cols] = azdias[cols].astype(float) 
    customers[cols] = customers[cols].replace({"X": np.nan, "XX": np.nan})
    customers[cols] = customers[cols].astype(float) 
    
    # Create unkown attributes
    attributes_values = pd.read_csv('data/DIAS Attributes - Values 2017.csv', sep=';')
    attributes_values["Attribute"] = attributes_values["Attribute"].ffill() # To simply the visualisation
    unkown_attributes_values = attributes_values[attributes_values["Meaning"] == "unknown"].dropna().reset_index(drop=True)
    
    # Replace unkown attributes
    customers = unknown_to_NaN(customers, unkown_attributes_values)
    azdias = unknown_to_NaN(azdias, unkown_attributes_values)
    
    azdias["WOHNLAGE"] = azdias["WOHNLAGE"].replace({0: np.nan})
    customers["WOHNLAGE"] = customers["WOHNLAGE"].replace({0: np.nan})
    
    # Delete columns with too much missing values
    columns_to_delete = ["ALTER_KIND4", "ALTER_KIND3", "TITEL_KZ", "ALTER_KIND2", "ALTER_KIND1", "KK_KUNDENTYP", "KBA05_BAUMAX", "AGER_TYP", "EXTSEL992"]
    for column in columns_to_delete:
        del azdias[column]
        del customers[column]
    
    print("Deleting rows...")
    
    #customers = remove_rows(customers, threshold=50)
    azdias = remove_rows(azdias, threshold=50)
    
    print("Encoding...")
    del customers["CAMEO_DEU_2015"]
    del customers["D19_LETZTER_KAUF_BRANCHE"]

    del azdias["CAMEO_DEU_2015"]
    del azdias["D19_LETZTER_KAUF_BRANCHE"]

    customers = date_to_year(customers)
    azdias = date_to_year(azdias)
    
    customers["OST_WEST_KZ"] = customers["OST_WEST_KZ"].replace({"W": 0, "O": 1})
    azdias["OST_WEST_KZ"] = azdias["OST_WEST_KZ"].replace({"W": 0, "O": 1})
    
    customers["ANREDE_KZ"] = customers["ANREDE_KZ"].replace({1: 0, 2: 1})
    azdias["ANREDE_KZ"] = azdias["ANREDE_KZ"].replace({1: 0, 2: 1})
    
    
    imputer = SimpleImputer(strategy="most_frequent") # With this parameter, we will replace the NaN values by the most frequent value for this parameter.
    imputer.fit(azdias) # We will fit the imputer on the azidias esclusively, as it contains the most data. 
    

    azdias = pd.DataFrame(imputer.transform(azdias), columns = azdias.columns)
    customers = pd.DataFrame(imputer.transform(customers), columns = customers.columns)
    
    scaler = StandardScaler()
    scaler.fit(azdias)
    azdias = pd.DataFrame(scaler.transform(azdias), columns = azdias.columns)
    customers = pd.DataFrame(scaler.transform(customers), columns = customers.columns)
    
    
    
    
    return azdias, customers

def get_unkown_repr(attrib, unkown_attributes_values):
    unkown = unkown_attributes_values[unkown_attributes_values["Attribute"] == attrib]["Value"]
    unkown = unkown.astype(str).str.cat(sep=",")
    unkown = [int(x) for x in unkown.split(",")]
      
    return [unkown]


def replace_unkown_with_nan(val, unkown):
    if val in unkown:
        return np.nan
    else:
        return val

def unknown_to_NaN(df, unkown_attributes_values):
    for attrib in unkown_attributes_values.Attribute:
        unkown = get_unkown_repr(attrib, unkown_attributes_values)
        if attrib in df.columns:   # For some reasons, some attributes are not present in the datasets
            df[attrib] = df[attrib].apply(replace_unkown_with_nan, args=(unkown))
    return df

def remove_rows(df, threshold):
    df = df.dropna(thresh=df.shape[1]-threshold).reset_index(drop=True) # thresh (int, optional): Require that many non-NA values.
    
    return df

def date_to_year(df):
    df["EINGEFUEGT_AM"] = pd.to_datetime(df["EINGEFUEGT_AM"])
    df["EINGEFUEGT_AM"] = df['EINGEFUEGT_AM'].map(lambda x: x.year)
    
    return df