// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract BasicNFT is ERC721URIStorage {
    uint256 public tokenCounter;

    constructor() public ERC721("BasicNFT", "BSC") {
        tokenCounter = 0;
    }

    function create(string memory tokenURI) public returns (uint256) {
        uint256 newId = tokenCounter;
        _safeMint(msg.sender, newId);
        _setTokenURI(newId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newId;
    }
}
