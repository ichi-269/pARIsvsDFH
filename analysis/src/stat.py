from re import A
from sys import api_version
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

df_est = pd.read_csv('../data/as95_data/res_estimations_exp2.csv')
df_pred = pd.read_csv('../data/as95_data/res_predictions_exp2.csv')

df_est_freq1 = df_est[df_est['frequency'] == 1]
df_est_freq2 = df_est[df_est['frequency'] == 2]
df_est_freq3 = df_est[df_est['frequency'] == 3]
df_est_freq4 = df_est[df_est['frequency'] == 4]
df_est_freq5 = df_est[df_est['frequency'] == 5]
df_est_freq6 = df_est[df_est['frequency'] == 6]
df_est_freq7 = df_est[df_est['frequency'] == 7]
df_est_freq8 = df_est[df_est['frequency'] == 8]
df_est_freq9 = df_est[df_est['frequency'] == 9]
df_est_freq10 = df_est[df_est['frequency'] == 10]
df_est_freq11 = df_est[df_est['frequency'] == 11]
df_est_freq12 = df_est[df_est['frequency'] == 12]
df_est_freq13 = df_est[df_est['frequency'] == 13]

est_mean = []
est_std = []

# 刺激1
est_mean.append(df_est_freq1['estimation'].mean())
# 刺激2
est_mean.append(df_est_freq2['estimation'].mean())
# 刺激3
est_mean.append(df_est_freq3['estimation'].mean())
# 刺激4
est_mean.append(df_est_freq4['estimation'].mean())
# 刺激5
est_mean.append(df_est_freq5['estimation'].mean())
# 刺激6
est_mean.append(df_est_freq6['estimation'].mean())
# 刺激7
est_mean.append(df_est_freq7['estimation'].mean())
# 刺激8
est_mean.append(df_est_freq8['estimation'].mean())
# 刺激9
est_mean.append(df_est_freq9['estimation'].mean())
# 刺激10
est_mean.append(df_est_freq10['estimation'].mean())
# 刺激11
est_mean.append(df_est_freq11['estimation'].mean())
# 刺激12
est_mean.append(df_est_freq12['estimation'].mean())
# 刺激13
est_mean.append(df_est_freq13['estimation'].mean())

# 刺激1
est_std.append(df_est_freq1['estimation'].std())
# 刺激2
est_std.append(df_est_freq2['estimation'].std())
# 刺激3
est_std.append(df_est_freq3['estimation'].std())
# 刺激4
est_std.append(df_est_freq4['estimation'].std())
# 刺激5
est_std.append(df_est_freq5['estimation'].std())
# 刺激6
est_std.append(df_est_freq6['estimation'].std())
# 刺激7
est_std.append(df_est_freq7['estimation'].std())
# 刺激8
est_std.append(df_est_freq8['estimation'].std())
# 刺激9
est_std.append(df_est_freq9['estimation'].std())
# 刺激10
est_std.append(df_est_freq10['estimation'].std())
# 刺激11
est_std.append(df_est_freq11['estimation'].std())
# 刺激12
est_std.append(df_est_freq12['estimation'].std())
# 刺激13
est_std.append(df_est_freq13['estimation'].std())


print("mean", est_mean)
print("std", est_std)
