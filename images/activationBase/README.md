# Energy Price Predictor

### Contributors

   - Antea Bendo
   - Eleni Sklaveniti

Part of the course __‘M. Grum: Advanced AI-based ApplicaGon Systems’__ by the 
__‘Junior Chair for Business InformaGon Science, esp. AI-based ApplicaGon Systems’__ at University of Potsdam


## Working with this image

The current activation refers to the file activation_data.csv.

### Building the local docker image manually with `Dockerfile`.

1. Build docker image from Dockerfile specified.

    ```
    docker build --tag energy_predictor/activationbase:latest .
    ```

1. Have a look on the image created.

    ```
    docker run -it --rm energy_predictor/activationbase:latest sh
    ```

### Alternatively, build local docker image manually with `yml` file.

1. If not available, yet, create independent volume for being bound to image.

    ```
    docker volume create ai_system
    ```

1. Build image with `docker-compose`.

    ```
    docker-compose build
    ```

### Test local docker image.

1. Start image with `docker-compose`.

    ```
    docker-compose up
    ```

1. Test your image, e.g. by executing a shell.

    ```
    docker exec -it energy_predictor/activationbase:latest sh
    ```

1. Shut down image with `docker-compose`.

    ```
    docker-compose down
    ```

### Deploying the docker image to dockerhub.

1. To push the image to `https://hub.docker.com/` the following command can be used.

    ```
    docker image push energy_predictor/activationbase:latest
    ```

## Credits
The data used in this project is taken from the following api: [Energy Charts API](https://api.energy-charts.info/#/prices/day_ahead_price_price_get)


## License
This project is licensed under the [**GNU Affero General Public License v3.0 (AGPL-3.0)**](https://www.gnu.org/licenses/agpl-3.0.en.html) .
