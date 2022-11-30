# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 00:32:26 2022

@author: bipna
"""
from flask import Flask
import math

def integral(min,max,N):
    sum = 0
    dx = (max-min)/N
    for i in range(N):
        sum += abs(math.sin(min+dx*(i+0.5)))
    return sum*dx

app = Flask(__name__)
@app.route('/')
def index():
    return "Add numbers in the route to find the integral."

@app.route('/<min>/<max>')
def idtest(min,max):
    Ns = [10,100,1000,10000,100000,1000000]
    ookk = ""
    for N in Ns:
        number = integral(float(min),float(max),N)
        ookk+= str(number)+" "
    return (ookk)


@app.route('/<ok>')
def fof(ok):
    return "Please use url in route to find the integral"

if __name__ == "__main__":
    print("now starting to RUN")
    app.run(debug=True, host = "0.0.0.0", port =80)
