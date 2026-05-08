from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger

async def catch_exception_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.error(f"An error occurred: {str(exc)}")
        return JSONResponse(status_code=500, content={"message": "An internal server error occurred."})