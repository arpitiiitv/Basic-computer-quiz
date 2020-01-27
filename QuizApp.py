import requests
import json
import random

# UEL of open triva database
n=int(input("Enter number of questions :"))
url='https://opentdb.com/api.php?amount='+str(n)+'&category=18'

#get the given url into json_obje
json_obj = requests.get(url)
#load text of given json_obj into data 
# dict type data 
data=json.loads(json_obj.text)
# count is to inicate number of question
count=1
#to store score of player
score=0
#get all element whose key is result from data
for x in data['results']:
    #print question so key is 'question' here
    print(count,": ",x['question'],"\n")
    # get correct ans from data
    correct_ans=x['correct_answer']
    # get all incorrect number
    all_ans=x['incorrect_answers']
    # append correct ans into all_ans
    all_ans.append(correct_ans)
    #shuffle all ans to avoid cheating
    random.shuffle(all_ans)

    #printing all ans on console
    for i in range(len(all_ans)):
        #ASCII value of A is 65, so options will be A,B,...
        print(chr(65+i)," :",all_ans[i])
        #key index will store correct ans
        if all_ans[i]==correct_ans:
            key_index=chr(65+i)
        
    
    #take ans from user
    user_option=input("\nYour ans : ")
    # verify if option is valid upper case of lower case A,B,.. ,a,b,..
    # chr(65)=A ,chr(65+len(all_ans))) => if len ans = 3 then chr(65+len(all_ans)))=C
    if (user_option>=chr(65)  and user_option<=chr(65+len(all_ans))) or (user_option>=chr(97)  and user_option<=chr(97+len(all_ans))):
        # if user option is either correct option 
        # lower case of correct option
        if user_option==key_index or user_option==chr(ord(key_index)+32):
            #increrase score by 10
            score+=10
            print("Correct  :=> Current Score ",score,"\n")
            
        else:
            print("False  :=> Current Score ",score)  
            print(correct_ans,"\n")
    else:
            
        print("Invalid choice!!!! :=> Current Score ",score) 
        print(correct_ans,"\n")  
    count+=1

print("Total (Final) Score : ",score)