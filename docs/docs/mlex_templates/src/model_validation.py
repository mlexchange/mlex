from pydantic import BaseModel, Field
from typing import Optional

"""
Define you input parameters following the schema:

class Parameters(BaseModel):
    parameter: int = Field(description='this is a parameter')
    optional_parameter: str = Field(description='this is the an optional parameter')
    ...

For more data type options, please refer to: https://pydantic-docs.helpmanual.io/usage/types/
"""