angular.module('shelf', ['ui.select', 'ngSanitize', 'restangular', 'ngRoute', 'angularUtils.directives.dirPagination']).config(
    function(paginationTemplateProvider) {
        paginationTemplateProvider.setPath('/static/bower_components/angular-utils-pagination/dirPagination.tpl.html');
    }
).config(
    function(RestangularProvider) {
        RestangularProvider.setBaseUrl('/api')
    }
);
