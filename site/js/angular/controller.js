var module = angular.module("shelfModule");

module.controller("BodyController", function($rootScope, $scope, $location, Restangular) {
    $scope.menuClass = function(page) {
        var current = $location.path().substring(1);
        return page === current ? "active" : "";
    };

    $scope.login = function() {
        var loginModel = $scope.loginModel;
        if (loginModel) {
            Restangular
                .one("api-token-auth")
                .post("", {"username": loginModel.username, "password": loginModel.password})
                .then( function (response) {
                    var token = response.token;
                    $.cookie("djangocookie", token, { expires: 1, path: '/'});

                    $("#login-form-container").hide();
                    $("#page-content").show();
                    $rootScope.$broadcast('authorized');
                }, function(response) {
                    console.log("Error");
                });
        }
    };

    if (!$.cookie("djangocookie")) {
        $("#page-content").hide();
        $("#login-form-container").show();

        $(document).keypress(function(e) {
            if(e.which == 13) {
                $scope.login();
            }
        });

        $(".submit").click( function() {
            $scope.login();
        });
    } else {
        $("#page-content").show();
        $("#login-form-container").hide();
        Restangular.setDefaultHeaders({"Authorization": "Token " + $.cookie("djangocookie")});
        $rootScope.$broadcast("authorized");
    }
});