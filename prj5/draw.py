from os import lseek
import matplotlib.pyplot as plt
with open("new_data1.csv", "r") as f:
    data = f.readlines()
x=[]
y=[]
data.pop(0)
for i in range(3):
    y_s=[]
    for j in range(6):
        t=data[0].split(',')
        data.pop(0)
        if i==0: x.append(t[1])
        y_s.append(eval(t[-1]))
    y.append(y_s)
ls=[]
for i in range(3):
    l,=plt.plot(x,y[i])
    ls.append(l)
plt.legend()
plt.xlabel("Package Size", fontproperties = 'Times New Roman',fontsize=25)
plt.ylabel("Loss Rate", fontproperties = 'Times New Roman',fontsize=25)
# plt.title("Speed-Block_Size", fontdict={'family' : 'Times New Roman', 'size'   : 26})
plt.tick_params(axis='both', labelsize=15)
plt.legend(handles=ls,labels=['Number=4k','Number=8k','Number=16k'], prop={'family' : 'Times New Roman', 'size'   : 22})
plt.grid()
plt.show()
        