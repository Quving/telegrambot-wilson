FROM python:3.6

LABEL maintainer="vinh-ngu@hotmail.com"

ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"
ENV OPENSSL_CONF "/etc/ssl/"

# Install PhantomJS
RUN wget "https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2"
RUN tar xvjf $PHANTOM_JS.tar.bz2
RUN rm $PHANTOM_JS.tar.bz2 && mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

# Install Dependencies for T-Bot
WORKDIR /project
ADD . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
