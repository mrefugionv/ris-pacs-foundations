#  This code defines the database structure of the 
# Entity-Relationship Diagram presented on "5_ris_pacs_integration.md"
# Created on  https://dbml.dbdiagram.io/docs

Table patient {
  patient_id integer [primary key] 
  medical_record_number verchar [note:'unique']
  first_name varchar
  last_name varchar
  date_of_birth datetime
  gender char
  contact_info varchar [note:'or json']
  primary_physician_id integer [ref: > physician.physician_id, unique]
  insurance_id varchar
  status enum [note: 'active/inactive /deceased']
}

Table study {
  study_id integer [primary key]
  patient_id integer [ref: > patient.patient_id, unique]
  request_id integer
  accession_number varchar [note:'unique']
  study_datetime datetime
  modality_id integer
  body_part varchar
  status enum [note: 'scheduled / in_progress / completed / canceled']
  referring_physician_id integer [ref: > physician.physician_id, unique]
  performing_tecnologist_id varchar
}

Table report {
  report_id integer [primary key]
  study_id integer [ref: > study.study_id, unique]
  report_datetime datetime
  radiologist_id integer [ref: > physician.physician_id, unique]
  findings text
  impression text
  status enum [note:' draft / final / amended / canceled']
  signed_datetime datetime
  distribution_list text [note:'or json']
}

Table order_request{
  request_id integer [primary key]
  patient_id integer [ref: > patient.patient_id, unique]
  ordering_physician_id integer [ref: > physician.physician_id, unique]
  requested_procedure_code varchar
  clinical_indication text
  priority enum [note:' routine /urgent / stat']
  request_datetime datetime
  status enum [note:'oredered / scheduled / completed / canceled']
}

Table scheduled_appointment{
  apointment_id integer [primary key]
  requested_id  integer [ref: > order_request.request_id, unique]
  modality_id integer [ref: > modality.modality_id, unique]
  scheduled_start datetime
  scheduled_end datetime
  room varchar
  performing_technologist_id integer [ref: > physician.physician_id, unique]
  status enum [note:'booked / arrived / no-show / completed']
}

Table modality {
  modality_id integer [primary key]
  modality_type enum [note:'CT / MR / US /CR/ MG']
  ae_title varchar
  ip_address varchar
  port integer
  location varchar
  manufacturer varchar
  model varchar
}

Table physician {
  physician_id  integer [note:'unique']
  physician_name varchar
  speciality varchar
  role enum (' ordering / refering / radiologist / technician')
  contact_info varchar [note:'or json']
  license_number varchar
}

Table audit_log {
  log_id integer [primary key]
  user_id integer
  action enum [note: 'create / update / delete/ login']
  entity_type enum [note: ' patient / report / order_request / scheduled_appointment/ physician / modality']
  entity_id integer
  datetime timestamp
  previous_value text
  new_value text
}