from app.utils.jwt_utils import create_jwt

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    user_data = {"username": "ahmed"}  # Example user data
    token = create_jwt(user_data)
    print(f"Generated Token: {token}")
