# importer les bibliothèques

import pandas as pd
import json


# Importation et encoding 
drugs_df = pd.read_csv("drugs.csv")
pubmed_df = pd.read_csv("pubmed.csv")


# Création d'une fonction qui corrige le format date


def correct_date_pubmed(input_date):
    try :
        input_date = pd.to_datetime(
            input_date,
            format = "%d/%m/%Y"
        )
    except :
        input_date = pd.to_datetime(input_date,
                       format = "%Y-%m-%d"
                      )
    
    return input_date


# la fonction renvoie une table qui contient les variables suivantes: le médicament, l'article , le journal et la date de publication

def get_pub(input_drug):
    output = (pubmed_df
    .assign(drug = input_drug)
    .assign(date_pub = lambda X : X.date.apply(correct_date_pubmed))
    .assign(title_upper = lambda X : X.title.str.upper())
    .loc[
     lambda X : X.title_upper.str.find(input_drug.upper()) != -1, 
     ["drug","title","journal", "date_pub"]])
    return output

df_pub = pd.DataFrame()
for drug in drugs_df.drug:
    df_pub = pd.concat([df_pub,get_pub(drug)], ignore_index = True)

    
df_pub

