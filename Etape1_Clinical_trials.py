#!/usr/bin/env python


# importer les bibliothèques


import pandas as pd
import json



# Importation et encoding 7
# coding: utf-8

clinical_trials_df = pd.read_csv("clinical_trials.csv", encoding = "utf8<" )
drugs_df = pd.read_csv("drugs.csv")




# Création d'une fonction qui corrige le format date

def correct_date_clinical(input_date):
    try :
        input_date = pd.to_datetime(
            input_date,
            format = "%d %B %Y"
        )
    except :
        input_date = pd.to_datetime(input_date,
                       format = "%d/%m/%Y"
                      )
    
    return input_date


# Création d'une fonction qui renvoie le médicament, l'article scientifique, le journal de publication et la date de publication par le clique.


def get_clinical_trials(input_drug):
    output = (clinical_trials_df
    .assign(drug = input_drug)
    .assign(date_cli = lambda X : X.date.apply(correct_date_clinical))
    .assign(title_upper = lambda X : X.scientific_title.str.upper())
    .loc[
     lambda X : X.title_upper.str.find(input_drug.upper()) != -1, 
     ["drug","scientific_title","journal", "date_cli"]])
    return output

df_clin = pd.DataFrame()
for drug in drugs_df.drug:
    df_clin = pd.concat([df_clin,get_clinical_trials(drug)], ignore_index = True)
    #(get_clinical_trials(drug), ignore_index = True)
    
df_clin

