FROM python:3-alpine
LABEL name scabi
LABEL src "https://github.com/remiflavien1/scabi"
LABEL dockerfile fractalizers
RUN pip3 install scabi
ENTRYPOINT ["scabi"]
CMD ["-h"]