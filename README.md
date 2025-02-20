# calculator
# "Калькулятор для расчета калорий или денег"
*Программа рассчитывает остаток денег/калорий на сегодня, 
потраченных денег или съеденных калорий за сегодня/за неделю.*

# Создание виртуального окружения для python3.11.4

1. Скачайте python:
    ```
    wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
    ```

2. Распакуйте архив и перейдите в распакованную директорию:
    ```
    tar -xvf Python-3.11.4.tgz
    cd Python-3.11.4/
    ```
   
3. Запустите следующую команду проверки зависимостей для установки python3.11.4:
    ```
    sudo ./configure --enable-optimizations
    ```
   
4. Затем запустите команду make, чтобы скомпилировать исходный код Python:
    ```
    sudo make -j $(nproc)
    ```

5. Запустите команду для альтернативной установки python3.11.4 чтобы не затирать системную версию python:
    ```
    sudo make altinstall
    ```

6. Для создания виртуального окружения используем следующую команду:
    ```
    python3.11 -m venv venv
    ```