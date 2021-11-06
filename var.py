import sys
import os
import numpy as np

#change directory
os.chdir("/home/renata/emittedir")

#read emission times
t_emi = open('emitted_P6P_inter_'+sys.argv[1],'r')
lines = t_emi.readlines()
t_emi_list = []
for x in lines:
    t_emi_list.append(x.split(' ')[0])
t_emi.close()


#change directory
os.chdir("/home/renata/sum_P6P6T_inter_"+sys.argv[1])

#time of emission of each exciton into array
t = 0
Ld_emi_list = []
for arquivo in os.listdir():
    for i in t_emi_list:
        if (arquivo.endswith(str(i))):
            y = []
            files = open(arquivo,"r")
            positions = files.readlines()
            y.append(positions)
            files.close()
            y_array = np.asarray(y,float)
            sigma = np.var(y_array)
            Ld_emi = np.sqrt(sigma)
            Ld_emi_list.append(Ld_emi)
            print(i,sigma,file=open('var_P6P_t','a'))

os.chdir("/home/renata/")

Ld_emi_array = np.asarray(Ld_emi_list,float)
Ld_emi_bar = np.mean(Ld_emi_array)
print(sys.argv[1],Ld_emi_bar,file=open('Ld_inter','a'))



#y1 = []
#g = open("sum_PPtf","r")
#posicoes = g.readlines()
#y1.append(posicoes)
#g.close()
#y1 = np.asarray(y1,float)
#sigma1 = np.var(y1)
#print("sigma²(tf)=",sigma1)
#Ld = np.sqrt(sigma1)
#print("Ld=",Ld)



#f1 = open("sum_dt_3_dy_1_"+sys.argv[1],"r")
#lines1 = f1.readlines()
#positions1 = np.asarray(lines1,float)

#f2 = open("sum_dt_3_dy_2_"+sys.argv[1],"r")
#lines2 = f2.readlines()
#positions2 = np.asarray(lines2,float)
#
#f3 = open("sum_dt_3_dy_3_"+sys.argv[1],"r")
#lines3 = f3.readlines()
#positions3 = np.asarray(lines3,float)
#
#f4 = open("sum_dt_3_dy_4_"+sys.argv[1],"r")
#lines4 = f4.readlines()
#positions4 = np.asarray(lines4,float) 
#
#f5 = open("sum_dt_3_dy_5_"+sys.argv[1],"r")
#lines5 = f5.readlines()
#positions5 = np.asarray(lines5,float)
#
#f6 = open("sum_dt_3_dy_6_"+sys.argv[1],"r")
#lines6 = f6.readlines()
#positions6 = np.asarray(lines6,float) 
#
#f7 = open("sum_dt_3_dy_7_"+sys.argv[1],"r")
#lines7 = f7.readlines()
#positions7 = np.asarray(lines7,float) 
#
#f8 = open("sum_dt_3_dy_8_"+sys.argv[1],"r")
#lines8 = f8.readlines()
#positions8 = np.asarray(lines8,float) 
#
#f9 = open("sum_dt_3_dy_9_"+sys.argv[1],"r")
#lines9 = f9.readlines()
#positions9 = np.asarray(lines9,float)


#sigma_dy_1 = np.var(positions1)
#sigma_dy_2 = np.var(positions2)
#sigma_dy_3 = np.var(positions3)
#sigma_dy_4 = np.var(positions4)
#sigma_dy_5 = np.var(positions5)
#sigma_dy_6 = np.var(positions6)
#sigma_dy_7 = np.var(positions7)
#sigma_dy_8 = np.var(positions8)
#sigma_dy_9 = np.var(positions9)


#print(sys.argv[1], sigma_dy_1, file=open("var_t_dt_3_dy_1","a"))
#print(sys.argv[1], sigma_dy_2, file=open("var_t_dt_3_dy_2","a"))
#print(sys.argv[1], sigma_dy_3, file=open("var_t_dt_3_dy_3","a"))
#print(sys.argv[1], sigma_dy_4, file=open("var_t_dt_3_dy_4","a"))
#print(sys.argv[1], sigma_dy_5, file=open("var_t_dt_3_dy_5","a"))
#print(sys.argv[1], sigma_dy_6, file=open("var_t_dt_3_dy_6","a"))
#print(sys.argv[1], sigma_dy_7, file=open("var_t_dt_3_dy_7","a"))
#print(sys.argv[1], sigma_dy_8, file=open("var_t_dt_3_dy_8","a"))
#print(sys.argv[1], sigma_dy_9, file=open("var_t_dt_3_dy_9","a"))





#to verify, uncomment:

#m = sum(yilist)/len(yilist)

#var = sum((yi-m)**2 for yi in yilist)/len(yilist)

#print(var)
