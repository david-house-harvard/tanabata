Tanabata - RaccoonGang auto-testing framework
---

This is an initial effort for our auto-testing activities.

Project's goal
===
* For BA's/PM's to have a simple way to create Scenarios.
* For QA engineers to be able to create `BDD`, `Load`, `E2E` tests based on predefined templates.


Installation
===

Local installation
---

    pip install -r requirements.txt


Usage
===

We use a Makefile to run different scenarionas (We plan to use Paver in a future).
We can run DART project tests via Chrome, Firefox, Phantom, Opera, Safari, Edge, IE.

Current set of commands:
```
dart_firefox:
	behave -D instance_url=<STAGE_URL> -D browser=firefox projects/dart/features

dart_chrome:
	behave -D instance_url=<STAGE_URL> -D browser=chrome projects/dart/features

dart_ie:
	behave -D instance_url=<STAGE_URL> -D browser=ie projects/dart/features

dart_edge:
		behave -D instance_url=<STAGE_URL> -D browser=edge projects/dart/features

dart_phantomjs:
	behave -D instance_url=<STAGE_URL> -D browser=phantomjs projects/dart/features

dart_opera:
	behave -D instance_url=<STAGE_URL> -D browser=opera projects/dart/features

dart_safari:
	behave -D instance_url=<STAGE_URL> -D browser=safari projects/dart/features

dart:
	make dart_chrome
	make dart_firefox

dart_docker:
	behave -D instance_url=${STAGE_URL} -D browser=phantomjs -D docker projects/dart/features

courselets_docker:
	behave -D instance_url=${STAGE_URL} -D browser=phantomjs -D docker projects/courselets/features


dart_firefox_local:
	behave -D instance_url=http://localhost:8001 -D browser=firefox projects/dart/features


Basically you can use behave directly:
    behave -D instance_url=<INSTANCE URL>
```


Docker
---

To start develop/tests using docker containers use `envs/local.env.example` as an example for docker envirement:
```
PROJECT=<project_name>
STAGE_URL=<stage_url>
WAIT=<seconds>
USERNAME=<myname>
PASSWORD=<mypassword>
```

We are discussing a posibility to have a separate configuration file for each project. 
ALso we need a simple way to add new project, to add new testing type for the project.
We will have a custom command to add a new project and to choose a custom testing type.

Then run docker via:
```
docker-compose up -d tanabata
```

To run container in developer mode set `BEHAVE_DEBUG_ON_ERROR` to `True` in your project and run container with the following command:

     docker-compose run --service-ports tanabata

To run pre-builded image with a latest code run next:

    docker-compose -f docker-compose-latest.yml up tanabata

Issues
---

Currently we can't run tests started in the docker container against the local deployment.
This is happened due to network isolation - docker container lived in an isolated network so we can't say to test against localhost:8001.
This can be fixed with `network-mode=host` but it will brokes linking to phantomjs container (or any other container linked to tanabata container).




Project aims/TODO's
===

* Use Paver to run different types of tests
* Run project in Docker agains locahost
* Integrate Load/Performance, E2E tests
* Add reporting reature
* Add UI to be able to add/edit scenarios for BA's/PM's
* Add UI to run scenarious (using Jupiter)
