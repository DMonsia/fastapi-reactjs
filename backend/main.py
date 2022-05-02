import email
import fastapi as _fastapi

import fastapi.security as _security
import sqlalchemy.orm as _orm

import services as _services
import schemas as _schemas
import database as _db

app = _fastapi.FastAPI()


@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_database),
):
    db_user = await _services.get_use_by_email(email=user.email, db=db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")
    return await _services.create_user(user, db)
