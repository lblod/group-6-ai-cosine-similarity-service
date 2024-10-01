# see https://github.com/mu-semtech/mu-python-template for more info
import json
from threading import Thread
from requests import post
from escape_helpers import sparql_escape_string, sparql_escape_uri
from helpers import query, update
import time

def getEmbeddings():
    queryResults = query("""PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX ext: <http://mu.semte.ch/vocabularies/ext/>
SELECT ?sub ?embedding
WHERE {
    VALUES (?embedding) { ("[1,3,3,7]") }
    ?sub a <https://productencatalogus.data.vlaanderen.be/ns/ipdc-lpdc#InstancePublicServiceSnapshot>.
}""")
    # ?sub ext:hasEmbedding ?embedding.

    print("got results")

    # TODO: loop and combine paginated responses

    return [(binding["sub"]["value"], json.loads(binding["embedding"]["value"]))
            for binding in queryResults["results"]["bindings"]]

@app.route("/query-weights")
def queryWeights():
    queryEmbeddings = json.loads(request.args.get('query'))
    dataEmbeddings = getEmbeddings()

    # TODO: find optimal solution

    # TODO: return ?sub (first half of tuple in embeddings)

# TODO: future, maybe in hackathon
@app.route("/query-sentence")
def querySentence():
    # TODO: we _might_ want to implement this.  This will wire services
    # together but this part of AI is more systems programming so that
    # makes sense.
    print("hello")


###################
### FUTURE WORK ###
###################

# FUTURE: ingest embeddings at boot

# embeddings = [
#   # ("http://something/23423", [34,.433,4.43,.34,.34,34.,34534,.3,]), ...
# ]
#
# @app.route("/ingest", methods=["POST"])
# def ingest():
#     embeddings = getEmbeddings()
#     return "Ingested embeddings"

# def ingestWithDelay():
#     time.sleep(5)
#     post("http://localhost/ingest")

# FUTURE: ingestion on startup
# Thread(target = lambda: queryWithDelay()).start()
