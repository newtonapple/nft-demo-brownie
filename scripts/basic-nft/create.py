#!/usr/bin/python3
from brownie import BasicNFT, accounts, network, config

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"
token_uri = "https://ipfs.io/ipfs/Qmd43BkzrobSXoxrkzV74yZ5sVqkUbwdqQW3EbFB3h7rHt?filename=lion.json"

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    nft = BasicNFT[len(BasicNFT) - 1]
    token_id = nft.tokenCounter()
    transaction = nft.create(token_uri, {"from": dev})
    transaction.wait(1)
    print("You can view your NFT at {}".format(OPENSEA_FORMAT.format(nft.address, token_id)))
    print('Please give up to 20 minutes, and hit the "refresh metadata" button...')
