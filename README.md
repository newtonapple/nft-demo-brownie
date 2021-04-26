# nft-demo-brownie
A simple NFT demo using Brownie.

https://metamask.io/


## Setup:
### Setup `.env`:
```
cp .env.example .env
```
Follow instruction in .env to filling the necessary environment variables.

### Metamask:
* Install: https://metamask.io/
* create a new wallet.
* switch network to Rinkeby Test Network.
* fund your wallet tweeting your public wallet address & copying the tweet to https://faucet.rinkeby.io/

### IPFS
* Install `ipfs` command line: https://docs.ipfs.io/install/command-line/#official-distributions.
* Start IPFS daemon by running:
  * `ipfs daemon`
* Upload image asset to IPFS:
  * `curl -X POST -F file=@assets/img/lion.png 'http://localhost:5001/api/v0/add'`
  * take note of `Hash` field in the JSON response.
  * The IPFS image URL would be: https://ipfs.io/ipfs/[Hash]?filename=lion.png
* Upload JSON metadata to IPFS:
  * replace the `image` field in [assets/nft-metadata/lion.json](assets/nft-metadata/lion.json) with the IPFS image URL returned from previous step.
  * `curl -X POST -F file=@assets/nft-metadata/lion.json 'http://localhost:5001/api/v0/add'`
  * take note of `Hash` field in the JSON response.
  * The IPFS NFT `tokenURI` would be: https://ipfs.io/ipfs/[Hash]?filename=lion.json
  * replace the `token_uri` in [script/basic-nft/create.py](script/basic-nft/create.py) with the `tokenURI` from previous step.

Install brownie:
```
pip install eth-brownie
```

## Deploy BasicNFT Smart Contract to Rinkeby testnet:
```
 brownie run scripts/basic-nft/deploy.py --network rinkeby
 ```


 ## Create a BasicNFT on Rinkeby testnet:
 ```
 brownie run scripts/basic-nft/create.py --network rinkeby
 ```