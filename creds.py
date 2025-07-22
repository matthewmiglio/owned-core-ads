import json
from typing import List


class CredsManager:
    def __init__(self):
        self.creds_file_path = r"creds.json"

    def set_creds(self, creds: List[dict]):
        # all the first keys should be username and the second keys should be password
        if not all("username" in cred and "password" in cred for cred in creds):
            raise ValueError(
                "Each credential must contain 'username' and 'password' keys."
            )

        with open(self.creds_file_path, "w") as creds_file:
            json.dump(creds, creds_file, indent=4)

    def get_creds(self) -> List[dict]:
        try:
            with open(self.creds_file_path, "r") as creds_file:
                return json.load(creds_file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError(
                "Credentials file is corrupted or not in valid JSON format."
            )
        
    def get_password(self,username):
        creds = self.get_creds()
        for cred in creds:
            if cred.get("username") == username:
                return cred.get("password")
        print(f'[!] Warning: No password found for username: {username}')
        return None


if __name__ == "__main__":
    creds_manager = CredsManager()
    creds_manager.set_creds(
        [
            {"username": "username_here", "password": "password_here"},
            {"username": "username_here", "password": "password_here"},
            {"username": "username_here", "password": "password_here"},
        ]
    )

    creds = creds_manager.get_creds()
    print(creds)
