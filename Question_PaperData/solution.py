import json

v = list()
dp = list()
easy_question_comb = []
med_question_comb = []
hard_question_comb = []

def dataReaderFromJson(fileName):
    try:
        with open(fileName) as f:
            json_data = json.load(f)
            return json_data        
    except Exception as err:
        print('Failed to read questions: ',err)


def finder(index,sum,a,sum_gl,dec_par):     
    # print(index,sum,a,sum_gl)               
    try:           
        if sum_gl == sum:                                               
            te = v[:]
            if(dec_par == 'e'):
                easy_question_comb.append(te)                              
            elif(dec_par == 'm'):
                med_question_comb.append(te)
            elif(dec_par == 'h'):
                hard_question_comb.append(te)
        if index == len(a) or sum > sum_gl or dp[index][sum] :
            return
        finder(index+1,sum,a,sum_gl,dec_par)
        v.append(index)        
        finder(index + 1,sum + a[index],a,sum_gl,dec_par)
        v.pop()
        dp[index][sum] = 1          
    except Exception as err:
        print('Error finding indeces: ',err)

def global_initializer():
    global v,dp
    v = []
    dp = [[0 for x in range(1005)] for y in range(1005)]        

def questionIndexFinder(fin_d,e_m,m_m,h_m):
    try:
        global_initializer()
        # print(fin_d['eas_lis']) 
        easy = False
        medium = False
        hard = False     
        finder(0,0,fin_d['eas_lis'],e_m,'e') 
        easy_question_comb[0]    
        global_initializer()        
        finder(0,0,fin_d['med_lis'],m_m,'m')    
        global_initializer()        
        finder(0,0,fin_d['har_lis'],h_m,'h')            
        if(len(easy_question_comb) > 0 and len(easy_question_comb[0])):
            easy = True        
        if(len(med_question_comb) > 0 and len(med_question_comb[0])):
            medium = True
        if(len(hard_question_comb) > 0 and len(hard_question_comb[0])):
            hard = True          
        if(easy and medium and hard):
            print("*****************************************************Total Marks:",(e_m+m_m+h_m))
            print("********************Easy Questions**********************"," Marks: ",e_m)
            for i in easy_question_comb[0]:                              
                print("Question no:- ",fin_d['eas_qData'][fin_d['eas_lis'][i]][0]," Marks: ",fin_d['eas_lis'][i])
                del fin_d['eas_qData'][fin_d['eas_lis'][i]][0]                
            print("********************Medium Questions********************"," Marks: ",m_m)
            for i in med_question_comb[0]:                
                print("Question no:- ",fin_d['med_qData'][fin_d['med_lis'][i]][0]," Marks: ",fin_d['med_lis'][i])
                del fin_d['med_qData'][fin_d['med_lis'][i]][0]
            print("********************Hard Questions**********************"," Marks: ",h_m)
            for i in hard_question_comb[0]:                
                print("Question no:- ",fin_d['har_qData'][fin_d['har_lis'][i]][0]," Marks: ",fin_d['har_lis'][i])
                del fin_d['har_qData'][fin_d['har_lis'][i]][0]
        else:
            print("Can't generate questions with given requirements.")

    except Exception as err:
        print('Exception in formatting questions: ',err)


def dataSeggregater(data):
    try:
        temp_easy_questStor = dict()
        temp_medium_questStor = dict()
        temp_hard_questStor = dict()
        temp_easy_list = list()
        temp_med_list = list()
        temp_hard_list = list()  
        final_dict = dict()       
        if not data == None:
            for i in data:
                if i['diff'] == 'easy':
                   temp_easy_list.append(i['marks']) 
                   if not i['marks'] in temp_easy_questStor:
                       temp_easy_questStor[i['marks']] = []                                            
                   temp_easy_questStor[i['marks']].append(i['qNo'])
                elif i['diff'] == 'medium':
                   temp_med_list.append(i['marks']) 
                   if not i['marks'] in temp_medium_questStor:
                       temp_medium_questStor[i['marks']] = []                                            
                   temp_medium_questStor[i['marks']].append(i['qNo'])
                elif i['diff'] == 'hard':
                   temp_hard_list.append(i['marks']) 
                   if not i['marks'] in temp_hard_questStor:
                       temp_hard_questStor[i['marks']] = []                                            
                   temp_hard_questStor[i['marks']].append(i['qNo'])
            final_dict['eas_lis'] = temp_easy_list
            final_dict['eas_qData'] = temp_easy_questStor
            final_dict['med_lis'] = temp_med_list
            final_dict['med_qData'] = temp_medium_questStor
            final_dict['har_lis'] = temp_hard_list
            final_dict['har_qData'] = temp_hard_questStor
            return final_dict

    except Exception as err:
        print("Error seggregating data: "+err)


def main():
    try:
        inp = input("Enter Input: format(Totalmarks, easy easy%, medium medium%, hard hard%):\n").split(',')
        # inp = "20, easy 25, medium 50, hard 25".split(",")
        totalmarks =  int(inp[0])                     
        easy_percentage =  int(inp[1].strip().split('easy')[1])                     
        medium_percentage =  int(inp[2].strip().split('medium')[1])        
        hard_percentage =  int(inp[3].strip().split('hard')[1])                                       
        easy_marks = int((totalmarks * easy_percentage)/100)
        medium_marks = int((totalmarks * medium_percentage)/100)
        hard_marks = int((totalmarks * hard_percentage)/100)        
        if (easy_marks+medium_marks+hard_marks) == totalmarks:
            data = dataReaderFromJson('questions.txt')             
            fin_d = dict()                        
            fin_d = dataSeggregater(data)                        
            # print(fin_d)
            if not fin_d == None:
                questionIndexFinder(fin_d,easy_marks,medium_marks,hard_marks)            
            else:
                print('Error seggregating data.')

        else:
            print("There's a mismatch in total marks and the percentage distribution.")
    except Exception as err:
        print("Something wen't wrong: ",err)



# 20, easy 25, medium 50, hard 25
# 120, easy 10, medium 30, hard 60
if __name__ == "__main__":
    main()