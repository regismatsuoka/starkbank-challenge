# starkbank-demo
Using the Stark Bank API

This DEMO app aims to demonstrate how to use the Stark Bank API to generate customer billing invoices for payment via Pix and receive webhook calls updating the payment status.

It was built as a docker container.

To build the image and launch the container, use:

* docker-compose up -d --build

The container will produce an automatic batch of 8-12 invoices each 3 hours interval.  However it is possible to send a batch of invoices for processing on a one-off basis by running:

* docker exec -it starkbank-teste-demo /app/app/misc/send_invoice_batch_demo.sh

It is also to send invoice manually through the endpoint https://matsuoka.ngrok.app/api/invoice

Processing returns from Stark Bank are received in the following webhook while the service is active in docker:
https://matsuoka.ngrok.app/api/webhook

## Developer notes for the evaluation team: 

1) This app was made in a very simple way to demonstrate the conceptual understanding of the process. FLASK was used as a web server, which is not recommended for production use. 

2) Any use of "sensitive" data may appear in this github given the "developer" nature of the demonstration project as long I am using the ".env" file approach. Its important to mention that in a production environment, the use of secret management agents in the Cloud is strongly recommended avoiding this security issue.

3) Sensitive data defined in ENV variables file (.env)

If you have any questions, please contact: regis@matsuokadasilva.com

