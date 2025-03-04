import React, { useEffect, useState } from "react";
import axios from "axios";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import { Pagination, Navigation } from "swiper/modules";
import "./home_slider.css";

export default function HomeSlider() {
    const [sites, setSites] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios
            .get("http://localhost:8000/default/sites/") // Update with your API URL
            .then((response) => {
                setSites(response.data);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <Swiper
            slidesPerView={1}
            spaceBetween={30}
            loop={false}
            pagination={{ clickable: true }}
            navigation={true}
            modules={[Pagination, Navigation]}
            className="mySwiper mySwiperhomeSlider featured_slide-content"
        >
          <div className="feature_app_overview_overlay feature_app_overview_overlay_left"></div>
          <div className="feature_app_overview_overlay feature_app_overview_overlay_right"></div>
          <div className="feature_app_overview_overlay feature_app_overview_overlay_down"></div>
            {sites.map((site) => (
                <SwiperSlide key={site.id}>
                    <div className="slide-content">
                        <img src={site.image} alt={site.name} className="slide-image" />
                        <p className="featured_sites">
                          <span>{site.featured}</span>
                          <span>{site.name}</span>
                          <span>{site.description}</span>
                        </p>
                    </div>
                </SwiperSlide>
            ))}
        </Swiper>
    );
}
