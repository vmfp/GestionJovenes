# -*- coding: utf-8 -*-

import pytz
from odoo import models, fields, api
from datetime import timedelta, datetime, date


class YoungDashboard(models.Model):
    _inherit = 'young.curriculum.vitae'


    @api.model
    def total_young(self):
        #import ipdb; ipdb.set_trace()

        query = '''select count(*) from young_curriculum_vitae'''
        cr = self._cr
        cr.execute(query)
        count_young = cr.fetchall()
        total_young = count_young[0][0]

        cr.execute(""" select count(*) from young_curriculum_vitae where id in (select cv_id from young_insertion) """)
        job_obt = cr.fetchall()
        total_job = job_obt[0][0]

        cr = self._cr
        query_cat_list = '''select count(*) from young_curriculum_vitae where id not in (select cv_id from young_insertion)'''
        cr.execute(query_cat_list)
        desem_total = cr.fetchall()

        cr = self._cr
        query_cat_list = '''select count(*)from young_curriculum_vitae where cat_list in ('A','B','C','D','E','F')'''
        cr.execute(query_cat_list)
        cat_list = cr.fetchall()

        cr = self._cr
        query_cat_list = '''select count(*)from young_curriculum_vitae where cat_list in ('A','B','C','D')'''
        cr.execute(query_cat_list)
        em_cat = cr.fetchall()

        query_e = """select count(*)from young_curriculum_vitae where cat_list = 'E' """
        cr.execute(query_e)
        e = cr.fetchall()

        query_g = """select count(*)from young_curriculum_vitae where cat_list = 'G' """
        cr.execute(query_g)
        g = cr.fetchall()

        query_a = """select count(*)from young_curriculum_vitae where cat_list = 'A' """
        cr.execute(query_a)
        a = cr.fetchall()

        query_b = """select count(*)from young_curriculum_vitae where cat_list = 'B' """
        cr.execute(query_b)
        b = cr.fetchall()

        query_c = """select count(*)from young_curriculum_vitae where cat_list = 'C' """
        cr.execute(query_c)
        c = cr.fetchall()

        query_d = """select count(*)from young_curriculum_vitae where cat_list = 'D' """
        cr.execute(query_d)
        d = cr.fetchall()

        query_f = """select count(*)from young_curriculum_vitae where cat_list = 'F' """
        cr.execute(query_f)
        f = cr.fetchall()

        query_no = """select count(*)from young_curriculum_vitae where cat_list = 'no category' """
        cr.execute(query_no)
        no_category = cr.fetchall()


        return {'total_young': total_young,
                'total_job': total_job,
                'job_category':cat_list[0][0],
                'back_study':e[0][0],
                'entrepreneurship':g[0][0],
                'category_a': a[0][0],
                'category_b': b[0][0],
                'category_c': c[0][0],
                'category_d': d[0][0],
                'category_e': e[0][0],
                'category_f': f[0][0],
                'desem_total': desem_total[0][0],
                'em_cat': em_cat[0][0],
                'no_category':no_category[0][0]}


    @api.model
    def get_categories(self):
        cr = self._cr
        query_a = """select count(*)from young_curriculum_vitae where cat_list = 'A' """
        cr.execute(query_a)
        a = cr.fetchall()

        query_b = """select count(*)from young_curriculum_vitae where cat_list = 'B' """
        cr.execute(query_b)
        b = cr.fetchall()

        query_c = """select count(*)from young_curriculum_vitae where cat_list = 'C' """
        cr.execute(query_c)
        c = cr.fetchall()

        query_d = """select count(*)from young_curriculum_vitae where cat_list = 'D' """
        cr.execute(query_d)
        d = cr.fetchall()

        query_e = """select count(*)from young_curriculum_vitae where cat_list = 'E' """
        cr.execute(query_e)
        e = cr.fetchall()

        query_f = """select count(*)from young_curriculum_vitae where cat_list = 'F' """
        cr.execute(query_f)
        f = cr.fetchall()

        query_g = """select count(*)from young_curriculum_vitae where cat_list = 'G' """
        cr.execute(query_g)
        g = cr.fetchall()

        query_no = """select count(*)from young_curriculum_vitae where cat_list = 'no category' """
        cr.execute(query_no)
        no_category = cr.fetchall()

        category = ['A','B','C','D','E','F','G','Sin Categoria']

        total = [a[0][0],b[0][0],c[0][0],d[0][0],e[0][0],f[0][0],g[0][0],\
                 no_category[0][0]]

        final = [total, category]
        return final


    @api.model
    def get_gender(self):
        cr = self._cr
        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'male' """)
        male = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'female' """)
        female = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'other' """)
        other = cr.fetchall()

        gender = ['Masculino','Femenino','Otros']

        total = [male[0][0],female[0][0],other[0][0]]

        final = [total, gender]
        return final

    @api.model
    def get_other_graph(self):
        label = 'Edad de Jóvenes'

        cr = self._cr
        cr.execute(""" select count(*) from young_curriculum_vitae where age >= 16 AND age <= 17 """)
        g1 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where age >= 16 AND age <= 17 AND id in (select cv_id from young_insertion) """)
        g11 = cr.fetchall()


        cr.execute(""" select count(*) from young_curriculum_vitae where age >= 18 AND age <= 30 """)
        g2 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where age >= 18 AND age <= 30 AND id in (select cv_id from young_insertion) """)
        g22 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where age > 30 """)
        g3 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where age > 30 AND id in (select cv_id from young_insertion) """)
        g33 = cr.fetchall()

        age = ['16-17','18-30','> 30']

        total = [g1[0][0],g2[0][0],g3[0][0]]
        total2 = [g11[0][0],g22[0][0],g33[0][0]]

        final = [total, age, label, total2]
        return final



    @api.model
    def unemployed(self):
        cr = self._cr
        cr.execute(""" select count(*) from young_curriculum_vitae where id not in (select cv_id from young_insertion) """)
        unemp = cr.fetchall()


        return {'total_sale': unemp[0][0],
             'total_order_count': 0,
             'total_refund_count': 0,
             'total_session': 0,
             'today_refund_total': 0,
             'today_sale': 0,}

    @api.model
    def job_placement(self, ):
        cr = self._cr
        query = """select count(*)from young_curriculum_vitae where cat_list in ('A','B','C','D','E','F')"""
        cr.execute(query)
        placement = cr.fetchall()

        return {'total_placement':placement[0][0]}

    @api.model
    def get_bygrade(self):
        cr = self._cr
        cr.execute(""" select count(*) from young_curriculum_vitae where civil_status = 'single' """)
        basic = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where civil_status = 'married' """)
        secun = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where civil_status = 'concubine' """)
        superi = cr.fetchall()

        grade = ['Soltero','Casado','Unión Libre']

        total = [basic[0][0],secun[0][0],superi[0][0]]

        final = [total, grade]
        return final

    @api.model
    def get_gender_empleo(self):
        label = 'Genero x Empleo'

        cr = self._cr
        cr.execute(""" select count(*) from young_curriculum_vitae where gender =  'male' """)
        g1 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender =  'male' AND id in (select cv_id from young_insertion) """)
        g11 = cr.fetchall()


        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'female' """)
        g2 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'female'  AND id in (select cv_id from young_insertion) """)
        g22 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'other' """)
        g3 = cr.fetchall()

        cr.execute(""" select count(*) from young_curriculum_vitae where gender = 'other' AND id in (select cv_id from young_insertion) """)
        g33 = cr.fetchall()

        gender = ['Masculino','Femenino','Otro']

        total = [g1[0][0],g2[0][0],g3[0][0]]
        total2 = [g11[0][0],g22[0][0],g33[0][0]]

        final = [total, gender, label, total2]
        return final



         