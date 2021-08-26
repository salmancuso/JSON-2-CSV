import json
import csv
from tqdm import tqdm



def openJsonFile(filePath):
    with open("./results/companyDataResults.csv", "a") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open(filePath) as f:
            data = json.load(f)
            for i in tqdm(range(len(data))):
                try:
                    companyType = data[i]['companyCategories'][0]
                except:
                    companyType = ""
                try:
                    companyRevenue = data[i]['companyRevenue']
                except:
                    companyRevenue = ""
                try:
                    companyID = data[i]['companyID']
                except:
                    companyID = ""
                try:
                    companyEmployeeSize = data[i]['companyEmployeeSize']
                except:
                    companyEmployeeSize = ""
                try:
                    companyName = data[i]['companyName']
                except:
                    companyName = ""
                try:
                    healthRankingDataScore = data[i]['companyRankings']['healthRankingData']['score']
                except:
                    healthRankingDataScore = ""
                try:
                    healthRankingDataRank = data[i]['companyRankings']['healthRankingData']['rank']
                except:
                    healthRankingDataRank = ""
                try:
                    salaryRankingDataScore = data[i]['companyRankings']['salaryRankingData']['score']
                except:
                    salaryRankingDataScore = ""
                try:
                    salaryRankingDataRank = data[i]['companyRankings']['salaryRankingData']['rank']
                except:
                    salaryRankingDataRank = ""
                try:
                    workEnvRankingDataScore = data[i]['companyRankings']['workEnvironmentRankingData']['score']
                except:
                    workEnvRankingDataScore = ""
                try:
                    workEnvRankingDataRank = data[i]['companyRankings']['workEnvironmentRankingData']['rank']
                except:
                    workEnvRankingDataRank = ""
                try:
                    zippiaUnifiedScoresUnifiedSalary = data[i]['companyRankings']['zippiaUnifiedScores']['unifiedSalary']
                except:
                    zippiaUnifiedScoresUnifiedSalary = ""
                try:
                    zippiaUnifiedScoresOverallRank = data[i]['companyRankings']['zippiaUnifiedScores']['overallRank']
                except:
                    zippiaUnifiedScoresOverallRank = ""
                try:
                    zippiaUnifiedScoresUnifiedHealth = data[i]['companyRankings']['zippiaUnifiedScores']['unifiedHealth']
                except:
                    zippiaUnifiedScoresUnifiedHealth = ""
                try:
                    zippiaUnifiedScoresUnifiedWorkEnv = data[i]['companyRankings']['zippiaUnifiedScores']['unifiedWorkEnvironment']
                except:
                    zippiaUnifiedScoresUnifiedWorkEnv = ""
                try:
                    zippiaUnifiedScoresOverallScore = data[i]['companyRankings']['zippiaUnifiedScores']['overallScore']
                except:
                    zippiaUnifiedScoresOverallScore = ""
                try:
                    companyURLs = data[i]['companyURLs']
                except:
                    companyURLs = ""
                try:
                    companyWebsite = data[i]['companyWebsite']
                except:
                    companyWebsite = ""
                try:
                    companyNameAlises = data[i]['companyNameAlises']
                except:
                    companyNameAlises = ""
                try:
                    companyMedianEmployeeSalary = data[i]['companyMedianEmployeeSalary']
                except:
                    companyMedianEmployeeSalary = ""
                try:
                    companyEmployeeProfileEthnicities = data[i]['companyEmployeeProfileSummary']['ethnicities']
                    ethnicDetailsDict = {}
                    for n in range(len(companyEmployeeProfileEthnicities)):
                        companyEmployeeProfileEthnicitiesCount = data[i]['companyEmployeeProfileSummary']['ethnicities'][n]['count']
                        companyEmployeeProfileEthnicitiesEthnicity = data[i]['companyEmployeeProfileSummary']['ethnicities'][n]['ethnicity']
                        ethnicDetailsDict[companyEmployeeProfileEthnicitiesEthnicity] = companyEmployeeProfileEthnicitiesCount
                except:
                    ethnicDetailsDict = ""
                try:
                    companyEmployeeProfileGender = data[i]['companyEmployeeProfileSummary']['genders']
                    genderDetailsDict = {}
                    for n in range(len(companyEmployeeProfileGender)):
                        companyEmployeeProfilegenderCount = data[i]['companyEmployeeProfileSummary']['genders'][n]['count']
                        companyEmployeeProfileGenderType = data[i]['companyEmployeeProfileSummary']['genders'][n]['gender']
                        genderDetailsDict[companyEmployeeProfileGenderType] = companyEmployeeProfilegenderCount
                except:
                    genderDetailsDict = ""

                if "companyCategories" in data[i]:
                    companyCategoriesCount = len(data[i]['companyCategories'])
                    if companyCategoriesCount == 1:
                        for cc in range(companyCategoriesCount):
                            companyCategories = f"{data[i]['companyCategories'][cc]}"
                    elif companyCategoriesCount >0 and companyCategoriesCount > 1:
                        for cc in range(companyCategoriesCount):
                            companyCategories = f"{data[i]['companyCategories'][cc]}, {companyCategories}"

                dataOut.writerow([companyID,
                    companyName,
                    companyEmployeeSize,
                    companyRevenue,
                    companyType,
                    healthRankingDataScore,
                    healthRankingDataRank,
                    salaryRankingDataScore,
                    salaryRankingDataRank,
                    workEnvRankingDataScore,
                    workEnvRankingDataRank,
                    zippiaUnifiedScoresUnifiedSalary,
                    zippiaUnifiedScoresOverallRank,
                    zippiaUnifiedScoresUnifiedHealth,
                    zippiaUnifiedScoresUnifiedWorkEnv,
                    zippiaUnifiedScoresOverallScore,
                    companyURLs,
                    companyWebsite,
                    companyNameAlises,
                    ethnicDetailsDict,
                    genderDetailsDict, 
                    companyCategories,
                    companyMedianEmployeeSalary])

                




if __name__ == "__main__":
    with open("./results/companyDataResults.csv", "w") as rawDataOut:
        dataOut = csv.writer(rawDataOut, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dataOut.writerow(["companyID,", "companyName,", "companyEmployeeSize,", "companyRevenue,","companyType", "healthRankingDataScore,", "healthRankingDataRank,", "salaryRankingDataScore,", "salaryRankingDataRank,", "workEnvRankingDataScore,", "workEnvRankingDataRank,", "zippiaUnifiedScoresUnifiedSalary,", "zippiaUnifiedScoresOverallRank,", "zippiaUnifiedScoresUnifiedHealth,", "zippiaUnifiedScoresUnifiedWorkEnv,", "zippiaUnifiedScoresOverallScore,", "companyURLs,", "companyWebsite,", "companyNameAlises,", "ethnicDetailsDict,", "genderDetailsDict", "companyCategories", "companyMedianEmployeeSalary"])
    
    openJsonFile('./rawData/CompanyDataDump3.json')