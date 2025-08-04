# `WS` /account/link

Linking student accounts to parents or classes, has to do with invite generation as well.


### Operations

---

#### parent:create_invite
Parent wants to create an invite

##### Required Data
|name|type|description|
|-|-|-|
|email?|string|Email of the student, if present, and student is already registered, send an email to the student|

##### Ok Response
|name|type|description|
|-|-|-|
|invite_id|string|Id of the newly created invite|
|invite_code|string|Code of the new invite, can be used to join the invite|


```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: creation:failed
    end

    break User not parent
        Server -->> Client: creation:failed
    end

    Server -->> Database: invite.insert
    Server -->> Client: invite:created
    Note left of Server: invite_id:str, invite_code:str
```

---

#### parent:revoke_invite
Parent wants to revoke an invite

##### Required Data
|name|type|description|
|-|-|-|
|invite_id|string|Identification of the invite|

##### Ok Response
|name|type|description|
|-|-|-|
|invite_id|string|Id of the deleted invite|

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: revoke:rejected
    end

    break User not parent
        Server -->> Client: revoke:rejected
    end

    break Invite doesn't exist
        Server -->> Client: revoke:rejected
    end

    break Parent didn't create the invite
        Server -->> Client: revoke:rejected
    end

    Server -->> Database: invite.delete
    Server -->> Client: revoke:success
    Note left of Server: invite_id:str
```

---

#### student:link
Operation used whenever a student wants to use an invite code to link to either a parent or a class

##### Required Data
|name|type|description|
|-|-|-|
|invite_code|string|Code of the invite, given by the parent|

##### Ok Response
No Data

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: link:rejected
    end

    break User not student
        Server -->> Client: link:rejected
    end

    break Invite doesn't exist
        Server -->> Client: link:rejected
    end

    break Student already linked to target of invite
        Server -->> Client: link:rejected
    end

    Server -->> Database: invite.add(user)

    Server -->> Client: link:success
```

---

#### student:unlink
Operation is used whenever a student wants to unlink from either a parent or a class

##### Required Data
|name|type|description|
|-|-|-|
|type|Literal["class", "parent"]|What the user wants to unlink from|

##### Ok Response
No Data

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: unlink:rejected
    end

    break Type invalid
        Server -->> Client: unlink:rejected
    end

    break User not student
        Server -->> Client: unlink:rejected
    end

    break Type not already linked
        Server -->> Client: unlink:rejected
    end

    Server -->> Database: student.remove(type)
```

---

#### teacher:create_class
This operation is used whenever a teacher wants to create a class


##### Required Data
|name|type|description|
|-|-|-|
|name|string|Name of the class|

##### Ok Response
|name|type|description|
|-|-|-|
|class_id|string|New class ID|

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: creation:unsuccessful
    end

    break User is not teacher
        Server -->> Client: creation:unsuccessful
    end

    Server -->> Database: class.insert

    Server -->> Client: class:created
    Note left of Server: class_id:str
```

---

#### teacher:regenerate_code
Operation is used whenever a teacher wants to refresh a classes code

##### Required Data
|name|type|description|
|-|-|-|
|class_id|string|Id of the class|

##### Ok Response
|name|type|description|
|-|-|-|
|class_code|string|New class code|

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    break User not authenticated
        Server -->> Client: regenerate:rejected
    end

    break User not teacher
        Server -->> Client: regenerate:rejected
    end

    break Class doesn't exist
        Server -->> Client: regenerate:rejected
    end

    Server -->> Database: class.refresh_invite_code

    Server -->> Client: regenerate:success
    Note left of Server: class_code:str
```


