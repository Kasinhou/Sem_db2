# Datova vrstva pre tabulku operator
import src.db as db

def list_operators():
    sql = '''
        select operator_id, system_group_id, rod_cislo, username, role, active
        from operator
        order by operator_id
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


def add_operator(system_group_id, rod_cislo, username, role, active):
    sql = '''
        insert into operator (system_group_id, rod_cislo, username, role, active) 
        values (:1, :2, :3, :4, :5)
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [system_group_id, rod_cislo, username, role, active])
            conn.commit()


def update_operator(operator_id, system_group_id, rod_cislo, username, role, active):
    sql = '''
        update operator 
        set system_group_id = :1, rod_cislo = :2, username = :3, role = :4, active = :5 
        where operator_id = :6
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [system_group_id, rod_cislo, username, role, active, operator_id])
            conn.commit()


def delete_operator(operator_id):
    sql = '''
        delete from operator 
        where operator_id = :1
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [operator_id])
            conn.commit()
