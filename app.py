from flask import Flask, request, jsonify, render_template
from model_module import TagPredictor

app = Flask(__name__)

# instance de la classe de modèle
model = TagPredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # request.json pour récupérer les données du corps de la requête POST
    data = request.json
    print(data)
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    tags = model.predire_tags(question)
    return jsonify({"tags": tags})

if __name__ == '__main__':
    app.run(debug=True)

