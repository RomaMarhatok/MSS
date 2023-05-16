from faker.providers import BaseProvider


class DoctorSpecializationProvider(BaseProvider):
    __provider__ = "doctor_specialization"
    __lang__ = "ru_RU"

    doctor_specializations = [
        "Терапевт",
        "Педиатр",
        "Отоларинголого",
        "Окулист",
        "Дераматолог",
        "Хирург",
        "Ортопед",
        "Неврапотолог",
        "Каридиолог",
        "Фтизиатр",
        "Психиатр",
    ]

    @classmethod
    def specialization(cls) -> str:
        return cls.random_element(cls.doctor_specializations)
