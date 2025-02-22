from fastapi import HTTPException, status


def not_accept_406_exc(detail: str):
    not_accept = HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail=detail,
    )
    return not_accept


def unauth_401_exc(detail: str):
    unregistered_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
    )
    return unregistered_exc


def something_wrong_400_exc(detail: str):
    something_wrong_exc = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=detail
    )
    return something_wrong_exc


def user_already_find_202(detail: str):
    accept = HTTPException(
        status_code=status.HTTP_202_ACCEPTED,
        detail=detail,
    )
    return accept
