import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  transparent?: boolean;
  maxSize?: "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "fit";
  fixedSize?: "w-1/4" | "w-1/3" | "w-1/2" | "w-2/3" | "w-3/4";
  onClick?: () => void;
  className?: string;
  boxShadow?:
    | "shadow-sm"
    | "shadow"
    | "shadow-md"
    | "shadow-lg"
    | "shadow-lg"
    | "shadow-xl"
    | "shadow-2xl";
  ref?: any;
}

const Card: FC<Props> = ({
  children,
  maxSize,
  transparent,
  onClick,
  fixedSize,
  className,
  boxShadow,
  ref,
}) => {
  const baseClasses = "p-8 rounded-lg";
  const sizeClasses = {
    fit: "max-w-fit",
    xs: "max-w-xs",
    sm: "max-w-sm",
    md: "max-w-md",
    lg: "max-w-lg",
    xl: "max-w-xl",
    "2xl": "max-w-2xl",
  };
  const bgColor = transparent ? "" : "bg-nord-polar-night-medium";

  let sizeClass;
  if (maxSize) {
    sizeClass = sizeClasses[maxSize];
  } else if (fixedSize) {
    sizeClass = fixedSize;
  }

  const finalClasses = `${baseClasses} ${sizeClass} ${bgColor} ${
    boxShadow && boxShadow
  } ${className}`;

  return (
    <div className={finalClasses} onClick={onClick} ref={ref}>
      {children}
    </div>
  );
};

export default Card;
