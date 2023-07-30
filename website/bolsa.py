from flask import Blueprint, send_file, render_template
from . import projeto1
import os
bolsa = Blueprint('bolsa', __name__)

@bolsa.route('/projeto1')
def home():
    image_base64, date, variation= projeto1.save_image64()
    # juntar listas de data e variação para fazer o loop
    data_combined = zip(date, variation)

    # Convert data_combined to a list of dictionaries
    #data_list = [{'date': date_item, 'variation': variation_item} for date_item, variation_item in zipped_data]

    return render_template('projeto1.html', image_base64=image_base64,date=date , variation=variation, data_combined=data_combined)






    
