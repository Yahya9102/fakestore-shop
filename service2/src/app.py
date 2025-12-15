from flask import Flask, render_template




def show_products():

## ÖVNING
## SKRIV KOD FÖR ATT GÖRA ANROP MOT SERVICE 1
## RENDERA SVARET I VÅR HTML SIDA


    products = resp.json()
    return render_template("products.html", products=products) 



