export const steps = ['credential', 'code', 'success'] as const;
export type Step = (typeof steps)[number];

export function isStep(value: Step) {
	return steps.includes(value);
}
