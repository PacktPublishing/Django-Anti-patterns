<!-- Bad practice: Complex template logic -->
{% if user.is_authenticated %}
    {% if user.orders.count > 0 %}
        <h2>Orders</h2>
        <ul>
            {% for order in user.orders %}
                <li>{{ order.product }} - {{ order.quantity }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No orders yet.</p>
    {% endif %}
{% endif %}