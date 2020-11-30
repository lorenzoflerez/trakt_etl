#!/bin/bash

sudo yum upgrade -y
sudo yum install -y git
sudo yum install -y python3

function instalado() {

#Comprobamos si esta instalado el paquete wget mediante el comando rpm
aux=$(rpm -qa python3)
aux2=$(rpm -qa git)

#Filtramos el resultado del comando rpm mediante un grep y guardamos el resultado.
if `echo "$aux" | grep "python3" >/dev/null`
then
return 1
else
return 0
fi
}

#Llamamos a la función 
instalado $1 &> /dev/null

#Comprobamos el resultado... si da 1 es que esta instalado y si da 0 es que no esta instalado. 
if [ "$?" = "1" ]
then

#Si python esta instala librerias
pip3 -m pip install --upgrade pip3
pip3 install pandas
pip3 install boto3
pip3 install requests
pip3 install simplejson

#Clonamos el repositorio
git clone --branch master https://github.com/lorenzoflerez/trakt_etl.git



#Si no estuviese instalado...por  ejemplo lo instalamos...

else

yum install python3
fi
