class BootstrapFormMixin():
    def set_up_form(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] += ' form-control'
