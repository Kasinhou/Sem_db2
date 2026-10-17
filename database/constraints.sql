-- obmedzenia na povolené hodnoty
ALTER TABLE unit ADD CONSTRAINT chk_unit_status
    CHECK (status IN ('AVAILABLE','DISPATCHED','MAINTENANCE','OUT_OF_SERVICE'));

ALTER TABLE operator ADD CONSTRAINT chk_operator_active
    CHECK (active IN ('Y','N'));

ALTER TABLE operator ADD CONSTRAINT chk_operator_role
    CHECK (role IN ('DISPATCHER','SUPERVISOR','ADMIN'));

ALTER TABLE fault_report ADD CONSTRAINT chk_fault_status
    CHECK (status IN ('OPEN','IN_PROGRESS','RESOLVED'));

ALTER TABLE case_file ADD CONSTRAINT chk_case_status
    CHECK (status IN ('OPEN','ACTIVE','CLOSED','CANCELLED'));

ALTER TABLE call_record ADD CONSTRAINT chk_call_status
    CHECK (status IN ('COMPLETED','MISSED','TRANSFERRED','DROPPED'));

ALTER TABLE attachment ADD CONSTRAINT chk_attachment_entity_type
    CHECK (entity_type IN ('UNIT','CASE_FILE','CALL_RECORD','FAULT_REPORT'));

ALTER TABLE attachment ADD CONSTRAINT chk_attachment_type
    CHECK (attachment_type IN ('PHOTO','INVOICE_SCAN','RECORDING','DOCUMENT'));

-- CALL_RECORD musí mať buď contact_id, alebo unit_id (nikdy oboje, nikdy ani jedno)
ALTER TABLE call_record ADD CONSTRAINT chk_call_source
    CHECK (
        (contact_id IS NOT NULL AND unit_id IS NULL) OR
        (contact_id IS NULL AND unit_id IS NOT NULL)
        );

-- konzistencia časov
ALTER TABLE case_file ADD CONSTRAINT chk_case_dates
    CHECK (closed_at IS NULL OR closed_at >= opened_at);

ALTER TABLE fault_report ADD CONSTRAINT chk_fault_dates
    CHECK (resolved_at IS NULL OR resolved_at >= reported_at);

ALTER TABLE case_unit_assignment ADD CONSTRAINT chk_cua_dates
    CHECK (arrived_at IS NULL OR arrived_at >= dispatched_at);

ALTER TABLE call_record ADD CONSTRAINT chk_call_duration
    CHECK (duration_seconds >= 0);