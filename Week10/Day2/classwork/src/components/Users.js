const User = (props) =>{
    const {info}=props;
    console.log('props=>', info);
    // const style = {infoUsers}
    return(
        <div className = "infoUsers">

        <img src={`https://robohash.org/1?size=150x150`}/>

            <h2>{info.name}</h2>
            <p>{info.email}</p>
            <p>{info.username}</p>
        </div>
    );
};

export default User;