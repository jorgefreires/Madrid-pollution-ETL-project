import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def unir(lista_meses):

    # Esta funcion une todos los archivos de original_data en un solo df limpio

    dfs = []

    for e in lista_meses:   

        df = pd.read_csv(f'../original_data/{e}', delimiter=';')
    
        dfs.append(df)

    # Se unen todos los df de los distintos meses en uno solo

    total = pd.concat(dfs, ignore_index=True)

    total.columns = [col.lower() for col in total.columns]   # Se ponen los nombres de las columnas en minúsculas por comodidad

    # Es siempre la misma provincia y municipio y el punto de muestre es redundante pues se tienen datos sobre la estacion, por lo que se borran estos datos

    total.drop(['provincia', 'municipio', 'punto_muestreo'], axis=1, inplace=True)

    '''
    Todas las columnas del estilo v01 muestran si los datos están validados o no. Se borran puesto que hay muy pocos no 
    validados(30 de 3960 para noviembre de 2022) y además se considera que los datos importan aunque no esten validados
    '''

    for e in total.columns:

        if 'v' in e: total.drop([e], axis=1, inplace=True)
        else: pass

    # Las columnas de la hora se cambian por la hora como id del 1 al 24

    total.rename(columns={'h01': '1', 
                          'h02': '2',
                          'h03': '3',
                          'h04': '4',
                          'h05': '5',
                          'h06': '6',
                          'h07': '7',
                          'h08': '8',
                          'h09': '9',
                          'h10': '10',
                          'h11': '11',
                          'h12': '12',
                          'h13': '13',
                          'h14': '14',
                          'h15': '15',
                          'h16': '16',
                          'h17': '17',
                          'h18': '18',
                          'h19': '19',
                          'h20': '20',
                          'h21': '21',
                          'h22': '22',
                          'h23': '23',
                          'h24': '24'
                          }, inplace=True)

    # Se crea una nueva columna idnicando un id para la unidad de medida de cada magniud

    total.insert(2, 'unidad_medida', 0)

    for row in range(len(total)):

        if total.magnitud.iloc[row] == 1: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 6: total.unidad_medida.iloc[row] = 2
        elif total.magnitud.iloc[row] == 7: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 8: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 12: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 9: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 10: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 14: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 20: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 30: total.unidad_medida.iloc[row] = 1
        elif total.magnitud.iloc[row] == 35: total.unidad_medida.iloc[row] = 1
        else: pass

    return total


def scrapping():

    # Se instala y se define el driver de chrome

    PATH = ChromeDriverManager().install()     

    driver=webdriver.Chrome(PATH) 

    # Se entra en la página web para crear una lista que contiene todos los datos requeridos

    url = 'https://www.eltiempo.es/calidad-aire/madrid#pollution_table'

    driver.get(url)

    time.sleep(5)

    try: #cookies
        driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]/span').click()

    except: pass

    time.sleep(5)

    driver.execute_script("window.scrollBy(0, 1200);")

    time.sleep(5)

    datos = [e.text for e in driver.find_elements(By.TAG_NAME, 'span')]

    driver.quit()

    # Se obtienen los datos sobre la cantidad de los contaminantes y sus medidas unidades de medida

    no2_pespa = datos[364]
    so2_pespa = datos[366]
    co_pespa = datos[370]
    o3_aguirre = datos[272]
    no2_aguirre = datos[274]
    so2_aguirre = datos[276]
    pm25_aguirre = datos[278]
    pm10_aguirre = datos[280]
    co_aguirre = datos[282]
    o3_soria = datos[188]
    no2_soria = datos[190]
    o3_villaverde = datos[446]
    no2_villaverde = datos[448]
    o3_farolillo = datos[286]
    no2_farolillo = datos[288]
    pm10_farolillo = datos[292]
    o3_campo = datos[218]
    no2_campo = datos[220]
    pm25_campo = datos[223]
    pm10_campo = datos[225]
    o3_barajas = datos[198]
    no2_barajas = datos[200]
    o3_carmen = datos[374]
    no2_carmen = datos[376]
    so2_carmen = datos[378]
    co_carmen = datos[382]
    no2_moratalaz = datos[342]
    so2_moratalaz = datos[344]
    pm10_moratalaz = datos[347]
    no2_cuatro = datos[242]
    pm25_cuatro = datos[245]
    pm10_cuatro = datos[247]
    o3_pilar = datos[208] 
    no2_pilar = datos[210] 
    no2_vallecas = datos[387] 
    pm10_vallecas = datos[391] 
    no2_mendez = datos[331]
    pm25_mendez = datos[334]
    pm10_mendez = datos[336]
    no2_castellana = datos[231]
    pm25_castellana = datos[234]
    pm10_castellana = datos[236]
    o3_retiro = datos[404]
    no2_retiro = datos[406]
    no2_castilla = datos[353]
    pm25_castilla = datos[356]
    pm10_castilla = datos[358]
    o3_ensanche = datos[262] 
    no2_ensanche = datos[264] 
    no2_embajada = datos[437]
    pm10_embajada = datos[441]
    no2_sanchi = datos[415]
    pm25_sanchi = datos[418]
    pm10_sanchi = datos[420]
    o3_pardo = datos[252]
    no2_pardo = datos[254]
    o3_juan = datos[309]
    no2_juan = datos[311]
    o3_olivos = datos[425]
    no2_olivos = datos[427]
    pm10_olivos = datos[431]

    # Se hace una lista para almacenar los valores de los id de las estaciones

    estaciones = [4,4,4,8,8,8,8,8,8,16,16,17,17,18,18,18,24,24,24,24,27,27,35,35,35,35,36,36,36,38,38,38,39,39,40,40,47,47,47,48,48,48,49,49,50,50,50,
    54,54,55,55,57,57,57,58,58,59,59,60,60,60]

    # Se hace una lista para los valores de las magnitudes

    magnitudes = [8,1,6,14,8,1,9,10,6,14,8,14,8,14,8,10,14,8,9,10,14,8,14,8,1,6,8,1,10,8,9,10,14,8,8,10,8,9,10,8,9,10,14,8,8,9,10,14,8,8,10,8,9,10,
    14,8,14,8,14,8,10]

    # Se hace una lista con los valores

    variables = [    no2_pespa,    so2_pespa,    co_pespa,    o3_aguirre,    no2_aguirre,    so2_aguirre,    pm25_aguirre,    pm10_aguirre,    co_aguirre,    o3_soria,    no2_soria,    o3_villaverde,    no2_villaverde,    o3_farolillo,    no2_farolillo,    pm10_farolillo,    o3_campo,    no2_campo,    pm25_campo,    pm10_campo,    o3_barajas,    no2_barajas,    o3_carmen,    no2_carmen,    so2_carmen,    co_carmen,    no2_moratalaz,    so2_moratalaz,    pm10_moratalaz,    no2_cuatro,    pm25_cuatro,    pm10_cuatro,    o3_pilar,    no2_pilar,    no2_vallecas,    pm10_vallecas,    no2_mendez,    pm25_mendez,    pm10_mendez,    no2_castellana,    pm25_castellana,    pm10_castellana,    o3_retiro,    no2_retiro,    no2_castilla,    pm25_castilla,    pm10_castilla,    o3_ensanche,    no2_ensanche,    no2_embajada,    pm10_embajada,    no2_sanchi,    pm25_sanchi,    pm10_sanchi,    o3_pardo,    no2_pardo,    o3_juan,    no2_juan,    o3_olivos,    no2_olivos,    pm10_olivos]

    valores = []

    for e in variables: valores.append(e.split(' ')[0])

    # Se hace una lista con sus unidades de medida según su id

    unidades_medida = []

    for e in variables: 

        if e.split(' ')[1] == 'ug/m3': e = 1

        else: e = 2
        
        unidades_medida.append(e)

    # Se hacen listas para el año, mes, día y hora

    año = [datos[185][-4:] for i in range(len(variables))]

    mes = [datos[185][13:15] for i in range(len(variables))]

    dia = [datos[185][10:12] for i in range(len(variables))]

    hora = [datos[185][:2] for i in range(len(variables))]

    # Se crea un df para almacenar los datos del scrapping

    data = {
        'estacion': estaciones,
        'magnitud': magnitudes,
        'unidad_medida': unidades_medida,
        'ano': año,
        'mes': mes,
        'dia': dia,
        'hora': hora,
        'valor': valores
    }

    data = pd.DataFrame(data)

    # Se cambian los tipos de datos

    for e in data:
        
        try: data[e] = data[e].astype('int64')

        except: data[e] = data[e].astype('float64')

    return data