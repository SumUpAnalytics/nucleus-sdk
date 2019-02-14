# Install docker
Follow instructions on https://docs.docker.com/install/ to install docker for your host OS. For Linux users, the post installation steps on https://docs.docker.com/install/linux/linux-postinstall/ MUST be followed to allow docker command to run without sudo.

# Import docker image
* Download the docker image from the download link above. You can copy & paste the link to a web browser or use wget below (note it is IMPORTANT to put the link in single quotes)
```
wget -O nucleus-image.tgz 'DOWNLOAD-LINK'
```

* Load the docker image
```
docker load --input nucleus-image.tgz
```

# Start Nucleus Rest API server container
```
./start-rest-nucleus.sh nucleus-license-file
```

# Connect to Nucleus Rest API server
In your script using Nucleus APIs, set the API host to "http://localhost:50000"
