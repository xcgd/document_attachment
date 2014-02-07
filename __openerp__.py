# -*- coding: utf-8 -*-
{
    'name': 'Document Attachment',
    'version': '1.0',
    'author': 'XCG Consulting',
    'category': 'Dependency',
    'description': """Enchancements to the ir.attachment module
to manage kinds of attachments that can be linked with OpenERP objects.

The implenter has to:
 - Pass 'res_model' and 'res_id' in the context.
 - Define menus and actions should it want to allow changing document types.
    """,
    'website': 'http://www.openerp-experts.com',
    'depends': [
        'base',
        'document',
    ],
    'data': [
        'document_attachment.xml',
    ],
    'test': [
    ],
    'installable': True,
}
