from fastapi import HTTPException, status


class DBAPICallError(HTTPException):
    def __init__(self, msg: str = "..."):
        super().__init__(
            detail=f"DB api call failed: {msg}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class AdError(HTTPException):
    def __init__(self, detail: str, status_code: int):
        super().__init__(
            detail=detail,
            status_code=status_code,
        )


class AdNotFoundError(AdError):
    def __init__(self, ad_id: int):
        super().__init__(
            detail=f"Ad with id={ad_id} was not found", status_code=status.HTTP_404_NOT_FOUND
        )


class AuthError(HTTPException):
    def __init__(self, detail: str, status_code: int):
        super().__init__(
            detail=detail,
            status_code=status_code,
        )


class TokenNotFoundError(AuthError):
    def __init__(self):
        super().__init__(
            detail="Token was not found",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class TokenIncorrectError(AuthError):
    def __init__(self):
        super().__init__(
            detail="Token incorrect",
            status_code=status.HTTP_403_FORBIDDEN,
        )


class AccessDeniedError(AuthError):
    def __init__(self):
        super().__init__(
            detail="Token denied",
            status_code=status.HTTP_403_FORBIDDEN,
        )
