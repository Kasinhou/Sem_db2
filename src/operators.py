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


def get_operator_xml(operator_id):
    sql = '''
          select xmlserialize(document
              xmlroot(
                     xmlelement("operator",
                        xmlattributes(o.operator_id as "operator_id"),
                 --viacero stĺpcov vyrobí viacero samostatných child elementov naraz – každý s vlastným otváracím aj zatváracím tagom:
                        xmlforest(
                                o.username as "username",
                                o.role as "role",
                                o.active as "active_state"
                        ),
                     -- osoba
                        xmlelement("osoba",
                               xmlforest(
                                       pd.rod_cislo as "rod_cislo",
                                       pd.name as "name",
                                       pd.surname as "surname"
                               )
                        ),
                   -- domovska stanica operatora
                        xmlelement("operator_group",
                               xmlattributes(sg.system_group_id as "system_group_id"),
                               xmlforest(
                                       sg.name as "group_name",
                                       sg.region as "group_region"
                               )
                        ),
                    -- pripady priradené k operatorovi
                        xmlelement("cases",
                                   xmlattributes(count(cf.case_id) as "number_of_cases"),
                            -- poznamky k tomuto konkretnemu pripadu
                                   xmlagg(
                                       case when cf.case_id is not null then 
                                           xmlelement("case", 
                                                  xmlattributes(cf.case_id as "case_id"),
                                                  xmlforest(
                                                          cf.status as "status",
                                                          cf.opened_at as "opened_at",
                                                          cf.closed_at as "closed_at" 
                                                  ),
                                                  xmlelement("notes", 
                                                         (select xmlagg( 
                                                                 xmlelement("note", 
                                                                        xmlattributes( 
                                                                                 n.note_id as "note_id",
                                                                                 n.operator_id as "operator_id",
                                                                                 n.created_at as "created_at"
                                                                        ), 
                                                                        n.note_text) 
                                                                        order by n.created_at)
                                                          from case_note n
                                                          where n.case_id = cf.case_id) 
                                       )
                                )
                            end
                            order by cf.opened_at
                        )
                    )
                ),
                version '1.0'
            )
            as clob indent size = 2)

          from operator o
             join personal_data pd on pd.rod_cislo = o.rod_cislo
             join system_group sg on sg.system_group_id = o.system_group_id
             left join case_file cf on cf.created_by = o.operator_id
        where o.operator_id = :1
        group by o.operator_id, o.username, o.role, o.active,
                              pd.rod_cislo, pd.name, pd.surname,
                              sg.system_group_id, sg.name, sg.region

          '''

    with db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, [operator_id])
            row = cur.fetchone()

            # row is None, operátor s ID neexistuje
            # row[0] is None, riadok existuje, ale CLOB vyšiel NULL
            if row is None or row[0] is None:
                return None
            return row[0].read()
