"""
A module for account selection and management
Does stuff like picks the least used account
"""
from typing import List
import os
import json
import random

class AccountManager():
    def __init__(self,account_names:List[str]):
        print(f'AccountManager recieved these account names: {account_names}')
        self.account_names = account_names
        self.json_path = r'account_usage.json'
        
        #make sure json exists, and contains all the given names
        if not os.path.exists(self.json_path):
            self.create_json()
        content = self.read_json()
        existing_names = set(content.keys())
        print(f'These names already exist in the JSON: {existing_names}')
        for name in self.account_names:
            if name not in existing_names:
                content[name] = 0
        with open(self.json_path, 'w') as f:
            json.dump(content, f, indent=4)

    def create_json(self):
        content = {name: 0 for name in self.account_names}
        with open(self.json_path, 'w') as f:
            json.dump(content, f, indent=4)

    def read_json(self):
        with open(self.json_path, 'r') as f:
            return json.load(f)
        
    def reset_json(self):
        os.remove(self.json_path)
        self.create_json()

    def select_least_used_account(self):
        accounts = self.read_json()  # assumes returns a dict like {'acc1': 3, 'acc2': 1, 'acc3': 1}

        #remove accounts that aren't in self.account_names
        accounts = {k: v for k, v in accounts.items() if k in self.account_names}

        if not accounts:
            raise ValueError("⚠ No accounts found in the JSON data.")

        # Find the minimum usage count
        min_count = min(accounts.values())

        # Get all accounts with that minimum count
        least_used_accounts = [acc for acc, count in accounts.items() if count == min_count]

        # Pick one at random among ties
        selected_account = random.choice(least_used_accounts)

        return selected_account
    
    def increment_account_uses(self,account_name:str):
        #make sure it lines up with initalized names
        if account_name not in self.account_names:
            print(f'[!] Warning. You just tried to increment the uses of an account that does not exist in the account manager: {account_name}')
            print(f'Existing names are {self.account_names}')
            return False
        
        #make sure it lines up with the json data
        accounts = self.read_json()
        if account_name not in accounts:
            print(f'[!] Warning. The account {account_name} does not exist in the JSON data.')
            return False
        
        #increment it, rewrite data
        accounts[account_name] += 1
        with open(self.json_path, 'w') as f:
            json.dump(accounts, f, indent=4)



def test():
    #load with new names
    #reset json
    #print starting json content
    test_names = ['acc1', 'acc2', 'acc3']
    manager = AccountManager(test_names)
    manager.reset_json()
    content = manager.read_json()
    print(f'This is the starting json content')
    for k,v in content.items():
        print(f'\t{k}: {v}')
    print('\n')

    #show what selecting from a list of all zeros looks like
    for i in range(10):
        print(f'At this point the least used account is {manager.select_least_used_account()}')
    print('\n')

    #update a random name
    random_valid_name = random.choice(test_names)
    print(f'Attempting to increment a valid name: {random_valid_name}')
    manager.increment_account_uses(random_valid_name)
    content = manager.read_json()
    print(f'This is the updated json content')
    for k,v in content.items():
        print(f'\t{k}: {v}')
    print('\n')

    for i in range(10):
        print(f'At this point the least used account is {manager.select_least_used_account()}')
    print('\n')

    #update a non-existent name
    random_invalid_name = random.choice(test_names) + 'invalid_append_string'
    print(f'Attempting to increment an invalid name: {random_invalid_name}')
    print('This should raise a warning!')
    manager.increment_account_uses(random_invalid_name)
    content = manager.read_json()
    print(f'This is the updated json content')
    for k,v in content.items():
        print(f'\t{k}: {v}')
    print('\n')

if __name__ == '__main__':
    test()