from fastapi import FastAPI
import dash_labs as dl
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from pyspark.sql import SparkSession


app=FastAPI()


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


@app.get("/")
def read_main():
    df = spark.createDataFrame(
        [
            (1, "foo"),  # create your data here, be consistent in the types.
            (2, "bar"),
        ],
        ["id", "label"]  # add your column names here
    )
    df_str=df.collect()
    return {"lohith says": f"DF is => ${df_str}"}
