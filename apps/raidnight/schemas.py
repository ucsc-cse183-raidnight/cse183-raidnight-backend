from __future__ import annotations

import enum
import pathlib
from typing import List, Optional, Union

from pydantic import BaseModel, confloat, conlist, constr, stricturl


# ==== Input ====
# ---- Sessions ----
class RuleOperator(str, enum.Enum):
    EQ = 'eq'  # =
    GE = 'ge'  # >=
    GT = 'gt'  # >
    LE = 'le'  # <=
    LT = 'lt'  # <


class SessionRule(BaseModel):
    operator: RuleOperator
    value: int


class SessionRuleWithRole(SessionRule):
    role_id: int


class SessionRole(BaseModel):
    name: constr(strip_whitespace=True, max_length=128)
    rules: Optional[List[SessionRule]]
    icon: Optional[Union[
        stricturl(allowed_schemes={'http', 'https'}, max_length=512),
        pathlib.Path
    ]]
    children: Optional[List[SessionRole]]


class CreateSession(BaseModel):
    name: constr(strip_whitespace=True, max_length=128)
    description: Optional[constr(strip_whitespace=True, max_length=2048)]
    roles: conlist(SessionRole, min_items=1)


class EditSession(BaseModel):
    name: constr(strip_whitespace=True, max_length=128)
    description: Optional[constr(strip_whitespace=True, max_length=2048)]
    rules: List[SessionRuleWithRole]


class SelectSessionTime(BaseModel):
    offset: confloat(ge=0, le=168)
    duration: confloat(ge=0, le=168)
    timezone: constr(strip_whitespace=True, max_length=512)


# ---- Signups ----
class SignupTime(BaseModel):
    offset: confloat(ge=0, le=168)
    duration: confloat(ge=0, le=168)
    timezone: constr(strip_whitespace=True, max_length=512)


class SignupRole(BaseModel):
    role_id: int
    weight: int


class EditSignup(BaseModel):
    times: List[SignupTime]
    roles: List[SignupRole]


# forward refs
SessionRole.update_forward_refs()
