import './Exercise.css'

const Exercise = () =>{
const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial"
};

return (
<div>
    <h1 style={style_header}>Lorem bla bla</h1>
    <p className = 'para'>This is a paragraph.</p>
        <a href="https://example.com">This is a link</a>
        <form>
          <input type="text" placeholder="Input field" />
          <button type="submit">Submit</button>
        </form>
        <img src="https://example.com/image.jpg" alt="Example" />
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
        </ul>
</div>

)
};

export default Exercise;