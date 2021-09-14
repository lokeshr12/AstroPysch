from PythonFramework.utilities.KeywordAutomation import KeywordAutomation

def test_Initiator_global_local(executionSheet,localtorun):
    print(localtorun)
    print("reached test Initiator",executionSheet)
    try : 
        mkskwdTest = KeywordAutomation(True,executionSheet,localtorun)
    
    