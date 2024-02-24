from configparser import ConfigParser
config = ConfigParser()
config.read("C:\\Users\\TAPAS\\PycharmProjects\\nopCommerce\\Configurations\\config.ini")

print(config.get("common-info","baseurl"))