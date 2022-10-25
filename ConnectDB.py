import os

import psycopg2
conn = psycopg2.connect(database="latzqtwv",
                        user="latzqtwv",
                        password=os.environ.get("POSTGRESQL_PWD", ""),
                        host="mouse.db.elephantsql.com",
                        port="5432"
                        )
print("Database connected...")
