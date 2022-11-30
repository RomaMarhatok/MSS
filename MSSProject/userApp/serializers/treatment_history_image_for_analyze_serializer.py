from rest_framework.serializers import ModelSerializer
from typing import OrderedDict
from ..models import TreatmentHistoryImageForAnalyzes


class TreatmentHistoryImageForAnalyzesSerializer(ModelSerializer):
    class Meta:
        model = TreatmentHistoryImageForAnalyzes
        fields = (
            "treatment_history",
            "image_for_analyzes",
        )
