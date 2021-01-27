from odoo import models, fields, api


class DietFactsProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    calories = fields.Integer("calories")
    servingsize = fields.Float("serving size")
    lastupdate = fields.Date("last update")
    dietitem = fields.Boolean("diet item")
    product_template_nutiriton = fields.One2many("product.template.nutiriton", "product_id", "Nutrient")

class DietFacts_Res_User_Meal(models.Model):
    _name = "res.users.meal"
    mealdate = fields.Datetime("meal date")
    name = fields.Char("meal name")
    mealuser = fields.Many2one("res.users", "user meal")
    notes = fields.Text("notes")
    item_id = fields.One2many("res.users.mealitem", "meal_id")
    totalcalories = fields.Integer(string="Total Meal Calories", store=True, compute="_calccolaries")

    @api.depends("item_id")
    def _calccolaries(self):
        currentcalories = 0
        for itemcalories in self.item_id:
            currentcalories = currentcalories + (itemcalories.calories * itemcalories.servings)
            self.totalcalories = currentcalories


class DietFacts_Res_User_Mealitem(models.Model):
        _name = "res.users.mealitem"
        meal_id = fields.Many2one("res.users.meal")
        meal_item = fields.Many2one("product.template", "meal item")
        servings = fields.Float("serving size")
        notes = fields.Text("notes meal item")
        calories = fields.Integer(related="meal_item.calories", string="calories per item", store=True, readonly=True)

class DietFacts_nutrition_menu(models.Model):
        _name = "nutrition.item"
        unitofmeasure = fields.Many2one("uom.uom", "Unit Of Measure")
        name = fields.Char("Name Nutrient")
        describe = fields.Text("notes meal item")

class DietFacts_nutrition_page(models.Model):
    _name = "product.template.nutiriton"
    nutrient_id = fields.Many2one("nutrition.item", "Nutrient")
    product_id = fields.Many2one("product.template", "Product_Name")
    value = fields.Float("Value")
    uom = fields.Char(related="nutrient_id.unitofmeasure.name", string="Unit Of Measure", readonly=True)





