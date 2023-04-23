def day_finder(inp):
    inp=inp.lower()
    if('-' in inp):
        day=inp.split('-')[0]
        month=inp.split('-')[1]
        year=inp.split('-')[2]
    elif('-' not in inp):
        day=inp.split(' ')[0]
        month=inp.split(' ')[1]
        year=inp.split(' ')[2]
    def leap_year(year):
        if(year%100==0 and year%400==0):
            return True
        elif(year%100==0 and year%400!=0):
            return False
        elif(year%4==0):
            return True
        else:
            return False
    def get_key(val):
        for key, value in d_week.items():
            if val == value:
                return key
    def cent_get_code(cent):
        t_centuries=(6,4,2,0)
        r=cent%400
        if(r==0):
            return t_centuries[0]
        elif(r==100):
            return t_centuries[1]
        elif(r==200):
            return t_centuries[2]
        elif(r==300):
            return t_centuries[3]
    d_month={"january":1,"february":4,"march":4,"april":0,"may":2,"june":5,"july":0,"august":3,"september":6,"october":1,"november":4,"december":6}
    d_week={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thrusday':4,'Friday':5,'Saturday':6}
    d_month_s={'01':1,"02":4,"03":4,"04":0,"05":2,"06":5,"07":0,"08":3,"09":6,"10":1,"11":4,"12":6}
    if((month[0]) in '0123456789'):
        cent=(int(year)//400)*400
        cent_p=int(year)%400
        if((leap_year(int(year)) is True) and (month=='01' or month=='02')):
            find=((int(day)+int(d_month_s[month])+cent_get_code(cent)+cent_p+(cent_p//4)-1)%7)-1
        else:
            find=((int(day)+int(d_month_s[month])+cent_get_code(cent)+cent_p+(cent_p//4))%7)-1

    elif(month[0].isalpha()):
        cent=(int(year)//400)*400
        cent_p=int(year)%400
        if((leap_year(int(year)) is True) and (month=='january' or month=='february')):
            find=((int(day)+int(d_month[month])+cent_get_code(cent)+cent_p+(cent_p//4)-1)%7)-1
        else:
            find=((int(day)+int(d_month[month])+cent_get_code(cent)+cent_p+(cent_p//4))%7)-1
    if(find<0 and find!=-7):
        find=7+find
    return get_key(find)
    
print(day_finder(input("[*] ENTER A DATE (in DD-MM-YYYY / DD MONTH YYYYY) : ")))