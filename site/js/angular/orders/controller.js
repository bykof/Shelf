var module = angular.module("shelfModule");
var searchTimer = false;

module.controller("OrderListController", function($rootScope, $scope, $timeout, Restangular, loaderTexts) {
    if (!$.cookie("djangocookie")) {
        return
    }

    getOrdersByPage(1);

    $scope.pageChanged = function(newPageNumber) {
        getOrdersByPage(newPageNumber);
    };

    $scope.clearOrderSearch = function() {
        $scope.orderSearch = "";
    }

    $scope.$watch("orderSearch", function(newValue, oldValue) {
        if (newValue && newValue.length >= 3) {
            if(searchTimer){
                $timeout.cancel(searchTimer);
            }

            searchTimer = $timeout(function(){
                getOrdersByPage(1);
            }, 1000);

            $("#search-delete-icon").removeClass("search");
            $("#search-delete-icon").addClass("remove circle");
        } else {
            if(oldValue && oldValue.length >= 3 && newValue.length < oldValue.length) {
                getOrdersByPage(1)
            }
            $("#search-delete-icon").addClass("search");
            $("#search-delete-icon").removeClass("remove circle");
        }
    });

    function getOrdersByPage(pageNumber) {
        var listLoader = $("#list-loader");
        $scope.loaderText = loaderTexts.getRandomText();
        listLoader.addClass("active");
        if ($scope.orderSearch != "" || $scope.orderSearch.length >= 3) {
            Restangular.one("orders").get({"page": pageNumber, "search": $scope.orderSearch}).then( function(response) {
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