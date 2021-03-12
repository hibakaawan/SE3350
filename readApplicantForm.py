import pandas as pd



filename = input("Please enter the file name for TA applicants: ")

try:                            # trying userInput
    df = pd.read_csv(filename)

except FileNotFoundError:       # returns "Sorry..." if file does not exist
    print("Sorry, the file you typed in: {}, does not exist".format(filename))
    quit()                      # terminates program

dict1 = df.to_dict(orient='list')    # converts dataframe to dictionary of lists


# Stores each list in the dictionary based on key
courseCode = dict1['Course Code']

appName = dict1['Applicant Name']
appEmail = dict1['applicant email']
fundable = dict1['Applicant status ( 1- Fundable, 2-NotFundable,3-External)']
numHours = dict1['5or10 hrs']
courseRank = dict1['Course Rank']
q1 = dict1['Q1']
a1 = dict1['A1']
q2 = dict1['Q2']
a2 = dict1['A2']
q3 = dict1['Q3']
a3 = dict1['A3']

#empty lists to store 1st, 2nd and 3rd priority students
firstPriority = []
secondPriority = []
thirdPriority = []

#iterates through fundable list to find the index of 1st, 2nd and 3rd priority students and adds to appropriate list
sum = 0
for i in fundable:
    if i == 1:
        firstPriority.append(appName[sum])
    elif i == 2:
        secondPriority.append(appName[sum])
    else:
        thirdPriority.append(appName[sum])
    sum +=1

#removes duplicates
firstPriority = list(dict1.fromkeys(firstPriority))
secondPriority = list(dict1.fromkeys(secondPriority))
thirdPriority = list(dict1.fromkeys(thirdPriority))


print('These are the prioritization of students as required by the school of graduate studies\n\n1st Priority:')
for i in firstPriority:
    print(i)

print('\n2nd Priority:')
for i in secondPriority:
    print(i)

print('\n3nd Priority:')
for i in thirdPriority:
    print(i)
######################################################################################################################
filename = input("Please enter the file name for enrollment hours: ")

try:                            # trying userInput
    df = pd.read_csv(filename)

except FileNotFoundError:       # returns "Sorry..." if file does not exist
    print("Sorry, the file you typed in: {}, does not exist".format(filename))
    quit()                      # terminates program

#calculates required ta hours and adds new column to dataframe
df['Required TA Hours'] = ((df['Previous TA hours']/df['Previous Enrollments'])*df['Current Enrollemnts '])

#creating new dataframe which outputs the course code and the required TA hours for it
result_df =df[['Course Code', 'Required TA Hours']]
print(result_df)

final_dict = dict(zip(result_df['Course Code'], result_df['Required TA Hours']))
print(final_dict)
