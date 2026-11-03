# docker compose

Run the DAG API separately.

In a DAG repo, create folders:
- dags/my_forecast_pkg/forecast_dags.py
- dags/.airflowignore
- logs
- plugins
- tests

## .airflowignore
```
my_forecast\.py
test_dag\.py
my_forecast_pkg/forecast_utild\.py
```

## test_dag_imports.py
```py
import sys
from pathlib import Path
from airflow.models import DagBag

# ensure absolute imports work, if not run from repo root
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

def test_my_forecast_dag():
    dagbag = DagBag(
        dag_folder="dags/my_forecast_pkg",
        include_examples=False,
    )
    assert dagbag.import_errors == {}

    dag = dagbag.dags["my_forecast_new"]
    assert dag is not None
    assert dag.dag_id == "my_forecast_new"
    assert "fetch_regions" in dag.task_ids
    assert "forecast" in dag.task_ids

if __name__ == "__main__":
    test_my_forecast_dag()
```

## .env.airflow
```
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=False
# API running on the Windows/LINUX host (bind it to 0.0.0.0:8000)
DAG_API_URL=http://123.45.678.9:8000 # from `ip route show default`
# Run `id -u` in WSL and set it here to avoid root-owned logs/
AIRFLOW_UID=1000
```

## docker-compose.yaml
```yaml
x-airflow-common: &airflow-common
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.0}
  user: "${AIRFLOW_UID:-50000}:0"
  env_file:
    - .env.airflow
  environment: &airflow-env
    AIRFLOW__CORE__EXECUTOR: LocalExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__LOAD_EXAMPLES: "false"
    AIRFLOW__CORE__DAGS_FOLDER: /opt/airflow/dags
    AIRFLOW__WEBSERVER__SECRET_KEY: local-dev-secret-key
    # Lets DAGs import `dags.my_forecast_pkg...`
    PYTHONPATH: /opt/airflow
    # HTTP connections used by the DAGs (my-forecast-api container). from `ip route show default`
    AIRFLOW_CONN_MY_FORECAST_API: ${DAG_API_URL:-http://123.45.678.9:8000}
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
  extra_hosts:
    - "host.docker.internal:host-gateway"
  depends_on:
    postgres:
      condition: service_healthy

services:
  # Optional: only started with `docker compose --profile api up`. By default the
  # API is expected to run on the Windows host (host.docker.internal:8000).
  # If used, set DAG_API_URL=http://my-forecast-api:8000
  my-forecast-api:
    profiles: ["api"]
    build:
      context: ${DAG_API_CONTEXT:-../my-forecast}
    environment:
      # Skips prd and returns local/test results
      IS_LOCAL_TEST_API: "true"
    ports:
      - "127.0.0.1:8000:8000"
    restart: unless-stopped

  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    ports:
      - "127.0.0.1:${POSTGRES_HOST_PORT:-5433}:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U airflow -d airflow"]
      interval: 5s
      timeout: 5s
      retries: 10
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    restart: unless-stopped

  airflow-init:
    <<: *airflow-common
    command:
      - bash
      - -c
      - |
        airflow db migrate &&
        airflow users create \
          --username airflow \
          --password airflow \
          --firstname Local \
          --lastname Admin \
          --role Admin \
          --email airflow@example.com \
        || true
    restart: "no"

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "127.0.0.1:8080:8080"
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 5
    depends_on:
      postgres:
        condition: service_healthy
      airflow-init:
        condition: service_completed_successfully
    restart: unless-stopped

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler
    depends_on:
      postgres:
        condition: service_healthy
      airflow-init:
        condition: service_completed_successfully
    restart: unless-stopped

volumes:
  postgres-db-volume:
```

## requirements-local.txt
```
apache-airflow>=2.8,<3
apache-airflow-providers-http
pytest
pytest-cov
pendulum
```
