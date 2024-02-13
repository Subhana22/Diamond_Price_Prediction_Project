

'''path="notebooks/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(file,"w") as f:
    pass'''

from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(1,0.3,62.1,58,4.27,4.29,2.66,499,"Ideal","E","SI1")
data=custdataobj.get_data_as_dataframe()
print(data)
