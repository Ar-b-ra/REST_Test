const form = document.getElementById("deposit-form");
const calculateButton = document.getElementById("calculate-button");
const resultDiv = document.getElementById("result");

calculateButton.addEventListener("click", (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const depositData = {
        date: formData.get("date"),
        periods: parseInt(formData.get("periods")),
        amount: parseInt(formData.get("amount")),
        rate: parseInt(formData.get("rate")),
    };
    console.log('Request data:', depositData); // Add this line for debugging
    fetch("/deposit", {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(depositData),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        if (data.error) {
            resultDiv.innerText = `Error: ${data.error}`;
        } else {
            resultDiv.innerText = `Result: ${JSON.stringify(data)}`;
        }
    })
    .catch((error) => {
        console.error('Request error:', error); // Add this line for debugging
        resultDiv.innerText = `Error: ${error.message}`;
    });
});