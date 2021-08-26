import json
import csv
from tqdm import tqdm
import re


####################################################
####################################################
##### LOAD GLOBAL OBJECTS
####################################################
####################################################
with open('./rawData/userProfileData.json') as f:
    data = json.load(f)


####################################################
####################################################
##### FUNCTIONS
####################################################
####################################################

#### USER PROFILE DATA
def userProfileDataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            try:
                companyCode = data[i]['company']
            except:
                companyCode = ""
            try:
                educationMajor = data[i]['educationMajor']
            except:
                educationMajor = ""
            try:
                educationLevel = data[i]['educationLevel']
            except:
                educationLevel = ""
            try:
                gender = data[i]['gender']
            except:
                gender = ""
            try:
                userGroup = data[i]['userGroup']
            except:
                userGroup = ""

            dataOut.writerow([userID, educationLevel, educationMajor, gender, userGroup])

#### COMPANY RATINGS
def userProfile_companyRatings_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            companyRatingDict = (data[i]['companyRatings'])
            try:
                for companyCode, companyRating in companyRatingDict.items():
                    dataOut.writerow([userID,companyCode,companyRating])
            except:
                None


#### EMAILS CLICKED
def userProfile_emailsClicked_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            emailsClickedDict = (data[i]['emailsClicked'])
            for ecd in range(len(emailsClickedDict)):
                try:
                    campaignId = data[i]['emailsClicked'][ecd]['campaignId']
                except:
                    campaignId = ""
                try:
                    companyId = data[i]['emailsClicked'][ecd]['companyID']
                except:
                    companyId = ""
                try:
                    companyName = data[i]['emailsClicked'][ecd]['companyName']
                except:
                    companyName = ""
                try:
                    diversityScore = data[i]['emailsClicked'][ecd]['diversityScore']
                except:
                    diversityScore = ""
                try:
                    position = data[i]['emailsClicked'][ecd]['position']
                except:
                    position = ""
                try:
                    timeStamp = data[i]['emailsClicked'][ecd]['timestamp']
                except:
                    timeStamp = ""

                dataOut.writerow([userID, campaignId, companyId, companyName, diversityScore, position, timeStamp])


#### EMAILS OPENED
def userProfile_emailsOpened_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            emailsOpenedDict = (data[i]['emailsOpened'])
            for eod in range(len(emailsOpenedDict)):
                try:
                    campaignId = data[i]['emailsOpened'][eod]['campaignId']
                except:
                    campaignId = ""
                try:
                    timeStamp = data[i]['emailsOpened'][eod]['timestamp']
                except:
                    timeStamp = ""
                
                dataOut.writerow([userID, campaignId, timeStamp])


#### EMAILS SENT
def userProfile_emailsSent_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            emailsSentDict = (data[i]['emailsSent'])
            for esn in range(len(emailsSentDict)):
                try:
                    campaignId = data[i]['emailsSent'][esn]['campaignId']
                except:
                    campaignId = ""
                try:
                    timeStamp = data[i]['emailsSent'][esn]['timestamp']
                except:
                    timeStamp = ""

                dataOut.writerow([userID, campaignId, timeStamp])



#### USER LOCATIONS
def userProfile_locations_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            locationsDict = (data[i]['locations'])
            for loc in range(len(locationsDict)):
                try:
                    city = data[i]['locations'][loc]['city']
                except:
                    city = ""
                try:
                    state = data[i]['locations'][loc]['state']
                except:
                    state = ""
                
                dataOut.writerow([userID, city, state])


#### USER PREFERRED LEVEL
def userProfile_preferredLevel_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            if "preferredLevels" in str(data[i]):
                levelDict = (data[i]['preferredLevels'])
                for pl in range(len(levelDict)):
                    try:
                        levelTitle = data[i]['preferredLevels'][pl]
                        levelNumber = pl
                    except:
                        levelTitle = ""
                    dataOut.writerow([userID, levelNumber, levelTitle])


#### USER PREFERRED TITLE
def userProfile_preferredTitles_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            if "preferredTitles" in str(data[i]):
                titleDict = (data[i]['preferredTitles'])
                for pt in range(len(titleDict)):
                    try:
                        normalizedTitle = data[i]['preferredTitles'][pt]['normalizedTitle']
                    except:
                        normalizedTitle = ""
                    try:
                        originalSearch = data[i]['preferredTitles'][pt]['originalSearch']
                    except:
                        originalSearch = ""
                    
                    dataOut.writerow([userID, normalizedTitle, originalSearch])


#### USER ETHNICITY
def userProfile_ethnicityDistribution_DataParse(fileName):
    with open(f"./results/{fileName}.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            userID = data[i]['userId']
            if "ethnicityDistribution" in data[i]:
                asian = data[i]["ethnicityDistribution"]["Asian"]
                blackAfricanAmerican = data[i]["ethnicityDistribution"]["Black or African American"]
                hispanic = data[i]["ethnicityDistribution"]["Hispanic or Latino"]
                unknown = data[i]["ethnicityDistribution"]["Unknown"]
                white = data[i]['ethnicityDistribution']['White']

                dataOut.writerow([userID, asian, blackAfricanAmerican, hispanic, unknown, white])





####################################################
####################################################
##### MAIN LOOP
####################################################
####################################################
####################################################
if __name__ == "__main__":
    fileNames = ["userProfile","userProfile_companyRatings", "userProfile_emailsClicked", "userProfile_emailsOpened", "userProfile_emailsSent", "userProfile_locations", "userProfile_preferredLevel", "userProfile_preferredTitles", "userProfile_ethnicityDistribution"]
    fileNames = ["userProfile_ethnicityDistribution"]

    for fileName in fileNames:
        if fileName == "userProfile":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID","educationLevel", "educationMajor", "gender", "userGroup"])
            userProfileDataParse(fileName)

        elif fileName == "userProfile_companyRatings":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID","companyCode", "companyRating"])
            userProfile_companyRatings_DataParse(fileName)

        elif fileName == "userProfile_emailsClicked":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "campaignId", "companyId", "companyName", "diversityScore", "position", "timeStamp"])
            userProfile_emailsClicked_DataParse(fileName)

        elif fileName == "userProfile_emailsOpened":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "campaignId", "timeStamp"])
            userProfile_emailsOpened_DataParse(fileName)

        elif fileName == "userProfile_emailsSent":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "campaignId", "timeStamp"])
            userProfile_emailsSent_DataParse(fileName)

        elif fileName == "userProfile_locations":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "city", "state"])
            userProfile_locations_DataParse(fileName)

        elif fileName == "userProfile_preferredLevel":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "levelNumber", "levelTitle"])
            userProfile_preferredLevel_DataParse(fileName)

        elif fileName == "userProfile_preferredTitles":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID", "normalizedTitle", "originalSearch"])
            userProfile_preferredTitles_DataParse(fileName)

        elif fileName == "userProfile_ethnicityDistribution":
            with open(f"./results/{fileName}.csv", "w") as rawDataOut:
                dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                dataOut.writerow(["userID","asian","blackAfricanAmerican","hispanic","unknown","white"])
            userProfile_ethnicityDistribution_DataParse(fileName)