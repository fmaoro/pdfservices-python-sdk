# Copyright 2024 Adobe
# All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Adobe and its suppliers, if any. The intellectual
# and technical concepts contained herein are proprietary to Adobe
# and its suppliers and are protected by all applicable intellectual
# property laws, including trade secret and copyright laws.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Adobe.

from abc import ABC, abstractmethod


class TSAOptions(ABC):
    """
    This abstract class represents the basic contract for the timestamp authority options to be used with
    :class:`PDFElectronicSealParams<adobe.pdfservices.operation.pdfjobs.params.eseal.electronic_seal_params.PDFElectronicSealParams>`.
    """

    @abstractmethod
    def to_dict(self):
        pass
