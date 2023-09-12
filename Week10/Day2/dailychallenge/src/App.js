import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './App.css'; // You can create this file to add custom styles if needed

function App() {
  return (
    <div className="carousel-wrapper">
      <Carousel>
        <div>
          <img src="/img/hongkong.jpg" alt="Hong Kong" />
          <p className="legend">Hong Kong</p>
        </div>
        <div>
          <img src="img/Macao.jpg" alt="Macao" />
          <p className="legend">Macao</p>
        </div>
        <div>
          <img src="img/Japan.jpg" alt="Japan" />
          <p className="legend">Japan</p>
        </div>
        <div>
          <img src="img/LasVegas.jpg" alt="Las Vegas" />
          <p className="legend">Las Vegas</p>
        </div>
      </Carousel>
    </div>
  );
}

export default App;
