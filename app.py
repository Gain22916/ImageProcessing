from flask import Flask, request
import json
import requests


global LINE_API_KEY
LINE_API_KEY = 'Bearer H9zHxu1IDMdWw9/IlDTHnieguNyPrLBrVPriCOycpSHboHvlBUZeQ1y0bCco0eRU2ZknEUmxrM83E+ovUkBNnxpm+teQH5Pbtiifm8ZYp/nNXuSjjjIRLnLapQm96Rd6ux7u+A5nqfcnze2q+lYHKgdB04t89/1O/w1cDnyilFU='


app = Flask(__name__)
 
@app.route("/")
def hello():
   return "Hello World!d : Gain Testing"

if __name__ == "__main__":
  app.run()
