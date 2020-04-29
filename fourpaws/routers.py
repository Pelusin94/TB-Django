class FourPawsRouter(object):

    def db_for_read(self, model, **hint):
        if model._meta.app_label == 'fourpaws':
            return 'fourpaws'
        return None

    def db_for_write(self, model, **hint):
        if model._meta.app_label == 'fourpaws':
            return 'fourpaws'
        return None

    def allow_syncdb(self, db, model):
        if db == 'fourpaws':
            return model._meta.app_label == 'fourpaws'
        elif model._meta.app_label == 'fourpaws':
            return False
        return None