# from flask import abort, render_template
# from flask_login import login_required

# from src.models.barbershops import Barbershop


# @login_required
# def barbershops(barbershop_id):
#     barbershops = Barbershop.query.filter_by(id=barbershop_id).first() or abort(
#         404, "Barbearia não encontrada."
#     )
#     return render_template("barbershops.html", barbershops=barbershops)
