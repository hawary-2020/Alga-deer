{
    'name': 'Hospital management',
    'version': '1.1',
    'sequence': -100,
    'description': """
    Management of health care 
    """,
    'category': 'Services,Hospital',
    'website': 'https://www.hospital.com',
    'application': True,
    'depends': ['mail', 'project'],
    'data': [
        '/odoo/custom/Hospital/security/ir.model.access.csv',
        '/odoo/custom/Hospital/views/menu.xml',
        '/odoo/custom/Hospital/views/patient.xml',
        '/odoo/custom/Hospital/views/appointment.xml',
        '/odoo/custom/Hospital/views/laboratory.xml',
        '/odoo/custom/Hospital/views/kids.xml',
        '/odoo/custom/Hospital/views/doctors.xml',
    ],
    'summary': 'health care system',
}
