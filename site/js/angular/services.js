var module = angular.module("shelfModule");
var loaderTexts = [
    "Wasche die Hardware mit Seife...",
    "Suche Rechnungen in der Mülltone...",
    "Mache Yoga..."
];

module.service("loaderTexts", function() {
    this.getRandomText = function() {
        return loaderTexts[Math.floor((Math.random() * loaderTexts.length) + 0)];
    }
});