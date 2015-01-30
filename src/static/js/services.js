var shelfModule = angular.module("shelf");

shelfModule.service("articleService", function($http, $q) {
    $http.defaults.headers.common['X-CSRFToken'] = $.cookie('csrftoken');

    return ({
        getArticles: getArticles,
        getArticle: getArticle
    });

    function getArticles() {
        var request = $http({
            method: "get",
            url: "api/articles/?format=json"
        });

        return request.then(handleSuccess, handleError);
    }

    function getArticle(id) {
        var request = $http({
            method: "get",
            url: "api/articles/" + id + "/?format=json"
        });

        return request.then(handleSuccess, handleError);
    }

    function handleError( response ) {
        if (
            ! angular.isObject( response.data ) ||
            ! response.data.message
            ) {
            return( $q.reject( "An unknown error occurred." ) );
        }
        // Otherwise, use expected error message.
        return( $q.reject( response.data.message ) );
    }


    // I transform the successful response, unwrapping the application data
    // from the API response payload.
    function handleSuccess( response ) {
        return(response.data);
    }
});

shelfModule.service("orderService", function($http, $q) {
    $http.defaults.headers.common['X-CSRFToken'] = $.cookie('csrftoken');

    return({
        getOrders: getOrders,
        getOrder: getOrder,
        getOptions: getOptions,
        deleteOrder: deleteOrder
    });

    function getOrders() {
        var request = $http({
            method: "get",
            url: "/api/orders/?format=json"
        });

        return(request.then(handleSuccess, handleError));
    }

    function getOptions() {
        var request = $http({
            method: "options",
            url: "/api/orders/"
        });

        return(request.then(handleSuccess, handleError));
    }

    function getOrder(orderId) {
        var request = $http({
            method: "get",
            url: "/api/orders/" + orderId + "?format=json"
        });

        return(request.then(handleSuccess, handleError));
    }

    function deleteOrder(orderId) {
        var request = $http({
            method: "delete",
            url: "/api/orders/" + orderId
        });

        return (request.then(handleSuccess, handleError));
    }

    function handleError( response ) {
        if (
            ! angular.isObject( response.data ) ||
            ! response.data.message
            ) {
            return( $q.reject( "An unknown error occurred." ) );
        }
        // Otherwise, use expected error message.
        return( $q.reject( response.data.message ) );
    }


    // I transform the successful response, unwrapping the application data
    // from the API response payload.
    function handleSuccess( response ) {
        return(response.data);
    }
});

shelfModule.service("loginService", function($http, $q) {
    $http.defaults.headers.common['X-CSRFToken'] = $.cookie('csrftoken');

    return ({
        login: login,
        logout: logout,
        isLoggedIn: isLoggedIn
    });

    function login(data) {
        var request = $http({
            method: "post",
            url: "/api/login/",
            data: data
        });
        return (request.then(handleSuccess, handleError));
    }

    function logout() {
        var request = $http({
            method: "get",
            url: "/api/logout/"
        });
        return (request.then(handleSuccess, handleError));
    }

    function isLoggedIn() {
        var request = $http({
            method: "get",
            url: "/api/is-logged-in/"
        });
        return (request.then(handleSuccess, handleError));
    }

    function handleError( response ) {
        if (
            ! angular.isObject( response.data ) ||
            ! response.data.message
            ) {
            return( $q.reject( "An unknown error occurred." ) );
        }
        // Otherwise, use expected error message.
        return( $q.reject( response.data.message ) );
    }


    // I transform the successful response, unwrapping the application data
    // from the API response payload.
    function handleSuccess( response ) {
        return(response.data);
    }
});