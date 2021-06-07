"""
Code written for plotting purpose of
2020/2021 ed of Astropi challenge, team Eposat.
Code was edited to two trajectories, from two available data sets
jesto_data01.csv (19/20 ed) and data01.csv (20/21 ed)

"""
from csv import reader
from matplotlib import pyplot #as plt
from dateutil import parser
col_counter=0

#data01.csv and jesto_data01.csv must be saved in the same directory of this code

# First create data lists:
with open('data01.csv', 'r') as f:
    dat = list(reader(f))
with open('jesto_data01.csv', 'r') as g:
    dat1 = list(reader(g))



#Now print info and enter data sets reference:
print(type(dat))
print(len(dat))
print(type(dat[0]))
print(len(dat[0]))



for el in dat[0]:
    print(str(col_counter) + '   ' + el)
    col_counter +=1

a=int(input('Please enter latitude line number'))
b=int(input('Please enter longitude line number'))

print(type(dat1))
print(len(dat1))
print(type(dat1[0]))
print(len(dat1[0]))

# Now reset col_counter value:
col_counter=0



for el in dat1[0]:
    print(str(col_counter) + '   ' + el)
    col_counter +=1

c=int(input('Please enter latitude line number'))
d=int(input('Please enter longitude line number'))


#Now, get lat, long values from dat lists
#next two lines get latitude value series: 
lat = [float(i[a]) for i in dat[1::]]
lat1 = [float(i[c]) for i in dat1[1::]]
#next two lines get longitude value series:
long = [float(i[b]) for i in dat[1::]]
long1 = [float(i[d]) for i in dat1[1::]]

# now some silly stuff to print headers:
headers=dat[0]


pyplot.title('Traiettoria da '+ str(round(lat[0],2)) + ' , '+str(round(long[0],2)) + ' a ' + str(round(lat[-1],2)) + ' , ' +str(round(long[-1],2)))
pyplot.ylabel(headers[a])
pyplot.xlabel(headers[b])


# Finally plot the two trajectories:
"""
Use one of the two following
"""
pyplot.plot(long, lat,'.', markersize=1)
#pyplot.plot(time, temp, linewidth=1)

"""
Use one of the two following
"""
pyplot.plot(long1, lat1,'.', markersize=1)
#pyplot.plot(time, temp, linewidth=1)


pyplot.show()
#plt.scatter(time,temp, s=1, marker='.')
#plt.show()
