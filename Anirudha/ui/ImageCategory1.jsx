import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import '../ui/slider/home_slider.css';
import { Pagination, Navigation, Autoplay } from 'swiper/modules';

function ImageCategory1() {
  return (
    <div className="category-container">
      <Swiper
        slidesPerView={3} 
        spaceBetween={20} 
        loop={true}
        speed={800} // Smoother transition
        autoplay={{
          delay: 3000, // Slide every 3s
          disableOnInteraction: false,
        }}
        pagination={{ clickable: true }}
        navigation={true}
        modules={[Pagination, Navigation, Autoplay]}
        breakpoints={{
          320: { slidesPerView: 1, spaceBetween: 10 },
          480: { slidesPerView: 2, spaceBetween: 15 },
          768: { slidesPerView: 3, spaceBetween: 20 },
          1024: { slidesPerView: 4, spaceBetween: 25 },
        }}
        className="mySwiper mySwiperCategory1"
      >
        {[...Array(9)].map((_, index) => (
          <SwiperSlide key={index} className="category-slide">
            Slide {index + 1}
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
}

export default ImageCategory1;
