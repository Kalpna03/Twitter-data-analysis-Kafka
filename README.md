# Twitter-data-analysis-Kafka

The project relies on the following dependencies:
Kafka-Python:Facilitates interaction with Apache Kafka from Python applications.
Plotly:Enables the generation of dynamic and interactive visualizations of real-time data.
Java Runtime Environment (JRE):Required for running Apache Kafka.



Commands
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

      














.\bin\windows\kafka-server-start.bat .\config\server.properties


 kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tweet
            

kafka-console-consumer.bat --topic tweet --bootstrap-server localhost:9092  --from-beginning

















