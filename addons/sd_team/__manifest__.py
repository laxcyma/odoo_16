{
    'name': "sd_hospital_management",
    'author': "shalini",
    'sequence': -100,
    'category': 'Tutorials',
    'summary': "SD hospital management system",
    'depends': ["mail","sale"],
    'data': [
        "views/menu.xml",
        "views/patient.xml",
        "security/ir.model.access.csv",
        # "static/src/js/script.js",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
    #  To adding static files
    'assets': {
        'web.assets_backend': [
            'sd_team/static/src/js/script.js',
            # 'sd_team/static/src/js/action_call.js',
            # 'sd_team/static/src/xml/tree_button.xml',
                               ],
       #  'web.assets_frontend': ['sd_team/static/src/js/script.js']
    },
}
