from models import db, SubscriptionSchedule


def get_subscription_schedules():
    return SubscriptionSchedule.query.all()


def create_subscription_schedule(data):
    new_schedule = SubscriptionSchedule(**data)
    db.session.add(new_schedule)
    db.session.commit()
    return new_schedule
