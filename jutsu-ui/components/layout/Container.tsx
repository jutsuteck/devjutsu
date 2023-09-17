import { FC, ReactNode } from "react";

interface Props {
  children: ReactNode;
  maxWidth?: string;
}

const Container: FC<Props> = ({ children, maxWidth = "max-w-[90%]" }) => (
  <div className={`mx-auto p-4 ${maxWidth}`}>{children}</div>
);

export default Container;
