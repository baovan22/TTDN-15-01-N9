from odoo import models, fields

class LoaiVanBan(models.Model):
    _name = "loai_van_ban"
    _description = "Danh Mục Loại Văn Bản"
    _rec_name = "ten_loai"

    ten_loai = fields.Char(string="Tên Loại Văn Bản", required=True)
    mo_ta = fields.Text(string="Mô Tả")