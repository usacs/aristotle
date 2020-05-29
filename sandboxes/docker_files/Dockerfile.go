ARG PROJECT_ROOT

FROM golang:latest
ADD ${PROJECT_ROOT} .

RUN go build -o app
ENTRYPOINT app
# CMD ['go', 'run', '.']