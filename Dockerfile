FROM python:3

# Install PhantomJS
ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"
RUN wget "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2"
RUN  tar xvjf $PHANTOM_JS.tar.bz2
RUN rm $PHANTOM_JS.tar.bz2
RUN mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin 


# Install Dependencies for T-Bot
RUN pip3 install python-telegram-bot lxml cssselect requests selenium

ADD . /project
WORKDIR /project

CMD ["python3", "wilson.py"]
