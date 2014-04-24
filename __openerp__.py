# -*- coding: utf-8 -*-
{
    'name': 'Document Attachment',
    'version': '1.1.3',
    'author': 'XCG Consulting',
    'category': 'Dependency',
    'description': """Enchancements to the ir.attachment module
to manage kinds of attachments that can be linked with OpenERP objects.

The implenter has to:
 - Pass 'res_model' and 'res_id' in the context.
 - Define menus and actions should it want to allow changing document types.

Document attachments are displayed in a many2many field; it can optionally be
changed to work like a one2many field by using the
"domain="[('res_id', '=', id)]" attribute.
    """,
    'website': 'http://www.openerp-experts.com',
    'depends': [
        'base',
        'document',
    ],
    'data': [
        'security/ir.model.access.csv',
        'document_attachment.xml',
    ],
    'test': [
    ],
    'installable': True,
}
