from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Importing Flask Routes
from anime_flask.routing.basic.constructors import *
from anime_flask.routing.basic.basic_db import *
from anime_flask.routing.core.planets import *
from anime_flask.routing.core.users import *

# @app.websocket_route('/chat')
# async def websocket_endpoint(websocket: WebSocket):
#     print("chat connection accepted")
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         data= '['+data+']'
#         keys_final = ast.literal_eval(data)
#         a = list(keys_final)
#         audio = Base64decode(a[2])
#         audio_path = "dialogflow\\dialogflow_and_server_response\\User_Response.wav"

#         result = json.loads(detect_intent_stream(a[0], a[1], audio_path, a[3]))

#         await websocket.send_json(result)
#         print(type(data))

# @app.websocket_route('/search_full')
# async def websocket_endpoint(websocket: WebSocket):
#     print("search_full connection accepted")
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(data)
#         full_result = part_id(data)
#         full_result.insert(0, "List of available full names are: ")

#         print(full_result)
#         await websocket.send_json(full_result)

# @app.websocket_route('/search_similar')
# async def websocket_endpoint(websocket: WebSocket):
#     print("search_similar connection accepted")
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(data)
#         full_result = similar_animes(data)
#         full_result.insert(0, "5 similar animes to " + data + " are: ")

#         print(full_result)
#         await websocket.send_json(full_result)

