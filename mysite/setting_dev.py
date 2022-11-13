
from .settings_common import *

SECRET_KEY = 'wu8)t=aa@gra@v90cb)#n_he)p(@rj9jirilwcry346vdly4x@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    #ロガー設定
    'loggers': {
        #Django利用のロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        #diaryアプリケーション利用のロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    #ハンドラ設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    #フォーマッタ設定
    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
