from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def sravan_portfolio_main():
    return render_template('main.html')

@app.route('/dna_classification')
def dna_classification_project():
    return render_template('dna.html')

@app.route('/board_game_review')
def board_game_review_project():
    return render_template('board_game_review.html')

@app.route('/breastcancer_prediction')
def breastcancer_prediction_project():
    return render_template('breastcancer.html')

@app.route('/mask_cnn_rnn')
def mask_cnn_rnn_project():
    return render_template('mask_rnn.html')

@app.route('/mnist')
def mnist_project():
    return render_template('mnist.html')

@app.route('/stock_market_clustering')
def stock_market_clustering_project():
    return render_template('stock.html')

@app.route('/credit_fraud_detection')
def credit_fraud_project():
    return render_template('credit_fraud.html')


if __name__ == "__main__":
    app.run(debug = 'True', host = '0.0.0.0')