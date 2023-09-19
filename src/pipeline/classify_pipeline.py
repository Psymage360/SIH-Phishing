import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object


class ClassifyPipeline:
    def __init__(self):
        pass
    def Classify(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
class CustomData:
    def __init__(  self,
        url:str):
        self.url=url
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "url":[self.url]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)