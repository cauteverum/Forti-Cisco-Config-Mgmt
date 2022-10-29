from commonFunctions import Common


class Forti: 
    def __init__(self): 
        self.master = "fortinet"
        self.wire = Common(self.master)

    def menuForti(self): 
        print("  Fortinet Menu  ".center(120,"$"))
        
        def innerFunc():
            ch = input("1-All devices in database\n2-Select and Show\n3-Send Script or Command\n4-Get Backup Config file\n(E/e) Exit----> ")
            if (ch == "E" or ch == "e"): 
                self.wire.shutDown()
            else: 
                if (ch == "1"): 
                    self.wire.getAllDevices()
                    innerFunc()

                elif (ch == "2"): 
                    quest = input("1-Select Device\n2-Show Selected Devices\n3-Select All Devices\n4-Remove From Selected\n5-Clear All Selected Devices\n(E/e) Exit----> ")
                    if (quest == "1"):
                        self.wire.selectDevices()
                        innerFunc()
                    elif (quest == "2"): 
                        self.wire.getSelectedDevices()
                        innerFunc()
                    elif (quest == "3"): 
                        self.wire.selectAllDevices()
                        innerFunc()
                    elif (quest == "4"): 
                        self.wire.removeFromSelected()
                        innerFunc()
                    elif (quest == "5"): 
                        self.wire.clearSelected()
                        innerFunc()


                elif (ch == "3"): 
                    quest = input("1-Send Command\n2-Send Script\n\n----> ")
                    if (quest == "1"):
                        self.wire.sendCommand()
                        innerFunc()
                    elif (quest == "2"):
                        self.wire.sendScript()
                        innerFunc()

                elif (ch == "4"): 
                    self.wire.getConfig()
                    innerFunc()

                else: 
                    print("Out of index. ")
                    innerFunc()


        innerFunc()