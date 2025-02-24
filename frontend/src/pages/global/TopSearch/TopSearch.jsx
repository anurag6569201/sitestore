import './TopSearch.css';

function TopSearch(){
    return (
        <div className="top-search">
            <div className="container">
                <div className="input-group">
                    <input type="text" className="form-control" placeholder="" />
                    <div className="input-group-append">
                        <button className="btn" type="submit"><i className="fa fa-search"></i></button>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default TopSearch;