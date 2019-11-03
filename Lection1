Tasks
===
### 1. sha256 sum
* create file with name `docker` with following content
```
docker-shmoker
```
* take sha256 checksum from file
#### Answer: sha256  checksum of mentioned file

### 2. ubuntu
* run ubuntu container in interactive mode
* take sha256 checksum of file `/etc/debian_release`
#### Answer: sha256 checksum of `/etc/debian_release`

### 3. centos
* run centos container in interactive mode
* find out which binary can used to take sha256 checksum
* take sha256 checksum of that binary
#### Answer: sha256 checksum of centos `sha256` binary

### 4. alpine
* run alpine container
* check content `/etc/passwd`

#### Answer:
* one-liner command that print number of records in `/etc/passwd` in alpine container.
* command should be run from docker host itself and begin from `docker run`

### 5. busybox
* run busybox container
* find out size of / filesystem
#### Answer:
* one-liner docker command that prints size of busybox `/` container
* command should be run from docker host itself and begin from `docker run`

### 6. hello-world
* run hello-world container
* find out which binary executes during container run
* take sha256sum that binary
#### Answer:
* sha256 checksum of main `hello-world` container binary
* yes, that's not possible to get inside `hello-world`


### 7. apache
* run httpd container in background
* run bash session inside this container (`exec` utility)
* find out which flavor of linux was used as base for httpd image
* find out which processes are running inside container `ps aux`
#### Answer:
* output of `ps aux | grep httpd`
* yeah, there's no `ps` command in `httpd` image by default.

### 8. compile c program
#### Source code:
```
int main () {
  puts("Hello, world!");
  return 0;
}
```
* run blank centos container, interactive
* install `gcc`, `make` - use yum
* create `/hello.c` file
* build it `make hello`
* run it `/hello`
* **take sha256sum**
* detach from container
* run blank ubuntu container, interactive
* do same in ubuntu ( note, you may need to install text editor also)
* build it, run it
* **take sha256sum**
* detach from container
* see last 2 containers (read about ps --last keys)
* check last 2 container sizes ( refrehs ps -s keys)
* read about `docker cp` command
* copy `/hello` file from each container locally into `hello_centos`, `hello_ubuntu`
* copy `hello_centos` into ubuntu container
* copy `hello_ubuntu` into centos container
* run both commands, to check if works
* optionally: copy, run both commands in busybox, alpine containers
*

#### Answer:
* sha256 sum of hello binary in ubuntu
* sha256 sum of hello binary in centos
