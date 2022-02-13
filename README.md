# DebVAder: Deblending galaxies with Variational Autoencoders
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![License][license-badge]][license-web]
[![Paper][arxiv-badge]][arxiv-paper]

[license-badge]: https://img.shields.io/badge/license-BSD-blue.svg?style=flat
[license-web]: https://choosealicense.com/licenses/bsd-3-clause/
[arxiv-paper]: https://arxiv.org/abs/2005.12039
[arxiv-badge]: https://img.shields.io/badge/arXiv-2005.12039-brightgreen.svg?style=flat
[dc2-paper]: https://arxiv.org/abs/2010.05926


This repo contains the scripts to use the deblending algorithm based on variational autoencoders presented in [Arcelin et al. (2020)][arxiv-paper]. It is pip installable and can be used exclusively (for now) on images generated by the [LSST DESC DC2 simulation][dc2-paper].

## Example

An example of application of `debvader` on DC2 images is presented in [this tutorial](notebooks/deblending_dc2_images.ipynb).

## Installation

It requires few packages to work:
- `tensorflow` == 2.1.0
- `tensorflow-probability` == 0.9.0
- `numpy`
- `matplotlib`
- `pandas`
- `jupyter`
- `sep`

It can then be pip installed with
``` 
pip install --index-url https://test.pypi.org/simple/ debvader 
```

## Authors

- [Bastien Arcelin](https://github.com/BastienArcelin) - arcelin at apc.in2p3.fr
- [Cyrille Doux](https://github.com/xuod)
- [Thomas Sainrat](https://github.com/thuiop)
- [Biswajit Biswas](https://github.com/b-biswas)
- [Alexandre Boucaud](https://github.com/aboucaud)

## License

BSD 3-Clause license, see the [LICENSE file](LICENSE) for more information

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/BastienArcelin"><img src="https://avatars.githubusercontent.com/u/43615932?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bastien Arcelin</b></sub></a><br /><a href="https://github.com/BastienArcelin/debvader/commits?author=BastienArcelin" title="Code">💻</a> <a href="#projectManagement-BastienArcelin" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!