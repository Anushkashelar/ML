// SPDX-License_Identifier: MIT
pragma solidity
construct crud{
    struct User{
        uint id;
        string name;
    }
    User[] public users;
    uint public nextId = 0;
    function create(string memory name) public{
        users.push(User(nextId, name));
        nextId++
    }

    function read(uint id)view public returns(uint, sting memory){
        for(uint i = 0; i< users.length; i++){
            if(users[i].id== id){
                return(users[i].id, users[i].name)
            }
        }
    }
}