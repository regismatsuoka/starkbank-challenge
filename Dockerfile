FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y cron curl coreutils

RUN curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
| tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
| tee /etc/apt/sources.list.d/ngrok.list \
&& apt update \
&& apt install ngrok

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN ngrok config add-authtoken 2w2fra6Qlu7T3Sn1D82RsM0n5AO_3VRcJgUZUsJqSkiVhSoah

COPY . .

EXPOSE 5000

RUN chmod +x /app/app/misc/boot.sh
RUN chmod +x /app/app/misc/schedule_job.sh
RUN chmod +x /app/app/misc/send_invoice_batch_demo.sh

ENTRYPOINT ["bash", "/app/app/misc/boot.sh"]

