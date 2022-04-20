import joblib
from h2o_wave import Q, ui, on
import numpy as np
import pandas as pd

from components import (
    get_meta,
    get_header,
    get_footer,
    get_user_input_form,
    get_status
)


async def make_base_ui(q: Q):
    q.client.theme = 'MCAC-Dark'

    q.page['meta'] = get_meta(q.client.theme)
    q.page['header'] = get_header()
    q.page['input_form'] = get_user_input_form()
    q.page['footer'] = get_footer()

    warn = "Fill the form and submit to check the eligibility!"
    q.page['status'] = get_status(warn, 0)


async def process_analysis(q: Q):
    loan_amount = float(q.args.loan_amount)
    loan_term = float(q.args.loan_terms)
    gender = q.args.gender
    status = q.args.status
    dependents = q.args.dependents
    graduated = q.args.graduated
    employment = q.args.employment
    area = q.args.area

    credit_history = float(q.args.credit_history)
    loan_amount_log = np.log(loan_amount)
    total_income = float(q.args.total_income)
    total_income_log = np.log(total_income)
    emi = loan_amount/loan_term
    balance_income = total_income - emi

    if gender == 'male':
        Gender_Male = 1
        Gender_Female = 0
    elif gender == 'female':
        Gender_Male = 0
        Gender_Female = 1

    if status == 'married':
        Married_Yes = 1
        Married_No = 0
    elif status == 'single':
        Married_Yes = 0
        Married_No = 1

    if dependents == '0':
        Dependents_0 = 1
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 0
    elif dependents == '1':
        Dependents_0 = 0
        Dependents_1 = 1
        Dependents_2 = 0
        Dependents_3 = 0
    elif dependents == '2':
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 1
        Dependents_3 = 0
    elif dependents == '3':
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 1

    if graduated == 'yes':
        Education_Graduate = 1
        Education_NotGraduate = 0
    elif graduated == 'no':
        Education_Graduate = 0
        Education_NotGraduate = 1

    if employment == 'yes':
        Self_Employed_No = 0
        Self_Employed_Yes = 1
    elif employment == 'no':
        Self_Employed_No = 1
        Self_Employed_Yes = 0

    if area == 'rural':
        Property_Area_Rural = 1
        Property_Area_Semiurban = 0
        Property_Area_Urban = 0
    elif area == 'semi_urban':
        Property_Area_Rural = 0
        Property_Area_Semiurban = 1
        Property_Area_Urban = 0
    elif area == 'urban':
        Property_Area_Rural = 0
        Property_Area_Semiurban = 0
        Property_Area_Urban = 1

    print(credit_history, loan_amount_log, total_income, total_income_log, emi, balance_income, gender, status, dependents,
          graduated, employment, area)
    print(type(credit_history), type(loan_amount_log), type(total_income), type(total_income_log), type(emi), type(balance_income),
          type(gender), type(status), type(dependents), type(graduated), type(employment), type(area))

    data = pd.DataFrame([[credit_history, loan_amount_log, total_income, total_income_log, emi, balance_income, Gender_Female, Gender_Male,
                          Married_Yes, Married_No, Dependents_3, Dependents_0, Dependents_1, Dependents_2, Education_Graduate, Education_NotGraduate,
                         Self_Employed_Yes, Self_Employed_No, Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban]],
                        columns = ['Credit_History', 'LoanAmount_log', 'TotalIncome', 'TotalIncome_log', 'EMI', 'Balance_Income', 'Gender_Female', 'Gender_Male',
                          'Married_No', 'Married_Yes', 'Dependents_3', 'Dependents_0', 'Dependents_1', 'Dependents_2', 'Education_Graduate', 'Education_Not Graduate',
                         'Self_Employed_No', 'Self_Employed_Yes', 'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban'])
    await getPrediction(q, data)


async def getPrediction(q: Q, df):
    model = joblib.load('Data/forest_model.sav')
    prediction = model.predict(df)
    print("Received")
    if prediction[0] == 0:
        warn = "Sorry! You are not eligible for a home loan."
        q.page['status'] = get_status(warn, 1)
    else:
        warn = "Congratulations! You are eligible for a home loan."
        q.page['status'] = get_status(warn, 2)
    await q.page.save()

