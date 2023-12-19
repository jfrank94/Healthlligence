import pandas as pd 
import math 

def clinical_measures(df, measure, val_1, val_2=None, bp_flag=False):
    cm_df = df[df["Clinical_Measures"] == measure]
    cm_res = cm_df[(val_1 >= cm_df["Min_Value"]) & (val_1 < cm_df["Max_Value"])]
    if bp_flag: 
        bp_sys, bp_dia = val_1, val_2
        cm_res = cm_df[(bp_sys >= cm_df["Min_Value_Systolic"]) & (bp_sys <= cm_df["Max_Value_Systolic"]) & (bp_dia >= cm_df["Min_Value_Diastolic"]) & (bp_dia <= cm_df["Max_Value_Diastolic"])]
    cm_dec_rec = cm_res["Decision_Recommended"].values 
    cm_base_stat = cm_res["Base_Statement"].values[0] if type(cm_res["Base_Statement"].values[0]) != float else "No Base Statement"
    cm_type = cm_res["Decision_Type"].values[0]

    print("{} Decision Recommendations: ".format(measure))
    print(cm_dec_rec)
    print("{} Base Statement: ".format(measure))
    print(cm_base_stat)
    print("Type of Intervention/Action: ")
    print(cm_type)

    return cm_dec_rec, cm_base_stat, cm_type

cm_df = pd.read_csv("Clinical Measures Decision Table - DT for Script.csv")

clinical_measures(cm_df, "Blood Sugar (BS)", 150)
print("=================================================")
clinical_measures(cm_df,  "Blood Pressure (BP)", 120, 60, True)
print("=================================================")
clinical_measures(cm_df, "Resting Heart Rate (RHR)", 120)
