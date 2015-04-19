var module = angular.module("shelfModule");

module.controller("InvoiceListController", function($scope, Restangular) {
    Restangular.one("invoice-documents").get().then( function(response) {
        $scope.invoice_documents = response;
    });
});