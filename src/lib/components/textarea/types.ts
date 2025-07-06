import type { ClassValue, HTMLTextareaAttributes } from "svelte/elements";

export type tTextareaProps = HTMLTextareaAttributes & {
    // Classes:

    // --- Default Classes:
    inputClass?: ClassValue,
    labelClass?: ClassValue,

    classLabel?: ClassValue
    
    // Extra Props Here:
    label?: string,
    cap?: number;
};