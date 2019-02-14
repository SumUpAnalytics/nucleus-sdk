#set -x

ver="0.0.3"
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

# create nucleus-mysql-data volume if not already created
nucleus_mysql_data=$(docker volume ls -q | grep -w nucleus-mysql-data)
#echo $nucleus_mysql_data
if [ "$nucleus_mysql_data" = "nucleus-mysql-data" ]; then
    echo "Found docker volume nucleus-mysql-data as persistent storage for Nucleus data"
else
    echo "Create docker volume nucleus-mysql-data as persistent storage for Nucleus data"
    docker volume create nucleus-mysql-data
fi 

# start a new container, copy the license file to the container and start api server
docker run -d --name nucleus-api-server -e "PYTHONIOENCODING=utf8" -v nucleus-mysql-data:/var/lib/mysql -p 50000:5000 nucleus:$ver
docker cp $license_file nucleus-api-server:/usr/local/lib/python3.5/dist-packages/nucleus/resources
docker exec -it nucleus-api-server rest_nucleus
