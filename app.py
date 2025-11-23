from dash import Dash

from index import lyt
from callbacks import callbacks_master

app = Dash(__name__)

app.layout = lyt

callbacks_master(app)

server = app.server

if __name__=="__main__":
    app.run(debug=True, port="8050") # for local development
    # app.run()