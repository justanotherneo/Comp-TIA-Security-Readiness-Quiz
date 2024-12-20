import random
import time

#program logic 
    #greet user and give info about the quiz as well as instructions for input
    #user is presented with multiple choice sec+ quiz questions 
    #user inputs answer into program
    #program evaluate users answer and tells the if it is correct or not
    #this process continues untill the end where there final score and grade is given
    #the last section will tell the user what section of the sec+ study guide they need to focus on
     
#program outline
    #ascii art
    #user instructions
    #list of dictionaries containing each question, possible answers, and correct answer
    #while loop to keep the program running and output each new question as user answers
    #counter used as index to get the right question, answer, and choices
    #if and elif statements to evaluate the answer and sanitize input
    #function to evaluate users score
    #print statement to tell user what section of study guide this quiz was based on
    




    # artwork, contact, welcome user, explain program

print(r'''\
                                                                                                                                                 
         _______________        
       /               | 
      /        _____   |
      |        \    |  |        ______                 __  __                 _____                                                                                   
      \         \   |__|      /   __  \             /   ___   \              |     |                                                                                          
        \         \         /    /  \  \          /    /    \__|             |     |                                                       
          \         \      /    /____\  \       /    /                  _____|     |_____                                     
 _____      \        /     |    _________\     |    |                  |                 |                                                  
|     \     /       /      |   |               |    |                  |_____       _____|                                                     
|      \___/       /       \    \     ___       \    \      ____             |     |                                                  
|                 /         \    \___/  /         \   \____/  /              |     |                                                                
 \_______________/           \_________/            \_______/                |_____|                                                                                           
                                                                                                                                             

                    Am I ready to take the the Comp TIA Sec+ Exam?
                        Not if you get any of these wrong
                                 Level 0
      
      by: Vergil 
      YT, FB, IG, TT, SC: crzycybr
      vergil@crzycybersecurity.com

      ''')

#welcome user and give instructions

print(r'''Welcome to my very basic Comp TIA Security+ Readiness Evaluation. This test 
      was designed to evaluate if you are ready to take the exam. There are 5 levels ranging
      from easiest to hardest. The first three levels focus on basics and memorization orientated
      questions, while the last two focus on concepts and word problems that are more in line 
      with actual questions from the exam.

      There will be ten multiple choice questions. Unlike the exam you will have three 
      answers to choose from. Make you selection by entering just the letter of the 
      selection you believe is correct. At the end of the test you will be given a score,
      but will also have immediate feedback. 

      This is level 0 (see what I did there?). If you get ANY of these wrong. You have hella
      studying to do before you even look at their website.

      ''')

input('Press enter to begin')
#list containing dictionaries for each question that contain the question, choices, and correct answer

questions = [{'Q' : 'What service typically operates on port 161?', 'c' : ['A. SNMP Trap', 'B. SSH', 'C. SMTP'], 
               'ca' : 'a'},
{'Q' : 'What notorious insecure legacy service runs on port 23' , 'c' : ['A. FTP' , 'B. SSH', 'C. Telnet'], 'ca': 'c'},
{'Q' : 'What port does DNS typically operate on?', 'c' : ['A. 45', 'B. 150', 'C. 53'], 'ca' : 'c'}, 
{'Q' : 'What does SMTP stand for?', 'c' : ['A. Standard Mail Transfer Protocol', 'B. Simple Mail Transfer Protocol', 'C. Service Management Transport Protocol']
 , 'ca' : 'b'}, {'Q' : 'What service usually operates on port 21?', 'c' : ['A. FTP', 'B. SSH', 'C. SMTP'], 'ca' : 'a'},
 {'Q' : '10.145.50.255 and 172.100.10.45 are examples of what type of IP Address?', 'c' : [ 'A. Private Ip Addresses', 'B. Public Ip Addresses', 'C. IPv6 Addresses'],
  'ca' : 'a'}, {'Q' : 'Specificall targeting the CEO or other top level employee via phishing is called?', 'c' : ['A. Spear Phishing', 'B. Whaling',
'C. Vishing'], 'ca' : 'b'}, {'Q' : 'Port 69 typicall runs what service?', 'c' : ['A. Giggity Network Protocol', 'B. Trivial File Transfer Protocol', "C. Free Telephone Protocol"], 'ca' : 'b'},
{'Q' : 'Adversaries sending targeting voice calls in a social engineering attack is known as?', 'c' : ['A. Vishing', 'Smishing', 'Spam Attack'], 'ca' : 'a'}, 
{'Q' : 'What is it called when an attacker who has compromised a system attempts to gain higher level access to the compromised system?', 'c' : ['A. Leveling Up',
'B. Pivoting', 'C. Privilidge Escalation'], 'ca' : 'c'}]


   
#main program function containing while loop, answer evaluation, counters for indexes and answers

def main():  

    incorrect = 0
    correct = 0
    counter = 0

    while counter < len(questions):

       
            
        print(questions[counter]['Q'])
        print('\n' .join(questions[counter]['c']))
        
        while True:  # loop until valid input is given
            user_answer = input('Your selection (a, b, or c): \n').lower()
            
            # Validate the input
            if user_answer not in ['a', 'b', 'c']:
                print("Invalid choice. Please select 'a', 'b', or 'c'.")
            else:
                break

        #check user's answer vs correct answer in dictionary
        if user_answer != questions[counter]['ca']:
            print('That is incorrect')
            incorrect += 1
            
            

        else:
            print('That is correct.')
            correct += 1 
            
        counter += 1    

        
    score = round(100/correct)  

    if score <= 70: 
        print(f'You got {correct} out 10. You scored a {score}%. You need to hit those books and learn the basics, \nyou are no where near ready')
    else:
        print(f'You got {correct} out of 10. You scored a {score}%. Don\'t be too pleased. This is the easiest one, \n but I\'m sure your mom would still be proud :)')
        


    

main()


