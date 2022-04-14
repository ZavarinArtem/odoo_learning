{
    'name': 'Tutorial theme',
    'summary': "Test module for learning purpose",
    'description': 'A description for your theme.',

    'author': "S.P.O.C",
    'website': "https://spoc.com.ua/",
    'license': "LGPL-3",

    'category': 'Theme/Creative',
    'version': '15.0.1.1.2',

    'depends': ['website', ],
    'data': [
        'views/layout.xml',
        'views/pages.xml',
    ],
    'assets': {
        'web.assets_frontend': {
            '/theme_tutorial/static/scss/style.scss',
        },
        'web._assets_primary_variables': {
            '/theme_tutorial/static/scss/primary_variables.scss',
        },
        'web._assets_frontend_helpers': {
            '/theme_tutorial/static/scss/bootstrap_overridden.scss',
        },
    },
}
