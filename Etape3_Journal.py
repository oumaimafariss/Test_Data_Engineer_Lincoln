#!/usr/bin/env python

# importer les bibliothèques

import pandas as pd
import json


# Importation et encoding 
# coding: utf-8

clinical_trials_df = pd.read_csv("clinical_trials.csv", encoding = "utf8<" )
drugs_df = pd.read_csv("drugs.csv")
pubmed_df = pd.read_csv("pubmed.csv")



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
    #(get_clinical_trials(drug), ignore_index = True)
    
df_pub

# Creation de la table journal


df_journal=pd.DataFrame()
df_journal = pd.concat([df_clin,df_pub], ignore_index = True)
df_journal=df_journal.drop(columns=["scientific_title","title"])
df_journal

