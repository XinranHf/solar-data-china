import torch
import segmentation_models_pytorch as smp
import torchvision.models as tvm

def get_resnet34_unet_12bands():
    # Create SMP Unet with ResNet34 encoder, no weights (random init), 12 input channels
    model = smp.Unet(
        encoder_name="resnet34",
        encoder_weights=None,
        in_channels=12, 
        classes= 2 # output 2 channels to match mask channels
    )

    # Load torchvision pretrained ResNet34
    tv_resnet = tvm.resnet34(weights=tvm.ResNet34_Weights.IMAGENET1K_V1)
    pretrained_conv1 = tv_resnet.conv1  # [64, 3, 7, 7]

    # Find the first conv layer in SMP model
    # usually model.encoder has a ._modules['0'] or similar
    encoder_conv1 = None
    for m in model.encoder.modules():
        if isinstance(m, torch.nn.Conv2d) and m.in_channels == 12:
            encoder_conv1 = m
            break
    if encoder_conv1 is None:
        raise RuntimeError("Could not find encoder conv1 with 12 input channels")

    with torch.no_grad():
        # initialize weights
        new_weight = torch.zeros_like(encoder_conv1.weight)

        # copy RGB weights
        new_weight[:, :3, :, :] = pretrained_conv1.weight

        # average RGB weights for other 9 channels
        mean_rgb = pretrained_conv1.weight.mean(dim=1, keepdim=True)  # [64,1,7,7]
        new_weight[:, 3:, :, :] = mean_rgb.repeat(1, 9, 1, 1)

        encoder_conv1.weight.copy_(new_weight)

    return model
