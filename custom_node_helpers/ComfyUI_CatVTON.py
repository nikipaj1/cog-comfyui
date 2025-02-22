from custom_node_helper import CustomNodeHelper

MODELS = [
    "cloth_segm.pth",
    "cloth_agnostic.pth",
    "warp_net.pth",
    "gen_net.pth",
    "mobile_warp_net.pth",
    "mobile_gen_net.pth",
]


class ComfyUI_CatVTON(CustomNodeHelper):
    @staticmethod
    def models():
        return MODELS

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type_in(["CatVTONLoader", "CatVTONMobileLoader"]):
            weights_to_download.extend(MODELS)

    @staticmethod
    def weights_map(base_url):
        return {
            model: {
                "url": f"{base_url}/custom_nodes/Comfyui-CatVTON/checkpoints/{model}.tar",
                "dest": "ComfyUI/custom_nodes/Comfyui-CatVTON/checkpoints",
            }
            for model in MODELS
        }
