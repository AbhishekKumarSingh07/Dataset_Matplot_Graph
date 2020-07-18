#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:48:57 2019

@author: akki
"""
import pandas as pd
import matplotlib.pyplot as plt


data= pd.read_csv('matches.csv')            
teams=[]
won=[]
loss=[]
for dt in data[data['season']==2008].winner.unique():
    count_won=(data.where((data.winner==dt) & (data.season==2008))).id.count()
    count_loss=((data.where(((data.team1==dt) | (data.team2==dt)) & (data.season==2008))).id.count())-count_won
    teams.append(dt)
    won.append(count_won)
    loss.append(count_loss)
    
team_sname=[]

for team in teams:
    short_form = ''
    for initial in team.split(' '):
       short_form = short_form + initial[0]
    team_sname.append(short_form)

#pd.DataFrame(team_won, index=['Won']).T.to_csv('Soln.csv')
#print(team_sname,won)


#print(team_sname,won,loss)


win_pos = [1,2,3,4,5,6,7,8]
range_y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lost_pos=[1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]


plt.bar(win_pos,won,width=0.4,color='c',alpha=0.6,label='Won')
plt.bar(lost_pos,loss,width=0.4,color='r',alpha=0.6,label='Lost')
plt.yticks(range_y)
plt.ylabel("Matches")
plt.xticks(win_pos,team_sname,rotation='vertical')
plt.grid(True)
plt.legend()
plt.title('IPL 2008')
plt.show()

    
  
            
    



    
