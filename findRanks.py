import xlrd
import xlwt
from operator import itemgetter


wb = xlrd.open_workbook("everyone.xls")
wb
sheet =wb.sheet_by_index(0)
ev = {}
inc = []
rend = 3000 #change 3
for r in range(1,rend):
    l = []
    l.append(sheet.cell(r,0).value.strip().encode('ascii','ignore'))
    l.append(sheet.cell(r,1).value.strip().encode('ascii','ignore'))
    l.append(sheet.cell(r,2).value.strip().encode('ascii','ignore'))
    l.append(sheet.cell(r,3).value.strip().encode('ascii','ignore'))
    ev[l[1]] = l
    #print l
   
f = open("usernames.txt")
users = f.read().split("\r")
final = []
for user in users:
    try:
        final.append([ev[user][1],int(ev[user][0])])
    except KeyError:
        inc.append(user)

sfinal = sorted(final,key=itemgetter(1))

rank = 1
for u in sfinal:
    print rank,u[0],u[1]
    rank = rank+1

print len(sfinal)
print inc
