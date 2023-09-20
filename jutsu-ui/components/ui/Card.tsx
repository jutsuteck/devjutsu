import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  maxSize?: "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "fit";
  transparent?: boolean;
  className?: string;
  onClick?: () => void;
  fixedHeight?: string;
}

const Card: FC<Props> = ({
  children,
  maxSize = "md",
  transparent,
  className,
  onClick,
  fixedHeight,
}) => {
  const baseClasses = "p-8 w-full rounded-lg";
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

  const finalClasses = `${baseClasses} ${sizeClasses[maxSize]} ${bgColor} ${className}`;

  return (
    <div className={`${finalClasses} ${fixedHeight}`} onClick={onClick}>
      {children}
    </div>
  );
};

export default Card;
