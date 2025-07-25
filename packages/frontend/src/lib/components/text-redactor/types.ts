import type { ClassValue, HTMLAttributes } from "svelte/elements";

export type tTextRedactorProps = HTMLAttributes<HTMLSpanElement> & {
    // Classes:
    className?: ClassValue,


    // Extra Props Here:
    number?: number,
    char?: string,
    text?: string,


};