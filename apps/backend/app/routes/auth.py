from fastapi import APIRouter

from app.service.auth import login

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/login')
def login_handler(req):
    return login(req)
