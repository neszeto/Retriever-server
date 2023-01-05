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
SET plan = "FNA of submandibular lymph nodes - large lymphoblasts noted. Recommend referral to Oncology vs palliative care."
WHERE id = 40; 


DELETE FROM retrieverapi_medicalrecords
WHERE id = 26;

INSERT INTO retrieverapi_owners
VALUES (56, 1, 12);