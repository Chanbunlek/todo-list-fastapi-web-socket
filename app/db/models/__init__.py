from app.db.session import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from pkgutil import iter_modules
from importlib import import_module

for _, module_name, _ in iter_modules(__path__):
    import_module(f".{module_name}", package=__name__)
