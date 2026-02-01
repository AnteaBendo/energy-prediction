
# Energy Price Prediction

### Contributors

- Antea Bendo
- Eleni Sklaveniti

Part of the course __‘M. Grum: Advanced AI-based Application Systems’__ by the
__‘Junior Chair for Business Information Science, esp. AI-based Application Systems’__ at University of Potsdam


## Working with this image

### Building the local docker image manually with `Dockerfile`.

1. Build docker image from Dockerfile specified.

    ```
    docker build --tag codebase_energy_prediction:latest .
    ```

1. Have a look on the image created.

    ```
    docker run -it --rm codebase_energy_prediction:latest sh
    ```

### Alternatively, build local docker image manually with `yml` file.

1. If not available yet, create independent volume for being bound to image.

    ```
    docker volume create ai_system
    ```

1. Build image with `docker-compose`.

    ```
    docker-compose build
    ```

### Test local docker container.

1. Start container with `docker-compose`.

    ```
    docker-compose up
    ```

1. Test your container, e.g. by executing a shell.

    ```
    docker exec -it codebase_energy_prediction sh
    ```

1. Shut down container with `docker-compose`.

    ```
    docker-compose down
    ```

### Deploying the docker image to dockerhub.

1. To push the image to `https://hub.docker.com/` the following command can be used.

    ```
    docker image push anteab/codebase_energy_prediction:latest
    ```
## Model Characterization
The model is a Sequential Feedforward Neural Network featuring three dense layers 
($16, 8, 1$ neurons) using Leaky ReLU activations for hidden layers and a Linear activation for the
regression output. It processes a 2-dimensional input shape and uses a Normal kernel initializer. Optimization is handled by Adam with a 
learning rate of 0.00005, monitored via TensorBoard.

## Credits
The data used in this project is taken from the following api: [Energy Charts API](https://api.energy-charts.info/#/prices/day_ahead_price_price_get)


## License
This project is licensed under the [**GNU Affero General Public License v3.0 (AGPL-3.0)**](https://www.gnu.org/licenses/agpl-3.0.en.html) .
