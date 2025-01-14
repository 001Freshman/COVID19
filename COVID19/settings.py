"""
Django settings for COVID19 project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import pymongo
import pymysql
import pandas as pd

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-df*ce25qal#^&2245v^&jh!o0$#7_w1o1e@252y7!va0o@8^tn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'COVID19.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'COVID19.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PROVINCES = ['黑龙江', '上海', '内蒙古', '吉林', '辽宁', '河北', '天津', '山西', '陕西', '甘肃', '宁夏', '青海', '新疆', '西藏', '四川', '重庆',
             '山东', '河南', '江苏', '安徽', '湖北', '浙江', '福建', '江西', '湖南', '贵州', '广西', '海南', '广东', '北京', '云南', '香港',
             '澳门', '台湾']
COUNTRIES = ['Afghanistan【阿富汗】', 'Albania【阿尔巴尼亚】', 'Algeria【阿尔及利亚】', 'Andorra【安道尔】', 'Angola【安哥拉】',
             'Antigua and Barbuda【安提瓜和巴布达】', 'Argentina【阿根廷】', 'Armenia【亚美尼亚】', 'Australia【澳大利亚】',
             'Austria【奥地利】', 'Azerbaijan【阿塞拜疆】', 'Bahrain【巴林】', 'Bangladesh【孟加拉】', 'Barbados【巴巴多斯】',
             'Belarus【白俄罗斯】', 'Belgium【比利时】', 'Belize【伯利兹】', 'Benin【贝宁】', 'Bhutan【不丹】', 'Bolivia【玻利维亚】',
             'Bosnia and Herz.【波黑】', 'Botswana【博茨瓦纳】', 'Brazil【巴西】', 'Bulgaria【保加利亚】', 'Burkina Faso【布基纳法索】',
             'Burundi【布隆迪】', 'Cambodia【柬埔寨】', 'Cameroon【喀麦隆】', 'Canada【加拿大】', 'Cape Verde【佛得角】',
             'Central African Rep.【中非共和国】', 'Chad【乍得】', 'Chile【智利】', 'China【中国】', 'Colombia【哥伦比亚】',
             'Comoro【科摩罗】', 'Congo【刚果（布）】', 'Costa Rica【哥斯达黎加】', 'Croatia【克罗地亚】', 'Cuba【古巴】', 'Cyprus【塞浦路斯】',
             'Czech Rep.【捷克】', 'Dem. Rep. Congo【刚果（金）】', 'Denmark【丹麦】', 'Djibouti【吉布提】', 'Ecuador【厄瓜多尔】',
             'Egypt【埃及】', 'El Salvador【萨尔瓦多】', 'Eq. Guinea【赤道几内亚】', 'Eritrea【厄立特里亚】', 'Estonia【爱沙尼亚】',
             'Ethiopia【埃塞俄比亚】', 'Fiji【斐济】', 'Finland【芬兰】', 'France【法国】', 'Gabon【加蓬】', 'Gambia【冈比亚】',
             'Georgia【格鲁吉亚】', 'Germany【德国】', 'Ghana【加纳】', 'Greece【希腊】', 'Grenada【格林纳达】', 'Guatemala【危地马拉】',
             'Guinea-bissau【几内亚比绍】', 'Guinea【几内亚】', 'Guyana【圭亚那】', 'Haiti【海地】', 'Honduras【洪都拉斯】',
             'Hungary【匈牙利】', 'Iceland【冰岛】', 'India【印度】', 'Indonesia【印度尼西亚】', 'Iran【伊朗】', 'Iraq【伊拉克】',
             'Ireland【爱尔兰】', 'Israel【以色列】', 'Italy【意大利】', 'Ivory Coast【科特迪瓦】', 'Jamaica【牙买加】', 'Japan【日本本土】',
             'Jordan【约旦】', 'Kazakhstan【哈萨克斯坦】', 'Kenya【肯尼亚】', 'Korea【韩国】', 'Kuwait【科威特】', 'Kyrgyzstan【吉尔吉斯斯坦】',
             'Lao PDR【老挝】', 'Latvia【拉脱维亚】', 'Lebanon【黎巴嫩】', 'Lesotho【莱索托】', 'Liberia【利比里亚】', 'Libya【利比里亚】',
             'Lithuania【立陶宛】', 'Luxembourg【卢森堡】', 'Macedonia【北马其顿】', 'Madagascar【马达加斯加】', 'Malawi【马拉维】',
             'Malaysia【马来西亚】', 'Maldive【马尔代夫】', 'Mali【马里】', 'Malta【马耳他】', 'Marshall Is.【马绍尔群岛】',
             'Mauritania【毛里塔尼亚】', 'Mauritius【毛里求斯】', 'Mexico【墨西哥】', 'Moldova【摩尔多瓦】', 'Monaco【摩纳哥】',
             'Mongolia【蒙古】', 'Montenegro【黑山】', 'Morocco【摩洛哥】', 'Mozambique【莫桑比克】', 'Myanmar【缅甸】',
             'Namibia【纳米比亚】', 'Nepal【尼泊尔】', 'Netherlands【荷兰】', 'New Zealand【新西兰】', 'Nicaragua【尼加拉瓜】',
             'Nigeria【尼日利亚】', 'Niger【尼日尔】', 'Norway【挪威】', 'Oman【阿曼】', 'Pakistan【巴基斯坦】', 'Panama【巴拿马】',
             'Papua New Guinea【巴布亚新几内亚】', 'Paraguay【巴拉圭】', 'Peru【秘鲁】', 'Philippines【菲律宾】', 'Poland【波兰】',
             'Portugal【葡萄牙】', 'Qatar【卡塔尔】', 'Romania【罗马尼亚】', 'Russia【俄罗斯】', 'Rwanda【卢旺达】', 'San.Marino【圣马力诺】',
             'Saudi Arabia【沙特阿拉伯】', 'Senegal【塞内加尔】', 'Serbia【塞尔维亚】', 'Seychelles【塞舌尔】', 'Sierra Leone【塞拉利昂】',
             'Singapore【新加坡】', 'Slovakia【斯洛伐克】', 'Slovenia【斯洛文尼亚】', 'Solomon Is.【所罗门群岛】', 'Somalia【索马里】',
             'South Africa【南非】', 'Spain【西班牙】', 'Sri Lanka【斯里兰卡】', 'St.Lucia【圣卢西亚】', 'Sudan【苏丹】',
             'Suriname【苏里南】', 'Swaziland【斯威士兰】', 'Sweden【瑞典】', 'Switzerland【瑞士】', 'Syria【叙利亚】',
             'Tajikistan【塔吉克斯坦】', 'Tanzania【坦桑尼亚】', 'Thailand【泰国】', 'Togo【多哥】', 'Trinidad and Tobago【特立尼达和多巴哥】',
             'Tunisia【突尼斯】', 'Turkey【土耳其】', 'Uganda【乌干达】', 'Ukraine【乌克兰】', 'United Kingdom【英国】',
             'United States【美国】', 'Uruguay【乌拉圭】', 'Uzbekistan【乌兹别克斯坦】', 'Vanuatu【瓦努阿图】', 'Vatican【梵蒂冈】',
             'Venezuela【委内瑞拉】', 'Vietnam【越南】', 'Yemen【也门】', 'Zambia【赞比亚】', 'Zanzibar【韩国】', 'Zimbabwe【津巴布韦】']

mongo_client = pymongo.MongoClient(host="localhost", port=27017)
mongo_world = mongo_client.covid19.world
mongo_migration = mongo_client.covid19.migration
mongo_china = mongo_client.covid19.china
mongo_provinces = mongo_client.covid19.province

world_name = pd.read_sql('select * from zh2en', pymysql.connect(
    host='localhost',
    user='root',
    passwd='19834044876',
    db='covid19',
    port=3306,
    charset='utf8'
))
