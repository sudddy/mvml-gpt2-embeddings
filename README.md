# mvml-gpt2-embeddings
This repo is responsible for storing the content into a in-memory db(faiss) by creating it as a embedding.


## Deployment

* Create a dockerfile
* Create a requirements.txt file using `pip freeze > requirements.txt' 

* The project can be deployed to AWS EC2 instance using the docker file. 
* Build the docker image using `docker build -t my-app-name .`
* Run the docker using `docker run -p 8080:8080 my-app-name`.
* Deploy the docker image to the AWS Ec2 instance 

[or]

* Save the docker file in the AWS S3 bucket and use it via Aws amplify


## Run locally

* Please clone the repository using the current link - `git clone git@github.com:sudddy/mvml-gpt2-embeddings.git` 
* Please install the dependencies using the command - `pipenv install` (Make sure python is installed - version above 9 )
* `pip3 install pipenv` - if pipenv is not found. 
* After the installations are done, please use "./bootstrap.sh" inside the project folder. 


## API Access

- Once the app is running locally, use `http://192.168.1.78:3567/add` in the postman/insomnia locally. 
- Body json : `{input : "This is the text"}`
- Once the API is hit, it will store the embeddings in the faiss database. 
- This will create a `faiss_index.index` locally (in-memory db) and we can query from it, later. 