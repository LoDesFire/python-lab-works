function displayLocalTime() {
    const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const date = new Date();
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };
    const localTime = date.toLocaleString("ru-RU", options);
    document.getElementById("timezone").textContent = "Таймзона: " + userTimezone;
    document.getElementById("local-time").textContent = "Время: " + localTime;
}
