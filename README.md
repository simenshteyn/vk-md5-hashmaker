# vk-md5-hashmaker
Console program, designed to create MD5-hashed text file, available for import into Vkontakte Ads Manager.

Vk-md5-hashmaker — консольная программа, предназначенная для создания текстового MD5 файла. Запустите программу и введите название текстового файла для импорта (например, in.txt). В исходном текстовом файле электронные адреса и/или номера телефонов должны располагаться по одному на строке. Программа приводит их в формат, совместимый с vk, шифрует в хэш MD5 и сохраняет в отдельный файл.

Под Windows доступен установщик в MSI формате. Порядок работы:
1) Установите программу из MSI пакета.
2) Скопируйте исходный файл для обработки в папку с установленной программой (это должен быть текстовый файл, каждый номер/электронный адрес на новой строке);
3) Запустите программу vk-md5-hashmaker.exe
4) Введние в консоли название файла, например in.txt и нажмите Enter;
5) Программа обработает записи в файле и создаст хэш файл для импорта в vk.
