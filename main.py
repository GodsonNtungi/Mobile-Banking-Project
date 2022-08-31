# import used packages
import streamlit as st
import pandas as pd
import joblib
from os.path import dirname, join, realpath

question_ans = {1: 'Yes', 2: 'No', 3: 'I dont know', 4: 'Refused to answer'}


# creating a function to format questions
def func(value):
    return question_ans[value]


# Heading
st.header('Mobile banking challenge')
st.image('Images/pic.webp', width=600)
st.markdown('#### A model to predict whether a person will use mobile or internet banking ')

# Creating a form to obtain values used in the model
my_form = st.form(key='mobile_form')
country_code = my_form.selectbox("select country_code", (1, 32, 71, 48, 25, 77, 141, 97, 60, 69, 130, 44, 47,
                                                         63, 51, 110, 59, 105, 49, 116, 58, 3, 99, 137, 126, 45,
                                                         46, 117, 75, 121, 8, 120, 11, 12, 74, 5, 61, 33, 124,
                                                         42, 89, 2, 87, 106, 132, 122, 127, 40, 95, 23, 104, 56,
                                                         142, 109, 34, 111, 101, 17, 86, 107, 68, 112, 10, 125, 118,
                                                         65, 79, 0, 119, 136, 27, 135, 91, 37, 50, 36, 76, 28,
                                                         102, 131, 15, 30, 92, 14, 84, 62, 108, 85, 94, 78, 55,
                                                         22, 139, 113, 129, 18, 70, 31, 19, 88, 93, 20, 100, 115,
                                                         29, 134, 98, 53, 6, 54, 140, 43, 21, 96, 82, 35, 133,
                                                         138, 73, 83, 24, 114, 41, 38, 81, 143, 9, 57, 123, 72,
                                                         67, 16, 64, 4, 13, 39, 128, 80, 66, 52, 7, 26, 103,
                                                         90))
region = my_form.selectbox('Select region', (-1, 0, 1, 2, 3, 4, 5, 6, 7))
age = my_form.number_input('Age', max_value=100, min_value=5, step=1, )
FQ1 = my_form.selectbox('The client Has ATM/debit card', (1, 2, 3, 4), format_func=func)
FQ2 = my_form.selectbox('The client has an ATM connected to an account with his name?', (1, 2, 3, 4), format_func=func)
FQ3 = my_form.selectbox('The client purchased with the ATM', (1, 2, 3, 4), format_func=func)
FQ4 = my_form.selectbox('The client has a credit card', (1, 2, 3, 4), format_func=func)
FQ5 = my_form.selectbox('The client used the credit card in 12 months', (1, 2, 3, 4), format_func=func)
FQ6 = my_form.selectbox('The client has deposited money to a bank account in the last 12 months', (1, 2, 3, 4),
                        format_func=func)
FQ7 = my_form.selectbox('The client has withdrawn money from a bank account in the last 12 months', (1, 2, 3, 4),
                        format_func=func)
FQ8 = my_form.selectbox('The client has savings in the last 12 months to start a business/farm', (1, 2, 3, 4),
                        format_func=func)
FQ9 = my_form.selectbox('The client has savings in the last 12 months for old age', (1, 2, 3, 4), format_func=func)
FQ10 = my_form.selectbox('The client has saved  money at a bank/financial institutions', (1, 2, 3, 4), format_func=func)
FQ11 = my_form.selectbox('The client has saved money at groups/clubs of any informal type', (1, 2, 3, 4),
                         format_func=func)
FQ12 = my_form.selectbox(
    'The client has a loan from formal financial institutions to purchase land, home, or apartment', (1, 2, 3, 4),
    format_func=func)
FQ13 = my_form.selectbox('The client has borrowed money for health/medical purposes in the last 12 months',
                         (1, 2, 3, 4),
                         format_func=func)
FQ14 = my_form.selectbox('The client has borrowed money to start/grow business or farm', (1, 2, 3, 4), format_func=func)
FQ15 = my_form.selectbox('The client has borrowed money from formal financial institutions - 12 months', (1, 2, 3, 4),
                         format_func=func)
FQ16 = my_form.selectbox('The client has borrowed money from friends, relatives, or family - 12 months', (1, 2, 3, 4),
                         format_func=func)
FQ17 = my_form.selectbox('The client has borrowed money from an informal saving. I.e group or club', (1, 2, 3, 4),
                         format_func=func)
FQ18 = my_form.selectbox('The client What is the possibility of coming up with 1/20 of per capita in 1 month',
                         (1, 2, 3, 4), format_func=func)
FQ19 = my_form.selectbox('The client source of money for above question', (1, 2, 3, 4, 5, 6, 7, 8))
FQ20 = my_form.selectbox('The client sent/gave money to friend/relative', (1, 2, 3, 4), format_func=func)
FQ21 = my_form.selectbox('The client received money from friend or relative', (1, 2, 3, 4), format_func=func)
FQ22 = my_form.selectbox('The client has payments for electricity, water, or trash in the last 12 months', (1, 2, 3, 4),
                         format_func=func)
FQ23 = my_form.selectbox('The client has received salary/wages in the last 12 months', (1, 2, 3, 4), format_func=func)
FQ24 = my_form.selectbox('The client is employed by government or public sector -12 months', (1, 2, 3, 4),
                         format_func=func)
FQ25 = my_form.selectbox('The client received any form of financial support from the government', (1, 2, 3, 4),
                         format_func=func)
FQ26 = my_form.selectbox('The client received pension in the last 12 months', (1, 2, 3, 4), format_func=func)
FQ27 = my_form.selectbox('The client a/c that received money from the government for first the first time?',
                         (1, 2, 3, 4),
                         format_func=func)
FQ28 = my_form.selectbox('The client  opened the a/c to receive payments from the government', (1, 2, 3, 4),
                         format_func=func)
FQ29 = my_form.selectbox('29. The client received money for  sale of livestock, agricultural products, crops, '
                         'produce? ( '
                         '12 months)', (1, 2, 3, 4), format_func=func)
FQ30 = my_form.selectbox('The client Was this your first a/c for transaction in above question 29', (1, 2, 3, 4),
                         format_func=func)
FQ31 = my_form.selectbox('The client  opened the a/c to receive payments in question 29', (1, 2, 3, 4),
                         format_func=func)
FQ32 = my_form.selectbox('The client received money from his/her business in the last 12 months', (1, 2, 3, 4),
                         format_func=func)
FQ33 = my_form.selectbox('The client owns a mobile phone', (1, 2, 3, 4), format_func=func)
FQ34 = my_form.selectbox('The client has national ID card', (1, 2, 3, 4), format_func=func)
FQ35 = my_form.selectbox('The client a/c received money from your employer for the first time ?', (1, 2, 3, 4),
                         format_func=func)
FQ36 = my_form.selectbox('The client opened the a/c to receive the money in above question', (1, 2, 3, 4),
                         format_func=func)
FQ37 = my_form.selectbox('The client owns a bank a/c', (1, 2, 3, 4), format_func=func)

submit = my_form.form_submit_button(label='Predict')

# importing all the important models and data used in preprocessing and predicting

model = joblib.load(join(dirname(realpath(__file__)),'Models/mobileModel.sav'))
oneHot = joblib.load(join(dirname(realpath(__file__)), 'preprocessing/Onehot.pkl'),)
scaler = joblib.load(join(dirname(realpath(__file__)), 'preprocessing/scaler.pkl'),)
importance = pd.read_csv(join(dirname(realpath(__file__)), 'Data/moreimportant.csv'),)
importance.set_index('Features',inplace=True)

# performing preprocessing
@st.cache
def preprocess(data):
    categorical_features = ['country_code', 'region', 'FQ1', 'FQ2', 'FQ3', 'FQ4', 'FQ6', 'FQ7', 'FQ8', 'FQ9', 'FQ10',
                            'FQ11', 'FQ12', 'FQ13', 'FQ14', 'FQ15', 'FQ16', 'FQ18', 'FQ19', 'FQ20', 'FQ21', 'FQ22',
                            'FQ23', 'FQ24', 'FQ25', 'FQ26', 'FQ29', 'FQ32', 'FQ33', 'FQ34', 'FQ37']

    data['age'] = scaler.transform(data['age'].values.reshape(-1, 1))
    newData = oneHot.transform(data[categorical_features])
    data2 = pd.DataFrame(newData.toarray(),columns=oneHot.get_feature_names_out())

    return pd.concat([data2, data['age']], axis=1)


if submit:
    values = {'country_code': country_code,
              'region': region,
              'age': age,
              'FQ1': FQ1,
              'FQ2': FQ2,
              'FQ3': FQ3,
              'FQ4': FQ4,
              'FQ6': FQ6,
              'FQ7': FQ7,
              'FQ8': FQ8,
              'FQ9': FQ9,
              'FQ10': FQ10,
              'FQ11': FQ11,
              'FQ12': FQ12,
              'FQ13': FQ13,
              'FQ14': FQ14,
              'FQ15': FQ15,
              'FQ16': FQ16,
              'FQ18': FQ18,
              'FQ19': FQ19,
              'FQ20': FQ20,
              'FQ21': FQ21,
              'FQ22': FQ22,
              'FQ23': FQ23,
              'FQ24': FQ24,
              'FQ25': FQ25,
              'FQ26': FQ26,
              'FQ29': FQ29,
              'FQ32': FQ32,
              'FQ33': FQ33,
              'FQ34': FQ34,
              'FQ36': FQ36,
              'FQ37': FQ37, }

    data = pd.DataFrame(values, index=[0])
    preprocessedData = preprocess(data)
    # predicting the output
    output = model.predict(preprocessedData[importance.iloc[:165].index])
    probability = model.predict_proba(preprocessedData[importance.iloc[:165].index])
    col={0:'Mobile Money',1:"Internet Banking"}
    if output[0] == 1:
        st.markdown(f'##### Your likely to use {col[output[0]]} 🏦, the probability is {round(max(probability[0])*100,2)} %')
    else:
        st.markdown(f'##### Your likely to use {col[output[0]]}  📱,the probability is {round(max(probability[0])*100,2)} %')