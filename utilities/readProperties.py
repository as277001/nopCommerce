from configparser import ConfigParser
config = ConfigParser()
config.read("C:\\Users\\TAPAS\\PycharmProjects\\nopCommerce\\Configurations\\config.ini")


class readConfig:

    @staticmethod
    def geturl():
        url=config.get("common-info","baseurl")
        return url

    @staticmethod
    def getusername():
        username = config.get("common-info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common-info", "password")
        return password
