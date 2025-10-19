document.getElementById('predictForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    pregnancies: +document.getElementById('pregnancies').value,
    glucose: +document.getElementById('glucose').value,
    bp: +document.getElementById('bp').value,
    skin: +document.getElementById('skin').value,
    insulin: +document.getElementById('insulin').value,
    bmi: +document.getElementById('bmi').value,
    dpf: +document.getElementById('dpf').value,
    age: +document.getElementById('age').value
  };

  try {
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    const container = document.getElementById('result-container');
    const posCard = document.getElementById('positive-card');
    const negCard = document.getElementById('negative-card');

    // Reset visibility
    posCard.style.display = 'none';
    negCard.style.display = 'none';
    container.classList.remove('hidden');

    // Show only the relevant card
    if (result.prediction === "Positive") {
      posCard.style.display = 'block';
      document.getElementById('positive-prob').textContent = result.probability + "%";
    } else {
      negCard.style.display = 'block';
      document.getElementById('negative-prob').textContent = result.probability + "%";
    }
  } catch (error) {
    console.error("Prediction error:", error);
  }
});
