from fastapi import Header, HTTPException

def get_current_user(authorization: str = Header(...)):
    if authorization != "Bearer secret-token":
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return "admin"
