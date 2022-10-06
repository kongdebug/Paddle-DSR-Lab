from .pixel_loss import L1Loss, MSELoss, CharbonnierLoss, \
                        CalcStyleEmdLoss, CalcContentReltLoss, \
                        CalcContentLoss, CalcStyleLoss, EdgeLoss

from .builder import build_criterion
