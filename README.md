# Latent Diffusion MIDI

Fork of Latent Diffusion repo for generating sequences of MIDI music from scratch. We use a dataset of MIDI files, convert them to images using `midi2img`, and train the model to learn the distribution and create similar MIDI music from pure Gaussian noise.

The **full paper** describing our methods, experiments, and results is linked [here](https://drive.google.com/file/d/1uU9gxCaahy-RzhJvdvLl--Xy2FbWy6Tv/view?usp=sharing).

<img width="529" alt="Screenshot 2024-07-23 at 8 52 34 PM" src="https://github.com/user-attachments/assets/dc164129-e2dc-44c4-bb72-adbdd7bdb48d">

## Our Approach and Motivation
We observed that the main challenge with applying diffusion models to this problem space lies in the lack of continuity in the MIDI domain. Prior works have solved this continuity issue by using a VAE to map from the discrete MIDI domain to a continuous latent variable space. Instead of utilising a VAE to map to a continuous domain, we believe it will be more useful to employ an encoder-decoder architecture for solving the continuity issue. Moreover, latent diffusion has shown remarkable results in vision due to the more semantic meaning of the encoded domain. Our hypothesis is that using a latent-diffusion approach will result in high-quality MIDI generation, and specifically that the encoder-decoder architecture will perform a better job at finding a latent domain that is more meaningful for the diffusion model. Finally, an encoder-decoder architecture has greater visibility due to the underlying attention mechanisms that can be used to further analyse intermediate outputs. Moreover, using a non-VAE approach to access the latent space gives us a deterministic method to interact with the area, which we believe makes the model better during training for the reconstruction

---

You can find the original latent diffusion repo and their complete documentation [here](https://github.com/CompVis/latent-diffusion).
