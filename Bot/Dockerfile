FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV DISCORD_TOKEN=$DISCORD_TOKEN
ENTRYPOINT ["python3","discordbot.py"]