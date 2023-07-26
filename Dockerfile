FROM python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 3333
CMD python server.py
