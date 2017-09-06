# Datarevenue Code Challenge

Congratulations for making it to the Code Challenge. In this challenge the goal is to provision a docker container sucht that it is able to run a dask-cluster. This might sound complicated but it the challenge comes with a run configuration already. 

Of course this won't start multiple machines in the cloud and run a actual real cluster but instead it uses docker-compose and docker to emulate this situation. You need both installed on your system before you can proceed (We use this tools on a daily basis at datarevenue so it won't be in vain).

* [How to install docker](https://docs.docker.com/engine/installation/)
* [How to install docker-compose](https://docs.docker.com/compose/install/)

You only have to provision the docker container by implementing the dockerfile and run the bootstrap bash script. The solution can be expressed in as little as 5 lines.

This should be straightforward on all linux and osx systems. Windows users are probably better off running a virtual machine with a linux distro but theoretically docker and docker-compose should also run native on Windows.


## Notes
- This should take you between 20-60 minutes
- Use python3
- The dockerfile should inherit from `ubuntu:16.04` 
- You are not allowed to change any files.
- execute bootstrap.sh and email us the output along with your solution.


## References
* [dockerfile reference](https://docs.docker.com/engine/reference/builder/)
* [dask distributed](http://distributed.readthedocs.io/en/latest/install.html)
* [dask](https://dask.readthedocs.io/en/latest/install.html)
* [psutil (dask dependency)](https://pythonhosted.org/psutil/)