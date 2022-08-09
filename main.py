import requests
import pymysql
from bs4 import BeautifulSoup
from flask import Flask, request, render_template
import re

app = Flask(__name__)
data = ""


@app.route('/')
def index():
    return render_template('parse.html')


def read_password():
    with open("password.txt") as file:
        password = file.read().strip()
    return password


def connect_to_mars():
    password = read_password()
    conn = pymysql.connect(host="mars.cs.qc.cuny.edu", port=3306, user="yawe8598", passwd=password, database="yawe8598")
    return conn


@app.route('/parse', methods=['POST', 'GET'])
def parse():
    source_name = request.form["source_name"]
    url = request.form["source_url"]
    source_begin = request.form["source_begin"]
    source_end = request.form["source_end"]
    global data
    data = string_processing(url, source_begin, source_end)
    source_data_to_db(source_name, url, source_begin, source_end)
    occurrence_data_to_db()
    return data


def source_data_to_db(source_name, url, source_begin, source_end):
    conn = connect_to_mars()
    cursor = conn.cursor()
    sql = "INSERT INTO source (source_name, source_url,source_begin,source_end) VALUES (%s, %s, %s, %s)"
    val = (source_name, url, source_begin, source_end)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    print("insert to source database complete")


def string_processing(url, begin, end):
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    source = str(soup)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z", " ",
                "A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                "S", "T", "U", "V", "W", "X", "Y", "Z"]
    final_resul = source

    if begin in source:
        begin_text = begin
        x = re.search(re.escape(begin_text), source)
        ending_index = x.end()
        final_resul = source[ending_index:]
    else:
        print("begin not in text check again")
    if end in source:
        end_text = end
        start_index = final_resul.rfind(end_text)
        final_resul = final_resul[0:start_index]
    else:
        print("ending not in text")

    processed_string = ""
    for i in range(len(final_resul)):
        if final_resul[i] in alphabet:
            processed_string += final_resul[i]
    return processed_string.upper()


def word_frequency():
    data_lst = data.split()
    word_lst = {}
    for i in data_lst:
        if i not in word_lst:
            word_lst[i] = 1
        else:
            word_lst[i] += 1

    return word_lst


def get_source_id():
    conn = connect_to_mars()
    cursor = conn.cursor()
    sql = "SELECT source_id FROM source ORDER BY source_id DESC LIMIT 1"
    cursor.execute(sql)
    result = str(cursor.fetchall())
    source_id = ""
    for i in range(len(result)):
        if result[i].isalnum():
            source_id += result[i]
    return source_id


def occurrence_data_to_db():
    conn = connect_to_mars()
    cursor = conn.cursor()
    data = word_frequency()
    source_id = int(get_source_id())
    sql = "INSERT INTO occurrence (word, freq, source_id) VALUES (%s, %s, %s)"
    for i in data:
        val = (i, data.get(i), source_id)
        cursor.execute(sql, val)
    conn.commit()
    conn.close()
    print("insert to occurrence database successful")


def delete_db():
    conn = connect_to_mars()
    cursor = conn.cursor()
    query = "TRUNCATE occurrence"
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("delete successful")


if __name__ == '__main__':
    app.run()
    #print(get_source_id())
