import os

from .settings_common import *

#本番環境用セキュリティキーを生成し環境変数からの読み込みを行う
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

#デバッグモードを有効にするかどうか（本番時：False）
DEBUG = False

#許可するホスト名リスト
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
#静的ファイルの配置場所
STATIC_ROOT = '/user/share/nginx/html/static'
MEDIA_ROOT = '/user/share/nginx/html/media'

#Amazon SES関連設定
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

#ロギング
LOGGING = {
    'version': 1,
    'desable_existing_loggers':False,
    #ロガー設定
    'loggers':{
        #Django利用のロガー
        'django':{
            'handlers': ['file'],
            'level':'INFO',
        },
        #diaryアプリケーション利用のロガー
        'diary': {
            'handlers': ['file'],
            'level':'INFO',
        },
    },

    #ハンドラ設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRoatatingFileHandler',
            'formatter':'prod',
            'when': 'D', #ログローテーション間隔単位(D=day)
            'interval': 1, #ログローテーション単位(1日単位)
            'backupCount': 7, #保存しておくログファイル数
        },
    },

    #フォーマッタの設定
    'formatters':{
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
