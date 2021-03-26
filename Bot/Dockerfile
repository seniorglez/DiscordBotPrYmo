FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV DISCORD_TOKEN=NTg5NTMyODg5NzI5NzI4NjI4.XQVDSQ.o24gCxQ4GJc_SOPppraXazizkv4
ENTRYPOINT ["python3","discordbot.py"]