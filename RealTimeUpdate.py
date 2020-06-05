from flask import Flask, render_template, Response
from pykafka import KafkaClient

app = Flask(__name__)

@app.route('/topic/<topicname>')
def get_topics(topicname):
    client = KafkaClient(hosts='127.0.0.1:9092')
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data: {0} \n \n'.format(i.value.decode())
    return Response(events(),mimetype="text/event-stream")









if(__name__ == "__main__"):
    app.run(debug=True)