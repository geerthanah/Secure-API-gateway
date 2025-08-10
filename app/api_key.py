from fastapi import Header, HTTPException, status

VALID_API_KEYS = {"test-api-key-123", "sample-key-456"}

async def get_api_key_header(x_api_key: str = Header(...)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    return x_api_key
