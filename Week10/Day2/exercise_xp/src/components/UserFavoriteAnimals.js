const UserFavoriteAnimals = (props)=>{
    const {animals} = props;
    
    return(
        <ul>
         <h3>Favorite animals:</h3>
            {animals.map((animal, index)=>{
               return <li key={index}>{animal}</li>
            })}
        </ul>
    );
};

export default UserFavoriteAnimals;