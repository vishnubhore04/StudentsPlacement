import numpy as np
import pandas as pd
import json
import pickle
import config

class StudentData():
    def __init__(self,KNOWLEDGE,COMMUNICATION,PRESENTATION):
        self.KNOWLEDGE=KNOWLEDGE
        self.COMMUNICATION=COMMUNICATION
        self.PRESENTATION=PRESENTATION
    
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb")as f:
            self.model=pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.student_data=json.load(f)

    def get_predict_result(self):
        self.load_model()
        test_array=np.zeros(len(self.student_data["columns"]))
        test_array[0]=self.KNOWLEDGE
        test_array[1]=self.COMMUNICATION
        test_array[2]=self.PRESENTATION

        print("Test Array:",test_array)

        predict_result=self.model.predict([test_array])

        return predict_result
    
    if __name__ =="__main__":

        std_data=StudentData(KNOWLEDGE,COMMUNICATION,PRESENTATION)
        std_data.get_predict_result()

