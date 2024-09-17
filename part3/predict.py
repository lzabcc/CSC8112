import pandas as pd
import matplotlib.pyplot as plt

from ml_engine import MLPredictor


def predict(data_df):

    predictor = MLPredictor(data_df)

    predictor.train()

    predict_result = predictor.predict()

    figure = predictor.plot_result(predict_result)

    figure.savefig("prediction.png")

    plt.show()
