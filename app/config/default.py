import os

config = {
    # Google oauth2 web client config
    "google_client_id": "254515040416-vf53ucek5sgae1th84ss62mn09tls8o9.apps.googleusercontent.com",
    "google_client_secret": "E-Lphy5Fz4oU44mV_eBeEBte",

    # JWT Token Secret config
    "token_secret": os.environ.get('SECRET_KEY') or 'E-Lphy5Fz4oU44mV_eBeEBte'
}
