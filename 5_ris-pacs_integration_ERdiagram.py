#  This code defines the database structure of the 
# Entity-Relationship Diagram presented on "5_ris_pacs_integration.md"
# Created on  https://dbml.dbdiagram.io/docs
# https://dbdiagram.io/d


Table patients {
  patient_id integer [primary key] 
  medical_record_number varchar(50) [note:'unique']
  first_name varchar(30)
  last_name varchar(30)
  date_of_birth datetime
  gender varchar(15) [note:'default value: Not Specified']
  contact_info varchar(45) [note:'or json']
  primary_physician_id integer [ref: > physicians.physician_id, unique]
  insurance_id integer [note:'UN, Zerofill']
  patient_status enum [note: 'active/inactive /deceased']
}

Table studies {
  study_id integer [primary key]
  patient_id integer 
  request_id integer [ref: > order_requests.request_id, unique]
  accession_number varchar(45) [note:'unique']
  study_datetime datetime
  equipment_id integer [ref: > modalities.equipment_id, unique]
  body_part varchar(45)
  study_status enum [note: 'scheduled / in_progress / completed / canceled']
  ordering_physician_id integer [ref: > physicians.physician_id, unique]
  performing_technician_id integer [ref: > physicians.physician_id, unique]
}

Table reports {
  report_id integer [primary key]
  study_id integer [ref: > studies.study_id, unique]
  signed_datetime datetime
  radiologist_id integer [ref: > physicians.physician_id, unique]
  findings_text text
  report_status enum [note:' draft / final / amended / canceled']
  distribution_list varcgar(150) [note:'or json']
}

Table order_requests{
  request_id integer [primary key]
  patient_id integer [ref: > patients.patient_id, unique]
  ordering_physician_id integer [ref: > physicians.physician_id, unique]
  requested_procedure_code varchar(20)
  clinical_indication text(150)
  priority enum [note:' routine /urgent / stat']
  request_datetime datetime
  status enum [note:'oredered / scheduled / completed / canceled']
}

Table scheduled_appointments{
  appointment_id integer [primary key]
  request_id  integer [ref: > order_requests.request_id, unique]
  equipment_id integer [ref: > modalities.equipment_id, unique]
  scheduled_start datetime
  scheduled_end datetime
  room varchar
  performing_technician_id integer [ref: > physicians.physician_id, unique]
  appointment_status enum [note:'booked / arrived / no-show / completed']
}

Table modalities {
  equipment_id integer [primary key]
  modality_type enum [note:'CT / MR / US /CR/ MG']
  ae_title varchar(30)
  ip_address varchar(15)
  modality_port integer
  location varchar(45)
  manufacturer varchar(20)
  model varchar(15)
}

Table physicians {
  physician_id  integer [note:'unique']
  physician_name varchar(100)
  speciality varchar(20)
  date_of_birth datetime
  room varchar (20)
  contact_info varchar(50) [note:'or json']
  license_number varchar(30)
  physician_status enum [note:'active /inactive/deceased']
}

Table audit_log {
  log_id integer [primary key]
  user_id integer
  log_action enum [note: 'insert / update / delete']
  entity_type enum [note: ' patient / report / order_request / scheduled_appointment/ physician / modality']
  entity_id integer 
  datetime timestamp
  previous_value text
  new_value text
}
