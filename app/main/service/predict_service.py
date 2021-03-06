import numpy as np

from .. import model
from ..util.model import predict
from ..util.preprocess import preprocess, check_input


def make_prediction(data):
    data = data['data']
    try:
        data['engine_capacity'] = float(data['engine_capacity'])
    except:
        data['engine_capacity'] = np.nan
    
    try:
        data['insurance_price'] = float(data['insurance_price'])
    except:
        data['insurance_price'] = np.nan
    
    if data['fuel'] == '':
        data['fuel'] = 'other'
    
    if data['model'] == '':
        data['model'] = 'other'
    
    if data['type'] == '':
        data['type'] = 'other'
    
    if data['gearbox'] == '':
        data['gearbox'] = 'other'

    preprocessed = preprocess(data)
    result = model.predict(preprocessed)

    return {
        "price": round(np.exp(result[0]), 2)
    }, 201
