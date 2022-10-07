from .pixel_loss import L1Loss, MSELoss, CharbonnierLoss, \
                        CalcStyleEmdLoss, CalcContentReltLoss, \
                        CalcContentLoss, CalcStyleLoss, EdgeLoss
from .gradient_penalty import GradientPenalty

from .builder import build_criterion

from .ssim import SSIM
from .id_loss import IDLoss
