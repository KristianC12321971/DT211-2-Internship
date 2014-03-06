import urllib.request #imports library
#------------------------------------------------------------------------------#
#                               FUNCTIONS                                      #
#------------------------------------------------------------------------------#
def counting():#Function to count the amount of customers and put data in string
    num = 0
    for row in data: #pulls information line by line
        num += 1
        file.append(row) #putting the lines into an array called file
    return(num)#returning the number of lines/people are in the file 

def average_ints(array,number,j):#Function to get the average of the integer attributes
    i=0
    positive = 0
    negative = 0
    average_pos = 0
    average_neg = 0
    while(i<number):
        num = array[i].split(', ')
        if(array[i].find('>50K') != -1):#if the line is over 50K add that integer to average_pos
            average_pos = average_pos + int(num[j])
            positive += 1
        
        elif(array[i].find('<=50K') != -1):#if the line is under 50K add that integer to average_pos
            average_neg = average_neg + int(num[j])
            negative += 1
        i += 1
    #averaging the integers of above and below and then getting the average of those two
    average_pos = round(average_pos/positive)
    average_neg = round(average_neg/negative)
    average_int = round(average_pos+average_neg)/2
    return(average_int)

    
def average_strs(array,number,j):#Function gives weights to the string attributes
    i = 0
    average = {}
    key = []
    while(i<number):
        num = array[i].split(', ')
        #if the attribute is in the dictionary increment it
        if(num[j] in average):
            average[num[j]] += 1
    #if the attribute is not in the dictionary add it to it
        else:
            average[num[j]] = 1
            key.append(num[j])#adding the attribute in a array so it can be used later on
        i += 1
    i=0
    
    for key[i] in average:
        average[key[i]] =(average[key[i]]/number)#getting the weight of the attribute
    return(average)

#Function seperates attributes into two classes,gets the average of those
#two classes and then gets the average of those two averages
def classifier(att_dict,array,number,j):
    i = 0
    positive = 0
    negative = 0
    midpoint_pos = 0
    midpoint_neg = 0
    pos = {}
    neg = {}
    
    while(i<number):
        num = array[i].split(', ')
        weight = att_dict[num[j]]

        if(array[i].find('>50K') != -1):#if(
            midpoint_pos = midpoint_pos + weight
            positive += 1
        elif(array[i].find('<=50K') != -1):
            midpoint_neg = midpoint_neg + weight
            negative += 1
        i += 1
    midpoint = ((midpoint_pos/positive)+(midpoint_neg/negative))/2
    return(midpoint)
#------------------------------------------------------------------------------#
#                                    MAIN                                      #
#------------------------------------------------------------------------------#
data = open('sampledata.txt','r')#opening data file
file = [] #putting the file into an array to make it easier accessible to read
count = counting()
seventy_per = int(count*0.7)
#Weights-----------------------------------------------------
j = 1
workclass = average_strs(file,seventy_per,j)

j = 5
marital = average_strs(file,seventy_per,j)

j = 6
occupation = average_strs(file,seventy_per,j)

j = 7
relationship = average_strs(file,seventy_per,j)

j = 8
race = average_strs(file,seventy_per,j)

j = 9
gender = average_strs(file,seventy_per,j)
#Attributes-that-are-ints------------------------------------
j = 0
age = average_ints(file,seventy_per,j)

j = 4
education = average_ints(file,seventy_per,j)

j = 10
gain = average_ints(file,seventy_per,j)

j = 11
loss = average_ints(file,seventy_per,j)

j = 12
hours = average_ints(file,seventy_per,j)
#Classifier--------------------------------------------------
j = 1
workclass_mid = classifier(workclass,file,seventy_per,j)

j = 5
marital_mid = classifier(marital,file,seventy_per,j)

j = 6
occupation_mid = classifier(occupation,file,seventy_per,j)

j = 7
relationship_mid = classifier(relationship,file,seventy_per,j)

j = 8
race_mid = classifier(race,file,seventy_per,j)

j = 9
gender_mid = classifier(gender,file,seventy_per,j)
#--------------------------------------------------------

#------------------------------------------------------------------------------#
#                               TESTING                                        #
#------------------------------------------------------------------------------#
correct = 0
counter=0
while(seventy_per<count):#Tests the last 30% of the data
    num = file[seventy_per].split(', ')
    ovr = 0
    und = 0

    if(int(num[0]) > age):
        ovr += 1
    else:
        und += 1
        
    if(float(workclass[num[1]]) < workclass_mid):
        ovr += 1
    else:
        und += 1
        
    if(int(num[4]) > education):
        ovr += 1
    else:
        und += 1
        
    if(float(marital[num[5]]) > marital_mid):
        ovr += 1
    else:
        und += 1

    if(float(occupation[num[6]]) > occupation_mid):
        ovr += 1
    else:
        und += 1

    if(float(relationship[num[7]]) > relationship_mid):
        ovr += 1
    else:
        und += 1

    if(float(race[num[8]]) > race_mid):
        ovr += 1
    else:
        und += 1
        
    if(float(gender[num[9]]) > gender_mid):
        ovr += 1
    else:
        und += 1

    if(int(num[10]) > gain):
        ovr += 1
    else:
        und += 1
    if(int(num[11]) > loss):
        ovr += 1
    else:
        und += 1

    if(int(num[12]) > hours):
        ovr += 1
    else:
        und += 1

    if(ovr > und):#This decides whether it believes the person make under or over 50k
        answer = '>50K'
    else:
        answer = '<=50K'
    #This checks to see if you answer was right   
    if(file[seventy_per].find(answer) != -1):
        correct +=1
    else:
        correct += 0
        
    counter+=1
    seventy_per+=1
accuracy = round((correct/counter)*100) #Rounds the percentage
print("Income Predictor Accurracy",accuracy,"%")
data.close()
