import pickle

class SettingsManager:
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
        return
        print("log")
        print("settings", self.__settings)
        print("options", self.__options)
        
    def get(self, name):
        self.log()
        if name in self.__settings:
            return self.__settings[name]
        if name in self.__options:
            return self.__options[name]
        raise KeyError(f"{name}")

    def changeSettings(self, name, value):
        self.__settings[name] = value

    def set(self, name, value):
        self.__options[name] = value

    def saveSettings(self, fileName):
        with open(fileName, "wb+") as outputFile:
            pickle.dump(self.__settings, outputFile)

    def loadSettings(self, fileName):
        try:
            with open(fileName, "rb") as inputFile:
                self.__settings = pickle.load(inputFile)
            print("settings loaded")
            print(self.__settings)
        except FileNotFoundError:
            self.__settings = {}
