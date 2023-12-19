import pandas as pd 


data = []

def physical_impairment(*answers):
    '''
    1. Do you need someone to help you complete this survey?
    1a. If yes. Why do you need help? (Select all that apply)
    '''
    category = ["Physical Imapirment"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        ## Q1 & Q1a ##
        if answers[0] == "1 - Yes" and answers[1] == "1 - Hard of Hearing":
            barriers.append("Hearing Disorder")
        if answers[0] == "1 - Yes" and answers[1] == "2 - Vision Impaired":
            barriers.append("Vision Disorder")
        elif answers[0] == "1 - Yes" and answers[1] == "3 - Problems with Memory":
            barriers.append("Memory Disorder")
        elif answers[0] == "2 - No":
            barriers.append('N/A')
    except:
        print("Please enter correct answer.")


    ## CM Intervention ###
    if answers[0] == "1 - Yes" and barriers[-1] == "Hearing Disorder":
        cm_inter.append("Voice line should be TTY supported.")
    elif answers[0] == "1 - Yes" and barriers[-1] == "Vision Disorder":
        cm_inter.append("Send an alert to CM to confirm support from family or caregiver")
    elif answers[0] == "1 - Yes" and barriers[0] == "Hearing Disorder" and barriers[1] == "Vision Disorder":
        cm_inter.append("Send an alert to CM to see if member has used vision/hearing aid benefit.")
    elif answers[0] == "1 - Yes" and barriers[-1] == "Memory Disorder":
        cm_inter.append("Create an alert to CM for follow-up together more information. CM notes which will be evaluate for further intervention.")
    else:
        cm_inter.append("N/A")
    ## Patient Actions ###
    if "Hearing Disorder" in barriers or "Vision Disorder" in barriers or "Memory Disorder" in barriers:
        pa_inter.append("Patient will use equipment approved by health plan.")
    else:
        pa_inter.append("N/A")
    
    if problems == []:
        problems = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def language(*answers):
    '''
    1. Do you need someone to help you complete this survey? (Continued)
    2. What language do you prefer to speak?
    3. What language do you prefer to get written health information in?
    '''
    category = ["Language"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        if answers[0] == "1 - Yes" and answers[1] != "1 - English":
            barriers.append("Language")
        elif answers[1] == "1 - English":
            barriers.append('N/A')
    except:
        print("Please enter correct answer.")
    
    ### CM Intervention ###
    if barriers[-1] == "Language" and answers[1] != "6 - Other - FILL IN":
        cm_inter.append("Raise a task for translator service.")

    elif barriers[-1] == "Language" and answers[1] == "6 - Other - FILL IN":
        cm_inter.append("Create alert for further follow-up.")
    else:
        cm_inter.append("N/A")
    ### Patient Action ###
    if barriers[-1] == "Language":
        pa_inter.append("Patient will use interpreter services arrange by their care manager for their next doctor's visit.")
    else:
        pa_inter.append("N/A")

    if problems == []:
        problems = ["N/A"]
    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data

def advanced_directives(*answers):
    '''
    4. Do you have an advanced Directive for health care? 
    (This is a document that tells doctors and hospitals 
    what to do in case your are not able to speak for yourself.)
    4a. If yes, can you provide a copy to your care manager?
    4b. If no, would you like to talk with someone about getting an advance directive?
    '''
    category = ["Advanced Directives"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    
    def advanced_directives_4b(answer):
        ### CM Intervention ###
        if answer == "1 - Yes":
            cm_inter.append("CM: Create task for CM to talk to PCP about giving the patient an advance directive assist in scheduling an appointment.")
        else:
            cm_inter.append('N/A')
        ### Patient Action ###
        if answer == "1 - Yes":
            pa_inter.append("PA: Patient will follow up with appointment.")
        else:
            pa_inter.append('N/A')

    try:
        ## Q4 ##
        if answers[0] == "1 - Yes":
            barriers.append("Lack of communication")
        elif answers[0] == "2 - No":
            barriers.append('N/A')
    except:
        print("Please enter correct answer.")

    try: 
        ## Q4(a) ##
        if answers[1] == "1 - Yes":
            barriers.append('N/A')
        elif answers[1] == "2 - No":
            advanced_directives_4b(answers[2]) ## Must answer "yes" to invoke 4b.
    except: 
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def release_of_information(*answers):
    '''
    1. Do you need someone to help you complete this survey? (Continued)
    5. Can we talk to your support person or caregiver about your health if we cannot reach you or if there is an emergency?
    '''
    category = ["Release of Information (ROI)"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        if answers[0] == '1 - Yes' and answers[1] == '2 - No':
            barriers.append('Lack of caregiver')
        else:
            barriers.append('N/A')
    except:
        print("Please enter correct answer.")
    
   
    ### CM Intervention & Patient Action ###
    if answers[1] == '1 - Yes':
        cm_inter.append("Set preferred contact person.")
        pa_inter.append("Patient must share contact information with CM.")
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
   
    if problems == []:
        problems = ["N/A"]
    
    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def healthcare_provider(*answers):
    '''
    7. When was the last time you saw your doctor (Primary Care Provider)?
    '''
    category = ["Healthcare Provider"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        if answers[0] == "4 - Over a Year Ago":
            barriers.append("Non Compliance")
        elif answers[0] == "1 - This Month" or answers[0] == "2 - Three Months Ago" or answers[0] == "3 - Six Months Ago":
            barriers.append('N/A')
    except: 
        print("Please enter correct answer.")

    ### CM Intervention && Patient Actions ### 
    if barriers[-1] == "Non Compliance":
        cm_inter.append("CM to follow-up with doctor and alert patient for apt reminder.")
        pa_inter.append("Patient will go to scheduled doctor's appointment.")
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")

    if problems == []:
        problems = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def safety(*answers):
    
    '''
    9. What is your living situation? 
    10. Does your home have working smoke alarms?
    11. Do you always fasten your seat belt when you are in a car?
    '''
    category = ["Safety"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try: 
        ## Q9 ##
        if answers[0] == "1 - Alone":
            barriers.append('Living Alone')
        elif answers[0] == "4 - I don't have a place to live":
            barriers.append('Homelessness Z59.0')
        elif answers[0] == '2 - With someone' or answers[0].startswith('5 - Other'):
            barriers.append('N/A')
        
        ## Q10 & Q11 ##
        if answers[1] == '2 - No' or answers[2] == '2 - No':
            barriers.append('Safety barrier')
        elif answers[1] == '1 - Yes' and answers[2] == '1 - Yes':
            barriers.append('N/A')
    except:
        print('Please enter correct answer.')

    if problems == []:
        problems = ["N/A"]
    ### CM Intervention && Patient Actions ### 
    if barriers[0] == 'Homelessness Z59.0':
        cm_inter.append('CM will coordinate with social worker for referral to shelters/links to food pantry.')
        pa_inter.append('Patient will cooperate with social worker and use links to food pantry provided by CM.')
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    if 'Safety barrier' in barriers:
        idx = barriers.index('Safety barrier')
        cm_inter.append('CM will program care assistant to send an alert to patient to educate patient about this safety issue.')
        pa_inter.append('System will alert patient links to assistance programs and educational information')
        data.append(category + [barriers[idx]] + problems + [cm_inter[1]] + [pa_inter[1]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])

    return data 

def overall_health(*answers):

    problems, barriers, cm_inter, pa_inter = [], [], [], []
    '''
    TBD: There are no previous questions that leads to a "knowledge deficit". Consult with Amber to see if this 
    rule is needed without a knowledge deficit.
    12. How is your overall health?
    '''
    category = ["Overall Health"]
    try:
        if answers[0] == "1 - Excellent" or answers[0] == "5 - Poor":
            problems.append("Patient does not understand disease process.")
        elif answers[0] == "2 - Very Good" or answers[0] == "3 - Good" or answers[0] == "4 - Fair":
            problems.append("N/A")
    except: 
        print("Please enter correct answer.")
    
    ### CM Interventions & Patient Actions ### 
    if answers[0] == "1 - Excellent" or answers[0] == "5 - Poor":
        cm_inter.append("CM to create an alert for patient for possible education on this condition.")
        pa_inter.append("Patient will read all educational materials and links provided.")
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")

    if barriers == []:
        barriers = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def medication(*answers):
    '''
    15. How many different prescriptions are you taking?
    15a. If greater than 0. Do you take your prescriptions as prescribed?
    '''
    category = ["Medication"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q15 ##
        if answers[0] == "4 - 10+":
            barriers.append("Polypharmacy")
        else:
            barriers.append("N/A")
        ## Q15(a) ##
        if answers[0] != "1 - None" and (answers[1] == "2 - No" or answers[1] == "3 - Sometimes"):
            barriers.append("NC Medication")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Polypharmacy":
        cm_inter.append("CM will coordinate with PCP for a home health nurse to do a medication reconciliation and visit.")
        pa_inter.append("Patient will participate and work with nurse and pharmacy on reconciliation.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
 
    if barriers[-1] == "NC Medication":
        cm_inter.append("CM will send patient educational materials in regards to medication regimen importance.")
        pa_inter.append("Patient will be complaint with their primary doctor's treatment plan.")
        if len(cm_inter) == 1:
            data.append(category + [barriers[1]] + problems + cm_inter + pa_inter)
        else:
            data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    
    return data 

def emergency_room(*answers):
    '''
    16. How many times in the last 6 months have you been to the emergency room?
    '''
    category = ["Emergency Room"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try: 
        if answers[0] == "3 - 3-4" or answers[0] == "4 - 5+":
            barriers.append("In appropriate use of emergency room")
        else:
            barriers.append("N/A")
    except: 
        print("Please enter correct answer.")

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "In appropriate use of emergency room":
        cm_inter.append('Educate patient the difference between ER vs. Urgent Care, and send a list of Urgent Care facilities in the area.')
        pa_inter.append('Patient will verbalize understanding of use of ER vs. Urgent Care and read list of Urgent Care facilities in area.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    if problems == []:
        problems = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def hospital_admission(*answers):
    '''
    17. How many times in the last 6 months were you admitted to the hospital?
    ''' 
    category = ["Hospital Admission"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "3 - 3-4" or answers[0] == "4 - 5+":
            barriers.append("At risk for readmission")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "At risk for readmission":
        cm_inter.append("CM to look for gaps in care, such as, patient needing oxygen, home health, pain management, etc.")
        pa_inter.append("Patient must follow up with CM/PCP to mitigate gaps in care.")
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
    
    if problems == []:
        problems = ["N/A"]

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def oral_health(*answers):
    '''
    18. How is the health of your mouth?
    19. Do you have a dentist that you visit regularly (at least once a year)?
    '''
    category = ["Oral Health"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q18 ##
        if answers[0] == "5 - Poor":
             barriers.append("Poor oral health")
        else:
            barriers.append("N/A")
        
        ## Q19 ##
        if answers[1] == "2 - No":
            barriers.append("Non Compliance")
        else:
            barriers.append("N/A")
    except:
        print("Please enter the correct answer.")
    

    if problems == []:
        problems = ["N/A"]
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Poor oral health":
        cm_inter.append("Create task for CM for benefit check and facilitate dental appointment. Also, will prompt CM to complete oral assessment (OHRA).")
        pa_inter.append("Patient must follow up on benefit check, and complete oral assessment (OHRA) with CM.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])

    if barriers[-1] == "Non Compliance":
        cm_inter.append("CM to follow up on doctor and alert patient for apt reminder.")
        pa_inter.append("Patient will go to scheduled doctor's appointment.")
        if len(cm_inter) == 1:
            data.append(category + [barriers[1]] + problems + cm_inter + pa_inter)
        else:
            data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])

    return data 

def sleep(*answers):
    '''
    20. How many hours of sleep do you usually get each night?
    21. Do you snore or has anyone told you that you snore?
    '''
    category = ["Sleep"]
    problems, barriers, cm_inter, pa_inter = [], ["Altered sleep patterns"], [], []
    
    try: 
        ## Q21 ##
        if answers[0] == "2 - No":
            barriers.append('Poor oral health')
        else:
            barriers.append('N/A')
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
     ### CM Interventions & Patient Actions ###
    if barriers[-1] == "N/A":
        data.append(category + barriers + problems + cm_inter + pa_inter)
    elif barriers[-1] == "Poor oral health":
        cm_inter.append("Create task for CM for benefit check and facilitate dental appointment. Also, will prompt CM to complete oral assessment (OHRA).")
        pa_inter.append("Patient must follow up on benefit check, and complete oral assessment (OHRA) with CM.")
        data.append(category + [barriers[0]] + problems + cm_inter + pa_inter)
        data.append(category + [barriers[1]] + problems + cm_inter + pa_inter)

    return data 

def cardiovascular(*answers):
    '''
    22. Have you ever been told you have a heart or vascular problem (including high blood pressure)?
    '''
    category = ["Cardiovascular"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "1 - Yes":
            barriers.append("Cardiovascular barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Cardiovascular barrier":
        cm_inter.append('CM will complete cardiovascular assessment.')
        pa_inter.append('Patient will complete cardiovascular assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 
    
def blood_sugar(*answers):
    '''
    23. Have you ever been told you have high blood sugar?
    '''
    category = ["Blood Sugar (Endocrine)"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "1 - Yes":
            barriers.append("Blood sugar barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Blood sugar barrier":
        cm_inter.append('CM will complete blood sugar assessment.')
        pa_inter.append('Patient will complete blood sugar assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def pulmonary(*answers):
    '''
    24. Have you every been told that you have a problem with your lungs?
    '''
    category = ["Pulmonary"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    
    try:
        if answers[0] == "1 - Yes":
            barriers.append("Pulmonary barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Pulmonary barrier":
        cm_inter.append('CM will complete pulmonary assessment.')
        pa_inter.append('Patient will complete pulmonary assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def gastrointestinal(*answers):
    '''
    25. Have you ever been told you have a problem with your stomach or intestines? (Do you have diffculty having a bowl movement?)
    '''
    category = ["Gastrointestinal"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    
    try:
        if answers[0] == "1 - Yes":
            barriers.append("Gastrointestinal barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Gastrointestinal barrier":
        cm_inter.append('CM will complete gastrointestinal assessment.')
        pa_inter.append('Patient will complete gastrointestinal assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def renal(*answers):
    '''
    26. Have you ever been told you have a problem with your kidneys or urinary system? (Do you have trouble urinating?)
    '''
    category = ["Renal"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    
    try:
        if answers[0] == "1 - Yes":
            barriers.append("Renal barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Renal barrier":
        cm_inter.append('CM will complete renal assessment.')
        pa_inter.append('Patient will complete renal assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def integumentary(*answers):
    '''
    27. Have you ever been told you have a problem with your skin? (Do you have any sores or wounds?)
    '''
    category = ["Integumentary"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    
    try:
        if answers[0] == "1 - Yes":
            barriers.append("Integumentary barrier")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Integumentary barrier":
        cm_inter.append('CM will complete integumentary assessment.')
        pa_inter.append('Patient will complete integumentary assessment with CM.')
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def pain(*answers):
    '''
    28. In the past 7, days have you felt pain?
    28(c). If yes. Rate your pain on a scale of 0-10 (with 0 being no pain and 10 being the worst pain).
    28(d). If yes. How do you treat the pain? (Select all the apply) 
    '''
    category = ["Pain Assessment"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        ## Q28 ##
        if answers[0] == "1 - Yes":
            barriers.append("Pain")
        else:
            barriers.append("N/A")
    except: 
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[-1] == "Pain" and (answers[1] == "4 - 7-9" or answers[1] == "5 - 10") and answers[2] == "1 - No":
        cm_inter.append("CM consult PCP or referral for pain management.")
        pa_inter.append("Patient will follow up with PCP/referral for pain management treatment")
    else:
        cm_inter.append('N/A')
        pa_inter.append('N/A')

    data.append(category + barriers + problems + cm_inter + pa_inter)
    return data 

def sensory_ability(*answers):
    '''
    1. Do you need someone to help you complete this survey?
    1a. If yes. Why do you need help? (Select all that apply)
    29. Do you have any problems with vision? (Select all that apply)
    30. Do you have any problems with hearing?
    '''
    category = ["Sensory Ability"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        ## Q29 ##
        if answers[0] == "1 - Yes" and answers[1] == "2 - Vision Impaired" and answers[2] == "1 - None":
            barriers.append("Vision disorder")
        else:
            barriers.append("N/A")
        ## Q30 ##
        if answers[4] != "None":
            barriers.append("Auditory disorder")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Vision disorder":
        cm_inter.append("Send task to CM to check benefit for obtaining glasses/contacts or an appointment for the optomologist.")
        pa_inter.append("Patient will obtain prescribed glasses/contacts or follow up with optomologist appointment.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    if barriers[-1] == "Auditory disorder":
        cm_inter.append("Send task to CM to check benefits for possible assistance from ENT or obtaining hearing test and aids.")
        pa_inter.append("Patient will obtain hearing test and aids or follow up with ENT consultation.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data

def assistance(*answers):
    '''
    31. Do you need help when seeing your healthcare providers (transportation, caregiver assistance, interpreter services)?
    31b. If yes. Do you put off or neglect going to the doctor or picking up your prescription(s) because of the distance or transportation?
    32. Do you use any durable medical equipment (DME)?
    33. Do you receive any in home assistance?
    33b. If no. Do you need any in home services?
    33c. If yes. What in home services do you feel you need. (Select all the apply)
    '''
    category = ["Assistance"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    try:
        ## Q31 ##
        if answers[0] == "1 - Yes":
            barriers.append("Lack of availability of services")
        else:
            barriers.append("N/A")
        
        ## Q31b ##
        if answers[1] == "1 - Yes":
            barriers.append("NC Medication")
            barriers.append("No transportation")
        else:
            barriers.append("N/A")
        
        ## Q32 ## 
        if answers[0] == "1 - Yes" and answers[2] == "2 - Caregiver Assistance" and answers[3] == "2 - No":
            barriers.append("No DME")
        else:
            barriers.append("N/A")
        
        ## Q33 ## 
        if answers[0] == "1 - Yes" and answers[4] == "2 - No":
            barriers.append("No caregiver")
        else:
            barriers.append("N/A")
        
        ## Q33b ##
        if answers[0] == "1 - Yes" and answers[5] == "2 - No":
            barriers.append("Lack of availability of services")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Lack of availability of services":
        cm_inter.append("CM to assist in providing patient a closer provider to where they live, and CM will complete transportation coordination assessment.")
        pa_inter.append("Patient to attend appointment to new provider and will complete transportation coordination assessment with CM.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    if "NC Medication" and "No transportation" in barriers: 
        idx_1, idx_2 = barriers.index("NC Medication"), barriers.index("No transportation")
        cm_inter.append("CM will check patient's transportation beenfit and set up transportation for the patient's appointments.") 
        cm_inter.append("CM will send patient educational materials in regards to medication regimen importance.")
        pa_inter.append("Patient will attend their appointments and use transportation arranged by their CM.")
        pa_inter.append("Patient will be compliant with medication regimen.")
        data.append(category + [barriers[idx]] + problems + [cm_inter[1]] + [pa_inter[1]])
        data.append(category + [barriers[idx]] + problems + [cm_inter[2]] + [pa_inter[2]])
    else:
        cm_inter.append("N/A")
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
        data.append(category + [barriers[1]] + problems + [cm_inter[2]] + [pa_inter[2]])
    
    if "No caregiver" in barriers:
        idx = barriers.index("No caregiver")
        cm_inter.append("CM will assist the patient in getting IHSS if the patient meets for these services.")
        pa_inter.append("Patient will work with their CM to possibly get IHSS.")
        data.append(category + [barriers[idx]] + problems + [cm_inter[3]] + [pa_inter[3]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[2]] + problems + [cm_inter[3]] + [pa_inter[3]])

    if "No DME" in barriers:
        idx = barriers.index("No DME")
        cm_inter.append("CM will coordinate with PCP and generate a referral for DME needed.")
        pa_inter.append("Patient will use new DME for ambulation and self-care.")
        data.append(category + [barriers[idx]] + problems + [cm_inter[4]] + [pa_inter[4]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[3]] + problems + [cm_inter[4]] + [pa_inter[4]])
    
    if answers[6] == "1 - Transportation" and "Lack of availability of services" in barriers: 
        idx = barriers.index("Lack of availability of services")
        cm_inter.append("CM to assist in providing patient a closer provider to where they live or providing transportation to closest provider.")
        pa_inter.append("Patient to attend appointment to new provider with possible transportation provided.")
        data.append([category + barriers[idx]] + problems + [cm_inter[5]] + [pa_inter[5]])
    elif answers[6] == "2 - Caregiver Assistance" and "Lack of availability of services" in barriers:
        idx = barriers.index("Lack of availability of services")
        cm_inter.append("CM will assist the patient in getting IHSS if the patient meets for these services.")
        pa_inter.append("Patient will work with her CM to possibly get IHSS.")
        data.append(category + [barriers[idx]] + problems + [cm_inter[5]] + [pa_inter[5]])
    elif answers[6] == "3 - Other - FILL IN" and "Lack of availability of services" in barriers:
        idx = barriers.index("Lack of availability of services")
        cm_inter.append("CM will identify other needs.")
        pa_inter.append("N/A")
        data.append(category + [barriers[idx]] + problems + [cm_inter[5]] + [pa_inter[5]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[4]] + problems + [cm_inter[5]] + [pa_inter[5]])

    return data 

def ambulation_status(*answers):
    '''
    31. Do you need help when seeing your healthcare providers (transportation, caregiver assistance, interpreter services)?
    34. How minutes can you walk or move around?
    35. Do you have trouble with your balance?
    36. Have you fallen in the last 6 months?
    '''
    category = ["Ambulation Status"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q34 ##
        if answers[0] == "1 - 0-15" and answers[1] == "2 - No":
            barriers.append("Sedentary lifestyle")
        else:
            barriers.append("N/A")
        
        ## Q35 ##
        if answers[2] == "1 - Yes":
            barriers.append("Fall risk")
        else:
            barriers.append("N/A")
        
        ## Q36 ##
        if answers[2] == "1 - Yes":
            barriers.append("Fall risk")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Sedentary lifestyle": 
        cm_inter.append("CM will coordinate with PCP and generate a referral for an outpatient physical and occupational therapy.")
        pa_inter.append("Patient will participate in physical and occupational therapy program.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    if answers[2] == "1 - Yes" and barriers[-1] == "Fall risk":
        cm_inter.append("CM will complete fall risk assessment.")
        pa_inter.append("Patient will complete fall risk assessment with CM.")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    return data 

def physical_activity(*answers):
    '''
    31. Do you need help when seeing your healthcare providers (transportation, caregiver assistance, interpreter services)?
    37. In the past 7 days, how many days did you exercise?
    '''
    category = ["Physical Activity"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q37 ##
        if answers[0] == "1 - 0" and answers[1] == "2 - No":
            barriers.append("Sedentary lifestyle")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Sedentary lifestyle":
        cm_inter.append("CM will coordinate with PCP and generate a referral for a outpatient physical and occupational therapy.")
        pa_inter.append("Patient will participate in physical and occupational therapy program.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    return data 

def functional_stats(*answers):
    '''
    31a. If yes. Please select the help you need? (Select all that apply)
    38. In the past 7 days, did you need help from others to take care of things such as laundry and housekeeping, 
        banking, shopping, using the telephone, food preparation, transportation, or taking your own medications?
    '''
    try: 
        ## Q38 ##
        if answers[0] == "1 - Yes" and answers[1] == "2 - Caregiver Assistance":
            barriers.append("No caregiver")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[0] == "No caregiver":
        cm_inter.append("CM will assist the patient in getting IHSS if the patient meets for these services.")
        pa_inter.append("Patient will work with their CM to possibly get IHSS.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])

    return data 

def tobacco_alcohol_use(*answers):
    '''
    45. Do you use any tobacco products (including smokeless tobacco)?
    45a. If yes. Are you interested in quitting tobacco?
    46. Do you consume alcoholic beverages?
    46a. If yes. In the past 7 days, how many days have you drank alcohol?
    46b. If yes. How many times in the past year have you had four or more alcoholic drinks in a day?
    46c. If yes. Are you interested in receiving help for your alcohol consumption?
    46d. If yes. Do you ever drive after drinking, or ride with a driver who has been drinking?
    '''

    category = ["Tobacco & Alcohol Use"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try: 
        ## Q45 & Q45a ##
        if answers[0] == "1 - Yes" and answers[1] == "2 - No":
            barriers.append("Tobacco use")
        else:
            barriers.append("N/A")
        
        ## Q46, Q46a-c ##
        if answers[2] == "1 - Yes" and (answers[3] == "3 - 3-4" or answers[3] == "4 - 5+") and (answers[4] == "3 - 3-4" or answers[4] == "4 - 5+") and (answers[5] == "1 - Yes" or answers[5] == "2 - No"):
            barriers.append("Alcohol use")
        else:
            barriers.append("N/A")
        
        ## Q46d ##
        if answers[2] == "1 - Yes" and (answers[6] == "1 - Yes" or answers[6] == "3 - Sometimes"):
            barriers.append("Safety barrier")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Tobacco use":
        cm_inter.append("CM will send patient educational pamphlets on the effects of tobacco. May also set up an appointment with PCP for an advance directive.")
        pa_inter.append("Patient will read educational materials received about smoking and its effects. May need to follow up appointment for any advance directive.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])

    if "Alcohol use" in barriers:
        idx = barriers.index("Alcohol use")
        cm_inter.append("CM will assist patient in finding a program to quit drinking such as a local AA group near the patient's home.")
        pa_inter.append("Patient will participate in a program to quit drinking.")
        data.append(category + [barriers[idx]] + problems + [cm_inter[1]] + [pa_inter[1]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
    
    if "Safety barrier" in barriers:
        idx = barriers.index("Safety barrier")
        cm_inter.append("CM will program care assistant to send an alert to patient to educate patient about this safety issue.")
        pa_inter.append("System will alert patient links to assistance programs and educational information")
        data.append(category + [barriers[idx]] + problems + [cm_inter[2]] + [pa_inter[2]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[2]] + problems + [cm_inter[2]] + [pa_inter[2]])
    
    return data

def mental_health(*answers):
    '''
    48. If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?
    49. Have your feelings caused you distress or interfered with your ability to get along socially with family or friends?
    50. How often is stress a problem for you in handling such things as (your health, your finances, your family or social relationships, or your work)?
    51. In the past 2 weeks, how often have you felt nervous, anxious, or on edge?
    52. In the past 2 weeks, how often were you not able to stop worrying or control your worrying?
    '''

    category = ["Mental Health"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q48 ##
        if answers[0] == "3 - Very Difficult" or answers[0] == "4 - Extremely Difficult":
            barriers.append("Ineffective coping")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]

    ### CM Interventions & Patient Actions ###
    if answers[1] == "Yes" and (answers[2] == "4 - Often" or answers[2] == "5 - Always") and (answers[3] == "2 - More than half the days" or answers[3] == "3 - Nearly everday") and (answers[4] == "2 - More than half the days" or answers[4] == "3 - Nearly everday"):
        cm_inter.append("CM send a task to social worker or behavioral health specialist.")
        pa_inter.append("Patient should follow up with social worker or behavioral health specialist.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data

def mental_health_phq(*answers):
    '''
    53. In the past 2 weeks, how often have you felt down, depressed, or hopeless?
    54. In the past 2 weeks, how often have you felt little interest or pleasure in doing things?
    55. In the past 2 weeks, how often have you had trouble falling or staying asleep, or been sleeping too much?
    56. In the past 2 weeks, how often have you felt tired or had little energy?
    57. In the past 2 weeks, how often have you had a poor appetite or overate?
    58. In the past 2 weeks, how often have you felt bad about yourself – or that you are a failure or have let yourself or your family down?
    59. In the past 2 weeks, how often have you had trouble concentrating on things, such as reading the newspaper or watching television?
    60. In the past 2 weeks, how often have you noticed moving or speaking so slowly that other people could have noticed? 
        Or the opposite – being so fidgety or restless that you have been moving around a lot more than usual?
    61. In the past 2 weeks, how often have you had thoughts that you would be better off dead or of hurting yourself in some way?
    '''

    category = ["Mental Health Depression - PHQ9"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []
    depr_thresh = 0
    try:
        for i in range(len(answers)):
            depr_thresh += int(answers[i][0])
        if depr_thresh > 10:
            barriers.append("Depression")
        else: 
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")

    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Depression":
        cm_inter.append("CM will coordinate with PCP and generate a referral for a home visiting social worker/mental health provider.")
        pa_inter.append("Patient will participate with social worker or assist an outpatient mental health treatment.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

def employment(*answers):
    '''
    62. Do you have a job?
    '''

    category = ["Employment"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "2 - No":
            barriers.append("Unemployment unspecified Z56.0")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Unemployment unspecified Z56.0":
        cm_inter.append("CM will coordinate with PCP for a social worker referral/links to food pantry.")
        pa_inter.append("Patient will attend cooperate with social worker and use links to food pantry provided by CM.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

def child_care(*answers):
    '''
    63. Do problems getting child care make it difficut for you to work or study?
    '''

    category = ["Child Care"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "1 - Yes":
            barriers.append("Dependent relative needing care at home Z63.6")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Dependent relative needing care at home Z63.6":
        cm_inter.append("CM will assist with obtaining IHSS.")
        pa_inter.append("Patient will coordinate with CM for IHSS.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

def education(*answers):
    '''
    63. Do problems getting child care make it difficut for you to work or study?
    '''

    category = ["Education"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "1 - Grade School":
            barriers.append("Other problems related to education or literacy Z55.8")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Other problems related to education or literacy Z55.8":
        cm_inter.append("CM will give patient links that can help with attending school.")
        pa_inter.append("Patient will use resources provided.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

def financial(*answers):
    '''
    65. In the past 12 months, have you worried that your food would run out before you had money to buy more?
    66. In the past 12 months, has your food run out before you had money to get more?
    67. In the past 12 months, has the electricity , gas , or water company threatened to shut off services in your home?
    68. How often does this describe you? I don’t have enough money to pay my bills?
    69. Are you worried or concerned that in the next two months you may not have stable housing?
    '''
    
    category = ["Financial"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        ## Q65 - Q68 ##
        if answers[0] == "1 - Yes" and answers[1] == "1 - Yes" and answers[2] == "1 - Yes" and (answers[3] == "4 - Often" or answers[3] == "5 - Always"):
            barriers.append("Low income Z59.6")
        else:
            barriers.append("N/A")

        ## Q69 ##
        if answers[4] == "1 - Yes":
            barriers.append("Problems related to housing and economic circumstances Z59.9")
            barriers.append("Inadequate housing Z59.1")
        else:
            barriers.append("N/A")
            barriers.append("N/A")

    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Low income Z59.6":
        cm_inter.append("CM will coordinate with PCP for a social worker referral/links to food pantry.")
        pa_inter.append("Patient will attend cooperate with social worker and use links to food pantry provided by CM.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])

    if barriers[1] == "Problems related to housing and economic circumstances Z59.9" and barriers[2] == "Inadequate housing Z59.1":
        cm_inter.append("CM will coordinate with PCP for a social worker referral/links to food pantry.")
        cm_inter.append("CM will coordinate with PCP for a social worker referral/links to food pantry.")
        pa_inter.append("Patient will attend cooperate with social worker and use links to food pantry provided by CM.")
        pa_inter.append("Patient will attend cooperate with social worker and use links to food pantry provided by CM.")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
        data.append(category + [barriers[2]] + problems + [cm_inter[2]] + [pa_inter[2]])
    else:
        cm_inter.append("N/A")
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[1]] + problems + [cm_inter[1]] + [pa_inter[1]])
        data.append(category + [barriers[2]] + problems + [cm_inter[2]] + [pa_inter[2]])

    return data 

def support(*answers):
    '''
    70. How often do you get the social and emotional support you need?
    '''
    
    category = ["Support"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "1 - Never" or answers[0] == "2 - Rarely":
            barriers.append("Lack of resources")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Lack of resources":
        cm_inter.append("CM will check patient's transportation benefits and coordinate available community services which the patient can participate in.")
        pa_inter.append("Patient will use transportation and participate in community programs such as CBAS.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

def home_safety(*answers):
    '''
    71. Do you feel safe at home?
    '''
    category = ["Home Safety"]
    problems, barriers, cm_inter, pa_inter = [], [], [], []

    try:
        if answers[0] == "2 - No":
            barriers.append("Safety barrier")
        else:
            barriers.append("N/A")
    except:
        print("Please enter correct answer.")
    
    if problems == []:
        problems = ["N/A"]
    
    ### CM Interventions & Patient Actions ###
    if barriers[0] == "Lack of resources":
        cm_inter.append("CM will program care assistant to send an alert to patient to educate patient about this safety issue.")
        pa_inter.append("System will alert patient links to assistance programs and educational information.")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    else:
        cm_inter.append("N/A")
        pa_inter.append("N/A")
        data.append(category + [barriers[0]] + problems + [cm_inter[0]] + [pa_inter[0]])
    
    return data 

### Testing ###
patient_df = pd.read_csv("patient-scenario.csv")
def decision_rules(patient_df, patient_num, data):
    patient = patient_df[patient_df["patient ID"] == patient_num]

    physical_impairment(patient["Q1"].values[0], patient["Q1(a)"].values[0])
    language(patient["Q1"].values[0], patient["Q2"].values[0])
    advanced_directives(patient["Q4"].values[0], patient["Q4(a)"].values[0], patient["Q4(b)"].values[0])
    release_of_information(patient["Q1"].values[0], patient["Q5"].values[0])
    healthcare_provider(patient["Q7"].values[0])
    safety(patient["Q9"].values[0], patient["Q10"].values[0], patient["Q11"].values[0])
    overall_health(patient["Q12"].values[0])
    medication(patient["Q15"].values, patient["Q15(a)"].values[0])
    emergency_room(patient["Q16"].values[0])
    hospital_admission(patient["Q17"].values[0])
    oral_health(patient["Q18"].values[0], patient["Q19"].values[0])
    sleep(patient["Q21"].values[0])
    cardiovascular(patient["Q22"].values[0])
    blood_sugar(patient["Q23"].values[0])
    pulmonary(patient["Q24"].values[0])
    gastrointestinal(patient["Q25"].values[0])
    renal(patient["Q26"].values[0])
    integumentary(patient["Q27"].values[0])
    pain(patient["Q28"].values[0], patient["Q28(c)"].values[0], patient["Q28(d)"].values[0])
    sensory_ability(patient["Q1"].values[0], patient["Q1(a)"].values[0], patient["Q29"].values[0]) ##NAN value for p2
    assistance(patient["Q31"].values[0], patient["Q31(a)"].values[0], patient["Q31(b)"].values[0], patient["Q32"].values[0], patient["Q33"].values[0], patient["Q33(b)"].values[0],
              patient["Q33(c)"].values[0])
    ambulation_status(patient["Q34"].values[0], patient["Q31"].values[0], patient["Q35"].values[0], patient["Q36"].values[0])
    physical_activity(patient["Q37"].values[0], patient["Q31"].values[0])
    tobacco_alcohol_use(patient["Q46"].values[0], patient["Q46(a)"].values[0], patient["Q46(b)"].values[0], patient["Q46(c)"].values[0],
                        patient["Q46(d)"].values[0])
    mental_health(patient["Q48"].values[0], patient["Q49"].values[0], patient["Q50"].values[0], patient["Q51"].values[0], patient["Q52"].values[0])
    mental_health_phq(patient["Q53"].values[0], patient["Q54"].values[0], patient["Q55"].values[0], patient["Q56"].values[0], 
                      patient["Q57"].values[0], patient["Q58"].values[0], patient["Q59"].values[0], patient["Q60"].values[0],
                      patient["Q61"].values[0])
    employment(patient["Q62"].values[0])
    child_care(patient["Q63"].values[0])
    education(patient["Q64"].values[0])
    financial(patient["Q65"].values[0], patient["Q66"].values[0], patient["Q67"].values[0], patient["Q68"].values[0], patient["Q69"].values[0])
    support(patient["Q70"].values[0])
    home_safety(patient["Q71"].values[0])


    output_data = pd.DataFrame(data, columns=["Category", "Barriers", "Problems", "CM Intervention", "Patient Intervention"])
    output_data.to_csv("output_data_{}.csv".format(patient_num))

for patient_num in patient_df["patient ID"]:
    data = []
    decision_rules(patient_df, patient_num, data)