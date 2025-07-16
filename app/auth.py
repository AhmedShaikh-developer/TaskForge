from fastapi import Request, HTTPException
from app.utils.jwt_utils import decode_jwt
import logging

logger = logging.getLogger("uvicorn.error")

async def auth_middleware(request: Request, call_next):
    try:
        logger.info(f"AuthMiddleware called for path: {request.url.path}")
        if request.url.path in ["/", "/docs", "/openapi.json"]:
            response = await call_next(request)
            return response

        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=403, detail="Authorization header missing or invalid")

        try:
            token = token[len("Bearer "):]
            user = decode_jwt(token)
            request.state.user = user
            logger.info(f"Authenticated user: {user}")
        except Exception as e:
            logger.error(f"Token error: {e}")
            raise HTTPException(status_code=403, detail=f"Token error: {str(e)}")

        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Middleware exception: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

