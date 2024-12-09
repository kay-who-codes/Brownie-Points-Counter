// Load points from localStorage
let points = parseInt(localStorage.getItem("browniePoints")) || 0;

// Update the display
const pointsDisplay = document.getElementById("points-display");
pointsDisplay.textContent = `Brownie Points: ${points}`;

// Handle increment button click
document.getElementById("increment-button").addEventListener("click", () => {
    points += 1;
    pointsDisplay.textContent = `Brownie Points: ${points}`;
    localStorage.setItem("browniePoints", points);
});

// Handle reset button click
document.getElementById("reset-button").addEventListener("click", () => {
    points = 0;
    pointsDisplay.textContent = `Brownie Points: ${points}`;
    localStorage.removeItem("browniePoints"); // Clear the value from localStorage
});
