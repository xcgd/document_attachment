from openerp.osv import fields, osv


class admin_doc_type(osv.Model):
    """Kind of an administrative document employees have to provide."""

    _name = 'admin_doc.type'

    _columns = {
        'name': fields.char('Description', size=256, required=True),
    }


class admin_doc(osv.Model):
    """An administrative document employees have to provide.
    Inherit[s] from ir.attachment to store documents as attachments.
    """

    _name = 'admin_doc'

    _inherits = {
        'ir.attachment': 'file_id',
    }

    _columns = {
        'type_id': fields.many2one('admin_doc.type',
                                   'Type',
                                   required=True),
        'file_id': fields.many2one('ir.attachment',
                                   'File',
                                   ondelete='cascade',
                                   required=True),
    }

    def create(self, cr, uid, vals, context=None):
        """- Fill the "name" from the original filename.
        - Associate the new attachment with the current employee.
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

        return super(admin_doc, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        """Fill the "name" from the original filename."""

        if 'datas_fname' in vals:
            vals['name'] = vals['datas_fname']

        return super(admin_doc, self).write(cr, uid, ids, vals,
                                            context=context)

    def unlink(self, cr, uid, ids, context=None):
        """Delete the attachment associated with records being deleted."""

        brs = self.browse(cr, uid, ids, context=context)
        attachment_ids = [br.file_id.id for br in brs]

        ret = super(admin_doc, self).unlink(cr, uid, ids, context=context)

        attachment_obj = self.pool.get('ir.attachment')
        attachment_obj.unlink(cr, uid, attachment_ids, context=context)

        return ret
