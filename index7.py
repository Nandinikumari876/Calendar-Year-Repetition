import calendar
def get_year():
     return int(input(" enter year :"))
def A(year):
   
    rem=year%100
   

    return rem
def A1(rem):
    x=rem%4
    return x

    
def B(y):
    if y==1:
        c=6
        return c
       
    elif y==2:
        c==11
        return c
        
    elif y==3:
       c=11
       return c
    elif y==0:
        c=11
        return c
    else:

       return "wrong"
def cal(c,year):
   next_year=c+year
   print("Calendar of the year u entered : ",calendar.calendar(year),"\nCalendar of the next same calendar year : ",calendar.calendar(next_year))


year=get_year()
rem=A(year)
y=A1(rem)
c=B(y)
cal(c,year)
