from flask import Flask,request,jsonify,render_template
from project_app.utils import StudentData


app=Flask(__name__)

@app.route("/")
def hello_flask():
    return render_template("index.html")

@app.route("/predict_result" ,methods=['GET'])
def predict_result():
     
     data=request.form
     print("Data >>",data)
    
     KNOWLEDGE=eval(data["KNOWLEDGE"])
     COMMUNICATION=eval(data["COMMUNICATION"])
     PRESENTATION=eval(data["PRESENTATION"])



     std_data=StudentData(KNOWLEDGE,COMMUNICATION,PRESENTATION)
     result=std_data.get_predict_result()

     return jsonify({"Result":f"student is{result}"})

    
app.run(debug=False)
