# Movie Recommendation API 

A movie Recommendation Engine which returns a list of similar movies 
build using content based Recommendation 



## Demo

![](https://media.giphy.com/media/RxM6bTb58GH6V7Oju0/giphy.gif)





## API Reference
#### API Endpoint
```
https://movie-recommendation-api1.herokuapp.com
````
#### Get Recommedations

```
  GET /recommedation/{Movie Name}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `movie_name` | `string` | **Required** Enter the name of the movie you want recommedation |

## Run Locally

Clone the project

```bash
  git clone https://github.com/saketkattu/movie-recomendation-api
```

Go to the project directory

```bash
  cd movie-recomendation-api
```

Create vitual enviroment and install dependencies 

```bash
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt 
```

Start the server

```bash
  uvicorn app:app --reload
```

## Tech Stack

**Application Development** FastAPI, Docker ,Heroku 

**Machine Learning** Sckit-Learn , Pandas ,Numpy ,Scipy 


## Future Improvements 

- Integrations with a frontend application
- Running a API in Dockerized Enviroment like Google App Engine
- Making the ML model better with addition of Data 
- Experimenting with the use of Deep Learning Techniques to improve the recmmedation system ( e.g TabNet, Embedding Layers)
- Building a Data Flywheel to automatically re-train the model based on addition of real world data 


