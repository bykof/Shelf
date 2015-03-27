var module = angular.module("shelfModule");

module.controller("OrderListController", function($rootScope, $scope, Restangular) {
    if (!$.cookie("djangocookie")) {
        return
    }

    $scope.orders = Restangular.all("orders").getList().$object;
});