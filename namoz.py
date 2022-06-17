import requests

TOKEN = '5093321564:AAGMR4PgwxHuLsu1EwUgIIlwETm1iKD-lac'


def namoz(btn_data):
    url = f'https://api.pray.zone/v2/times/this_week.json?city={btn_data}&school=1'
    res = requests.get(url)
    rest = []
    r = res.json()
    # print(r)
    r_time = r['results']['datetime']
    for i in range(7):
        x_rest = []

        x_rest.append(malTong(r_time[i]['times']['Imsak']))
        x_rest.append(malBom(r_time[i]['times']['Fajr']))
        x_rest.append(malQuy(r_time[i]['times']['Sunrise']))
        x_rest.append(malPes(r_time[i]['times']['Dhuhr']))
        x_rest.append(malAsr(r_time[i]['times']['Asr']))
        x_rest.append(malSho(r_time[i]['times']['Maghrib']))
        x_rest.append(malHuf(r_time[i]['times']['Isha']))
        x_rest.append(r['results']['datetime'][i]['date']['gregorian'])
        x_rest.append(r['results']['datetime'][i]['date']['hijri'])
        rest.append(x_rest)
    return rest


def malBom(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) + 54
    if y1_mal / 60 < 1:
        mal1 = x_mal + ':' + str(y1_mal)
    elif y1_mal / 60 == 1:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 60 < y1_mal < 70:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    else:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + str(y1_mal % 60)
    return mal1


def malAsr(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) + 37
    if y1_mal % 60 < 1:
        mal1 = x_mal + ':' + str(y1_mal)
    elif y1_mal / 60 == 1:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 60 < y1_mal < 70:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    else:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + str(y1_mal % 60)
    return mal1


def malQuy(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) + 5
    if y1_mal / 60 < 1:
        mal1 = x_mal + ':' + str(y1_mal)
    elif y1_mal / 60 == 1:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 60 <= y1_mal < 70:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    else:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + str(y1_mal % 60)
    return mal1


def malTong(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) + 26
    if y1_mal % 60 < 1:
        mal1 = x_mal + ':' + str(y1_mal)
    elif y1_mal / 60 == 1:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 60 < y1_mal < 70:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    else:
        x1_mal = int(x_mal) + 1
        mal1 = '0' + str(x1_mal) + ':' + str(y1_mal % 60)
    return mal1


def malPes(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) + 4
    if 0.1 <= y1_mal / 60 < 1:
        mal1 = x_mal + ':' + str(y1_mal)
    elif y1_mal / 60 == 1:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 0 <= y1_mal / 60 < 0.1:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    elif 60 < y1_mal < 70:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + '0' + str(y1_mal % 60)
    else:
        x1_mal = int(x_mal) + 1
        mal1 = str(x1_mal) + ':' + str(y1_mal % 60)
    return mal1


def malSho(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) - 3
    if y1_mal < 0:
        x1_mal = int(x_mal) - 1
        y1_mal = y1_mal + 60
        mal1 = str(x1_mal) + ':' + str(y1_mal)
    elif y1_mal == 0:
        mal1 = x_mal + ':' + '0' + str(y1_mal)
    elif 0 < y1_mal < 10:
        mal1 = x_mal + ':' + '0' + str(y1_mal)
    else:
        mal1 = x_mal + ':' + str(y1_mal)
    return mal1


def malHuf(mal):
    x_mal = mal[:2]
    y_mal = mal[3:]
    y1_mal = int(y_mal) - 12
    if y1_mal < 0:
        x1_mal = int(x_mal) - 1
        y1_mal = y1_mal + 60
        mal1 = str(x1_mal) + ':' + str(y1_mal)
    elif y1_mal == 0:
        mal1 = x_mal + ':' + '0' + str(y1_mal)
    elif 0 < y1_mal < 10:
        mal1 = x_mal + ':' + '0' + str(y1_mal)
    else:
        mal1 = x_mal + ':' + str(y1_mal)
    return mal1


def malNam(btn_data, vaq, btn_day):
    rest1 = namoz(btn_data)
    day = 0
    for i in range(7):
        if rest1[i][7] == btn_day:
            day = i
    x_Ton = rest1[day][0]
    x_Bom = rest1[day][1]
    x_Quy = rest1[day][2]
    x_Pes = rest1[day][3]
    x_Asr = rest1[day][4]
    x_Sho = rest1[day][5]
    x_Huf = rest1[day][6]
    x1_Ton = x_Ton[:2] + x_Ton[3:]
    x1_Bom = x_Bom[:2] + x_Bom[3:]
    x1_Pes = x_Pes[:2] + x_Pes[3:]
    x1_Asr = x_Asr[:2] + x_Asr[3:]
    x1_Quy = x_Quy[:2] + x_Quy[3:]
    x1_Sho = x_Sho[:2] + x_Sho[3:]
    x1_Huf = x_Huf[:2] + x_Huf[3:]
    x_vaq = vaq[:2] + vaq[3:]
    if x1_Bom <= x_vaq < x1_Quy:
        ret = 'Hozir Bomdod vaqti!'
    elif x1_Quy <= x_vaq < x1_Pes:
        x1 = int(x_vaq) % 100
        y1 = int(x_vaq) // 100
        x2 = int(x1_Pes) % 100
        y2 = int(x1_Pes) // 100
        if x2 - x1 < 0:
            ret = '0' + str(y2 - y1 - 1) + ':' + str(x2 - x1 + 60)
        elif x2 - x1 == 0:
            ret = str(y2 - y1) + ':00'
        elif 0 < x2 - x1 < 10 and 0 == y2 - y1:
            ret = '00' + ':0' + str(x2 - x1)
        elif 0 < x2 - x1 < 10:
            ret = '0' + str(y2 - y1) + ':0' + str(x2 - x1)
        elif x2 - x1 > 10 and y2 - y1 == 0:
            ret = '00' + ':' + str(x2 - x1)
        elif x2 - x1 > 10:
            ret = '0' + str(y2 - y1) + ':' + str(x2 - x1)
        ret = 'Peshingacha ' + ret + ' qoldi!'
    elif x1_Pes <= x_vaq < x1_Asr:
        ret = 'Hozir Peshin vaqti!'
    elif x1_Asr <= x_vaq < x1_Sho:
        ret = 'Hozir Asr vaqti!'
    elif x1_Sho <= x_vaq < x_Huf:
        ret = 'Hozir Shom vaqti!'
    elif x1_Huf <= x_vaq or x_vaq < x1_Ton:
        ret = "Hozir Hufton vaqti!"
    elif x1_Ton <= x_vaq < x1_Bom:
        x1 = int(x1_Ton) % 100
        y1 = int(x1_Ton) // 100
        x2 = int(x1_Bom) % 100
        y2 = int(x1_Bom) // 100
        if x2 - x1 < 0:
            ret = '0' + str(y2 - y1 - 1) + ':' + str(x2 - x1 + 60)
        elif x2 - x1 == 0:
            ret = str(y2 - y1) + ':00'
        elif 0 < x2 - x1 < 10 and 0 == y2 - y1:
            ret = '00' + ':0' + str(x2 - x1)
        elif 0 < x2 - x1 < 10:
            ret = '0' + str(y2 - y1) + ':0' + str(x2 - x1)
        elif x2 - x1 > 10 and y2 - y1 == 0:
            ret = '00' + ':' + str(x2 - x1)
        elif x2 - x1 > 10:
            ret = '0' + str(y2 - y1) + ':' + str(x2 - x1)
        ret = 'Bomdodgacha ' + ret + ' qoldi!'
    return ret
