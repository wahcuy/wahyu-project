let cart = [];

function addToCart(product, price) {
    cart.push({ product, price });
    displayCart();
}

function displayCart() {
    const cartList = document.getElementById('cart-list');
    const totalPriceElement = document.getElementById('total-price');
    cartList.innerHTML = '';
    let totalPrice = 0;

    cart.forEach((item, index) => {
        totalPrice += item.price;
        const li = document.createElement('li');
        li.textContent = `${item.product} - IDR ${item.price.toLocaleString()}`;
        cartList.appendChild(li);
    });

    totalPriceElement.textContent = `Total: IDR ${totalPrice.toLocaleString()}`;
}
