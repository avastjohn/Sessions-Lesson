import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()



def authenticate(username, password):
# returns id from users DB (or None)
    # connect_to_db()
    query = "SELECT username, password, id FROM users WHERE username = ?"
    connect_to_db()
    DB.execute(query, (username,))
    search_results = DB.fetchone()
    if username == search_results[0] and password == search_results[1]:
        return search_results[2]
    else:
        return None

def get_user_by_name(username):
# returns id for a user
    query = "SELECT id FROM users WHERE username = ?"
    connect_to_db()
    DB.execute(query, (username,))
    id_from_users = DB.fetchone()
    return id_from_users

def get_wall_posts_by_user_id(id_from_users):
# returns wall posts for a user's wall
    query = "SELECT author_id, created_at, content FROM wall_posts WHERE owner_id = ?"
    connect_to_db()
    DB.execute(query, (id_from_users,))
    wall_results = DB.fetchall()
    return wall_results

def new_wall_post(id_from_users):
# post a new message on a wall)=
    query = "INSERT into wall_posts VALUES ()"


# def main():
#     connect_to_db()
#     command = None
        
#     CONN.close()

# if __name__ == "__main__":
#     main()


"""

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

    CONN.close()

"""