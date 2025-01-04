"""
Schema validation.
"""

from typing import Type


class Validator:
    """Validates transliteration schema definition."""

    def __init__(self, defn: dict):
        self.defn = defn
        self.name = defn.get("name", "<unknown>")

    def run(self):
        """Validate source definition, raising ValueError if necessary."""
        self._validate_attr("name", type_=str, required=True, nonempty=True)
        self._validate_attr("description", type_=str, required=False)
        self._validate_attr("mapping", type_=dict, required=True)
        self._validate_attr("prev_mapping", type_=dict, required=False)
        self._validate_attr("next_mapping", type_=dict, required=False)
        self._validate_attr("ending_mapping", type_=dict, required=False)
        self._validate_samples()

    def _validate_attr(self, name: str, type_: Type, required: bool, nonempty: bool = False):
        value = self.defn.get(name)
        if required and value is None:
            raise ValueError(f"{self.name}: Missing schema {name}")
        if required and nonempty and not value:
            raise ValueError(f"{self.name}: Schema {name} should not be empty")
        if value is not None and not isinstance(value, type_):
            raise ValueError(f"{self.name}: Invalid schema {name}: {value}")

    def _validate_samples(self):
        samples = self.defn.get("samples")
        if samples is None:
            return
        if not isinstance(samples, list):
            raise ValueError(f"{self.name}: Invalid schema samples: {samples}")
        for sample in samples:
            self._validate_sample(sample)

    def _validate_sample(self, sample):
        message = f"{self.name}: Invalid schema sample: {sample}"
        if not isinstance(sample, list):
            raise ValueError(message)
        if len(sample) != 2:
            raise ValueError(message)
        if not isinstance(sample[0], str) or not isinstance(sample[1], str):
            raise ValueError(message)
