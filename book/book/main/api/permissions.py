
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    '''
    publisher access to create update delete and get books
    '''

    def has_permission(self, request, view):
        #Todo post request should be authorized only for publishers!
        if request.user.is_authenticated:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        SAFE_METHODS=['DELETE','PUT','GET']
        
        if request.method in permissions.SAFE_METHODS and  obj.publisher == request.user:
            return True

        return False
        


class IsViewer(permissions.BasePermission):
    '''
    viewer permission
    '''

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
    
        
        if request.method =='GET' :
            return True

        return False
        