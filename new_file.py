class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,                # Кол-во совершенных действий
                 duration: float,            # Длительность тренировки
                 weight: float,              # Вес спортсмена
                 LEN_STEP: float,            # Расстояние, за 1 шаг или гребок
                 M_IN_KM: int               # Для перевода значений из метров в км
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000
        
    
        

    def get_distance(self) -> float:            # расчёт дистанции, которую пользователь преодолел за тренировку
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM
         

    def get_mean_speed(self) -> float:         # расчёт средней скорости движения во время тренировки
        """Получить среднюю скорость движения."""
        return (self.action * self.LEN_STEP / self.M_IN_KM) / self.duration

    def get_spent_calories(self) -> float:       # расчёт количества потраченных калорий за тренировку
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:      # создание объекта сообщения о результатах тренировки
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):            # Бег
    """Тренировка: бег."""
    def __init__(self,
                 action: int,                # Кол-во совершенных действий
                 duration: float,            # Длительность тренировки
                 weight: float,              # Вес спортсмена
                 LEN_STEP: float,            # Расстояние, за 1 шаг или гребок
                 M_IN_KM: int               # Для перевода значений из метров в км
                 ) -> None:

                duration_minute = self.duration / 60



        return ((18 * ((self.action * self.LEN_STEP / self.M_IN_KM) / self.duration) - 20)) * self.weight / M_IN_KM * duration_minute
                  


class SportsWalking(Training):      # Спортивная ходьба
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: int,
                 M_IN_KM: int,
                 height: int) -> None:
                    
        super().__init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: int,
                 M_IN_KM: int
                 )
        self.height = height       

    


class Swimming(Training):           # Плавание
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

