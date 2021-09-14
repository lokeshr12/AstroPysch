import os


class KeywordAutomation:
    
    __TestPackage = ""
    __TestExecution = ""
    local = None
    
    
    
    
    def __init__(self,GenerateRepository, CommaSeparatedSheetName,localtorun,BrowserName="",):
        self.__TestPacakage="./WebAutomationTests/"+localtorun
        self.local=localtorun
        self.__TestExecution=self.__TestPacakage+os.path.sep+"ExecutionController.xlsx"
        
        
        
    