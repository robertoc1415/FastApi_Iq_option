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

    API = IQ_Option('bagoberto1370@gmail.com', 'Auto3113226598')

    API.connect()
    MODE = "PRACTICE" # PRACTICE / REAL
    API.change_balance(MODE) 

    BA = API.get_balance()
    BACA = API.get_currency()
    B = API.get_server_timestamp()

    # par="EURUSD"
    # par="EURUSD-OTC"
    # timeframe=1
    # timeframe2=1
    # entradaa = 1


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



    # order,id_buy=API.buy_digital_spot("EURUSD",100000,"call",1)
    # if order:
    #     order =True
    #     while True:
    #         check, win =API.check_win_digital_v2(id_buy)
    #         if check == True:
    #             break
    #         time.sleep(1)
    #             #resultado,lucro = API.check_win_v3(id)
    #     if win > 0:
    #         print("gancia de", win)
    #     elif win < 0:
    #         print("perdida de", win)
    #         quit()
    #     else:
    #         print("error al abrir operacion", id)

    #     print("\n")
    par = 'EURUSD'
    # entrada = 40000
    # direcao = 'call'
    # timeframe = 1 #apartir de 1 minuto en adelante

    # status,id = API.buy(entrada, par, direcao, timeframe)

    # # statuss,id_buy = API.buy(entrada, par, "call", timeframe)
    # if status == True:
    #     resultado,lucro = API.check_win_v3(id)
    # # if status==True:
    #     # resultado,lucro = API.check_win_v2(id)
    #     # resultado,lucro = API.check_win_v3(id_buy)
        
    #     print('RESULTADO: '+resultado+' / LUCRO: '+str(round(lucro, 2)))

    # if status:
    #     status =False
    #     while status ==False:
    #         status, lucro =API.check_win_digital_v2(id)
    #             #resultado,lucro = API.check_win_v3(id)
    #         if lucro > 0:
    #             print("gancia de", lucro)
    #         elif lucro < 0:
    #             print("perdida de", lucro)
    #             quit()
    # else:
    #         print("error al abrir operacion", id)

    # print("\n")


    # if status:
    #     status =False
    #     while status ==False:
    #             status, lucro =API.check_win_v3(id)
    #             #resultado,lucro = API.check_win_v3(id)
    #     if lucro > 0:
    #             print("gancia de", lucro)
    #     elif lucro < 0:
    #             print("perdida de", lucro)
    #             quit()
    #     else:
    #         print("error al abrir operacion", id)

    #     print("\n")



    check,id = API.buy(100000, "EURUSD", "call", 1)
    print("start check win please wait")
    polling_time=3
    print(API.check_win_v3(id))
    print(API.check_win_v2(id,polling_time))


    # def entrada(par, dir, timeframe2):
    #     global API

    #     print("abriendo operacion")

    #     #status, id =API.buy_digital_spot_v2(par, dir, timeframe2)
    #     status, id =API.buy(100000, par, dir, timeframe2)

    #     if status:
    #         status =False
    #         while status ==False:
    #             status, lucro =API.check_win_v3(id,polling_time=3)
    #             #resultado,lucro = API.check_win_v3(id)
    #         if lucro > 0:
    #             print("gancia de", lucro)
    #         else:
    #             print("perdida de", lucro)
    #     else:
    #         print("error al abrir operacion", id)

    #     print("\n")



    # print("\n")

    # while True:
    #     # df=get_data(par,1,200)
    #     # taxa, color=mova(df,20)
    #     # ssma_3=TA.SSMA(df,3)
    #     # ssma_50=TA.SSMA(df,50)

    #     if True:#ssma_3.iloc[-1] <= ssma_50.iloc[-1] and ssma_3.iloc[-2] > ssma_50.iloc[-2] and color=='red':
    #         entrada(par,'put',timeframe2=1)
    #     elif ssma_3.iloc[-1] >= ssma_50.iloc[-1] and ssma_3.iloc[-2] < ssma_50.iloc[-2] and color=='green':
    #         entrada(par,'call',timeframe2)
        
    #     print(f"[{datetime.now().strftime('%H:%M:%S')}]:: Esperando oportunidad", end="\r")