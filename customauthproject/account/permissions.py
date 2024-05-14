from rest_framework import permissions


class Permission1Check(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("account.permission1")


class Permission2Check(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("account.permission2")


class Permission3Check(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("account.permission3")
