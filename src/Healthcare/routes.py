from typing import List

from fastapi import APIRouter, status

from src.Healthcare.schemas import PatchPatient, Patient

api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "welcome"}


@api_router.get("/patient/{patient_id}", status_code=status.HTTP_200_OK)
async def get_onepatient_records(patient_id: int):
    return {"message": f"{patient_id} patient data will be displayed here"}


@api_router.get("/patients", status_code=status.HTTP_200_OK)
async def get_patients_records():
    return {"message": "all patients data will be displayed here"}


@api_router.post(
    "/patient", response_model=PatchPatient, status_code=status.HTTP_201_CREATED
)
async def create_patient_record():
    pass
