import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

result1 = pd.read_table('/home/jeet/Desktop/1860_1993_2050_NITROGEN_830/data-from-NASA/NOy-deposition1860.txt', sep='\s+')

print('--------------------------------------------\n')
print('Column names as follows :\n')
print('------------------------\n')
count = 0
for col in result1.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

result11 = result1['NOy-deposition']
result12 = result1['mg']
result13 = result1['N/m2/year']
result14 = result1['im']
result15 = result1['=']
result16 = result1['72']
result17 = result1['jm']
result18 = result1['=.1']
result19 = result1['48']
result110 = result1['year1860']

max1=max(max(result11),max(result12),max(result13),max(result14),max(result15),
        max(result16),max(result17),max(result18),max(result19),max(result110))
        
min1=min(min(result11),min(result12),min(result13),min(result14),min(result15),
        min(result16),min(result17),min(result18),min(result19),min(result110))        


plt.title('-------[ NOy-deposition - 1860 ]--------')
plt.xlabel('fequency of values -->')
plt.ylabel('data range -->')

plt.scatter(result11,np.arange(346),label="Max value for total data = 210.88")
plt.scatter(result12,np.arange(346),label="Min value for total data = 0.040000")
plt.scatter(result13,np.arange(346))
plt.scatter(result14,np.arange(346))
plt.scatter(result15,np.arange(346))
plt.scatter(result16,np.arange(346))
plt.scatter(result17,np.arange(346))
plt.scatter(result18,np.arange(346))
plt.scatter(result19,np.arange(346))
plt.scatter(result110,np.arange(346))

plt.legend()
plt.show

# data set for ------ NHx-deposition1993.txt ------------------

result2 = pd.read_table('/home/jeet/Desktop/1860_1993_2050_NITROGEN_830/data-from-NASA/NOy-deposition1993.txt', sep='\s+')

result21 = result2['NOy-deposition']
result22 = result2['mg']
result23 = result2['N/m2/year']
result24 = result2['im']
result25 = result2['=']
result26 = result2['72']
result27 = result2['jm']
result28 = result2['=.1']
result29 = result2['48']
result210 = result2['year1993']

max2=max(max(result21),max(result22),max(result23),max(result24),max(result25),
        max(result26),max(result27),max(result28),max(result29),max(result210))
        
min2=min(min(result21),min(result22),min(result23),min(result24),min(result25),
        min(result26),min(result27),min(result28),min(result29),min(result210))

plt.title('-------[ NOy-deposition - 1993 ]--------')
plt.xlabel('fequency of values -->')
plt.ylabel('data range -->')

plt.scatter(result21,np.arange(346),label="Max value for total data = 1756.53")
plt.scatter(result22,np.arange(346),label="Min value for total data = 0.0899999")
plt.scatter(result23,np.arange(346))
plt.scatter(result24,np.arange(346))
plt.scatter(result25,np.arange(346))
plt.scatter(result26,np.arange(346))
plt.scatter(result27,np.arange(346))
plt.scatter(result28,np.arange(346))
plt.scatter(result29,np.arange(346))
plt.scatter(result210,np.arange(346))

plt.legend()
plt.show

#----------- data analysis for NHx-deposition2050.txt ---------------

result3 = pd.read_table('/home/jeet/Desktop/1860_1993_2050_NITROGEN_830/data-from-NASA/NOy-deposition2050.txt', sep='\s+')

result31 = result3['NOy-deposition']
result32 = result3['mg']
result33 = result3['N/m2/year']
result34 = result3['im']
result35 = result3['=']
result36 = result3['72']
result37 = result3['jm']
result38 = result3['=.1']
result39 = result3['48']
result310 = result3['year2050']

max3=max(max(result31),max(result32),max(result33),max(result34),max(result35),
        max(result36),max(result37),max(result38),max(result39),max(result310))
        
min3=min(min(result31),min(result32),min(result33),min(result34),min(result35),
        min(result36),min(result37),min(result38),min(result39),min(result310))

plt.title('-------[ NOy-deposition - 2050 ]--------')
plt.xlabel('fequency of values -->')
plt.ylabel('data range -->')

plt.scatter(result31,np.arange(346),label="Max value for total data = 2218.51000")
plt.scatter(result32,np.arange(346),label="Min value for total data = 0.16")
plt.scatter(result33,np.arange(346))
plt.scatter(result34,np.arange(346))
plt.scatter(result35,np.arange(346))
plt.scatter(result36,np.arange(346))
plt.scatter(result37,np.arange(346))
plt.scatter(result38,np.arange(346))
plt.scatter(result39,np.arange(346))
plt.scatter(result310,np.arange(346))

plt.legend()
plt.show
