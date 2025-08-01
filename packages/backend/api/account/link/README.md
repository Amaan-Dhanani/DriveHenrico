# /auth/link (ws)

Used to link accounts to other accounts or classes

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Database

    critical Authentication Handshake
        Client -->> Server: auth:token
        Note right of Client: token

        break Authentication Failed
            Server -->> Client: auth:failed
        end 

        Server -->> Client: auth:success
    end

    alt teacher:create_class
        Client -->> Server: teacher:create_class
        Note right of Client: name:str

        break user.is_not_teacher
            Server -->> Client: creation:unsuccessful
        end 

        Server -->> Database: Insert Class

        Server -->> Client: class:created

        Note left of Server: class_id:str

    else teacher:regenerate_code
        Client -->> Server: teacher:regenerate_class_code
        Note right of Client: class_id:str
    
        break user.is_not_teacher
            Server -->> Client: regenerate:rejected
        end 
    
        break class.does_not_exist
            Server -->> Client: regenerate:rejected
        end
    
        Server -->> Database: Update class code
    
        Server -->> Client: regenerate:success
    
        Note left of Server: class_code:str

    else student:link_class
        Client -->> Server: student:link_class
        Note right of Client: class_code:str

        break user.is_not_student
            Server -->> Client: link:rejected
        end 

        break class.does_not_exist
            Server -->> Client: link:rejected
        end

        break user.already_in_class
            Server -->> Client: link:rejected
        end

        Server -->> Database: push user._id to class.students

        Server -->> Client: link:established

    else student:link_parent
        Client -->> Server: student:link_parent
        Note right of Client: invite_code:str
    
        break user.is_not_student
            Server -->> Client: link:rejected
        end 
    
        break invite.does_not_exist
            Server -->> Client: link:rejected
        end
    
        break user.already_has_parent
            Server -->> Client: link:rejected
        end
    
        Server -->> Database: Update parent_id in user
    
        Server -->> Client: link:established

    end
```