import json

syn_sent1=glob.glob('../CVPR_2023_backup/syn_sent1/ch3/*')
with open('dataset.json', "r") as json_file:
    syn_sent2=json.load(json_file)
syn_sent2_data=dict()
for file, _ in syn_sent2.items():

    file=file.split('!')[0].split('/')[-1].replace('.jpg','')
    loc=file.split('_')[2]+'_'+file.split('_')[3]
    year=int(file.split('_')[4])
    month=int(file.split('_')[5])
    key= loc+'_'+str(year)+'_'+str(month)
    if not syn_sent2_data.get(key):
        syn_sent2_data[key]=[]
    syn_sent2_data[key].append(file)
print('syn_sent2_data keys:',len(syn_sent2_data.keys()))

print('syn_sent1 whole_data:',len(syn_sent1))
syn_sent1=[file.split('/')[-1] for file in syn_sent1]
syn_sent1_data=dict()
for file in syn_sent1:
    loc=file.split('_')[2]+'_'+file.split('_')[3]
    year=int(file.split('_')[4])
    month=int(file.split('_')[5])
        
    key= loc+'_'+str(year)+'_'+str(month)
    if not syn_sent1_data.get(key):
        syn_sent1_data[key]=[]
    syn_sent1_data[key].append(file)

print('syn_sent1_data keys:',len(syn_sent1_data.keys()))

import itertools
import datetime

matched_dataset=dict()

for key, EO_list in syn_sent2_data.items():
    lon, lat, year, month=key.split('_')[:]
    year, month= int(year), int(month)
    if month==1:
        key_before=lon+'_'+lat+'_'+str(year-1)+'_'+str(12)
        key_after=lon+'_'+lat+'_'+str(year)+'_'+str(month+1)
    elif month==12:
        key_before=lon+'_'+lat+'_'+str(year)+'_'+str(month-1)
        key_after=lon+'_'+lat+'_'+str(year+1)+'_'+str(1)
    else:
        key_before=lon+'_'+lat+'_'+str(year)+'_'+str(month-1)
        key_after=lon+'_'+lat+'_'+str(year)+'_'+str(month+1)

    for EO in EO_list:
        ##if syn_sent1_data에 그 키가 없으면() continue? 
        sar_check_list=[]
        if syn_sent1_data.get(key_before):
            sar_check_list+=syn_sent1_data[key_before]
        if syn_sent1_data.get(key):
            sar_check_list+=syn_sent1_data[key]
        if syn_sent1_data.get(key_after):
            sar_check_list+=syn_sent1_data[key_after]
        if len(sar_check_list)==0: #when SAR don't have this date
            continue

        min=7
        diff=30
        saved_sar=None
        for SAR in sar_check_list:
            _, _, eo_lon, eo_lat, eo_year, eo_month, eo_day=EO.replace('.jpg', '').split('_')[:]
            _, _, sar_lon, sar_lat, sar_year, sar_month, sar_day=SAR.replace('.jpg', '').split('/')[-1].split('_')[:]
            eo_year, eo_month, eo_day= int(eo_year), int(eo_month), int(eo_day)
            sar_year, sar_month, sar_day = int(sar_year), int(sar_month), int(sar_day)
            eo_date=datetime.datetime(eo_year, eo_month, eo_day)
            sar_date=datetime.datetime(sar_year, sar_month, sar_day)

            diff=int(abs(eo_date-sar_date).days)
            if diff<min:
                min=diff
                saved_sar=SAR
            continue
        else:
            matched_dataset[saved_sar]=EO
print('matched_datset keys length:',len(matched_dataset.keys()))
print('matched_datset values length:',len(matched_dataset.values()))
print('matched_datset unique keys length:',len(list(set(matched_dataset.keys()))))
print('matched_datset unique values length:',len(list(set(matched_dataset.values()))))

import json
with open("step3_aligned.json", "w") as json_file:
    json.dump(matched_dataset, json_file, indent=4)

import json
with open('step3_aligned.json', 'r') as f:
    json_data = json.load(f)
for key,values in json_data.items():
    print(key,'' ,values)


print(len(list(set(list(json_data.keys())))))
print(len(list(set(list(json_data.values())))))


