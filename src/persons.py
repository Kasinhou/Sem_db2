# Datova vrstva pre tabulku personal_data
import src.db as db


def list_persons():
    sql = '''
        select rod_cislo, name, surname 
        from personal_data 
        order by rod_cislo
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


def add_person(rod_cislo, name, surname):
    sql = '''
        insert into personal_data (rod_cislo, name, surname) 
        values (:1, :2, :3)
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [rod_cislo, name, surname])
            conn.commit()


def update_person(rod_cislo, name, surname):
    sql = '''
        update personal_data 
        set name = :1, surname = :2 
        where rod_cislo = :3
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [name, surname, rod_cislo])
            conn.commit()


def delete_person(rod_cislo):
    sql = '''
        delete from personal_data 
        where rod_cislo = :1
    '''
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [rod_cislo])
            conn.commit()

def get_person_age(rod_cislo):
    sql = """
        select tp.person.get_age() age
        from (
            select t_person(rod_cislo, name, surname) as person
            from personal_data 
            where rod_cislo = :1
        ) tp
    """
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [rod_cislo])
            row = cur.fetchone()
            return row[0] if row else None


def get_person_sex(rod_cislo):
    sql = """
        select tp.person.get_sex() sex
        from (
            select t_person(rod_cislo, name, surname) as person
            from personal_data 
            where rod_cislo = :1
        ) tp
    """
    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [rod_cislo])
            row = cur.fetchone()
            return row[0] if row else None