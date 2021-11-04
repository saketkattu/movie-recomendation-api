
deployed link : https://movie-recommendation-api1.herokuapp.com/docs

# Movie Recommendation API 

A movie Recommendation Engine which returns a list of similar movies 
build using content based Recommendation 



## Demo

![](/misc/Movie Recomendation API.gif)





## API Reference

#### Get Recommedations

```http
  GET /recommedation/{Movie Name}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `movie_name` | `string` | **Required** Enter the name of the movie you want recommedation |

