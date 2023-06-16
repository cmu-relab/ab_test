import os, json

files = os.listdir('surveydata')
for f in files:
    data = json.load(open('surveydata/' + f, 'r'))
    print(data['survey_code'])
    
