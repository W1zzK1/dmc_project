import pandas as pd
import yargy_services as ys
import model as md
from datetime import datetime
start_time = datetime.now()

data = pd.read_excel('try.xlsx', header=None)

def findOrgName(text):
    result = md.classifier(text)  # Обработка названия
    orgName = md.findTegOrg(result)
    if len(orgName) == 0:
        return "Название найти не удалось"
    else:
        return orgName

def findAddress(text):
    address = md.findAddr(text)
    if len(address) == 0:
        return "Адрес не был найден"
    else:
        return address

def findEmail(text):
    email = md.findEmail(text)
    if len(email) == 0:
        return "Почат не указана"
    else:
        return email

def findNumber(text):
    number = md.findNumber(text)  # Обработка номера
    if len(number) == 0:
        return "Номер телефона не указан"
    else:
        return number

def findDopInfo(text):
    dopInfo = md.findDopInfo(result)  # обработка дополнительной информации
    if len(dopInfo) == 0:
        return "Нет дополнительной информации"
    else:
        return dopInfo

def findServices(text):
    services = ys.findServices(text)  # Обработка услуг лпу
    if len(services) == 0:
        return "Услуги не указаны"
    else:
        return services


result = pd.DataFrame()
result['raw_data'] = data[0]

try:
    result['LPU'] = result['raw_data'].apply(findOrgName)
    result['address'] = result['raw_data'].apply(findAddress)
    result['email'] = result['raw_data'].apply(findEmail)
    result['number'] = result['raw_data'].apply(findNumber)
    #result['dopInfo'] = result['raw_data'].apply(findDopInfo)
    result['services'] = result['raw_data'].apply(findServices)
except Exception:
    # result['LPU'] = result['raw_data'].apply(findOrgName)
    # result['address'] = result['raw_data'].apply(findAddress)
    # result['email'] = result['raw_data'].apply(findEmail)
    # result['number'] = result['raw_data'].apply(findNumber)
    # # result['dopInfo'] = result['raw_data'].apply(findDopInfo)
    # result['services'] = result['raw_data'].apply(findServices)
    result["Error"] = result['raw_data']

result.to_csv('result.csv', encoding='utf-8')
print(datetime.now() - start_time)