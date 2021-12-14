import matplotlib.pyplot as plt
with open("normal-seq.csv", "r") as f:
    data = f.readlines()
data.pop(0)
datas=[]
for item in data:
    k=item.split(',')
    strs=k[-1][0:-1]
    k.pop()
    k.append(strs)
    datas.append(k)
NN=datas[0:11]
YY=datas[11:22]
NY=datas[22:33]
YN=datas[33:44]
xtick=[]
x=[]
NN_data=[]
NY_data=[]
YY_data=[]
YN_data=[]
baseline=[]
for i in range(len(NN)):
    xtick.append(NN[i][3])
    x.append(i+1)
    NN_data.append(eval(NN[i][-1]))
    YN_data.append(eval(YN[i][-1]))
    YY_data.append(eval(YY[i][-1]))
    NY_data.append(eval(NY[i][-1]))
    baseline.append(0)
l1,=plt.plot(x,NN_data)
l2,=plt.plot(x,YN_data)
l3,=plt.plot(x,NY_data)
l4,=plt.plot(x,YY_data)
l5,=plt.plot(x,baseline)
plt.xticks(x,xtick)
plt.xlabel("Block Size", fontproperties = 'Times New Roman',fontsize=25)
plt.ylabel("Speed", fontproperties = 'Times New Roman',fontsize=25)
plt.title("Speed-Block_Size", fontdict={'family' : 'Times New Roman', 'size'   : 26})
plt.tick_params(axis='both', labelsize=15)
plt.legend(handles=[l1,l2,l3,l4],labels=['NN','YN','NY','YY'], prop={'family' : 'Times New Roman', 'size'   : 22})
plt.grid()
plt.show()