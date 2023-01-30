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


UPDATE retrieverapi_medicalrecords
SET assessment = "Ear cytology shows +1 cocci AS and +3 cocci AD."
WHERE id = 58; 


DELETE FROM retrieverapi_diagnoses
WHERE id = 14;

INSERT INTO retrieverapi_owners
VALUES (56, 1, 12);