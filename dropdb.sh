#!/bin/sh

rm -f db.sqlite3
rm -f user_manager/migrations/*.py
touch user_manager/migrations/__init__.py
rm -f asset_portal/migrations/*.py
touch asset_portal/migrations/__init__.py