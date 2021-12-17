import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    con = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password
    )

    return con


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def execute_read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def get_words_study():
    connection = create_connection("localhost", "root", "admin")
    query_words_study = '''
        SELECT 
        `dictionary_bd`.`words`.`word_eng`, 
        `dictionary_bd`.`words`.`word_rus`
        FROM
        `dictionary_bd`.`words`,
        `dictionary_bd`.`topic`
        WHERE
        `dictionary_bd`.`topic`.`study` = true
        AND `dictionary_bd`.`topic`.`id` = `dictionary_bd`.`words`.`id_topic`;
        '''

    return execute_read_query(connection, query_words_study)


def get_topic():
    connection = create_connection("localhost", "root", "admin")
    query_topic = '''
        SELECT 
        `dictionary_bd`.`topic`.`topic_name`
        FROM
       `dictionary_bd`.`topic`; 
        '''
    topic = execute_read_query(connection, query_topic)
    result_list = []
    for i in topic:
        result_list.append(i[0])
    return result_list


def get_words_topic(topic_name):
    connection = create_connection("localhost", "root", "admin")
    query_words_topic = "SELECT `dictionary_bd`.`words`.`word_eng`,`dictionary_bd`.`words`.`word_rus` FROM " \
                        "`dictionary_bd`.`words`,`dictionary_bd`.`topic` WHERE `dictionary_bd`.`topic`.`topic_name` = '" + \
                        topic_name + "' AND `dictionary_bd`.`topic`.`id` = `dictionary_bd`.`words`.`id_topic`; "
    words_topic = execute_read_query(connection, query_words_topic)
    result_list = []
    for i in words_topic:
        result_list.append(i[0] + " - " + i[1])
    return result_list


def study_status_true(topic_name):
    connection = create_connection("localhost", "root", "admin")
    update_status = "UPDATE `dictionary_bd`.`topic` SET topic.study = 1 WHERE  topic.topic_name = '" \
                    + topic_name + "';"
    execute_query(connection, update_status)


def study_status_false(topic_name):
    connection = create_connection("localhost", "root", "admin")
    update_status = "UPDATE `dictionary_bd`.`topic` SET topic.study = 0 WHERE  topic.topic_name = '" \
                    + topic_name + "';"
    execute_query(connection, update_status)


def add_word(topic_name, word_eng_t, word_rus_t):
    connection = create_connection("localhost", "root", "admin")
    query_id_topic = "select id from dictionary_bd.topic where topic_name = '" + topic_name + "';"
    id_topic = execute_read_query(connection, query_id_topic)
    query_insert_word = "INSERT INTO dictionary_bd.words values(" + str(id_topic[0][0]) + \
                              ",'" + word_eng_t + "', '" + word_rus_t + "');"
    execute_query(connection, query_insert_word)


def del_word(word_eng):
    connection = create_connection("localhost", "root", "admin")
    query_delete_word = "DELETE FROM dictionary_bd.words WHERE word_eng = '" + word_eng + "';"
    execute_query(connection, query_delete_word)


def add_dictionary(topic_name):
    connection = create_connection("localhost", "root", "admin")
    query_inset_word = "INSERT INTO `dictionary_bd`.`topic`(`topic_name`, `study`) VALUES ('" + topic_name + "', '0');"
    execute_query(connection, query_inset_word)


def del_dictionary(topic_name):
    connection = create_connection("localhost", "root", "admin")
    query_delete_dictionary = "DELETE FROM dictionary_bd.topic WHERE topic_name = '" + topic_name + "';"
    execute_query(connection, query_delete_dictionary)
