import { FC, ReactNode } from "react";

interface Props {
  text: string;
  icon?: ReactNode;
  transparent?: boolean;
  className?: string;
  type?: "button" | "submit" | "reset";
  onClick?: () => void;
}

const Button: FC<Props> = ({
  text,
  icon,
  transparent,
  className,
  onClick,
  type = "button",
  ...props
}) => {
  const baseClasses =
    "w-full text-nord-frost-dark font-semibold p-2 rounded-lg flex items-center justify-center";
  const defaultClasses = "bg-nord-frost-medium hover:bg-nord-frost-light";
  const transparentClasses =
    "border border-nord-frost-medium hover:bg-nord-polar-night-medium focus:bg-nord-polar-night-medium";
  const focusClasses =
    "focus:outline-none focus:ring-2 focus:ring-nord-frost-light";

  const finalClasses = `${baseClasses} ${
    transparent ? transparentClasses : defaultClasses
  } ${focusClasses} ${className}`;

  return (
    <button type={type} className={finalClasses} onClick={onClick} {...props}>
      {icon && <span className="mr-2">{icon}</span>}
      {text}
    </button>
  );
};

export default Button;
