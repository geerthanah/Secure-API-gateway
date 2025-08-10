from app.auth import create_access_token, verify_token

def test_token_flow():
    token = create_access_token({"sub": "testuser"})
    payload = verify_token(token)
    assert payload["sub"] == "testuser"
