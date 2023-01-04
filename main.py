if __name__ == '__main__':
    print("Hello, World!")

    from iqoptionapi.stable_api import IQ_Option
    import time, json, datetime, tzlocal
    from dateutil import tz
    #from datetime import datetime as dt
    from datetime import datetime
    from time import time, sleep
    import sys
    import numpy as np
    from talib.abstract import *
    import pandas as pd
    from finta import TA


    #coneccion
    #API = IQ_Option('robertocsm1220@gmail.com', 'R3113226598')

    API = IQ_Option('roberto.isajar@uao.edu.co', 'Auto3113226598')

    API.connect()
    MODE = "PRACTICE" # PRACTICE / REAL
    API.change_balance(MODE) 

    BA = API.get_balance()
    BACA = API.get_currency()
    B = API.get_server_timestamp()

    par="EURUSD"
    # par="EURUSD-OTC"
    timeframe=1
    timeframe2=1
    entradaa = 1


    # Looping para realizar a verificação se a API se conectou corretamente ou se deve tentar se conectar novamente

    while True:
        if API.check_connect() == False:
            print('Error al conectar')
            
            # No video é apresentado a função reconnect(), mas nas versão mais novas da API ela não está mais disponivel, sendo assim deve ser utilizado API.connect() para realizar a conexão novamente
            API.connect()
        else:
            print('Conectado')
            break
        
        time.sleep(1) 

    #print("Saldo actual: ",BA," ",BACA) 
    print("Saldo actual: ",BA," ",BACA)