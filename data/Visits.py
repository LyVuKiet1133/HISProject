class Visit():
    def __init__(self, **kwargs):
        self.entryId = None
        self.visitId = None
        self.medServiceId = None
        self.wardUnitId = None
        self.onDate = None
        self.insBenefitType = None
        self.insBenefitRatio = None
        self.priceId = None
        self.qmsNo = None
        self.ticketId = None
        self.createByWardUnitId = None
        for key, value in kwargs.items():
            setattr(self, key, value)
