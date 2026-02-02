def A():
    year=eval(input(" enter year :"))
    rem=year%100
    y=rem%4

    return year,y
    
def B(year,y):
    if y==1:
        return(" calender of this year repeat after 6 years that is",year+6)
    elif y==2:
        return(" calender repeat after 11years that is",year+11)
    elif y==3:
       return(" calender repeat after 11 years that is",year+11)
    elif y==0:
       return(" calender repeat after 11 years that is",year+28)
    else:
       return(" wrong")

year,y=A()
# print(year,y)
b=B(year,y)
print(b)




