from django.db import models


class BaseProduct(models.Model):
    price = models.PositiveIntegerField(default= 0, verbose_name = 'Цена')
    title = models.CharField(max_length = 50, verbose_name = 'Название')
    description = models.TextField(max_length=5000, verbose_name = 'Описание')
    image = models.ImageField(default = 'images/default.png',upload_to = 'images/', verbose_name = 'Фото')
    is_active = models.BooleanField(default=True, verbose_name ='Активен ли')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено')
    quantity = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Количество')

    def __str__(self):
        return self.title

class Computer(BaseProduct):
    cpu = models.CharField(max_length = 50, verbose_name = 'Процессор')
    gpu = models.CharField(max_length = 50, verbose_name = 'Видеокарта')
    ram = models.PositiveSmallIntegerField(verbose_name = 'Количество ОЗУ')
    memory = models.PositiveSmallIntegerField(verbose_name = 'Количество памяти')
    motherboard = models.CharField(max_length = 50, verbose_name = 'Матринская плата')
    fan = models.CharField(max_length = 50, verbose_name = 'Охлаждение')
    power = models.PositiveSmallIntegerField(verbose_name = 'Блок питания')

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'


class GPU(BaseProduct):
    clock = models.PositiveSmallIntegerField(verbose_name = 'Частота видеочипа')
    turbo_clock = models.PositiveSmallIntegerField(verbose_name = 'Турбочастота')
    connection_interface = models.CharField(max_length = 50, verbose_name = 'Интерфейс подключения')
    video_memory = models.PositiveSmallIntegerField(verbose_name = 'Объем видеопамяти')

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'


class CPU(BaseProduct):
    model = models.CharField(max_length = 50, verbose_name = 'Модель')
    socket = models.CharField(max_length = 50, verbose_name = 'Сокет')
    release = models.CharField(max_length = 50, verbose_name = 'Дата релиза')
    cors = models.PositiveSmallIntegerField(verbose_name = 'Количество ядер')
    streams = models.PositiveSmallIntegerField(verbose_name = 'Количество потоков')

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class RAM(BaseProduct):
    type = models.CharField(max_length = 50, verbose_name = 'Тип памяти')
    total_memory = models.PositiveSmallIntegerField(verbose_name = 'Суммарный объем памяти')
    module_memory = models.PositiveSmallIntegerField(verbose_name = 'Объем одного модуля памяти')
    clock_frequency = models.PositiveSmallIntegerField(verbose_name = 'Тактовая частота')
    voltage = models.PositiveSmallIntegerField(verbose_name = 'Напряжение питания')

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'


class BOX(BaseProduct):
    TYPE_BOX = (
        ('Mini-ITX', 'Mini-ITX'),
        ('MicroATX', 'MicroATX'),
        ('Midi Tower', 'Midi Tower'),
        ('Full Tower', 'Full Tower')
    )

    box_type = models.CharField(choices=TYPE_BOX, verbose_name = 'Типоразмер корпуса')
    length = models.PositiveSmallIntegerField(verbose_name = 'Длина')
    width = models.PositiveSmallIntegerField(verbose_name = 'Ширина')
    height = models.PositiveSmallIntegerField(verbose_name = 'Высота')
    weight = models.PositiveSmallIntegerField(verbose_name = 'Вес')

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'


class Monitor(BaseProduct):
    TYPE_MONITOR = (
        ('CRT', 'ЭЛТ'),
        ('LCD', 'ЖК'),
        ('PDP', 'Плазменный'),
        ('LED', 'LED-монитор'),
        ('OLED', 'OLED-монитор'),
        ('VRD', 'Виртуальные ретинальные дисплеи'),
    )

    diagonal = models.CharField(choices=TYPE_MONITOR, verbose_name = 'Диагональ')
    length = models.PositiveSmallIntegerField(verbose_name = 'Тип монитора')
    max_fps = models.PositiveSmallIntegerField(verbose_name = 'Макс. частота кадров')
    game_monitor = models.BooleanField(default = False, verbose_name = 'Игровой монитор')
    response_time = models.PositiveSmallIntegerField(verbose_name = 'Время отклика')

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'


class Mouse(BaseProduct):
    TYPE_SENSOR = (
        ('Optical LED', 'оптический светодиодный'),
        ('Optical laser', 'Оптический лазерный'),
        ('Doppler Shift', 'сенсор с технологией Doppler Shift'),
    )

    sensor_type = models.CharField(choices=TYPE_SENSOR, verbose_name = 'Тип сенсора')
    sensor_resolution = models.PositiveSmallIntegerField(verbose_name = 'Разрешение датчика')
    polling_frequency = models.PositiveSmallIntegerField(verbose_name = 'Частота опроса')
    speed = models.BooleanField(default = False, verbose_name = 'Скорость')
    maximum_acceleration = models.PositiveSmallIntegerField(verbose_name = 'Максимальное ускорение')

    class Meta:
        verbose_name = 'Мышь'
        verbose_name_plural = 'Мыши'


class Keyboard(BaseProduct):
    TYPE_SWITCHES = (
        ('Linear', 'Линейные'),
        ('Tactile', 'Тактильные'),
        ('Clicking', 'Щелкающие'),
    )

    type_switches = models.CharField(choices=TYPE_SWITCHES, verbose_name = 'Тип переключателей')
    keycaps_material = models.CharField(max_length = 50, verbose_name = 'Материал кейкапов')
    life_cycle = models.PositiveSmallIntegerField(verbose_name = 'Жизненный цикл')
    pressing_force = models.PositiveSmallIntegerField(verbose_name = 'Сила нажатия')
    programmable_keys = models.BooleanField(default = False, verbose_name = 'Программируемые клавиши')


    class Meta:
        verbose_name = 'Клавиатура'
        verbose_name_plural = 'Клавиатуры'
