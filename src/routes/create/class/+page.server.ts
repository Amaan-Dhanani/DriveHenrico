import type { Actions } from './$types';
import { error } from '@sveltejs/kit';
import { new_class } from '$lib/server/class_and_levels';

export const actions: Actions = {
    default: async ({ request, cookies }) => {
        const email = cookies.get("email");
        if (!email) throw error(400, "Missing email cookie");
        const formData = await request.formData();

        //CHANGE
        const info = Object.fromEntries(formData) as { fake: string; };
        //CHANGE

        console.log("calling function");


        const classID = await new_class(email);
        console.log(classID);
        return {classID: classID, info: info}
        
    }
};