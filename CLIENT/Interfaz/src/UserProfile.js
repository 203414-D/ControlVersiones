import { useParams } from "react-router";
import Profile from "./Profile";

export default function UserProfile(){

    var user_id = localStorage.getItem('user_id')

    return(
        <div>
            <Profile></Profile>
        </div>
    );
}