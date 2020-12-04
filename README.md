#Trakt_ETL

-----------------


| **`Documentation`** |
|-----------------|
| [![Documentation](https://img.shields.io/badge/api-reference-blue.svg)](https://trakt.docs.apiary.io/#reference) |


## Ejecucion



#### 
```shell
$ ./pandemia.sh
```

## Descripcion
Trackt es un servicio gratuito que te permite llevar un control de tus series y películas y llevar un registro de lo que has visto.
En este proyecto se realiza la extracción, transformacion y carga de algunos datos pcomo practica educativa

## Herramientas usadas en este repo:

![iam](/images/iam.png)
#### IAM
Con AWS Identity and Access Management (IAM) puede administrar el acceso a los servicios y recursos de AWS de manera segura. Además, puede crear y administrar usuarios y grupos de AWS, así como utilizar permisos para conceder o negar el acceso de estos a los recursos de AWS.

IAM es una característica de su cuenta de AWS que se ofrece sin cargos adicionales. Solo se le cobrará por la utilización de los demás servicios de AWS por parte de sus usuarios(https://aws.amazon.com/es/iam/)

![ec2](/images/ec2.png)
#### EC2
Amazon Elastic Compute Cloud (Amazon EC2) es un servicio web que proporciona capacidad informática en la nube segura y de tamaño modificable. Está diseñado para simplificar el uso de la informática en la nube a escala web para los desarrolladores. La sencilla interfaz de servicios web de Amazon EC2 permite obtener y configurar capacidad con una fricción mínima.(https://aws.amazon.com/es/ec2)


![s3](/images/s3.png)
#### S3
Amazon Simple Storage Service (Amazon S3) es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento líderes en el sector. Gracias a Amazon S3, clientes de todos los tipos y sectores pueden almacenar y proteger cualquier volumen de datos para los más variados fines, como usarlos en lagos de datos, sitios web, aplicaciones móviles, procesos de copia de seguridad y restauración, operaciones de archivado, aplicaciones empresariales, dispositivos IoT y análisis de big data.(https://aws.amazon.com/es/s3/) 

![cloudwatch](/images/cw.png)
#### CloudWatch
Amazon CloudWatch es un servicio de monitorización y observación creado para ingenieros de DevOps, desarrolladores, ingenieros de fiabilidad de sitio (SRE) y administradores de TI. CloudWatch ofrece datos e información procesable para monitorizar sus aplicaciones, responder a cambios de rendimiento que afectan a todo el sistema, optimizar el uso de recursos y lograr una vista unificada del estado de las operaciones. CloudWatch recopila datos de monitorización y operaciones en formato de registros, métricas y eventos, lo cual ofrece una vista unificada de los recursos, las aplicaciones y los servicios de AWS que se ejecutan en servidores locales y de AWS. Puede usar CloudWatch para detectar comportamientos anómalos en sus entornos, definir alarmas, comparar registros y métricas, realizar acciones automatizadas, resolver problemas y descubrir información para mantener sus aplicaciones
en ejecución sin problemas.(https://aws.amazon.com/es/cloudwatch/)


![lambda](/images/aws-lambda.png)
Con Lambda, puede ejecutar código para casi cualquier tipo de aplicación o servicio backend sin tener que realizar tareas de administración. Solo tiene que cargar el código y Lambda se encargará de todo lo necesario para ejecutar y escalar el código con alta disponibilidad. Puede configurar su código para que se active automáticamente desde otros servicios de AWS o puede llamarlo directamente desde cualquier aplicación web o móvil.(https://aws.amazon.com/es/lambda/)


## Modelo
![Base de Datos](/images/trakt_model.png)
