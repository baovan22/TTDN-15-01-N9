from odoo import models, fields

class DuTruKinhPhi(models.Model):
    _name = "du_tru_kinh_phi"
    _description = "Dự Trù Kinh Phí"

    name = fields.Char(string="Tên Khoản Chi", required=True)
    so_tien = fields.Float(string="Số Tiền", required=True)
    mo_ta = fields.Text(string="Mô Tả")

    cong_viec_ids = fields.Many2many("cong_viec", string="Công Việc")
