# Install

## Databricks Community Cloud
It's free for Community Edition: https://community.cloud.databricks.com/login.html

## Locally On Windows
- install jdk: https://www.oracle.com/au/java/technologies/downloads/
- add java `bin` path to system env var `PATH` and check java: `java --version`
- download apache spark: https://spark.apache.org/downloads.html
- unzip to a folder `c:/spark` and add to env var "SPARK_HOME" and add `bin` to env path
- check park version `spark-submit --version`
- install pyspark `pip install pyspark[ml,mllib,sql,pandas_on_spark]`
- copy `winutils.exe` from `https://github.com/cdarlint/winutils/tree/master/hadoop-3.3.5/bin` to `c:/hadoop/bin`
  and set env var `HADOOP_HOME` to `c:/hadoop`???
