class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, traning_type: str, duration: float, distance: float, speed: float, calories: float) -> None:
        self.traning_type = traning_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    
    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; ' 
                f'Дистанция: {self.distance:.3f} км; ' 
                f'Ср. скорость: {self.speed:.3f} км/ч; ' 
                f'Потрачено ккал: {self.calories:.3f}.'
        )



class Training:
    """Базовый класс тренировки."""

    def __init__(self, action: int, duration: float, weight: float, LEN_STEP: float, M_IN_KM: int) -> None:               # Кол-во совершенных действий duration: float,            # Длительность тренировки
                 
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
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:       # расчёт количества потраченных калорий за тренировку
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:      # создание объекта сообщения о результатах тренировки
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):            # Бег
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    time_min = 60
    
    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2)
                * self.weight / self.M_IN_KM * (self.duration * self.time_min))


class SportsWalking(Training):      # Спортивная ходьба
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, LEN_STEP: float, M_IN_KM: int, height: float) -> None:

        super().__init__(self, action: int, duration: float, weight: float)

        self.height = height
        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029
        time_min = 60

        def get_spent_calories(self) -> float:
            return ((self.coeff_calorie_3 + self.weight + (self.get_distance() 
                    ** 2 // self.height) * self.coeff_calorie_4 * self.weight)
                    * (self.duration * self.time_min))

class Swimming(Training):           # Плавание
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, LEN_STEP: float, M_IN_KM: float, length_pool: float, count_pool: int) -> None:
        super().__init__(self, action: int, duration: float, weight: float)
        self.LEN_STEP = 1.38
        self.length_pool = length_pool
        self.count_pool = count_pool
        coeff_calorie_5 = 1.1
        coeff_calorie_6 = 2

    def get_distance(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.coeff_calorie_5) * self.coeff_calorie_6 * self.weight



    
        
    
    



def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_class = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return dict_class(workout_type, data)
    


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

