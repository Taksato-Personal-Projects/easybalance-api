from core.env_variables import frontend_origin

origins = [
    frontend_origin,
    "http://localhost:3000"
]

methods = [
    "*"
]

headers = [
    "*"
]



cors_args = {
    "allow_origins": origins,
    "allow_credentials": True,
    "allow_methods": methods,
    "allow_headers": headers
}