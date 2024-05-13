const elements = {
    backLink: document.querySelectorAll(".back-link")
}


function doBackLink() {
    elements.backLink.forEach((item) => {
        item.addEventListener("click", (evt) => {
            evt.preventDefault();
            window.history.go(-1);
        });
    });
}

document.addEventListener("DOMContentLoaded", (evt) => {
    console.log("DOM loaded");
    doBackLink();
});