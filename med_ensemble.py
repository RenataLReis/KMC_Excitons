import sys

f = open("sum_"+sys.argv[1], "r")
positions = f.readlines()
y_med_ens = 0
for string_position in positions:
    position = float(string_position) #converts in float
    y_med_ens = y_med_ens + position
ybar = y_med_ens/1000
print(sys.argv[1], ybar, file=open("med_ens","a"))


