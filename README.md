# mlex
MLExchange is software infrastructure that deploys machine learning models to beamline scientists

This is a monorepo designed to hold all of mlexchange in one place. The abstraction layers are seperated out into the following layers:
1. application layer (in /apps), holding ingestion, store/search/rank and deploy apps
2. services layer (in /services) holding ingestion, store/search/rank and deploy services
3. data ( in /data/) local cache for ml data and databases

Additionally, the doc_compose folder contains the different docker compose files neccesary to run either the entirety of MLExchange, or any subset of its functionality.

## Up and Running

The commands to run MLExchange have been written into the Makefile for your convience. The Makefile will both build the docker-compose environments, and launch them. Choose the particular service, application, or any combination of MLexchange that you wish to run and the makefile should handle the complexity for you.

### Prerequisists
You must first install docker. You must also add your user to the docker group (the makefile assumes that you don't need a sudo to run docker)

### Example 1
We want to run the compute service, which allows us to launch containerized ml jobs through an api. Once we've installed docker, we run
```
make run_compute_service
```
The makefile will then do the following. 
1. It will first read out your username id and groupname id and print those to a special file called .env
2. It will then build the docker-compose environment corresponding to compute_service.yml (see doc_compose)
3. It will then run the docker-compose environment (making sure that the launched docker containers use the user/groupname id read from the .env file (without doing this step, any files the docker containers create have root permissions))

You can then access the compute-service at localhost:8080 (type this into your browser bar to see the fast-api documentation)


## Contents

MLExchange is designed to work as an ecosystem, with applications calling services, which themselves access databases, repositories and external services.

One way of understanding MLExchange is by tracing the flow of an ML model through its ecosystem. ![simple_mlexchange_schematic](https://user-images.githubusercontent.com/990372/124203769-4d2ff100-da92-11eb-891a-6a9c6becc51c.png)
An ML reseacher creates a new model, and the model is *ingested* into MLExchange. The model is then indexed in the *store/search/rank* step. The model is then *deployed* either directly into a beamline scientists workflow as a container or jupyter notebook, or within an MLExchange application.

These steps, ingest, store/search/rank, and deploy are broken out into two major abstraction layers, an application layer, which handles the client-facing code to create a user-interface to interact with the ML models, and a service layer, which handles the heavy computational tasks through API calls. Though not complete, the following figure illustrates how these abstraction layers interact: each application has an associated *workflow*. To complete the workflow, the
application accesses various services through API calls, which are also illustrated.
![MLExchange Services V1(1)](https://user-images.githubusercontent.com/990372/124203604-f32f2b80-da91-11eb-82f4-2198389f9318.png)

These abstraction layers are broken out into their own seperate folders within this repo. The outline of this repo is illustrated below.


```
.
├── apps
│   ├── deploy
│   ├── ingest
│   └── mlhub
├── config
├── data
│   ├── db
│   ├── local
│   └── README.md
├── db
│   ├── data_experiments
│   ├── ml_models
│   ├── tags
│   └── users
├── doc_compose
│   ├── compute_service.yml
│   ├── data_service.yml
│   ├── ingest_service.yml
│   ├── mhub_service.yml
│   ├── tag_service.yml
│   └── user_service.yml
├── docs
│   ├── logs
│   └── README.txt
├── Makefile
├── README.md
└── services
    ├── compute
    ├── data
    ├── ingest
    ├── mlhub
    ├── tag
    └── users
```

