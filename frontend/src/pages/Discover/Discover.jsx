import HomeSlider from '../global/slider/HomeSlider';
import Category from '../category/Category';
import TopSearch from '../global/TopSearch/TopSearch';

function Discover(){
    return (
        <>
            <div>
                <TopSearch/>
                <br />
                <HomeSlider/>
                <Category/>
            </div>
        </>
    );
}
export default Discover;