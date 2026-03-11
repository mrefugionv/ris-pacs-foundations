# About RIS–PACS Foundations Repository
Since my Professional Goal is to contribute to RIS/PACS implementation projects by combining technical understanding of standards, workflow awareness, documentation skills and systems thinking.

This repository represents the foundation for advancing into real-world healthcare IT environments, focused on the practical knowledge required to participate in RIS/PACS implementation projects.

## Contents:

### 1. Clinical Imaging Workflow 
[1_clinical_imaging_workflow](/1_clinical_imaging_workflow.md) 
    - Description: This document explains the basic workflow of a radiology study.\
    - Keywords:
      ```
      * Electronic Medical Record - EMR
      * Hospital Information System - HIS
      * Radiology Information System - RIS
      * Picture Archieving and Communication System - PACS
      * Modality
      * Study Instance UID
      * Series Instnace UID.
      ```


### 2. DICOM Basics
[2_dicom_basics](/2_dicom_basics.md)
  - Description: This document explains the basic concepts of DICOM standar; and a python exercise which demonstrates basic DICOM handling, including image visualization and extraction of key identifiers across the Patient–Study–Series–Instance hierarchy.\
  - Keywords:
    ```
    * Digital Imaging and Communication in Medicine - DICOM
    *  Patient–Study–Series–Instance Hierarchy
    *  DICOM object
    * TAG
    * Value Representation - VR
    * Service-Object Pair - SOP Class
    * Information Object Definition - IOD
    * DICOM Service Elements - DIMSE
    ```

### 3. DICOM Networking
[3_dicom_networking](/3_dicom_networking.md) 
   - Description: This document explains the basic network mechanism on how clinical images and related information are exchenges between nodes.\
   - Keywords: 
   ```
   * Aplication Entity - **AE**
   * AE Title
   * IP Adress
   * Port Number
   * Association
   * Service Class User - **SCU**
   * Service Class Provide - **SCP**
   * SOP Class
   * C-STORE
   * C-FIND 
   * C-MOVE
   * C-GET.
   ```

### 4. PACS Architecture
[4_pacs_arquitecture](/4_pacs_arquitecture.md)
   - Description: This document explains the core infrastructure that stores, manages, distributes, and displays medical images within a healthcare organization.\
   - Keywords: 
   ```
   * Picture And Communication System - PACS,
   * Modality
   * Local Area Network  - LAN
   * Wide Area Network  - WAN
   * PACS Server
   * Storage Area Network - SAN
   * Network Attached Storage -NAS
   * Cloud Storage
   * Backup and Redundacy
   * Redundant Array of Independent Disks - RAID
   * Replication
   * Failover
   * High Availability - HA
   * Diagnostic viewers
   * Clinical viewer
   * Zero footprint viewers.
   ```

### 5. RIS-PACS Integration 
[5_ris-pacs_integration](/5_ris-pacs_integration.md)
   - Description: This document explains the coordinated workflow between administrative processesin RIS and medical imaging throughout the radiology workflow in PACS.\
   - Keywords:
   ```
    * Accession number
    * Modality Worklist - MWL
    * Entity - Relation - ED Diagram
    * Procedure Request
    * Scheduling
    * Audit Log
   ```
   
### 6. HL7 Basics
[6_hl7_basics](/6_hl7_basic.md)
  - Description: This document explains the hl7 messages in clinical imaging workflow.
  - Keywords:
    ```
    * Health Level Seven - HL7
    * Admission-Discharge-Transfer - ADT
    * Order Message - ORM
    * Observation Results - ORU
    ```
