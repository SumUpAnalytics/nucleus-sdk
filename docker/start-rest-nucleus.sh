#set -x

ver="1.1.1"
if [ "$#" -lt 1 ]; then
    echo "Usage: ./start-rest-nucleus.sh license-file [nucleus-docker-image-version]"
    exit 1
fi

if [ "$#" -ge 1 ]; then
    license_file=$1
fi

if [ "$#" -ge 2 ]; then
    ver=$2
fi

# check if nucleus-api-server container is already running
nucleus_api_server=$(docker ps -a | grep -w nucleus-api-server)
#echo $nucleus_api_server

if [ "$nucleus_api_server" != "" ]; then
    echo "nucleus-api-server container already exists. Please remove it by running"
    echo "docker rm -f nucleus-api-server"
    exit 2
fi

# create nucleus-data volume if not already created
nucleus_data=$(docker volume ls -q | grep -w nucleus-data)
if [ "$nucleus_data" = "nucleus-data" ]; then
    echo "Found docker volume nucleus-data as persistent storage for Nucleus data"
else
    echo "Create docker volume nucleus-data as persistent storage for Nucleus data"
    docker volume create nucleus-data
fi 

# start a new container, copy the license file to the container and start api server
docker run -d --name nucleus-api-server -e "LANG=C.UTF-8" -p 50000:5000 nucleus:$ver
docker cp $license_file nucleus-api-server:/usr/local/lib/python3.6/dist-packages/nucleus/resources/nucleus.lic
docker exec -it nucleus-api-server rest_nucleus
