from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://lecyohrec1w4m8jbalj9:pscale_pw_Av5oQiypb5Wd9LDHsM5tAfgwVwbepmuQYs5RYh889jX@us-east.connect.psdb.cloud/jovincareers?charset=utf8mb4"

# engine = create_engine("mysql+pymysql://username:password@host/database?charset=utf8mb4")
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append(row._mapping)
  return jobs

def load_job_from_db(id):
   with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
       return None
    else:
       return dict(rows[0])
