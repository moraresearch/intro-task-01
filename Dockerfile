from python:3.10-alpine3.14

# Install required packages 
RUN pip3 install flask pysqlite3

#Copy python server configuration
COPY ./app/ /opt

#Change default directory 
WORKDIR /opt 

#Set startup web server 
CMD ["python3","/opt/apiServer.py"]