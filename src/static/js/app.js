angular.module('shelf', ['lumx', 'ngRoute', 'angularUtils.directives.dirPagination']).config(
    function(paginationTemplateProvider) {
        paginationTemplateProvider.setPath('/static/bower_components/angular-utils-pagination/dirPagination.tpl.html');
    }
);
