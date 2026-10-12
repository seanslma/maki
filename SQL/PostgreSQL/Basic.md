# Basic

- PostgreSQL offers more complex data types than MySQL
- performance: Suited for applications with high volume of both reads and writes

## install
```sh
sudo apt update
sudo apt install -y postgresql postgresql-contrib

sudo systemctl status postgresql
sudo service postgresql start
```

## create test db
```sh
# switch to admin account
sudo -u postgres psql

# create a user
CREATE USER testuser WITH PASSWORD 'testpass';

# create a db
CREATE DATABASE testdb OWNER testuser;

# grant privileges
GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;

\q
```

## test locally
```sh
psql -h localhost -U testuser -d testdb
```

## create a test table
```sh
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    customer VARCHAR(100) NOT NULL,
    product VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

INSERT INTO sales (
    date,
    customer,
    product,
    quantity,
    price
) VALUES
('2026-10-01', 'ABC Energy', 'Electricity Futures', 10, 85.50),
('2026-10-01', 'Queensland Mining', 'Coal Contract', 5, 120.00),
('2026-10-02', 'Retail Power Pty', 'Electricity Futures', 8, 87.25),
('2026-10-02', 'ABC Energy', 'Gas Hedge', 12, 45.75),
('2026-10-03', 'Industrial Corp', 'Electricity Futures', 15, 89.10);
```

## run test
```py
from sqlalchemy import create_engine, text
engine = create_engine(
    'postgresql+psycopg2://testuser:testpass@localhost:5432/testdb'
)
with engine.connect() as conn:
    result = conn.execute(text('SELECT count(*) FROM sales'))
    print(result.scalar())
```
