const elements = {
    backLink: document.querySelectorAll(".back-link"),
    messageAlerts: document.querySelectorAll(".message-alert"),
}


function doBackLink() {
    elements.backLink.forEach((item) => {
        item.addEventListener("click", (evt) => {
            evt.preventDefault();
            window.history.go(-1);
        });
    });
}

// Alerts auto hide
function autoHideMessageAlert(time, alert) {
    setTimeout(() => {
        alert.close()
    }, time);
}

function autoHideMessageAlertsAll(time, alerts) {
    const alertList = [...alerts].map(element => new bootstrap.Alert(element))
    alertList.forEach((item) => {
        autoHideMessageAlert(time, item);
    });
}

document.addEventListener("DOMContentLoaded", (evt) => {
    console.log("DOM loaded");
    doBackLink();
    autoHideMessageAlertsAll(3000, elements.messageAlerts);
});