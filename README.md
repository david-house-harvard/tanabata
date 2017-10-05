Tanabata - RaccoonGang auto-testing framework
---


This is an initial effort for our auto-testing activities



Installation
===

    pip install -r requirements.txt


Usage
===


    make love

OR

    behave -D instance_url=<INSTANCE URL>

Docker
===

To start develop using docker container copy `envs/local.env.example` into
`envs/local.env.example` and set required staging url.
Then run docker via `docker-compose up tanabata`


To run pre-builded image with a latest code run next:


    docker-compose -f docker-compose-latest.yml up tanabata
