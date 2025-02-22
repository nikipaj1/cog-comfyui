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
        # return MODELS
        return []

    @staticmethod
    def add_weights(weights_to_download, node):
        pass
        # if node.is_type_in(
        #     ["LoadAutoMasker", "LoadCatVTONPipeline", "AutoMasker", "CatVTON"]
        # ):
        #     weights_to_download.extend(MODELS)

    @staticmethod
    def weights_map(base_url):
        # hf_base = "https://huggingface.co/zhengchong/CatVTON/resolve/main"
        # return {
        #     model: {
        #         "url": f"{hf_base}/{model}",
        #         "dest": "ComfyUI/custom_nodes/Comfyui-CatVTON/model",
        #     }
        #     for model in MODELS
        # }
        return {}
