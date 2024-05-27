import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__society = None
__model = None




def get_price(location, sqft, area_type, bed, bath, society):

    try:
        index_loc = __data_columns.index(location.lower())
        index_society = __data_columns.index(society.lower())

    except:
        index_loc,index_society = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = area_type
    x[2] = bed
    x[3] = bath
    x[4] = sqft

    if (index_society & index_loc) >= 0:
        x[index_loc]= 1
        x[index_society] = 1

    return round(__model.predict([x])[0], 2)




def get_location_and_society():
    return __locations, __society


def load_saved_artifacts():
    print('Loading saved artifacts.... start')
    global __data_columns
    global __locations
    global __society
    global __model

    with open('./artifacts/columns.json', 'r') as file:
        __data_columns=json.load(file)['data_columns']
        __locations = __data_columns[:242]
        __society = __data_columns[242:-3]


    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('Loading saved artigacts done.')





if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_and_society())

    # print(get_price('1st phase jp nagar', 1000,2,3,3,'viistla' ))
    print(get_price('1st phase jp nagar', 500,1,2,2,'viistla' ))
