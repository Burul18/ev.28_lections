# # Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# # батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# # Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# # При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# # Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# # полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# # разряжен).
# # Также предусмотрите возможность заряжания батареи.

# class Phone:
#     def __init__(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery_level = 100

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен')
#         print(f'Уровень заряда: {self.__battery_level}')
#         self.__battery_level -= 0.5

#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен!')
#         print(f'OS: {self.__os}, imei: {self.__imei}')
#         self.__battery_level -= 0.5

#     def play_music(self):
#         if self.__battery_level < 5:
#             raise Exception('Телефон разряжен')
#         print('Слушаем Мирбека Атабекова')
#         self.__battery_level -= 5

#     def play_video(self):
#         if self.__battery_level < 10:
#             raise Exception('Телефон разряжен')
#         print('Смотрим видосы Кани на платформе')
#         self.__battery_level -= 7

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M%S')
#         while now().strftime('%M%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level += 1
#             print(f'Идет заряд вашей батареи. Ваш уровень батареи: {self.__battery_level}')


# phone = Phone('123 12313 123', 'iOS 15')
# phone.battery_level
# phone.battery_level
# phone.get_info
# phone.play_music
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.battery_level
# phone.charge_battery(3)

