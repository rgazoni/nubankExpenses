'''
For more information about Nubank API, link: https://github.com/andreroggeri/pynubank

'''
import sys
import argparse
from pynubank import Nubank
from datetime import date

#Account titles
TRANSFER_RECEIVED = 'Transferência recebida'
TRANSFER_SENT = 'Transferência enviada'
DEBIT_PURCHASE = 'Compra no débito'
PAYMENT_EFFECTED = 'Pagamento efetuado'
DEPOSIT_RECEIVED = 'Depósito recebido'

class Account(Nubank):

    def __init__(self, cpf, password, path_cert):
        super().__init__()
        
        self.cpf = cpf
        self.password = password
        self.path_cert = path_cert

        self.type_request = None

    def _authenticate_with_cert(self):
        #TODO check if self.cpf in only numbers
        #TODO check if self.path_cert is a real path
        super().authenticate_with_cert(self.cpf, self.password, self.path_cert) 

    def _request_validation(self, request):
        try:
            if(not(request.lower() == 'account' or request.lower() == 'card')):
                raise ValueError('Invalid request')
        except ValueError:
            print("A wrong key was passed as request. A request can be " 
            + "either an account data or credit card data.\n" +
            "Choose between:  'account'  or  'card'")
            exit(ValueError('ValueError: Invalid request parameter'))
        else:
            self.type_request = request.lower()

    def _todays_data(self):
        index=0
        data = list()
        raw_data = super().get_account_feed() if self.type_request == 'account' else super().get_card_feed()

        current_day = str(date.today())
        while raw_data[index]['postDate'] == current_day:
            data.append(raw_data[index])
            index += 1
        return data

    def _transfer_received(self, data):
        title = 'Transfer Received'
        amount = data['amount']
        name = data['originAccount']['name']
        date = data['postDate']
        print(f"Title: Transfer Received\nName: {name}\nAmount: {amount} reais\nDate: {date}\n --------------------------------")
        #TODO call DB class to store transaction

    def _transfer_sent(self, data):
        rawStr = data['detail']
        title = 'Transfer Sent'
        amount = rawStr[rawStr.find(u'\xa0'):].replace(',','.')
        name = rawStr[0:rawStr.find(' - ')]
        date = data['postDate']
        print(f"Title: Transfer sent\nName: {name}\nAmount:{amount} reais\nDate: {date}\n --------------------------------")
        #TODO call DB class to store transaction

    def _debit_purchase(self, data):
        rawStr = data['detail']
        title = 'Debit Purchase'
        amount = data['amount']
        date = data['postDate']
        name = rawStr[0:rawStr.find(' -')]
        print(f"Title: Debit Purchase\nName: {name}\nAmount: {amount} reais\nDate: {date}\n --------------------------------")
        #TODO call DB class to store transaction

    def _payment_effected(self, data):
        title = 'Payment Purchase'
        name = data['detail']
        date = data['postDate']
        amount = data['amount']
        print(f"Title: Payment Effected\nName: {name}\nAmount: {amount} reais\nDate: {date}\n --------------------------------")
        #TODO call DB class to store transaction

    def _deposit_received(self, data):
        title = 'Deposit Received'
        amount = data['amount']
        date = data['postDate']
        name = 'TransferInEvent'
        print(f"Title: Deposit Received\nName: {name}\nAmount: {amount} reais\nDate: {date}\n --------------------------------")
        #TODO call DB class to store transaction

    def feed_todays_data(self, request):
        '''
        The request can be either an account data or 
        credit card data (isn't implemented yet)
        '''
        self._request_validation(request)

        self._authenticate_with_cert()

        data = self._todays_data()
        for index in range(0, len(data)):

            if(self.type_request == 'account'):
                if(data[index]['title'] == TRANSFER_RECEIVED):
                    self._transfer_received(data[index])
                elif(data[index]['title'] == TRANSFER_SENT):
                    self._transfer_sent(data[index])
                elif(data[index]['title'] == DEBIT_PURCHASE):
                    self._debit_purchase(data[index])
                elif(data[index]['title'] == PAYMENT_EFFECTED):
                    self._payment_effected(data[index])
                elif(data[index]['title'] == DEPOSIT_RECEIVED):
                    self._deposit_received(data[index])
            
            else: #credit card request
                print('Nothing implemented yet')
                pass