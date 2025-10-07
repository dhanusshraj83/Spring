document.getElementById("scanBtn").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      function: () => document.body.innerText,
    },
    async (results) => {
      const text = results[0].result;

      // 👇 Connect to your backend here
      const response = await fetch("http://localhost:8000/api/phishing-check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: text }),
      });

      const result = await response.json();

      document.getElementById("result").innerText = result.is_phishing
        ? `⚠️ ${result.message}`
        : "✅ Safe Page";
    }
  );
});
