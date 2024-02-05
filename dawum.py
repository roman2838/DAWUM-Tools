import requests
from datetime import datetime
import matplotlib.pyplot as plt

class DawumTools:
    def __init__(self):
        self.DAWUM_API_URL = 'https://api.dawum.de/'
        self.connector = requests.get(self.DAWUM_API_URL)
        self.data = self.connector.json()
        print(self.connector)
    def GetInstitutes(self):
        print(self.connector)
        InstituteList = []
        for element in self.data['Institutes'].values( ):
            InstituteList.append(element['Name'])
        return InstituteList
    def GetParties(self):
        PartyList = []
        for element in self.data['Parties'].values( ):
            PartyList.append(element['Shortcut'])
        return PartyList
    def CreateHistoryGraph(self, i_party, i_institute, i_parliament):
            x = []
            y = []
            plt.style.use('fivethirtyeight')
            for survey in self.data['Surveys'].values():
                date_object = datetime.strptime(survey['Date'], "%Y-%m-%d" )
                day = date_object.day
                month = date_object.month
                year = date_object.year
                if self.data['Institutes'][survey['Institute_ID']]['Name'] == i_institute:
                    if self.data['Parliaments'][survey['Parliament_ID']]['Shortcut'] == i_parliament:
##                      print(survey['Institute_ID'])
                        for party in survey['Results']:
                            if self.data['Parties'][party]['Shortcut'] == i_party:
##                               print("Datum:{}.{}.{}: Institut: {}, Party: {}, Result: {}".format(day, month, year, survey['Institute_ID'], party,survey['Results'][party]) ) 
                               x.append(f"{day}.{month}.{year}")
                               y.append(survey['Results'][party])

            
##            for i in range(1,100):
####                print("{} : {}".format(x[i], y[i]))
            plt.plot(x,y)
            plt.show()
##    def get_data(institute, party):


