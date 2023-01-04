DELETE FROM retrieverapi_owners
WHERE id = 10;


SELECT 
    p.id AS PatientId,
    d.diagnosis AS Diagnosis
FROM retrieverapi_patients p 
JOIN retrieverapi_medicalrecords mr 
    ON mr.patient_id = p.id
JOIN retrieverapi_diagnoses d 
    ON d.id = mr.diagnosis_id;


UPDATE retrieverapi_medications
SET name = "Clavamox"
WHERE id = 3; 


DELETE FROM retrieverapi_medicalrecords
WHERE id = 4;

INSERT INTO retrieverapi_medicalrecordmedications
VALUES (56, 1, 12);