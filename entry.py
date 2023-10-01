from lomond import WebSocket
import json
from loguru import logger

JSON_OUTPUT = []

false = False

def main():
    websocket_addr = input("Enter ws address: ")
    websocket = WebSocket(websocket_addr)

    id_num = 1
    last_json = None
    poll_interval = 0

    def set_debuger_msg(ws, i):
        json = {"id":i,"method":"Overlay.setPausedInDebuggerMessage","params":{"message":"Paused in debugger"}}
        JSON_OUTPUT.append(json)
        ws.send_json(json)

    def get_properties(ws, i, property_id):
        json = {"id":i,"method":"Runtime.getProperties","params":{"objectId":property_id,"ownProperties":false,"accessorPropertiesOnly":false,"nonIndexedPropertiesOnly":false,"generatePreview":true}}
        JSON_OUTPUT.append(json)
        ws.send_json(json)

    def set_debugger(ws, i):
        json = {"id":i,"method":"Debugger.stepInto","params":{"breakOnAsyncCall":False,"skipList":[]}}
        JSON_OUTPUT.append(json)
        ws.send_json(json)

    for event in websocket.connect(poll=0.3):
        print(f"Event: {event.name}")
        if event.name == 'poll':
            if poll_interval == 1:
                set_debugger(websocket, id_num)
                id_num += 1
            elif poll_interval == 2:
                set_debuger_msg(websocket, id_num)
                id_num += 1
            elif poll_interval == 3:
                for scope in last_json[0]["scopeChain"]:
                    get_properties(websocket, id_num, scope["object"]["objectId"])
                    id_num += 1
                poll_interval = 0
            poll_interval += 1
        elif event.name == 'text':
            # poll_interval = 0
            JSON_OUTPUT.append(event.json)

            last_json = event.json

            if event.json.get("method") == "Debugger.paused":
                ...
        else:
            print("Unkown event type: {}".format(event.name))


try:
    main()
except Exception as ex:
    logger.exception(ex)
except:
    print("Brina")
finally:
    with open('output.json', 'w') as f:
        json.dump(JSON_OUTPUT, f, indent=4)

