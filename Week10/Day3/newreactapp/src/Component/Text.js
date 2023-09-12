import React, { useEffect, useState } from 'react';

const Text = (props) => {
    const [users, setUsers] = useState([]);
  useEffect(() => {
    if (props.txt === 'Alex') {
      console.log('Text=>', props.txt);
    }
  }, [props.txt]);

  return (
    <div>
      <h1>Text Component</h1>
      <p>{props.txt}</p>
    </div>
  );
}

export default Text;




// import React from 'react';

// class Text extends React.Component {
//   render() {
//     const { txt } = this.props;
//     return (
//       <div>
//         <h2>Text Component</h2>
//         <p>{txt}</p>
//       </div>
//     );
//   }
// }

// export default Text;
