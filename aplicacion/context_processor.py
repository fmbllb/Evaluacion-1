def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        carrito = request.session.get("carrito", [])
        if isinstance(carrito, list):
            for item in carrito:
                try:
                    total += item.get("cantidad", 0) * item.get("precio", 0)
                except (TypeError, KeyError):
                    continue
    return {"total_carrito": total}

