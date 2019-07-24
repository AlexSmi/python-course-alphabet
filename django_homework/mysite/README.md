# 1. Run docker server

# 2. Run command in terminal 
`$ docker run hello-world`

# 3. Path to homework folder 
`python-course-alphabet/django_homework/mysite`

# 4. Run command in terminal 
`:$ make init`

# 5. After install all docker container will be run, then execute command 
`$ make up`

# 6. At last, you must input correct working url: 
`localhost`
   End

# ERROR
If you use Ubuntu and have error like this: Couldn’t connect to Docker daemon at http+docker://localhost – is it running
How to fix: 
1. Create the docker group.
$ sudo groupadd docker

2. Add your user to the docker group.
$ sudo usermod -aG docker $USER

3. Log out and log back in so that your group membership is re-evaluated or reload system 

4. Verify that you can run docker commands without sudo.
$ docker run hello-world
