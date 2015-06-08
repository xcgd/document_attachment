# -*- coding: utf-8 -*-
##############################################################################
#
#    Document Attachment, for OpenERP
#    Copyright (C) 2013 XCG Consulting (http://odoo.consulting)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Document Attachment',
    'version': '1.4',
    'author': 'XCG Consulting',
    'category': 'Hidden/Dependency',
    'description': """Enchancements to the ir.attachment module
to manage kinds of attachments that can be linked with OpenERP objects.

The implenter has to:
 - Pass 'res_model' and 'res_id' in the context.
 - Define menus and actions should it want to allow changing document types.

Document attachments are displayed in a many2many field; it can optionally be
changed to work like a one2many field by using the
"domain="[('res_id', '=', id)]" attribute.
    """,
    'website': 'http://odoo.consulting/',
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
