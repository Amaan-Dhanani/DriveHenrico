# API Reference

To allow for easy communication between client and server, this project contains a public api. This api could be used in any setting so long as you follow the protocols of each websocket or http(s) route.

All api endpoints would start with the api subdomain, `api.domain.com`. This allows us to separate concerns between our frontend, database, and backend servers.

## Error Messages
Every time the server fails, either unexpectedly or expectedly within a websocket or http request, the backend sends a message to the client.

### Websocket Error
```json
{
    "error": "Generic Error Info",
    "operation": "some:operation"
}
```

All websocket errors will follow this basic structure, stating the name of the error and the operation.


## Authentication
Most requests require some sort of authentication before "privileged" information or permissions are sent or given. This includes all the requests under the `account` path.

### Websocket Authentication
Whenever opening a websocket connection, the client must first send a auth:token message. This message would contain the following:

```json
{
    "operation": "auth:token",
    "data": {
        "token": "o38..."
    }
}
```

In order to get a token, take a look at the [auth/session](https://github.com/Amaan-Dhanani/DriveHenrico/blob/main/docs/api/auth/index.md) route