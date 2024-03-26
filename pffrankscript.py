from msilib.schema import Directory
import os
from time import time

# Using readlines()
#file1 = open('pass rush draft.txt', 'r')
file2 = open('cb all pro 2024 pff.txt', 'r')
#file3 = open('draft names.txt', 'r')
path_ = "C:/Users/chuke/Documents/CB compare/Data Folder/"
directory = os.fsencode(path_)

#go through folder and create of all files under 12 characters
file_list = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    filename = str(filename) 
    #print(filename)
        #print(file)
    if len(filename) != 'Null':
        test = path_ + filename
        stripped_line = test.rstrip()
        test = stripped_line
         
        file_list.append(test)
#print(file_list)

#Lines = file1.readlines()
average_allpro = file2.readlines()
#draft_names = file3.readlines() 
count = 0
combine_pffstats = []
allpro_combine = []
names = []



for line2 in average_allpro:
    allpro_combine.append(line2)


average_for_allpro = []
Combine_line = []
player_comparison = []
average_for_allpro = allpro_combine[1].split('\t')
ideal_traits = []





    
for f in file_list:
    file1 = open(f, 'r')
    Lines = file1.readlines()
    
    for player in Lines:
        #print(player)
        Combine_line = player.rstrip('\n').split(',')
        #print(Combine_line)
        
        if (Combine_line[0] == 'player' ):
            continue
        
        else:
    


    
            if(Combine_line[7] == ''):
                catch_rate == float_avg_catch_rate
            else:
                catch_rate = float(Combine_line[7])
            #contested_catch = float(Combine_line[8])
    
    #print(true_prgrade)
            if(Combine_line[8] == ''):
                cov_percent == float_avg_cov_p
            else:
                cov_percent = float(Combine_line[8])
                
            #print(win_rate)
            #print(win_rate)
            if(Combine_line[10]== ''):
                cov_snap_per_t == float_avg_cspt
            else:
                cov_snap_per_t = float(Combine_line[10])
            
            #grades_offense = float(Combine_line[19])
            
            if(Combine_line[14]== ''):
                forced_incompletion_rate == float_avg_forced_incompletion
            else:
                forced_incompletion_rate = float(Combine_line[14])
                
            if(Combine_line[16]== ''):
                cov_def_grade == float_avg_cdg
            else:    
                cov_def_grade = float(Combine_line[28])
            
            targeted_qb_rating = float(Combine_line[35])
            
            if(Combine_line[17]== ''):
                grades_defense == float_avg_gd
            else:    
                grades_defense = float(Combine_line[17])
            
            if(Combine_line[18]== ''):
                grades_defense_penalty == float_avg_gdp
            else:    
                grades_defense_penalty = float(Combine_line[18])
                
            if(Combine_line[21]== ''):
                grades_tackle == float_avg_gt
            else:    
                grades_tackle = float(Combine_line[21])
                
            if(Combine_line[21]== ''):
                missed_tackle_rate = float_avg_mtr
            else:    
                missed_tackle_rate = float(Combine_line[21])

            #average of all pro pff stats from college
            float_avg_catch_rate = float(average_for_allpro[7])
            float_avg_cov_p = float(average_for_allpro[8])
            float_avg_cspt = float(average_for_allpro[10])   
            float_avg_forced_incompletion = float(average_for_allpro[14])
            float_avg_cdg = float(average_for_allpro[16])
            float_avg_gd = float(average_for_allpro[17])
            float_avg_gdp = float(average_for_allpro[18])
            float_avg_gt = float(average_for_allpro[21])
            float_avg_mtr = float(average_for_allpro[24])
    
    
            #print(catch_rate)
    

    

            if((float_avg_catch_rate - 30 <= catch_rate <= float_avg_catch_rate + 30 )
                and ((float_avg_cov_p -3.00)  <= cov_percent <= (float_avg_cov_p+100))
                #and ((float_avg_cspt -5.00)  <= cov_snap_per_t <= (float_avg_cspt + 300))
                and ((float_avg_forced_incompletion -8) <= forced_incompletion_rate <= (float_avg_forced_incompletion + 300))
                and ((float_avg_cdg -4) <= cov_def_grade <= (float_avg_cdg + 300))
                and ((float_avg_gd -5) <= grades_defense <= (float_avg_gd + 300))
                #and ((float_avg_gdp -5) <= grades_defense_penalty <= (float_avg_gdp + 300))
                #and ((float_avg_gt -10) <= grades_tackle <= (float_avg_gt + 300))
                #and ((float_avg_mtr -100) <= missed_tackle_rate <= (float_avg_mtr + 509))
                and (Combine_line[2] == 'CB'or Combine_line[2] == 'S')
                #and (Combine_line[33] == '2023' or Combine_line[33] == '2022' )
                ):
                    player_comparison.append(player)
    

Lines = open('cb list.txt', 'r')
combinelist = Lines.readlines()
combine_list = []
player_profile = []   
for line in combinelist:
    combine_list.append(line)
pc = []
final_list = []
for player in combine_list:
    player_profile = player.rstrip('\n').split('\t')
    for player1 in player_comparison:
         pc = player1.rstrip('\n').split(',')
         if(pc[0]== player_profile[0]):
             final_list.append(player1)
             
#print(final_list)
             
        
    
 


#for j in names:
    #for i in player_comparison:
        #named = i.split('\t')
        #if j == named[0]:
            #player_comparison.remove(i)


    #final_results = []
    #for i in player_comparison:
    #    named = i.rstrip('\n').split('\t')
    #    for n in names:
    #        na = n.rstrip('\n')
    #        if named[0] == na:
    #            final_results.append(i)

 






      

with open('pff_stats2024.txt', 'w') as f:
    f.write('player	player_id	position	team_name	player_game_count	batted_passes	declined_penalties	franchise_id	grades_pass_rush_defense	hits	hurries	pass_rush_opp	pass_rush_percent	pass_rush_win_rate	pass_rush_wins	penalties	prp	sacks	snap_counts_pass_play	snap_counts_pass_rush	total_pressures	true_pass_set_batted_passes	true_pass_set_hits	true_pass_set_hurries	true_pass_set_pass_rush_opp	true_pass_set_pass_rush_percent	true_pass_set_pass_rush_win_rate	true_pass_set_pass_rush_wins	true_pass_set_prp	true_pass_set_sacks	true_pass_set_snap_counts_pass_play	true_pass_set_snap_counts_pass_rush	true_pass_set_total_pressures\n')
    for w in final_list:
        f.write(w)
        f.write('\n')





        





