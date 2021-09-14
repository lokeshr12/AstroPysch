import config
from WebAutomationTests.global_local.testcases.test_TestScenarioExecution import test_Initiator_global_local


with open("config.py","r") as readConfig:
    localtorun=""
    excelToRun={}
    readConfig=readConfig.read().split("\n")
    excutionSheet=""
    
    for line in readConfig:
        if "locals" in line:
            localtorun="".join(line.split("=")[1].replace('"',""))  
            excutionSheet=localtorun.split(",")
            if config.executionType:
                break
        
    for line in readConfig:
        for i in range(len(excutionSheet)):
            if "execution_"+excutionSheet[i] in line and "locals" not in line:
                excelToRun[excutionSheet[i]]=line.split("=")[1].replace('"',"")
                if config.executionType:
                    break
            
    testExecutor ="test_Initiator_"+localtorun
    globals()[testExecutor](excelToRun[localtorun],localtorun)