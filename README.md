# GMRC Annotations

This repo provides support for representing and annotating multimodal interaction, following the GMRC (Goal-oriented Multimodal Robot Collaboration) framework.
GMRC is an easy-to-use representation for storing and exchanging recordings and annotations of multimodal interaction data.

The goal of GMRC is to exchange these interactions, where contributors are free to generate interactions in any way they like but need to represent
the starting conditions, the goals and the recoding of the interaction in a uniform way. The interactions are represented in different modalities: 
video, image, audio, text, while the data units are aligned in so-called temporal and spatial containers. 

A white paper explaining the overall goals and motivation can be found [here](https://docs.google.com/document/d/1wJrdSAilPiCYvwBuoLEU5oWcOKk0lQw7GdWtirRwL20/edit?usp=sharing).

## [Data Representation](gmrc/representation/README.md)

This repository provides the [`gmrc.representation`](gmrc/representation/README.md) Python package with data classes for
the representation of multi-modal interaction. A detailed description of the representation model can be found in the
[README](gmrc/representation/README.md) of this package. For usage outside of this repository a distribution of the
package can be built from the `setup.py` by executing

    > python setup.py sdist

## [Annotation Tool](gmrc/annotation/README.md)

In addition to the `gmrc.representation` package, this repo provides a tool that allows you to load multi-modal interaction
data with annotations and to manually edit the data by grounding it to the 
temporal and spatial containers ads well as by adding any annotations. For a
detailed description see the [README](gmrc/annotation/README.md) of the annotation
tool.

## Example data

Example data can be found in [*example_data/*](example_data) directory. Some of them are annotated by human and some are by machihne.

### example_data/erc

This includes [Taewoon Kim](https://tae898.github.io/)'s work on emotion recognition in conversation, which also includes a script that annotates the friends MELD dataset into the GMRC format, using [the existing annotations](https://github.com/declare-lab/MELD/tree/master/data/MELD). It's currently a private repo and work in progress. If you want access to it, [write me an email](mailto:tae898@gmail.com).

## TODOs

1. Fix `example_data/example-scenario/`
1. Emotion should span out in multiple signals / modalities, especially in time. Emotion should also be grounded to the face boudning box.
1. Add a feature that shows the detected person's name on the bounding box. 
1. The text modality GUI section support is minimal. Add more functions (e.g. time duration using endtime and startime, display speaker, display emotion of the text, etc.)
1. Include a "master time horizontal slider" that moves every time in all modalities. Currently you have to do this individually, which is not so user-friendly. 
1. Make the GUI tool more extendable, such that annotation is more intuitive and well visualized.
1. Support audio playback
1. Support video playback

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/leolani/cltl-combot/blob/main/LICENCE) for more information.

## Authors
* [Piek Vossen](https://github.com/piekvossen)
* [Thomas Baier](https://github.com/numblr)
* [Taewoon Kim](https://tae898.github.io/)
* [Selene Báez Santamaría](https://selbaez.github.io/)
* [Lea Krause](https://github.com/orgs/cltl/people/lkra)
* [Jaap Kruijt]()
