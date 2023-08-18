# Error

## Java gateway process exited before sending its port number

## Caused by: java.net.SocketTimeoutException: connect timed out
Even run Spark in local mode, it communicates over the network just like any other Spark deployment. 
This means that the Firewall can potentially affect the communication between different Spark components.

In local mode, Spark's `driver program` communicates with the `worker threads` over TCP/IP, and the default port used is typically 7077. 

Reason: Firewall blocked the java binary to access the network

Check if there is a firewall blocking the REST API call from the cluster to DIS nodes. 

Try this???
https://stackoverflow.com/questions/60916259/sparkexception-python-worker-failed-to-connect-back-when-execute-spark-action
```
HADOOP_HOME = C:\Hadoop
JAVA_HOME = C:\Java\jdk-11.0.6
PYSPARK_DRIVER_PYTHON = jupyter
PYSPARK_DRIVER_PYTHON_OPTS = notebook
PYSPARK_PYTHON = python
```

try this???
```
SPARK_LOCAL_IP = 127.0.0.1
```

## org.apache.spark.SparkException: Python worker failed to connect back
could not find python
```
PYSPARK_PYTHON = c:/my/folder/to/python.exe
os.environ['PYSPARK_PYTHON'] = 'C:/Users/sma/conda-envs/elchapo/python.exe'
```
This solves the previous issue: **java.net.SocketTimeoutException: connect timed out**
