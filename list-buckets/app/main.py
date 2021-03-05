from google.cloud import storage
from flask import Flask, render_template

app = Flask (__name__)

def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    buckets_names = []
    for bucket in buckets:
       buckets_names.append(bucket.name)

    return buckets_names

@app.route('/')
def results():
        my_list = list_buckets()
        return render_template('my_view.html',my_list=my_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
