# Vueling-scrapper

Vueling's web scrapper to notify when the slider has changes to check if there are new offers.

Notice that we are using ``` seleniarm ``` docker image in order to make it work in a M1 Macbook chip. You can change it to normal selenium image.

For more information please check these links out:

[Selnium problems with M1 processor](https://github.com/SeleniumHQ/docker-selenium/issues/1076)

[Seleniarm Docker image in Dockerhub](https://hub.docker.com/r/seleniarm/hub/tags?page=1&ordering=last_updated)

You can set the options via env file or you can input them running first:

``` docker-compose up chrome ```

and then

``` docker-compose run --rm app ```
