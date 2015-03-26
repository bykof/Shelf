var module = angular.module("shelfModule");

module.controller("BodyController", function($scope, $location) {
    $scope.menuClass = function(page) {
        var current = $location.path().substring(1);
        return page === current ? "active" : "";
    };
});