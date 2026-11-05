from pydantic import BaseModel


class Patient(BaseModel):
    patient_id: int
    age: int
    gender: str
    symptoms: str
    symptoms_cout: int
    disease: str


class PatchPatient(BaseModel):
    age: int
    symptoms: str
    symptoms_count: int
    disease: str
