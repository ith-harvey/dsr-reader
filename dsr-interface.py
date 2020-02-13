import sys
import argparse
from web3 import Web3, HTTPProvider

from pymaker.deployment import DssDeployment
from pymaker.dsr import Dsr
from pymaker import Address

class DsrInterface:
     def __init__(self, args: list, **kwargs):

         self.network = args[0]

         endpoint_uri = f"https://parity0.{self.network}.makerfoundation.com:8545"

         self.web3 = kwargs['web3'] if 'web3' in kwargs else Web3(HTTPProvider(endpoint_uri=endpoint_uri,
                                                                               request_kwargs={"timeout": 10}))

         self.our_address = self.web3.toChecksumAddress(args[1])

         print(f"Account address = {self.our_address}")

         self.web3.eth.defaultAccount = self.our_address
         self.mcd = DssDeployment.from_node(self.web3)

         dsr_client = Dsr(mcd=self.mcd, owner=Address(self.web3.eth.defaultAccount))

         if dsr_client.has_proxy():
            print(f"Has DS-Proxy: True")
            proxy = dsr_client.get_proxy()
            human_readable_balance = "{:,}".format(dsr_client.get_balance(proxy.address).__float__())

            print(f"DS-Proxy address = {proxy.address.address}")
            print(f"DS-Proxy balance = {human_readable_balance}")

         else:
            print(f"Has DS-Proxy: False")

if __name__ == '__main__':
    DsrInterface(sys.argv[1:])
