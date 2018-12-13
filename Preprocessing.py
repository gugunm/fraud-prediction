import pandas as pd

def load_praproses(input_path, output_path):
    file_input = open(input_path, 'r')

    data = pd.read_csv(file_input, sep=';')

    file_input.close()

    sex     = {'male':1 , 'female':2}
    smoker  = {'yes':1, 'no':0}
    region  = {'southwest':1 , 'northwest':2, 'southeast':3, 'northeast':4}

    data.sex = [sex[item] for item in data.sex]
    data.smoker = [smoker[item] for item in data.smoker]
    data.region = [region[item] for item in data.region]
    data['bmi'] = data['bmi'].str.replace(',','.')
    data['charges'] = data['charges'].str.replace('.','')

    bmi = data['bmi'].values
    column_bmi = []
    for i in bmi:
        column_bmi.append(float(i[:5]))

    charges = data['charges'].values
    column_charges = []
    for j in charges:
        column_charges.append(int(j))

    del data['bmi']
    del data['charges']
    data.insert(loc=2, column='bmi2', value=column_bmi)
    data.insert(loc=6, column='charges', value=column_charges)
    
    bins = [0, 10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
    labels = [1,2,3,4,5,6,7,8, 9, 10]
    data['bmi'] = pd.cut(data['bmi2'], bins=bins, labels=labels)
    del data['bmi2']
    
    bins = [0, 10, 20, 30, 40, 50, 60, 70 ,80, 90, 100]
    labels = [1,2,3,4,5,6,7,8, 9, 10]
    data['ages'] = pd.cut(data['age'], bins=bins, labels=labels)
    del data['age']

    df = pd.read_csv('./input/insurance_data.csv')
    label = df['insuranceclaim'].values
    data.insert(loc=7, column='insuranceclaim', value=label)

    data.to_csv(output_path, index=False)
#    print(data)

    return data

#load_praproses('./input/insurance_awal.csv', './input/insurance_bersih.csv')