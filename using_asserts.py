# Dangerous code!

def delete_product(user, product_id):
    assert user.is_admin()
    user.delete_product(product_id)


# Handle this properly by raising an error

def delete_product(user, product_id):
    if not user.is_admin():
        raise AuthError("User must have admin privileges")
    else:
        user.delete_product(product_id)
