FROM python:3.10.13-bullseye

RUN mkdir "/srcs"
WORKDIR "/srcs"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY be be
COPY api api
COPY manage.py manage.py
COPY --chmod=0755 entrypoint.sh entrypoint.sh

ENV PROCESSES=10
ENV THREADS=20
ENV PORT=8000
ENV MAX_REQUEST=5000

CMD ["./entrypoint.sh"]

ENTRYPOINT ["/bin/bash", "-c"]