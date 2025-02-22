from custom_node_helper import CustomNodeHelper


class ComfyUI_CatVTON(CustomNodeHelper):
    @staticmethod
    def models():
        # return MODELS
        return []

    @staticmethod
    def add_weights(weights_to_download, node):
        pass

    @staticmethod
    def weights_map(base_url):
        return {}
