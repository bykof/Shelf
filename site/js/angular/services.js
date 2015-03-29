var module = angular.module("shelfModule");
var loaderTexts = [
    "Wasche die Hardware mit Seife...",
    "Suche Rechnungen in der Mülltone...",
    "Mache Yoga...",
    "Versuche die Maus zu fangen...",
    "Suche ANY KEY auf der Tastatur...",
    "Fixe schnell ein paar Bugs...",
    "Suche schnell die Codezeilen...",
    "Versuche mich mit 127.0.0.1 zu verbinden...",
    "Gehe kurz schlafen...",
];

module.service("loaderTexts", function() {
    this.getRandomText = function() {
        return loaderTexts[Math.floor((Math.random() * loaderTexts.length) + 0)];
    }
});