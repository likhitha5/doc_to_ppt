
// PresentationViewer component to render a slide-based presentation.
// It displays different types of slides (title, content, summary) and navigates through them.
// It also handles the display of images associated with each slide from the provided API URL.

import React, { useState } from 'react';
import API_BASE_URL from "../config";

const PresentationViewer = ({ slides }) => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const renderSlide = (slide) => {
    const renderImage = () => {
      console.log(slide);
      if (slide.image && typeof slide.image === 'string') {
        return <img src={`${API_BASE_URL}/uploads/${slide.image}`} alt="Slide visual" />;
      }
      return null;
    };

    switch (slide.type) {
      case 'title':
        return (
          <div className="title-slide">
            <h1>{slide.title}</h1>
            {slide.subtitle && <h2>{slide.subtitle}</h2>}
            {renderImage()}
          </div>
        );
      case 'content':
        return (
          <div className="content-slide">
            <h2>{slide.title}</h2>
            <ul>
              {slide.content.map((point, idx) => (
                <li key={idx}>{point}</li>
              ))}
            </ul>
            {renderImage()}
          </div>
        );
      case 'summary':
        return (
          <div className="summary-slide">
            <h2>{slide.title}</h2>
            <div className="summary-content">
              {slide.content.map((point, idx) => (
                <p key={idx}>{point}</p>
              ))}
            </div>
          </div>
        );
      default:
        return (
          <div className="unknown-slide">
            <p>Unknown slide type: {slide.type}</p>
          </div>
        );
    }
  };

  return (
    <div className="presentation-viewer">
      <div className="slide-container">
        {slides.length > 0 && renderSlide(slides[currentSlide])}
      </div>
      <div className="controls">
        <button 
          onClick={() => setCurrentSlide(prev => Math.max(0, prev - 1))}
          disabled={currentSlide === 0}
        >
          Previous
        </button>
        <span>{currentSlide + 1} / {slides.length}</span>
        <button 
          onClick={() => setCurrentSlide(prev => Math.min(slides.length - 1, prev + 1))}
          disabled={currentSlide === slides.length - 1}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default PresentationViewer;
