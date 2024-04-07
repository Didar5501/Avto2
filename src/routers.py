class AvtoRouter:

    route_app_labels = {"avto_bs"}
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "avto_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "avto_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "avto_db"
        return None


class CCRouter:

    route_app_labels = {"avto_cc"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "cc_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "cc_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "cc_db"
        return None