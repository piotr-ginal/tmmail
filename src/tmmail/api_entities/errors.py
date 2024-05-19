from pydantic import BaseModel, Field


class ConstraintViolation(BaseModel):
    property_path: str = Field(alias="propertyPath")
    message: str
    code: str
