FROM python:3.9-alpine

ENV HOST 0.0.0.0
ENV PORT 5001
ENV DEBUG true

COPY . /api
WORKDIR /api

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

EXPOSE 5001

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5001"]
