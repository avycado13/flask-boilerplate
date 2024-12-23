import secrets
import passlib


class Config:
    APP_NAME = "Plastokens"
    SECRET_KEY = secrets.token_urlsafe()
    SECURITY_PASSWORD_SALT = str(secrets.SystemRandom().getrandbits(128))
    # Change for production env
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS=False
    # Flask Security
    SECURITY_ANONYMOUS_USER_DISABLED=True
    SECURITY_REGISTERABLE = True
    SECURITY_POST_LOGIN_VIEW = "/"
    SECURITY_POST_LOGOUT_VIEW = "/"
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_USERNAME_ENABLE = True
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = False
    # WebAuthn
    SECURITY_WEBAUTHN = True
    SECURITY_WAN_ALLOW_AS_FIRST_FACTOR = True
    SECURITY_WAN_ALLOW_AS_MULTI_FACTOR = True
    SECURITY_WAN_ALLOW_AS_VERIFY = True
    # Two Factor
    SECURITY_TWO_FACTOR_ENABLED_METHODS = ["authenticator"]
    SECURITY_TWO_FACTOR = True
    SECURITY_TOTP_SECRETS = {"1": passlib.totp.generate_secret()}
    SECURITY_TOTP_ISSUER = "Plastokens"
    SECURITY_TWO_FACTOR_REQUIRED=False
