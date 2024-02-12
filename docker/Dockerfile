FROM debian:bookworm AS base-image
RUN apt-get update && useradd -m --system crackme
RUN apt-get install --assume-yes --no-install-recommends python3

FROM base-image AS compile-image
RUN apt-get install -y --no-install-recommends make git python3-pip &&\
    pip install --upgrade pip

WORKDIR /usr/app
COPY . .
RUN make install

FROM base-image AS production-image
COPY crackme_bin/crackme /usr/local/bin/crackme
RUN chmod 751 /usr/local/bin/crackme
WORKDIR /home/crackme/
# RUN python3 -m site # if this ever breaks to get dist-packages folder.
COPY --from=compile-image /usr/local/lib/python3.10/dist-packages/ /usr/local/lib/python3.10/dist-packages/
COPY --from=compile-image /usr/local/bin/crackme_651db8f78b6aa566ae7234ec /usr/local/bin/

USER crackme
CMD crackme
