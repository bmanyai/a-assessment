from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
   response = {"message":"Hello Proxy!"}
   return jsonify(response)

if __name__ == "__main__":
   app.run(host='0.0.0.0',port='9090',debug = False)
