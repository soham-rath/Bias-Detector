const LOCAL_API_URL = "http://127.0.0.1:5000/analyze";

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message && message.action === "analyze") {
    (async () => {
      try {
        const response = await fetch(LOCAL_API_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: message.text }),
        });

        if (!response.ok) {
          const txt = await response.text().catch(() => "");
          sendResponse({
            ok: false,
            error: `API error ${response.status}: ${txt}`,
          });
          return;
        }

        const data = await response.json();
        sendResponse({ ok: true, result: data });
      } catch (err) {
        sendResponse({ ok: false, error: String(err) });
      }
    })();
    return true;
  }

  if (message && message.action === "ping") {
    sendResponse({ ok: true, version: "1.0.0" });
  }
});
