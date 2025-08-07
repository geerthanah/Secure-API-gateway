from fastapi import FastAPI, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import verify_token
from app.limiter import rate_limiter
from app.api_key import get_api_key_header
from app.models import init_db

app = FastAPI(title="Secure API Gateway")

@app.on_event("startup")
async def startup():
    init_db()

security = HTTPBearer()

@app.get("/secure-data")
async def secure_data(token: HTTPAuthorizationCredentials = Depends(security),
                      api_key: str = Depends(get_api_key_header)):
    verify_token(token.credentials)
    await rate_limiter(api_key)
    return {"message": "You have accessed a protected route!"}
