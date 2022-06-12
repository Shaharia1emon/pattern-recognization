import pandas as pd
import math
emon = pd.read_csv('Book1.csv')
print(emon.to_string())

# CALCULATING THE ENTROPY for the whole data set
def entropy(maleCount, femaleCount, totalData):
    if totalData == 0 or maleCount == 0 or femaleCount == 0:
        return 0
    else:
        return round(-(maleCount / totalData) * (math.log2(maleCount / totalData)) \
                     - (femaleCount / totalData) * (math.log2(femaleCount / totalData)), 4)

#shaharia bhuiyan emon.
#cse1901016029.(16a2)
# CALCULATING THE ENTROPY attribute wise ...
def atrributeEntropy(attribute, condition):
    yesCount, noCount, yesMaleCount, yesFemaleCount, noMaleCount, noFemaleCount = 0, 0, 0, 0, 0, 0
    for datum in range(totalData):
        if emon.iloc[datum][attribute] <= condition:
            yesCount += 1
            if emon.iloc[datum]['Class'] == 'M':
                yesMaleCount += 1
            elif emon.iloc[datum]['Class'] == 'F':
                yesFemaleCount += 1
        else:
            noCount += 1
            if emon.iloc[datum]['Class'] == 'M':
                noMaleCount += 1
            elif emon.iloc[datum]['Class'] == 'F':
                noFemaleCount += 1

    yesEntropy = entropy(yesMaleCount, yesFemaleCount, yesCount)
    noEntropy = entropy(noMaleCount, noFemaleCount, noCount)

    # CALCULATING THE INFORMATION GAIN, attribute wise ...
    ig = mainEntropy - ((yesCount / totalData) * yesEntropy + (noCount / totalData) * noEntropy)

    resultDict = {'yes': yesEntropy, 'no': noEntropy, 'ig': round(ig, 4)}

    return resultDict


# main function to calculate the information gain
mainEntropy, maleCount, femaleCount = 0, 0, 0
totalData = len(emon)

for sanjida in range(totalData):
    if emon.iloc[sanjida]['Class'] == 'M':
        maleCount += 1
    elif emon.iloc[sanjida]['Class'] == 'F':
        femaleCount += 1

mainEntropy = entropy(maleCount, femaleCount, totalData)
#print(data)
print("Main Entropy: ", mainEntropy)

# hair length section ...
print()
hairLength = int(input("Enter the hair length <=: "))
hairLengthInfo = atrributeEntropy('Hair length', hairLength)

print("Hair Length Yes Entropy: ", hairLengthInfo['yes'])
print("Hair Length No Entropy: ", hairLengthInfo['no'])
print("Hair Length Information Gain: ", hairLengthInfo['ig'])

# weight section ...
print()
weightValue = int(input("Enter the weight <=: "))
weightInfo = atrributeEntropy('Weight', weightValue)

print("Weight Yes Entropy: ", weightInfo['yes'])
print("Weight No Entropy: ", weightInfo['no'])
print("Weight Information Gain: ", weightInfo['ig'])

# Age section ...
print()
age = int(input("Enter the age <=: "))
ageInfo = atrributeEntropy('Age', age)

print("Age Yes Entropy: ", ageInfo['yes'])
print("Age No Entropy: ", ageInfo['no'])
print("Age Information Gain: ", ageInfo['ig'])

