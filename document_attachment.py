from openerp.osv import fields, osv
from openerp.tools.translate import _


class document_attachment_type(osv.Model):
    """Kind of document that can be attached."""

    _name = 'document_attachment.type'

    _columns = {
        'name': fields.char(
            'Description',
            size=256,
            required=True
        ),

        'model': fields.char(
            'Model',
            size=128,
            required=True,
        ),
    }


class document_attachment(osv.Model):
    """A document that can be attached.
    Inherit[s] from ir.attachment to store documents as attachments.
    """

    _name = 'document_attachment'

    _inherits = {
        'ir.attachment': 'file_id',
    }

    _columns = {
        'type_id': fields.many2one(
            'document_attachment.type',
            'Type',
            required=True
        ),

        'file_id': fields.many2one(
            'ir.attachment',
            'File',
            ondelete='cascade',
            required=True
        ),
    }

    def create(self, cr, uid, vals, context=None):
        """- Fill the "name" from the original filename.
        - Associate the new attachment with the current object.
        """

        if not 'res_model' in context:
            raise osv.except_osv(
                _('Programming Error'),
                _("You must send the 'res_model' through the m2m context"),
            )
        if not 'res_id' in context:
            raise osv.except_osv(
                _('Programming Error'),
                _("You must send the 'res_id' through the m2m context"),
            )

        vals['name'] = vals['datas_fname']

        vals['res_model'] = context['res_model']
        vals['res_id'] = context['res_id']

        return super(document_attachment, self).create(
            cr, uid, vals, context=context
        )

    def write(self, cr, uid, ids, vals, context=None):
        """Fill the "name" from the original filename."""

        if 'datas_fname' in vals:
            vals['name'] = vals['datas_fname']

        return super(document_attachment, self).write(
            cr, uid, ids, vals, context=context
        )

    def unlink(self, cr, uid, ids, context=None):
        """Delete the attachment associated with records being deleted."""

        brs = self.browse(cr, uid, ids, context=context)
        attachment_ids = [br.file_id.id for br in brs]

        ret = super(document_attachment, self).unlink(
            cr, uid, ids, context=context
        )

        attachment_obj = self.pool.get('ir.attachment')
        attachment_obj.unlink(cr, uid, attachment_ids, context=context)

        return ret
