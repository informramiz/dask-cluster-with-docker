# Goal

The goal is to provision a docker container such that it is able to run a dask-cluster. 

Of course this won't start multiple machines in the cloud and run a actual real cluster but instead it uses docker-compose and docker to emulate this situation. You need both installed on your system before you can proceed.

* [How to install docker](https://docs.docker.com/engine/installation/)
* [How to install docker-compose](https://docs.docker.com/compose/install/)

This should be straightforward on all linux and osx systems. Windows users are probably better off running a virtual machine with a linux distro but theoretically docker and docker-compose should also run native on Windows.

## Run

Execute following command to run

```
./bootstrap.sh
```

After running this command, following output is generated.

```
worker_1          | INFO:__main__:======= TESTING DASK CLUSTER ========
dask-scheduler_1  | distributed.scheduler - INFO - Receive client connection: Client-8eb8c2e2-b948-11e7-8001-0242ac130003
worker_1          | INFO:__main__:Submitting job...
worker_1          | INFO:__main__:Result:
worker_1          | col1    49995000
worker_1          | col2    49995000
worker_1          | col1      125250
worker_1          | col2     4884249
worker_1          | dtype: int64
worker_1          | INFO:__main__:======= CLUSTER OK ========
```


## References
* [dockerfile reference](https://docs.docker.com/engine/reference/builder/)
* [dask distributed](http://distributed.readthedocs.io/en/latest/install.html)
* [dask](https://dask.readthedocs.io/en/latest/install.html)
* [psutil (dask dependency)](https://pythonhosted.org/psutil/)