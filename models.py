

class Schedule(object):
    def __init__(self, name: str, time: str, place: str, cost: str) -> None:
        self.name = name
        self.time = time
        self.place = place
        self.cost = cost


class Choreographer(object):
    def __init__(self, name: str, image: str, description: str, instagram: str, schedules) -> None:
        # name = 'Danelya'
        self.name = name
        # image = '/static_data/Danelya.jpg'
        self.image = image
        # description = 'Danelya - это танцор, хореограф, преподаватель, победитель многих танцевальных конкурсов, в том числе и международных. Основатель и ведущий хореограф танцевального проекта "Dance with Danelya".'
        self.description = description
        # instagram = '@danelya_dance'
        self.instagram = instagram
        # schedules = [Schedule('Salsa', '18:00', '1000'), Schedule('Salsa', '18:00', '1000')]
        self.schedules = schedules
