var module = angular.module("shelfModule");

module.run( function($rootScope, $location) {
    $rootScope.addMessage = function(message){
        $rootScope.info_message = message;
        $(".info-message-nag").nag("show");
        setTimeout(function() {
            $(".info-message-nag").nag("hide");
            $(".info-message-nag").nag("clear");
        }, 3000)
    };
    }).run (function(Restangular, GlobalService) {
    Restangular.setBaseUrl(GlobalService.apiServer);
    Restangular.setRequestSuffix('/');
});