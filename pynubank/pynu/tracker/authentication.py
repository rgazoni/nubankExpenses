#!/usr/bin/env python3
'''
WARNING: Be careful, Nubank can block your account for 72 hours if it detects any abnormal behavior! Because of this, avoid sending too many requests. You can also use the MockHttpClient, for more information: https://github.com/andreroggeri/pynubank 

'''

import sys
import argparse
from pynubank import Nubank

def args_requirements():
    parser = argparse.ArgumentParser(description='Nubank authentication')
    parser.add_argument('--cpf', "-c", required=True,
                        help= "Insert your CPF, ONLY numbers!")
    parser.add_argument('--password', "-p",required=True,
                        help= "Put in your password.")
    parser.add_argument('--file', "-f",required=True,
                        help= "Path to your certificate. If you don't have a certificate," +
                        "step by step here: https://github.com/andreroggeri/pynubank/blob/master/examples/login-certificate.md")

    args = parser.parse_args()
    return (args.cpf, args.password, args.file)


if __name__ == '__main__':
    nu = Nubank()
    cpf,password,cert = args_requirements()
    nu.authenticate_with_cert(cpf,password,cert)
#   To see if it's working print your account balance
#   print(nu.get_account_balance())