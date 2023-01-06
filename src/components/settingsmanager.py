import pickle
import sys

class SettingsManager:
    #FIXME: uses only settings
    def __init__(self, initialSettings = {}, initialOptions = {}):
        """
        Manage settings and options.


        Both settings and options are dictionaries. Settings are immutable and take precedence over options, which are mutable, i.e. if requested key is in both settings and options, the one in settings will be returned.
        """
        self.__settings = initialSettings
        self.__options = initialOptions


    def __contains__(self, X):
        return X in self.__settings or X in self.__options
    
    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, value):
        self.set(item, value)

    def log(self):
        print(self.__settings)
        return
        
    def get(self, name):
        if name in self.__settings:
            return self.__settings[name]
        raise KeyError(f"{name}")



    def set(self, name, value):
        self.__settings[name] = value



    def saveSettings(self, fileName):
        return False
        with open(fileName, "wb+") as outputFile:
            pickle.dump(self.__settings, outputFile)
        print("settings saved into file", file = sys.stderr)



    def loadSettings(self, fileName):
        try:
            with open(fileName, "rb") as inputFile:
                self.__settings = pickle.load(inputFile)
            print("settings loaded from file:", file = sys.stderr)
            print(self.__settings, file = sys.stderr)
        except FileNotFoundError:
            print("file not found while loading settings", file = sys.stderr)
            self.__settings = {}
        except EOFError:
            print("error reading file", file = sys.stderr)
            self.__settings = {}
