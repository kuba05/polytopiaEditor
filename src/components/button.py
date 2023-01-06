class Button():
    def __init__(self, image, onClick):
        self.image = image
        self.onClick = onClick

    def multipleFunctions(*func):
        def helper():
            last = 0
            for f in func:
                last = f()
            return last

        return helper
