from pydantic import BaseModel


class NotificationsBase(BaseModel):
    name: str
    active: bool

    class Config:
        orm_mode = True


class Notifications(NotificationsBase):
    id: int

    class Config:
        from_attributes: True
        orm_mode = True


class updateNotificationStatus(BaseModel):
    value: bool
