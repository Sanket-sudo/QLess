from flask import Flask, jsonify, request

import aprioriRec as ar 

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
	data = request.get_json()
	#return data['item']
	return redirect(url_for('products',prod_item = data['item']))
	
@app.route('/products/<prod_item>')
def recommendation(prod_id):
    # call recommendation function 
    product_list = list(ar.getItems(prod_item))
    return jsonify({"product_list":product_list})
	
'''	
if __name__ == "__main__":
	app.run()
'''
