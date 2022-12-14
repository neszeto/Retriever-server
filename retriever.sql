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


DELETE FROM authtoken_token
WHERE user_id = 6;