# Nameko examples for Pygotham 2016 talk

## Installation with PIP

```sh
pip install -r requirements.txt
```

## Running services

Services 2 - 5 require a [rabbitmq server](https://www.rabbitmq.com/download.html) running at `amqp://guest:guest@localhost`

```sh
nameko run service_{x}
```
