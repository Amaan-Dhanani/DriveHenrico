# QuestOwl 
 
## Sources
>**MongoDB Altas + SvelteKit + TailwindCSS**

## How to (components)

### Input
>Go to `$lib/components/input/components/input.svelte` to see the component. TypeScript files are used in `$lib/components/input`. The props of the component are as follows: 
> | Prop | Description | Example |
> |-|-|-|
> | `class` | Any other classes you want to add which will add on to the other classes that were used by default for styling. Overriding default classes work. | `ml-[45px]`
> | `label` | Adds a `<label>` element above the input box. However, since the styling of this label cannot be customized, it's recommended to omit the `label` prop and instead use your own HTML text element if custom styling is needed. | `Name`|
> 
> Note that other HTML `input` attributes (such as `required` and `disabled`) are also props, and these props can override defaults.
> Note the component needs access to `$lib/components/utils.ts`.

### Navigation
>Go to `$lib/components/navigation/Navigation.svelte` to find the navbar.  Each icon is made by the `Icon` component, which is found in `$lib/components/navigation/components/Icon.svelte`. The props of the Icon component are as follows:
>| Prop | Description | Example |
>|-|-|-|
>| `text` | Label displayed below the icon; also known as the option name. | `Discord` |
>| `paths` | Basically all of html of the path tag inside the svg element. It is recommended to write the path by declaring in as a string in the typescript section of `Navigation.svelte` and not being placed directly within the component. Do not use the `stroke` attribute inside `paths` unless necessary, as there is a dedicated `stroke` prop. | `<path d="M10 10 L90 10 L90 90 L10 90 Z">` |
>|`viewbox`| Basically whatever is in the `viewbox` attribute of the svg element. | `0 0 24 24`|
>| `stroke` | Basically, if it works, the stroke value will try to prevent having to write a `stroke` attribute in `paths`. Supports all HTML colors. | `#2d52cd` |
>|`center` | If set to `true`, icon will be larger and styled differently to represent the most centered option for navigation. | `true`
>| `fill` | Fill color for the svg. Supports all HTML colors. |`#2d52cd`|
>|`link` | URL path the user will navigate to upon clicking the icon. | `/dashboard` |

### Radio Horizontal/Category Select
>Go to `$lib/components/radio_horizontal/components/RadioHorizontal.svelte` to see the component. TypeScript files are used in `$lib/components/radio_horizontal`. 
>It is kind of hard to explain the props of this components, so I have a code sample:
> ```html
> <RadioHorizontal
> 	name="access"
> 	bind:selected={selected2}
> 	options={[
> 		{ label: 'Public', value: 'Public' },
> 		{ label: 'Private', value: 'Private' }
> 	]}
> />
> ```
>- The `name` prop can be used to reference the element, which is necessary during an HTML form. When a form is submitted, the `name` is used as the key in the key-value pair sent to the server.
> - `bind:selected` tells Svelte to keep the value of the selected option in sync with a variable.  In this case, `{selected2}` is the variable being bound. When the user selects a new option, `selected2` updates automatically. The string in `selected2` indicates the default value and is declared in the TypeScript portion of the Svelte page (not the component itself.
> - The `options` array defines the choices shown in the dropdown menu. Each object in the array has a `label` and a `value`.   `label` is the text displayed to the user.   `value`: This is the underlying value assigned when the option is selected.
> Note the component needs access to `$lib/components/utils.ts`.
### Textarea
>Go to `$lib/components/textarea/components/Textarea.svelte` to see the component. TypeScript files are used in `$lib/components/textarea`. The props of the component are as follows: 
> | Prop | Description | Example |
> |-|-|-|
> | `class` | Any other classes you want to add which will add on to the other classes that were used by default for styling. Overriding default classes work. | `ml-[45px]`
> | `cap` | Adds a cap to how many characters can be put, and will display the amounts of characters typed so far. the `maxlength` attribute is not recommended unless you want to add a cap without displaying the amount of characters.| `Name`|
> 
> Note that other HTML `textarea` attributes (such as `required` and `disabled`) are also props, and these props can override defaults.
> Note the component needs access to `$lib/components/utils.ts`.

## How to (server)
### Protected Page 
>There are certain pages we want to restrict so users can only access them if they are logged in. For example, a dashboard showing user stats should not render properly unless the user is signed in. 
>To enforce this, these pages are "protected" when an unauthorized user tries to access them, they are automatically redirected to the login page.
>To implement this, open `src/hooks.server.ts` and locate the following code:
> ```ts
> const is_protected =
>   event.url.pathname.startsWith("/dashboard") ||
>   event.url.pathname.startsWith("/account") ||
>   event.url.pathname.startsWith("/create");
> ```
> Add any additional protected routes here by including more conditions with `||`.


# NOTE TO SELF, TALK ABOUT `tempquest_pass` and `get_user_id`!
