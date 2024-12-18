# Gen-AI Product

Welcome to the Gen-AI product! This project leverages Gradio for creating an interactive web application for text generation and image generation using the Stable Diffusion model.

## Features

- **Text Generation**: Generate creative and coherent text based on user input.
- **Image Generation**: Create stunning images from textual descriptions using the Stable Diffusion model.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/zuliqarAlibati/Gen-AI.git
cd GenAI.ipynb
pip install -r requirements.txt
```

## Usage

Run the Gradio app:

```bash
python app.py
```

## Output

Generated images will be saved in the `output/images` directory.

## Demo

Check out the demo video below to see the image generation and text generation in action!

<video width="600" controls>
    <source src="output/demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

## Example Outputs

Here are some example images generated by the model:

![Llama 2](output/llama2.jpg)
![Tranquil](output/tranquil.jpg)

## Models Used

### Dolly 3B Model - by Databricks
---
1. Model Name: Dolly-v2-3b
2. Model Parameters: 3 Billion
3. Training: Instruction-tuned Model
4. Link: [Dolly-v2-3b](https://huggingface.co/databricks/dolly-v2-3b)
---

### Falcon 7B Model - by TII
---
1. Model Name: Falcon-7b-instruct
2. Model Parameters: 7 Billion
3. Training: Instruction-tuned Model
4. Link: [Falcon-7b-instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)
---

### Stable Diffusion v1-5 - by RunwayML
---
1. Model Name: stable-diffusion-v1-5
2. Model type: Diffusion-based text-to-image generation model
3. Model Description: Generate/modify images with text prompts.
4. Link: [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Gradio
- Stable Diffusion

Feel free to contribute to this project by opening issues or submitting pull requests.