import Test_Batch

import json

from flask import Flask, escape, request,jsonify

# from flask_cors import CORS

config_file_path="./bert_config.json"
model_path="./pytorch_model.bin"

model,device=Test_Batch.load_model(config_file_path,model_path)

dec=json.JSONDecoder()


app = Flask(__name__)
# cors = CORS(app)

@app.route('/get_answers',methods=['POST','GET'])
def get_answers():
    # print(request.form.get('context',force = True))
    # a=request.get_json(force = True)
    # dec.decode()
    data = dec.decode(request.get_json(silent=False,force = True))
    print(data)
    context =data['context']
    questions =data['questions']
    answers = Test_Batch.get_answers(model,device,context,questions)
    # print(answers) 
    return json.dumps(answers)


if __name__=="__main__":
    app.run(host = "localhost",port = 5000)