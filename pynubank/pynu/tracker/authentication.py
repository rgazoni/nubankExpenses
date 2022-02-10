#!/usr/bin/env python3
'''
WARNING: Be careful, Nubank can block your account for 72 hours if it detects any abnormal behavior! 
Because of this, avoid sending too many requests.
You can also use the MockHttpClient, for more information: https://github.com/andreroggeri/pynubank 

'''

import sys
import argparse
from pynubank import Nubank
from account import Account

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
    
    cpf,password,path_cert = args_requirements()
    nu = Account(cpf,password,path_cert)
    nu.feed_todays_data('account')