import { FC, useEffect } from "react";

interface Props {
  register: any;
  name: string;
  placeholder?: string;
  error?: string;
  autoComplete?: "on" | "off";
  transparent?: boolean;
  className?: string;
  noPaddingX?: boolean;
  autoFocus?: boolean;
}

const CustomTextArea: FC<Props> = ({
  register,
  name,
  placeholder,
  error,
  autoComplete,
  className,
  autoFocus,
}) => {
  const adjustHeight = (element: HTMLTextAreaElement | null) => {
    if (element) {
      element.style.height = "inherit";
      const scrollHeight = element.scrollHeight;
      element.style.height = scrollHeight + "px";
    }
  };

  const defaultStyle = `bg-nord-polar-night-medium text-nord-snowstorm-light w-full focus:outline-none`;
  const borderStyle = error
    ? "focus:border-nord-aurora-red"
    : "focus:border-nord-meadow";

  return (
    <>
      <textarea
        placeholder={placeholder}
        className={`${defaultStyle} ${borderStyle} ${className} resize-none overflow-hidden`}
        {...register(name)} // <-- Use the spread syntax here
        onInput={(e) => adjustHeight(e.target)} // <-- Use the onInput event to adjust height
        autoComplete={autoComplete}
        autoFocus={autoFocus}
      />
      <div className="h-3 mt-1">
        {error && <p className="text-sm text-nord-aurora-red">{error}</p>}
      </div>
    </>
  );
};

export default CustomTextArea;
