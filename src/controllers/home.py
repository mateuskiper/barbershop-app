from flask import abort, render_template


def index():
    products = {}
    return render_template("index.html", products=products)


# def product(product_id):
#     product = Product.query.filter_by(id=product_id).first() or abort(
#         404, "produto nao encontrado"
#     )
#     return render_template("product.html", product=product)