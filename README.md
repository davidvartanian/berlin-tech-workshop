# Berlin Tech Workshop - 23.03.2019
This repository contains resources for the Berlin Tech Collaboration Workshop.

## Environment Preparation
1. Make sure you have Python 3.6+ installed ([download here](https://www.anaconda.com/distribution/))
1. Install Pipenv if you don't have it already ([download here](https://pipenv.readthedocs.io/en/latest/)): $`pip install pipenv`
1. Setup IDE ([download PyCharm Community here](https://www.jetbrains.com/pycharm/download/))
1. Setup a Pipenv virtual environment inside PyCharm Community ([instructions here](https://www.jetbrains.com/help/pycharm/pipenv.html))
1. Install Postman ([download here](https://www.getpostman.com/downloads/))
1. Clone this project: $`git clone https://github.com/davidvartanian/berlin-tech-workshop.git`
1. Change to project directory: $`cd berlin-tech-workshop`
1. Run: $`pipenv install`

## What's gonna happen today
We are gonna work with a couple of microservices. The intention is to have a brief experience
of software development the way it happens at any standard workplace nowadays.

We're gonna work with two microservices:
1. Our suggestion is a link shortener, but you can do something else if you already have an idea
1. The second microservice will provide a security layer to the first microservice.

## Microservices in a nutshell
Before microservices software applications contained everything in the same place.
All responsibilities were satisfied at the same place. 
As you can imagine, this approach is very complicated to scale and mantain.

Microservices solve this problem by making the network have more protagonism.
Instead of coding in one place, with microservices the responsibilities or domains are isolated.

Virtualisation became also very important, allowing for containerisation, virtualisation, and deployment be automated. 
This is the discipline that we call DevOps.

## Containerisation
With this term we mean to create a virtual machine with only the resources we need to run one particular thing.
In our case, we're gonna put microservices into containers and make them be connected via a virtual network.
We use Docker to do so.

## Using the API
Let's create a link: POST http://localhost:8010/api/links/
```json
{
	"name": "My Link",
	"token": "abcdef",
	"url": "https://google.de"
}
```

Now let's go to the GraphQL interface: http://localhost:8010/graphql
```
query {
  links {
    id
    name
    token
    url
  }
}
```