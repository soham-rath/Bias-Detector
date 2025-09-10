(async function () {
  const bodyText = document.body.innerText;

  const response = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: bodyText }),
  });
  const result = await response.json();

  if (result.label === "Negative") {
    const regex = /\b(violence|war|hate|danger|attack)\b/gi;
    document.body.innerHTML = document.body.innerHTML.replace(
      regex,
      (match) => `<span style="background-color:yellow">${match}</span>`
    );
  }
})();
