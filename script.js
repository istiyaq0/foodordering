function placeOrder(menuItem, price) {
    fetch("/order", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `menu_item=${menuItem}&price=${price}`,
    })
        .then((response) => response.json())
        .then((data) => {
            alert(data.message);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}  

