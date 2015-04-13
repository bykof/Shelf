var module = angular.module("shelfModule");

module.controller("BodyController", function($scope, $location, Restangular, $route) {
    $scope.menuClass = function(page) {
        var current = $location.path().indexOf(page);
        return current > -1 ? "active" : "";
    };

    $scope.login = function() {
        var loginModel = $scope.loginModel;
        if (loginModel) {
            Restangular
                .one("api-token-auth")
                .post("", {"username": loginModel.username, "password": loginModel.password})
                .then( function (response) {
                    var token = response.token;
                    $.cookie("djangocookie_username", loginModel.username, { expires: 1, path: '/'});
                    $.cookie("djangocookie", token, { expires: 1, path: '/'});
                    Restangular.setDefaultHeaders({"Authorization": "Token " + token});
                    $scope.loginModel = null;
                    $("#login-form-container").hide();
                    $("#page-content").show();
                    $route.reload();
                }, function(response) {
                    console.log("Error");
                });
        }
    };

    if (!$.cookie("djangocookie")) {
        initLoginForm();
    } else {
        $("#page-content").show();
        $("#login-form-container").hide();
        Restangular.setDefaultHeaders({"Authorization": "Token " + $.cookie("djangocookie")});
    }

    $scope.logout = function() {
        $.removeCookie("djangocookie");
        Restangular.setDefaultHeaders({});
        initLoginForm();
    };

    function initLoginForm() {
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
    }

    $('.dropdown').dropdown();
});