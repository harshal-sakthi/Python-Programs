import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="hsnbrfdhkn",
    database="coding_connectivity",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        create_query = """
        CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            job VARCHAR(100)join
        );"""
        cursor.execute(create_query)
        insert_query = "INSERT INTO employees(name, job) VALUES (%s, %s)"
        values = [("Harshal", "IT"), ("Kaniyan", "Scientist"), ("Nikithan", "Pilot"), ("Sudharshanaa raaj", "Cricketer"), ("Shashwin Surya", "Doctor"), ("Suyambu Dharshan", "Chief Minister(CM)"), ("Ritik Raj", "Farmer"), ("Pregathesh Mahizan", "Archaeologist")]
        cursor.executemany(insert_query, values)
        connection.commit()

        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()
        with open("employees_output.txt", "w") as outfile:
            for row in result:
                outfile.write(f"{row}\n")

        for row1 in result:
            print(row1)
finally:
    connection.close()