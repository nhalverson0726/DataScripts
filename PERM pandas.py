import pandas as pd
import numpy as np
import os

os.chdir(r'C:\Users\njh42\Downloads')

# download perm data from 2020 to 20q5 from:
# https://www.dol.gov/agencies/eta/foreign-labor/performance

## Read PERM excel files from years 2020 - 2015
print('..n')
df1 = pd.read_excel('PERM_Disclosure_Data_FY2019.xlsx', 0, nrows = 102655)
print('...\n')
df2 = pd.read_excel('PERM_Disclosure_Data_FY2020.xlsx', 0, nrows = 9419)
print('...\n')
df3 = pd.read_excel('PERM_Disclosure_Data_FY2018_EOY.xlsx', 0, nrows = 119776)
print('...\n')
df4 = pd.read_excel('PERM_Disclosure_Data_FY17.xlsx', 0, nrows = 97603)
print('...\n')
df5 = pd.read_excel('PERM_Disclosure_Data_FY16.xlsx', 0, nrows = 126143)
print('...\n')
df6 = pd.read_excel('PERM_Disclosure_Data_FY15_Q4.xlsx', 0, nrows = 89299)
print('read complete')

# combine data frames into a master dataframe

df = pd.concat([df1, df2, df3, df4, df5, df6])
print('done.')

#remove all data that is not of interest

interestingcolumns =
    [
    'CASE_NUMBER',
    'DECISION_DATE',
    'EMPLOYER_NAME',
    'EMPLOYER_NUM_EMPLOYEES',
    'EMPLOYER_YR_ESTAB',
    'FW_OWNERSHIP_INTEREST',
    'PW_TRACK_NUM',
    'PW_SOC_CODE',
    'PW_SOC_TITLE',
    'PW_LEVEL_9089',
    'PW_AMOUNT_9089',
    'PW_UNIT_OF_PAY_9089',
    'PW_SOURCE_NAME_9089',
    'PW_SOURCE_NAME_OTHER_9089',
    'PW_DETERM_DATE',
    'PW_EXPIRE_DATE',
    'WAGE_OFFERED_FROM_9089',
    'WAGE_OFFERED_TO_9089',
    'WAGE_OFFER_UNIT_OF_PAY_9089',
    'JOB_INFO_WORK_CITY',
    'JOB_INFO_WORK_STATE',
    'JOB_INFO_WORK_POSTAL_CODE',
    'JOB_INFO_JOB_TITLE',
    'JOB_INFO_EDUCATION',
    'JOB_INFO_EDUCATION_OTHER',
    'JOB_INFO_MAJOR',
    'JOB_INFO_TRAINING',
    'JOB_INFO_TRAINING_NUM_MONTHS',
    'JOB_INFO_TRAINING_FIELD',
    'JOB_INFO_EXPERIENCE',
    'JOB_INFO_EXPERIENCE_NUM_MONTHS',
    'JOB_INFO_ALT_FIELD',
    'JOB_INFO_ALT_FIELD_NAME',
    'JOB_INFO_ALT_COMBO_ED_EXP',
    'JOB_INFO_ALT_COMBO_ED_EXP.1',
    'JOB_INFO_ALT_COMBO_ED_OTHER',
    'JOB_INFO_ALT_CMB_ED_OTH_YRS',
    'JOB_INFO_FOREIGN_ED',
    'JOB_INFO_ALT_OCC',
    'JOB_INFO_ALT_OCC_NUM_MONTHS',
    'JOB_INFO_ALT_OCC_JOB_TITLE',
    'JOB_INFO_JOB_REQ_NORMAL',
    'JOB_INFO_FOREIGN_LANG_REQ',
    'JOB_INFO_COMBO_OCCUPATION',
    'FOREIGN_WORKER_INFO_CITY',
    'FOREIGN_WORKER_INFO_STATE',
    'FW_INFO_POSTAL_CODE',
    'COUNTRY_OF_CITIZENSHIP',
    'FW_INFO_BIRTH_COUNTRY',
    'CLASS_OF_ADMISSION',
    'FOREIGN_WORKER_INFO_EDUCATION',
    'FW_INFO_EDUCATION_OTHER',
    'FOREIGN_WORKER_INFO_MAJOR',
    'FW_INFO_YR_REL_EDU_COMPLETED',
    'FOREIGN_WORKER_INFO_INST',
    'FW_INFO_TRAINING_COMP',
    'FW_INFO_REQ_EXPERIENCE',
    'FW_INFO_ALT_EDU_EXPERIENCE',
    'FW_INFO_REL_OCCUP_EXP',
    'JOB_INFO_WORK_CITY',
    'JOB_INFO_WORK_STATE',
    'JOB_INFO_JOB_TITLE',
    'JOB_INFO_EDUCATION',
    'JOB_INFO_EDUCATION_OTHER',
    'JOB_INFO_EXPERIENCE',
    'JOB_INFO_EXPERIENCE_NUM_MONTHS',
    'CLASS_OF_ADMISSION',
    'FOREIGN_WORKER_INFO_EDUCATION',
    'FW_INFO_EDUCATION_OTHER',
    'FOREIGN_WORKER_INFO_MAJOR',
    'FW_INFO_YR_REL_EDU_COMPLETED',
    'FOREIGN_WORKER_INFO_INST'
    ]


interestingdf = df[interestingcolumns]

# combine columns that are named differently but contain similar data

first = 
    ['EMPLOYER_YR_ESTAB',
     'PW_TRACK_NUM',
     'PW_AMOUNT_9089',
     'PW_UNIT_OF_PAY_9089',
     'PW_SOURCE_NAME_9089',
     'PW_SOURCE_NAME_OTHER_9089',
     'PW_DETERM_DATE',
     'WAGE_OFFERED_FROM_9089',
     'WAGE_OFFERED_TO_9089',
     'WAGE_OFFER_UNIT_OF_PAY_9089',
     'JOB_INFO_WORK_CITY',
     'JOB_INFO_WORK_STATE',
     'JOB_INFO_WORK_POSTAL_CODE',
     'JOB_INFO_JOB_TITLE',
     'JOB_INFO_EDUCATION',
     'JOB_INFO_EDUCATION_OTHER',
     'JOB_INFO_MAJOR',
     'JOB_INFO_TRAINING',
     'JOB_INFO_TRAINING_NUM_MONTHS',
     'JOB_INFO_TRAINING_FIELD',
     'JOB_INFO_EXPERIENCE',
     'JOB_INFO_EXPERIENCE_NUM_MONTHS',
     'JOB_INFO_ALT_FIELD',
     'JOB_INFO_ALT_FIELD_NAME',
     'JOB_INFO_ALT_COMBO_ED_EXP',
     'JOB_INFO_ALT_COMBO_ED_EXP.1',
     'JOB_INFO_ALT_COMBO_ED_OTHER',
     'JOB_INFO_ALT_CMB_ED_OTH_YRS',
     'JOB_INFO_FOREIGN_ED',
     'JOB_INFO_ALT_OCC',
     'JOB_INFO_ALT_OCC_NUM_MONTHS',
     'JOB_INFO_ALT_OCC_JOB_TITLE',
     'JOB_INFO_JOB_REQ_NORMAL',
     'JOB_INFO_FOREIGN_LANG_REQ',
     'FW_INFO_BIRTH_COUNTRY',
     'FOREIGN_WORKER_INFO_EDUCATION',
     'FW_INFO_EDUCATION_OTHER',
     'FW_INFO_YR_REL_EDU_COMPLETED',
     'FOREIGN_WORKER_INFO_INST',
     'FW_INFO_TRAINING_COMP',
     'FW_INFO_REQ_EXPERIENCE',
     'FW_INFO_ALT_EDU_EXPERIENCE']

second =

    ['EMPLOYER_YEAR_COMMENCED_BUSINESS',
     'PW_TRACK_NUMBER',
     'PW_WAGE',
     'PW_UNIT_OF_PAY',  
     'PW_WAGE_SOURCE',
     'PW_SOURCE_NAME_OTHER',
     'PW_DETERMINATION_DATE',
     'WAGE_OFFER_FROM',
     'WAGE_OFFER_TO',
     'WAGE_OFFER_UNIT_OF_PAY',
     'WORKSITE_CITY',
     'WORKSITE_STATE',
     'WORKSITE_POSTAL_CODE',
     'JOB_TITLE',
     'MINIMUM_EDUCATION',
     'JOB_EDUCATION_MIN_OTHER',
     'MAJOR_FIELD_OF_STUDY',
     'REQUIRED_TRAINING',
     'REQUIRED_TRAINING_MONTHS',
     'REQUIRED_FIELD_OF_TRAINING',
     'REQUIRED_EXPERIENCE',
     'REQUIRED_EXPERIENCE_MONTHS',
     'ACCEPT_ALT_FIELD_OF_STUDY',
     'ACCEPT_ALT_MAJOR_FLD_OF_STUDY',
     'ACCEPT_ALT_COMBO',
     'ACCEPT_ALT_COMBO_EDUCATION',
     'ACCEPT_ALT_COMBO_ED_OTHER',
     'ACCEPT_ALT_COMBO_EDUCATION_YRS',
     'ACCEPT_FOREIGN_EDUCATION',
     'ACCEPT_ALT_OCCUPATION',
     'ACCEPT_ALT_OCCUPATION_MONTHS',
     'ACCEPT_ALT_JOB_TITLE',
     'JOB_OPP_REQUIREMENTS_NORMAL',
     'FOREIGN_LANGUAGE_REQUIRED',
     'FOREIGN_WORKER_BIRTH_COUNTRY',
     'FOREIGN_WORKER_EDUCATION',
     'FOREIGN_WORKER_EDUCATION_OTHER',
     'FOREIGN_WORKER_YRS_ED_COMP',
     'FOREIGN_WORKER_INST_OF_ED',
     'FOREIGN_WORKER_TRAINING_COMP',
     'FOREIGN_WORKER_REQ_EXPERIENCE',
     'FOREIGN_WORKER_ALT_ED_EXP']
    
firstdf = interestingdf[first]

seconddf = interestingdf[second]

interestingdf = firstdf.combine_first(seconddf)

# Remove $ , from salaries and convert to float

interestingdf['WAGE_OFFERED_FROM_9089'] =\
    interestingdf['WAGE_OFFERED_FROM_9089'].str.replace(',', '')
interestingdf['WAGE_OFFERED_FROM_9089'] = \
    interestingdf['WAGE_OFFERED_FROM_9089'].str.replace('$', '')
interestingdf['WAGE_OFFERED_FROM_9089'] = \
    interestingdf['WAGE_OFFERED_FROM_9089].astype(float)


# find unique majors

uniquemajors = pd.unique(interestingdf['FOREIGN_WORKER_INFO_MAJOR'])

uniquemajors = [str(x) for x in list(uniquemajors)]



# find bioinformatics or computational biology majors

bioinfomajorslist =  \
    [x for x in unique majors \
     if ('BIOINFORMAITCS' or 'COMPUTATIONAL BIOLOGY') in x]

# Query bioinfomratics phd recipients

bioinfophddf = interestingdf.query(
    'FOREIGN_WORKER_INFO_MAJOR in @bioinfomajorslist\
    & FOREIGN_WORKER_INFO_EDUCATION == "Doctorate"'
    )

# Convert useful info in df into csv file           

useful = ['EMPLOYER_NAME',
          'JOB_INFO_WORK_CITY',
'JOB_INFO_WORK_STATE',
'EMPLOYER_NUM_EMPLOYEES',
'EMPLOYER_YR_ESTAB',
'FW_OWNERSHIP_INTEREST',
'PW_SOC_CODE',
'JOB_INFO_JOB_TITLE',
'WAGE_OFFERED_FROM_9089',
'WAGE_OFFERED_TO_9089',
'WAGE_OFFER_UNIT_OF_PAY_9089',
'FOREIGN_WORKER_INFO_EDUCATION',
'FW_INFO_EDUCATION_OTHER',
'FOREIGN_WORKER_INFO_MAJOR',
'FW_INFO_YR_REL_EDU_COMPLETED',
'FOREIGN_WORKER_INFO_INST',
'JOB_INFO_EDUCATION',
'JOB_INFO_EDUCATION_OTHER',
'JOB_INFO_MAJOR',
'JOB_INFO_EXPERIENCE'
    ]

bioinfophddf[useful].to_csv('Bioinfo_phd.csv')



