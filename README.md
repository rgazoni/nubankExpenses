# Nubank expense tracker
 
This is an independent project to track Nubank expenses. To fetch Nubank data we are going to use an unofficial Nubank API, that is going to be explained later. This data will be kept in a database container to be used and analyzed later.
 
The main goal of this project is to put in practice technologies such as containers, docker-compose, python, network between containers and so on.
 
This project is under development...

<br />

## How to set things up
# 
To set up the enviroment:

<code> docker-compose up -d --build</code>

List docker containers and enter inside container <strong>py_nu</strong>:

<code> docker ps </code>

<code> docker exec -it py_nu /bin/bash</code>

Enter the tracker directory and run authentication file helper for more info:

<code> cd tracker</code>

<code> ./authentication.py --help</code>


<div  align="right">
<img height="60" src="https://logodownload.org/wp-content/uploads/2019/08/nubank-logo-2-1532x1536.png">
</div>