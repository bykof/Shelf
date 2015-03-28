var module = angular.module("shelfModule");

module.controller("OrderListController", function($rootScope, $scope, Restangular, loaderTexts) {
    if (!$.cookie("djangocookie")) {
        return
    }

    getOrdersByPage(1, "");

    $scope.pageChanged = function(newPageNumber) {
        getOrdersByPage(newPageNumber, "");
    };

    $scope.$watch("orderSearch", function(newValue, oldValue) {
        if (newValue && newValue.length >= 3) {
            getOrdersByPage(1, newValue);
        } else {
            if(oldValue.length >= 3 && newValue.length < oldValue.length) {
                getOrdersByPage(1, "")
            }
        }
    });

    function getOrdersByPage(pageNumber, searchString) {
        var listLoader = $("#list-loader");
        $scope.loaderText = loaderTexts.getRandomText();
        listLoader.addClass("active");
        if (searchString != "") {
            Restangular.one("orders").get({"page": pageNumber, "search": searchString}).then( function(response) {
                $scope.totalOrders = response.count;
                $scope.orders = response.results;
                listLoader.removeClass("active");
            });
        } else {
            Restangular.one("orders").get({"page": pageNumber}).then( function(response) {
                $scope.totalOrders = response.count;
                $scope.orders = response.results;
                listLoader.removeClass("active");
            });
        }

    };
});