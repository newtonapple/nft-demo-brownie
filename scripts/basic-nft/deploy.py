#!/usr/bin/python3
import os
from brownie import BasicNFT, accounts, network, config
from dotenv import load_dotenv

load_dotenv()


def main():
    wallet = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    BasicNFT.deploy({"from": wallet}, publish_source=publish_source)
