-- nahodne data - zatial len na checkpoint, potom budeme riesit asi inak

-- personal_data
insert into personal_data (rod_cislo, name, surname) values ('900101/1001', 'Jozef', 'Novak');
insert into personal_data (rod_cislo, name, surname) values ('900202/1002', 'Maria', 'Kovacova');
insert into personal_data (rod_cislo, name, surname) values ('900303/1003', 'Peter', 'Horvath');
insert into personal_data (rod_cislo, name, surname) values ('900404/1004', 'Lucia', 'Vargova');
insert into personal_data (rod_cislo, name, surname) values ('900505/1005', 'Zuzana', 'Tothova');
insert into personal_data (rod_cislo, name, surname) values ('900606/1006', 'Roman', 'Balaz');
insert into personal_data (rod_cislo, name, surname) values ('900707/1007', 'Daniel', 'Kralik');
insert into personal_data (rod_cislo, name, surname) values ('900808/1008', 'Stefan', 'Stefanik');
insert into personal_data (rod_cislo, name, surname) values ('900909/1009', 'Gabriel', 'Molnar');
insert into personal_data (rod_cislo, name, surname) values ('901010/1010', 'Veronika', 'Sokolova');
insert into personal_data (rod_cislo, name, surname) values ('910101/2001', 'Martin', 'Maly');
insert into personal_data (rod_cislo, name, surname) values ('910202/2002', 'Jana', 'Velka');
insert into personal_data (rod_cislo, name, surname) values ('910303/2003', 'Tomas', 'Dlhy');
insert into personal_data (rod_cislo, name, surname) values ('910404/2004', 'Eva', 'Novotna');
insert into personal_data (rod_cislo, name, surname) values ('910505/2005', 'Juraj', 'Cierny');
insert into personal_data (rod_cislo, name, surname) values ('910606/2006', 'Katarina', 'Biela');
insert into personal_data (rod_cislo, name, surname) values ('910707/2007', 'Michal', 'Zeleny');
insert into personal_data (rod_cislo, name, surname) values ('910808/2008', 'Simona', 'Modra');
insert into personal_data (rod_cislo, name, surname) values ('910909/2009', 'Andrej', 'Kratky');
insert into personal_data (rod_cislo, name, surname) values ('911010/2010', 'Barbora', 'Stredna');

-- unit_type
insert into unit_type (unit_type_id, code, name) values (1, 'AMB', 'Ambulancia');
insert into unit_type (unit_type_id, code, name) values (2, 'FIRE', 'Hasicska jednotka');
insert into unit_type (unit_type_id, code, name) values (3, 'POLICE', 'Policajna hliadka');
insert into unit_type (unit_type_id, code, name) values (4, 'RESCUE', 'Horska zachranna sluzba');
insert into unit_type (unit_type_id, code, name) values (5, 'HAZMAT', 'Chemicka jednotka');
insert into unit_type (unit_type_id, code, name) values (6, 'DIVE', 'Potapacska jednotka');
insert into unit_type (unit_type_id, code, name) values (7, 'K9', 'Kynologicka jednotka');
insert into unit_type (unit_type_id, code, name) values (8, 'AIR', 'Letecka zachrana');
insert into unit_type (unit_type_id, code, name) values (9, 'MOTO', 'Motorizovana hliadka');
insert into unit_type (unit_type_id, code, name) values (10, 'BOAT', 'Vodna zachrana');

-- system_group
insert into system_group (system_group_id, parent_group_id, name, region) values (1, null, 'Operacne stredisko SR', 'Slovensko');
insert into system_group (system_group_id, parent_group_id, name, region) values (2, null, 'Operacne stredisko Zapad', 'Zapadne Slovensko');
insert into system_group (system_group_id, parent_group_id, name, region) values (3, 1, 'KS Bratislava', 'Bratislavsky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (4, 1, 'KS Kosice', 'Kosicky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (5, 2, 'KS Trnava', 'Trnavsky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (6, 2, 'KS Nitra', 'Nitriansky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (7, 3, 'Stanica Bratislava-Ruzinov', 'Bratislavsky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (8, 3, 'Stanica Bratislava-Petrzalka', 'Bratislavsky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (9, 5, 'Stanica Trnava-mesto', 'Trnavsky kraj');
insert into system_group (system_group_id, parent_group_id, name, region) values (10, 5, 'Stanica Piestany', 'Trnavsky kraj');

-- unit
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (1, 1, 7, 'AVAILABLE', t_gps_position(48.1486, 17.1077, null), t_equipment_tab('Defibrilator','Nosidla','Kyslik'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (2, 2, 7, 'DISPATCHED', t_gps_position(48.1600, 17.1200, null), t_equipment_tab('Hadice','Rebrik','Dychaci pristroj'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (3, 3, 8, 'AVAILABLE', t_gps_position(48.1200, 17.1050, null), t_equipment_tab('Vysielacka','Puta'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (4, 1, 8, 'MAINTENANCE', t_gps_position(48.1300, 17.1000, null), t_equipment_tab('Defibrilator','Nosidla'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (5, 4, 9, 'AVAILABLE', t_gps_position(48.3774, 17.5880, null), t_equipment_tab('Lano','Karabiny','Nosidla'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (6, 5, 9, 'OUT_OF_SERVICE', t_gps_position(48.3700, 17.5900, null), t_equipment_tab('Ochranny oblek','Detektor plynu'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (7, 6, 10, 'AVAILABLE', t_gps_position(48.5900, 17.8260, null), t_equipment_tab('Potapacsky vystroj','Cln'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (8, 7, 10, 'AVAILABLE', t_gps_position(48.5850, 17.8300, null), t_equipment_tab('Pes','Vysielacka'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (9, 8, 4, 'DISPATCHED', t_gps_position(48.7164, 21.2611, null), t_equipment_tab('Vrtulnik','Navijak','Nosidla'));
insert into unit (unit_id, unit_type_id, system_group_id, status, last_position, equipment) values (10, 9, 6, 'AVAILABLE', t_gps_position(48.3060, 18.0800, null), t_equipment_tab('Motorka','Lekarnicka'));

-- operator
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (1, 7, '900101/1001', 'jnovak', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (2, 7, '900202/1002', 'mkovac', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (3, 8, '900303/1003', 'phorvath', 'SUPERVISOR', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (4, 8, '900404/1004', 'lvarga', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (5, 9, '900505/1005', 'ztoth', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (6, 9, '900606/1006', 'rbalaz', 'SUPERVISOR', 'N');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (7, 10, '900707/1007', 'dkralik', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (8, 10, '900808/1008', 'sstefan', 'DISPATCHER', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (9, 4, '900909/1009', 'gmolnar', 'ADMIN', 'Y');
insert into operator (operator_id, system_group_id, rod_cislo, username, role, active) values (10, 6, '901010/1010', 'vsokol', 'DISPATCHER', 'N');

-- contact
insert into contact (contact_id, rod_cislo, phone_number) values (1, '910101/2001', '+421901111001');
insert into contact (contact_id, rod_cislo, phone_number) values (2, '910202/2002', '+421901111002');
insert into contact (contact_id, rod_cislo, phone_number) values (3, '910303/2003', '+421901111003');
insert into contact (contact_id, rod_cislo, phone_number) values (4, '910404/2004', '+421901111004');
insert into contact (contact_id, rod_cislo, phone_number) values (5, '910505/2005', '+421901111005');
insert into contact (contact_id, rod_cislo, phone_number) values (6, '910606/2006', '+421901111006');
insert into contact (contact_id, rod_cislo, phone_number) values (7, '910707/2007', '+421901111007');
insert into contact (contact_id, rod_cislo, phone_number) values (8, '910808/2008', '+421901111008');
insert into contact (contact_id, rod_cislo, phone_number) values (9, '910909/2009', '+421901111009');
insert into contact (contact_id, rod_cislo, phone_number) values (10, '911010/2010', '+421901111010');

-- case_file
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (1, 1, 'CLOSED', timestamp '2026-01-05 08:12:00', timestamp '2026-01-05 09:40:00', 'Jasno, 2 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (2, 2, 'OPEN', timestamp '2026-01-07 14:30:00', null, 'Dazd, 8 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (3, 3, 'CLOSED', timestamp '2026-01-10 21:05:00', timestamp '2026-01-10 22:15:00', 'Hmla, 1 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (4, 4, 'ACTIVE', timestamp '2026-01-12 03:45:00', null, 'Sneh, -3 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (5, 5, 'CLOSED', timestamp '2026-01-15 11:20:00', timestamp '2026-01-15 12:00:00', 'Polojasno, 5 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (6, 6, 'ACTIVE', timestamp '2026-01-18 17:00:00', null, 'Vietor, 6 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (7, 7, 'CLOSED', timestamp '2026-01-20 09:50:00', timestamp '2026-01-20 10:30:00', 'Jasno, 0 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (8, 8, 'OPEN', timestamp '2026-01-22 23:10:00', null, 'Dazd, 9 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (9, 9, 'CLOSED', timestamp '2026-01-25 06:35:00', timestamp '2026-01-25 07:55:00', 'Zamracene, 4 C');
insert into case_file (case_id, created_by, status, opened_at, closed_at, weather_snapshot) values (10, 10, 'CANCELLED', timestamp '2026-01-28 19:25:00', null, 'Sneh, -1 C');

-- fault_report
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (1, 1, 1, 'RESOLVED', timestamp '2026-01-05 10:00:00', timestamp '2026-01-05 15:00:00');
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (2, 2, 2, 'OPEN', timestamp '2026-01-06 11:30:00', null);
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (3, 3, 3, 'RESOLVED', timestamp '2026-01-07 09:15:00', timestamp '2026-01-07 12:45:00');
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (4, 4, 4, 'OPEN', timestamp '2026-01-08 16:20:00', null);
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (5, 5, 5, 'RESOLVED', timestamp '2026-01-09 07:40:00', timestamp '2026-01-09 10:10:00');
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (6, 6, 6, 'IN_PROGRESS', timestamp '2026-01-10 13:00:00', null);
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (7, 7, 7, 'RESOLVED', timestamp '2026-01-11 08:25:00', timestamp '2026-01-11 09:50:00');
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (8, 8, 8, 'OPEN', timestamp '2026-01-12 18:05:00', null);
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (9, 9, 9, 'RESOLVED', timestamp '2026-01-13 05:55:00', timestamp '2026-01-13 08:30:00');
insert into fault_report (fault_id, unit_id, reported_by, status, reported_at, resolved_at) values (10, 10, 10, 'IN_PROGRESS', timestamp '2026-01-14 20:40:00', null);

-- case_unit_assignment
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (1, 1, 1, timestamp '2026-01-05 08:15:00', timestamp '2026-01-05 08:35:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (2, 2, 2, timestamp '2026-01-07 14:35:00', timestamp '2026-01-07 14:55:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (3, 3, 3, timestamp '2026-01-10 21:10:00', null);
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (4, 4, 4, timestamp '2026-01-12 03:50:00', timestamp '2026-01-12 04:20:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (5, 5, 5, timestamp '2026-01-15 11:25:00', timestamp '2026-01-15 11:45:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (6, 6, 6, timestamp '2026-01-18 17:05:00', null);
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (7, 7, 7, timestamp '2026-01-20 09:55:00', timestamp '2026-01-20 10:15:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (8, 8, 8, timestamp '2026-01-22 23:15:00', timestamp '2026-01-22 23:40:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (9, 9, 9, timestamp '2026-01-25 06:40:00', timestamp '2026-01-25 07:05:00');
insert into case_unit_assignment (assignment_id, case_id, unit_id, dispatched_at, arrived_at) values (10, 10, 10, timestamp '2026-01-28 19:30:00', null);

-- call_record
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (1, 1, null, 1, 1, timestamp '2026-01-05 08:10:00', 95, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (2, null, 2, 2, 2, timestamp '2026-01-07 14:28:00', 140, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (3, 3, null, 3, 3, timestamp '2026-01-10 21:02:00', 60, 'MISSED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (4, null, 4, 4, 4, timestamp '2026-01-12 03:43:00', 200, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (5, 5, null, 5, 5, timestamp '2026-01-15 11:18:00', 75, 'TRANSFERRED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (6, null, 6, 6, 6, timestamp '2026-01-18 16:58:00', 110, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (7, 7, null, 7, 7, timestamp '2026-01-20 09:48:00', 50, 'DROPPED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (8, null, 8, 8, 8, timestamp '2026-01-22 23:08:00', 180, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (9, 9, null, 9, 9, timestamp '2026-01-25 06:33:00', 90, 'COMPLETED');
insert into call_record (call_id, contact_id, unit_id, operator_id, case_id, call_datetime, duration_seconds, status) values (10, null, 10, 10, 10, timestamp '2026-01-28 19:22:00', 130, 'MISSED');

-- attachment
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (1, 'CASE_FILE', 1, 1, 'PHOTO', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (2, 'CASE_FILE', 2, 2, 'INVOICE_SCAN', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (3, 'UNIT', 1, 3, 'PHOTO', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (4, 'CASE_FILE', 3, 4, 'DOCUMENT', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (5, 'UNIT', 5, 5, 'PHOTO', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (6, 'FAULT_REPORT', 4, 6, 'DOCUMENT', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (7, 'CASE_FILE', 5, 7, 'INVOICE_SCAN', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (8, 'UNIT', 9, 8, 'PHOTO', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (9, 'CASE_FILE', 7, 9, 'DOCUMENT', empty_blob());
insert into attachment (attachment_id, entity_type, entity_id, uploaded_by, attachment_type, file_content) values (10, 'CALL_RECORD', 10, 10, 'RECORDING', empty_blob());

-- case_note
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (1, 1, 1, 'Pacient stabilizovany na mieste.', timestamp '2026-01-05 08:40:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (2, 2, 2, 'Poziar lokalizovany, caka sa na posily.', timestamp '2026-01-07 15:00:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (3, 3, 3, 'Hliadka na mieste, situacia pod kontrolou.', timestamp '2026-01-10 21:20:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (4, 4, 4, 'Zasah v tazkom terene, sneh.', timestamp '2026-01-12 04:25:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (5, 5, 5, 'Zachrana ukoncena, zraneny prevezeny.', timestamp '2026-01-15 12:05:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (6, 6, 6, 'Unik chemikalie, evakuacia okolia.', timestamp '2026-01-18 17:30:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (7, 7, 7, 'Potapaci prehladavaju dno.', timestamp '2026-01-20 10:20:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (8, 8, 8, 'Pes nasiel stopu, pokracuje patranie.', timestamp '2026-01-22 23:45:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (9, 9, 9, 'Vrtulnik vzlietol, transport do nemocnice.', timestamp '2026-01-25 07:10:00');
insert into case_note (note_id, case_id, operator_id, note_text, created_at) values (10, 10, 10, 'Hliadka na ceste k miestu udalosti.', timestamp '2026-01-28 19:35:00');

commit;

-- posun sekvencii, kedze sme ich manualne vlozili
alter sequence seq_unit_type restart start with 11;
alter sequence seq_system_group restart start with 11;
alter sequence seq_unit restart start with 11;
alter sequence seq_operator restart start with 11;
alter sequence seq_contact restart start with 11;
alter sequence seq_case_file restart start with 11;
alter sequence seq_fault_report restart start with 11;
alter sequence seq_case_unit_assignment restart start with 11;
alter sequence seq_call_record restart start with 11;
alter sequence seq_attachment restart start with 11;
alter sequence seq_case_note restart start with 11;
