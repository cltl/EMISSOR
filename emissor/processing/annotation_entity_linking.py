import logging
import spacy
import time
import uuid

from emissor.annotation.brain.util import EmissorBrain
from emissor.annotation.persistence import ScenarioStorage
from emissor.representation.annotation import AnnotationType, EntityLink
from emissor.representation.scenario import Modality, TextSignal, Annotation

logger = logging.getLogger(__name__)

nlp = spacy.load('en_core_web_sm')


SPACY_ID = "SpaCY"


def _add_entity_links(signal: TextSignal, brain: EmissorBrain):
    # TODO: check if annotations already exist
    ner_mentions = [(mention, annotation)
                    for mention in signal.mentions
                    for annotation in mention.annotations
                    if annotation.type.lower() == AnnotationType.NER.name.lower()]

    for mention, annotation in ner_mentions:
        link_annotation = Annotation(AnnotationType.LINK.name, EntityLink(uuid.uuid4()), "linkin_tool", int(time.time()))
        mention.annotations.append(link_annotation)

        brain.denote_things(mention, link_annotation)

    return signal


def annotate_scenarios(storage: ScenarioStorage):
    scenario_ids = storage.list_scenarios()

    for scenario_id in scenario_ids:
        logger.info("Add tokenization and NER annotations to %s", scenario_id)

        # Load episodic memory
        storage.load_scenario(scenario_id)
        signals = storage.load_modality(scenario_id, Modality.TEXT)
        if signals is None:
            raise ValueError("Signals not found")
            # if we want to skip we could do continue, but print warning message
        for signal in signals:
            # check if annotations exist
            _add_entity_links(signal, storage.brain)
        storage.save_signals(scenario_id, Modality.TEXT, signals)
