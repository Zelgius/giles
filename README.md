# giles
A REST API ILS (library catalog system)

# Early Dev Guide
1. Install Docker
2. Run make dev-env to build developer docker image
3. Develop code, if you want to develop then test by running docker that works,
or you can mount a directory in and dev in the docker. Or mix-n-match
   a. If you don't mount a directory in the code will be in `/giles-dev`. Just
`docker run giles-dev -it -p 8080:8080` to expose port 8080 for testing on your machine.
   b. If you do want to mount your current working directory in then
``` docker run giles-dev -it -v `pwd`:/giles -p 8080:8080``` and your current directory
shoudl be within the docker container under `/giles`
