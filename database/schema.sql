-- vytvorenie tabuliek, constraintov a sekvencii

-- objekt gps pozicia
create or replace type t_gps_position as object (
    latitude    number(9,6),
    longitude   number(9,6),
    recorded_at timestamp,

    constructor function t_gps_position(lat number, lon number)
        return self as result,

    -- metoda na triedenie
    map member function sort_key return number
);
/

-- kolekcia
create or replace type t_equipment_tab as table of varchar2(100);
/

-- sekvencie pre primarne kluce tabuliek
create sequence seq_unit_type start with 1 increment by 1 nocache;
create sequence seq_system_group start with 1 increment by 1 nocache;
create sequence seq_unit start with 1 increment by 1 nocache;
create sequence seq_operator start with 1 increment by 1 nocache;
create sequence seq_contact start with 1 increment by 1 nocache;
create sequence seq_case_file start with 1 increment by 1 nocache;
create sequence seq_fault_report start with 1 increment by 1 nocache;
create sequence seq_case_unit_assignment start with 1 increment by 1 nocache;
create sequence seq_call_record start with 1 increment by 1 nocache;
create sequence seq_attachment start with 1 increment by 1 nocache;
create sequence seq_case_note start with 1 increment by 1 nocache;

-- jednotlive tabulky
create table personal_data (
    rod_cislo char(11) not null,
    name varchar2(20) not null,
    surname varchar2(30) not null,
    constraint pk_personal_data primary key (rod_cislo)
);

create table unit_type (
    unit_type_id integer default seq_unit_type.nextval not null,
    code varchar2(20) not null,
    name varchar2(50) not null,
    constraint pk_unit_type primary key (unit_type_id),
    constraint uq_unit_type_code unique (code)
);

create table system_group (
    system_group_id number default seq_system_group.nextval not null,
    parent_group_id number,
    name varchar2(100) not null,
    region varchar2(100) not null,
    constraint pk_system_group primary key (system_group_id),
    constraint fk_sysgroup_parent
        foreign key (parent_group_id) references system_group (system_group_id)
);

create table unit (
    unit_id number default seq_unit.nextval not null,
    unit_type_id integer not null,
    system_group_id number not null,
    status varchar2(20) not null,
    last_position t_gps_position,
    equipment t_equipment_tab,
    photo blob,
    constraint pk_unit primary key (unit_id),
    constraint fk_unit_type  foreign key (unit_type_id) references unit_type (unit_type_id),
    constraint fk_unit_group foreign key (system_group_id) references system_group (system_group_id)
)
nested table equipment store as unit_equipment_nt;

create table operator (
    operator_id number default seq_operator.nextval not null,
    system_group_id number not null,
    rod_cislo char(11) not null,
    username varchar2(30) not null,
    role varchar2(20) not null,
    active char(1) not null,
    constraint pk_operator primary key (operator_id),
    constraint uq_operator_username unique (username),
    constraint fk_operator_group
        foreign key (system_group_id) references system_group (system_group_id),
    constraint fk_operator_person
        foreign key (rod_cislo) references personal_data (rod_cislo)
);

create table contact (
    contact_id number default seq_contact.nextval not null,
    rod_cislo char(11) not null,
    phone_number varchar2(20) not null,
    constraint pk_contact primary key (contact_id),
    constraint fk_contact_person
        foreign key (rod_cislo) references personal_data (rod_cislo)
);

create table case_file (
    case_id number default seq_case_file.nextval not null,
    created_by number not null,
    status varchar2(20) not null,
    opened_at timestamp not null,
    closed_at timestamp,
    weather_snapshot clob,
    constraint pk_case_file primary key (case_id),
    constraint fk_case_operator
        foreign key (created_by) references operator (operator_id)
);

create table fault_report (
    fault_id number default seq_fault_report.nextval not null,
    unit_id number not null,
    reported_by number not null,
    status varchar2(20) not null,
    reported_at timestamp not null,
    resolved_at timestamp,
    constraint pk_fault_report primary key (fault_id),
    constraint fk_fault_unit foreign key (unit_id) references unit (unit_id),
    constraint fk_fault_operator foreign key (reported_by) references operator (operator_id)
);

create table case_unit_assignment (
    assignment_id number default seq_case_unit_assignment.nextval not null,
    case_id number not null,
    unit_id number not null,
    dispatched_at timestamp not null,
    arrived_at timestamp,
    constraint pk_case_unit_assignment primary key (assignment_id),
    constraint fk_cua_case foreign key (case_id) references case_file (case_id),
    constraint fk_cua_unit foreign key (unit_id) references unit (unit_id)
);

create table call_record (
    call_id number default seq_call_record.nextval not null,
    contact_id number,
    unit_id number,
    operator_id number not null,
    case_id number,
    call_datetime timestamp not null,
    duration_seconds number not null,
    status varchar2(20) not null,
    constraint pk_call_record primary key (call_id),
    constraint fk_call_contact foreign key (contact_id) references contact (contact_id),
    constraint fk_call_unit foreign key (unit_id) references unit (unit_id),
    constraint fk_call_operator foreign key (operator_id) references operator (operator_id),
    constraint fk_call_case foreign key (case_id) references case_file (case_id)
);

create table attachment (
    attachment_id number default seq_attachment.nextval not null,
    entity_type varchar2(20) not null,
    entity_id number not null,
    uploaded_by number not null,
    attachment_type varchar2(20) not null,
    file_content blob not null,
    constraint pk_attachment primary key (attachment_id),
    constraint fk_attachment_operator
        foreign key (uploaded_by) references operator (operator_id)
);

create table case_note (
    note_id number default seq_case_note.nextval not null,
    case_id number not null,
    operator_id number not null,
    note_text clob not null,
    created_at timestamp not null,
    constraint pk_case_note primary key (note_id),
    constraint fk_note_case foreign key (case_id) references case_file (case_id),
    constraint fk_note_operator foreign key (operator_id) references operator (operator_id)
);

-- doplnit check constraints:
-- status v unit
-- role v operator
-- status vo fault report
-- status v case_file
-- status v call_record
-- entity_type v attachment
-- attachment_type v  entity_type
-- active v operator
