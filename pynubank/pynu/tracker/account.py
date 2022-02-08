import sys
import argparse
from pynubank import Nubank
from datetime import date

RECEIVED_TRANSACTION = 'Transferência recebida'

class Account(Nubank):

    def __init__(self, cpf, password, path_cert):
        super().__init__()
        
        self.cpf = cpf
        self.password = password
        self.path_cert = path_cert

        #TODO change later to an individual class  -- RECEIVED_TRANSACTION
        self.amount = int()
        self.name = str()
        self.category = str()

        self._authenticate_with_cert()

    def _authenticate_with_cert(self):
        super().authenticate_with_cert(self.cpf, self.password, self.path_cert) 

    def _todays_data(self, request):
        index=0
        data = list()
        #control flow here
        if(request == 'account'):
            raw_data = super().get_account_feed()
        current_day = str(date.today())
        while raw_data[index]['postDate'] == current_day:
            data.append(raw_data[index])
            index += 1
        return data

    def _received_transaction(self, data): #data is a dictionary
        self.category = data['title']
        self.amount = data['amount']
        self.name = data['originAccount']['name']
        #TODO call DB class to store transaction

    def account_data(self):
        data = self._todays_data('account')
        for index in range(0, len(data)):
            if(data[index]['title'] == RECEIVED_TRANSACTION):
                self._received_transaction(data[index])
