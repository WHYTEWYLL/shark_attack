import pandas as pd
import numpy as np
import re

def arreglatitulo(df):
    """
    Como su nombre indica, dado un dataframe, filtra y reduce las posibles anomalias de sus 
    column names
    """
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(r'[^a-z]',"")
    df.columns=df.columns.str.replace("fatalyn","fatal")
    return df

def solomeses(df_no_unamed):
    """
    Para un dataframe, donde una de sus columnas se llama date,
    obtiene todos los valores realcionados con los meses del año.
    """
    df_no_unamed['date']=df_no_unamed['date'].str.extract(r'([A-z]+)' , expand=False)
    meses=["Jul" ,"Aug","Sep" ,"Jun" ,"Oct" ,"Jan" ,"Apr", "Dec"," May"," Mar","Nov","Feb"]  
    df_no_unamed=df_no_unamed[df_no_unamed['date'].isin(meses)]
    return df_no_unamed

def clentype(value):
    """
    Clasifica los valores en Unprovoked and Provoked dado un Pandas.Serie.
    """
    if str(value) not in ["Unprovoked","Provoked"]:
        value="Unprovoked"
        return str(value)
    return str(value)

def countries1(value):
    """
    Comprueba si los valores de  Pandas.Serie , son uno de los paises registrado.
    """
    countries=['UNITED STATES','USA', 'AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA', 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA AND HERZEGOWINA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REP', 'CHAD', 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS ISLANDS', 'COLOMBIA', 'COMOROS', 'CONGO', 'COOK ISLANDS', 'COSTA RICA', 'COTE D`IVOIRE', 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'DENMARK', 'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH POLYNESIA', 'FRENCH S. TERRITORIES', 'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HONDURAS', 'HONG KONG', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', 'KOREA (NORTH)', 'KOREA (SOUTH)', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAU', 'MACEDONIA', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'REUNION', 'ROMANIA', 'RUSSIAN FEDERATION', 'RWANDA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'ST VINCENT/GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME', 'SAUDI ARABIA', 'SENEGAL', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA', 'SPAIN', 'SRI LANKA', 'ST. HELENA', 'ST.PIERRE', 'SUDAN', 'SURINAME', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIAN ARAB REPUBLIC', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'TOGO', 'TOKELAU', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VATICAN CITY STATE', 'VENEZUELA', 'VIET NAM', 'VIRGIN ISLANDS (BRITISH)', 'VIRGIN ISLANDS (U.S.)', 'WESTERN SAHARA', 'YEMEN', 'YUGOSLAVIA', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE']
    value1=str(value).upper()
    if value1 not in countries:
        return "unknown"
    else:
        if value1=='UNITED STATES' or value1=='USA':
            return 'USA'
        return str(value)

def cleanactivity(value):
    """
    Obtiene todas las actividades que acaben en -ing dado un Pandas.Series, y si no 
    lo clasifica como Others, sino esta en nuestra lista de actividades.
    """
    activity=re.findall(r'\b(\w+ing)\b',str(value))
    if activity:
        if activity[0]  in ["Surfing","Swimming","Spearfishing","Fishing","Diving","Fishing"]:
            return str(activity[0]).capitalize()
        else:
            return "Others"


def sexclean(value):
    """
    Agrupa todos los valores , si son M / F. Segun si los valores en la Pandas.Serie contiene 
    dichas F o M
    """
    age=re.findall(r'[F|M]{1}',str(value))
    if age:
        return str(age[0])
    else:
        if (lambda value: value):
            return "F"
        return str(value)

def cleanage(value):
    """
    Agrupa todos los valores de dos digitos de edad para un Pandas.Series.
    """
   
    age=re.findall(r'\d{2}',str(value))
    if age:
        return int(age[0])
    else:
        if (lambda value: value):
            return 0
        return int(value)

def cleaninjury(values):
    """
    Clasifica los datos de un Pandas.Series en funcion de si contiene la
    palabra Fatal o no.
    """
    values=values.lower()
    fatal=re.findall('fatal',values)
    if fatal:
        return "Fatal"
    else:
        return "No Fatal"

def cleantime(value):
    """
    Clasifica los datos de un Pandas.Series en funcion de la hora
    entre morning','afternoon','night'
    """
    if str(value).lower() in ['morning','afternoon','night']:
        return str(value).capitalize()
    else:
        hora=re.findall(r'(\d{2})h', value)
        if hora:
                if int(hora[0])>=7 and int(hora[0])<12:
                    return "Morning"
                elif int(hora[0])>=12 and int(hora[0])<18:
                    return "Afternoon"
                else:
                    return "Evening"
        else:
            dia=re.findall(r'(afternoon| morning | evening)', value)
            if dia:
                return str(dia[0]).capitalize()
            else:
                return "Evening"