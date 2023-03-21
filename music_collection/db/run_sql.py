import psycopg2
import psycopg2.extras as ext
# this is it. No changes for any projects required - just copy/paste as needed - only change is the dbname

dbname = 'music_collection'

def run_sql(sql, values=None):
    # set up a variablefor the connection
    conn = None
    # set up an empty list which will be populated and then returned from this function
    results = []
    # try to connect to the db
    try:
        # conn = psycopg2.connect("dbname = 'task_manager'")
        conn = psycopg2.connect(f"dbname = '{dbname}'")
        # get a cursor from the db
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # execute the sql
        cur.execute(sql,values)
        # commit the execution
        conn.commit()
        # get the results
        results = cur.fetchall()
        # close the connection
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    # return the list
    return results