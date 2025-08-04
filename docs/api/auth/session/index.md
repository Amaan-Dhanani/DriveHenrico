## `WS` /auth/session
Used to create sessions for accounts within the database

### Operations

---

#### session:initiate
Initiate a session

##### Required Data
|name|type|description|
|-|-|-|
|method|string|Method used to initiate the session|
|email|string|Email of the account|
|password|string|Password of the account|

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database


    Client -->> Server: session:initiate
    Note right of Client: method, email, password

    break Session Rejected
        Server -->> Client: session:rejected
    end

    Server -->> Database: Insert Challenge

    Server -->> Client: session:challenge
```

---

#### session:verify:
Verify a session before its usable

##### Required Data
|name|type|description|
|-|-|-|
|challenge_id|Identification of the challenge|
|value|string|Value of the challenge, what's considered the key|

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database


    Client -->> Server: session:verify
    Note right of Client: challenge_id, value

    Server -->> Database: Insert session

    Server -->> Client: session:established
    Note left of Server: token
```