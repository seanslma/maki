# Dockerfile

## multiline 
https://github.com/moby/moby/issues/1799
```
RUN echo 'All of your\n\
multiline that you ever wanted\n\
into a dockerfile\n'\
>> /etc/example.conf
```
